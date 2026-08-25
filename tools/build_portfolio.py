# -*- coding: utf-8 -*-
"""Render the live site to a single PDF portfolio.

Prints each page with headless Edge, then merges them with the resume in
front and an outline so a reader can jump between projects.
"""
import os, subprocess, sys, time, shutil
from pypdf import PdfWriter, PdfReader

EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
BASE = "http://localhost:8123"
REPO = r"C:\Users\dmben\repos\PersonalWebsite"
OUT  = os.path.join(os.path.dirname(os.path.abspath(__file__)), "portfolio")

# order matters: this is the reading order of the finished document
PAGES = [
    ("index.html",              "Overview"),
    ("projects/litterbot.html", "Litter Collection Rover"),
    ("projects/quadrotor.html", "Quadrotor Flight Controller"),
    ("projects/qcar.html",      "Perception-Aware Autonomous Vehicle"),
    ("projects/manipulator.html", "Vision-Based Robotic Manipulator"),
    ("projects/satellite.html", "Satellite Attitude Control"),
    ("projects/hydrogen.html",  "Green Hydrogen Grid Stabilization"),
    ("projects/steadifly.html", "SteadiFly Flight Stabilizer"),
]

RESUME = os.path.join(REPO, "files", "Dante_Benedetti_Resume.pdf")


def render(path, dest):
    url = f"{BASE}/{path}"
    cmd = [
        EDGE, "--headless", "--disable-gpu", "--no-sandbox",
        "--no-pdf-header-footer",
        f"--print-to-pdf={dest}",
        url,
    ]
    subprocess.run(cmd, capture_output=True, timeout=240)
    # Edge occasionally returns before the write lands
    for _ in range(20):
        if os.path.exists(dest) and os.path.getsize(dest) > 1000:
            return True
        time.sleep(0.5)
    return False


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT, exist_ok=True)

    rendered = []
    for path, title in PAGES:
        dest = os.path.join(OUT, path.replace("/", "_").replace(".html", ".pdf"))
        ok = render(path, dest)
        n = len(PdfReader(dest).pages) if ok else 0
        print(f"  {'ok ' if ok else 'FAIL'} {title:<38} {n:>2} pages")
        if ok:
            rendered.append((dest, title))

    if not rendered:
        print("nothing rendered"); return 1

    writer = PdfWriter()

    # resume leads the document
    if os.path.exists(RESUME):
        start = len(writer.pages)
        for p in PdfReader(RESUME).pages:
            writer.add_page(p)
        writer.add_outline_item("Resume", start)
        print(f"  ok  {'Resume (front matter)':<38} "
              f"{len(PdfReader(RESUME).pages):>2} pages")

    for dest, title in rendered:
        start = len(writer.pages)
        for p in PdfReader(dest).pages:
            writer.add_page(p)
        writer.add_outline_item(title, start)

    writer.add_metadata({
        "/Title": "Dante Benedetti - Engineering Portfolio",
        "/Author": "Dante Benedetti",
        "/Subject": "Autonomous systems, controls, robotics, and embedded engineering",
        "/Keywords": "electrical engineering, controls, robotics, ROS 2, STM32, "
                     "computer vision, state estimation",
    })

    final = os.path.join(OUT, "Dante_Benedetti_Portfolio.pdf")
    with open(final, "wb") as fh:
        writer.write(fh)

    size = os.path.getsize(final)
    print(f"\n  merged -> {final}")
    print(f"  {len(writer.pages)} pages, {size/1024/1024:.2f} MB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
