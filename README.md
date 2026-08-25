# dantebenedetti.com

Source for my engineering portfolio — [dantebenedetti.com](https://dantebenedetti.com).

Static HTML, CSS, and vanilla JavaScript. No build step, no dependencies.
Served by GitHub Pages from `main` at the repository root.

---

## Sections

| Page | Live URL | Source |
|---|---|---|
| Home | [dantebenedetti.com](https://dantebenedetti.com) | [`index.html`](index.html) |
| Litter Collection Rover | [/projects/litterbot.html](https://dantebenedetti.com/projects/litterbot.html) | [`projects/litterbot.html`](projects/litterbot.html) |
| Quadrotor Flight Controller | [/projects/quadrotor.html](https://dantebenedetti.com/projects/quadrotor.html) | [`projects/quadrotor.html`](projects/quadrotor.html) |
| Perception-Aware Autonomous Vehicle | [/projects/qcar.html](https://dantebenedetti.com/projects/qcar.html) | [`projects/qcar.html`](projects/qcar.html) |
| Vision-Based Robotic Manipulator | [/projects/manipulator.html](https://dantebenedetti.com/projects/manipulator.html) | [`projects/manipulator.html`](projects/manipulator.html) |
| Reaction-Wheel Satellite Attitude Control | [/projects/satellite.html](https://dantebenedetti.com/projects/satellite.html) | [`projects/satellite.html`](projects/satellite.html) |
| Green Hydrogen Grid Stabilization | [/projects/hydrogen.html](https://dantebenedetti.com/projects/hydrogen.html) | [`projects/hydrogen.html`](projects/hydrogen.html) |
| SteadiFly Flight Stabilizer | [/projects/steadifly.html](https://dantebenedetti.com/projects/steadifly.html) | [`projects/steadifly.html`](projects/steadifly.html) |

## Downloads served by the site

| File | Link |
|---|---|
| Résumé | [/files/Dante_Benedetti_Resume.pdf](https://dantebenedetti.com/files/Dante_Benedetti_Resume.pdf) |
| LitterBot final report | [/files/LitterBot_Final_Report.pdf](https://dantebenedetti.com/files/LitterBot_Final_Report.pdf) |
| SteadiFly report | [/files/SteadiFly_Report.pdf](https://dantebenedetti.com/files/SteadiFly_Report.pdf) |
| Satellite attitude control report | [/files/Satellite_Attitude_Control_Report.pdf](https://dantebenedetti.com/files/Satellite_Attitude_Control_Report.pdf) |
| Satellite attitude control presentation | [/files/Satellite_Attitude_Control_Presentation.pdf](https://dantebenedetti.com/files/Satellite_Attitude_Control_Presentation.pdf) |
| SteadiFly source | [/files/SteadiFly_Source.zip](https://dantebenedetti.com/files/SteadiFly_Source.zip) |

## Related repositories

| Project | Repository |
|---|---|
| Litter Collection Rover | [benjam1ntavares/LitterBot_Official](https://github.com/benjam1ntavares/LitterBot_Official) |

---

## Layout

```
.
├── index.html              home: hero, about, projects, education, experience, contact
├── projects/               one detail page per project
├── css/style.css           single stylesheet; design tokens are the :root block at the top
├── js/main.js              mobile nav toggle + scroll reveal
├── images/                 one folder per project
│   ├── litterbot/  drone/  qcar/  manipulator/  werc/  steadifly/
│   └── headshot.jpg
├── files/                  publicly downloadable documents
└── CNAME                   custom domain record
```

### `files/` is allow-listed

Everything in `files/` is served publicly, so `.gitignore` blocks the whole
directory and re-admits individual documents by name:

```gitignore
files/*
!files/Dante_Benedetti_Resume.pdf
!files/LitterBot_Final_Report.pdf
```

Working material kept in that folder — source reports, transcripts, lab
write-ups — therefore stays local. **To publish a new document, add a matching
`!files/<name>` line.** Nothing else there will ever reach the web.

Raw camera video and full-resolution source photos are ignored for the same
reason: originals run 100–270 MB, past GitHub's 100 MB per-file limit. Only the
transcoded copies are tracked.

---

## Conventions

**Assets are versioned.** Stylesheet and script links carry a `?v=N` query.
Bump `N` in every HTML file when either changes, or returning visitors keep a
cached copy:

```bash
for f in index.html projects/*.html; do
  sed -i 's/v=14/v=15/g' "$f"
done
```

**Design tokens** live in the `:root` block at the top of `css/style.css` —
accent colours, ink, rules, and surfaces. Change them there, not inline.

**Images** are capped at `33vh` so no figure dominates the viewport, and every
`<img>` carries explicit `width`/`height` to prevent layout shift.

**The scroll reveal fails open.** CSS hides a section only while `<html>`
carries `js-reveal`, which `js/main.js` adds at runtime and removes again if
the IntersectionObserver has not reported shortly after load. If JavaScript
breaks, the page still renders.

**Third-party images.** `images/qcar/` and `images/manipulator/arm-hardware.jpg`
hold vendor product photography from Quanser and ROBOTIS, used to show the
platforms worked on. `images/satellite/reaction-wheel.jpg` and
`images/satellite/satellite-orbit.jpg` are NASA/JPL-Caltech public-domain
photographs, credited in their captions. Everything else is my own.

---

## Building the PDF portfolio

Some applications want a portfolio file rather than a link. `tools/build_portfolio.py`
prints every page of the site through headless Edge and merges the results, with the
resume in front and a bookmark per project:

```bash
python -m http.server 8123          # serve the site first
python tools/build_portfolio.py     # then render and merge
```

The output lands in the script's `portfolio/` folder as
`Dante_Benedetti_Portfolio.pdf`.

Print layout is controlled by the `@media print` block at the end of
`css/style.css`. It hides navigation and calls to action, forces the scroll
reveal visible, caps figures at 2.9in, and restores the multi-column grids —
a Letter page is only about 700px wide, which would otherwise trip the mobile
breakpoint and stack everything into one column. Video cannot embed in a PDF,
so `js/main.js` appends a print-only line under each clip giving its address.

## Local preview

```bash
python -m http.server 8000
```

Then open <http://localhost:8000>.

## Deploying

Push to `main`. GitHub Pages rebuilds automatically; a change is usually live
within a minute.
