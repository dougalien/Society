# The Perfect Society

A political philosophy game for grades 10 and 11. Students pick thinkers, answer 20 questions about the ideal society, press Analysis to see their percentage match against 21 philosophers, and explore a history timeline.

- Live version: https://claude.ai/artifact/LJeBpPeWnVLut19NuN1fRK (share it from the page's Share menu)
- Answer key for review: https://claude.ai/artifact/G2FJuHHDk3QbpZebN81Rjh

## Files

- `society-game.html`: the whole app in one file. Double-click to open it in a browser, or upload it to a school site or LMS.
- `data.py`: the answer key (thinkers, history, questions, and which thinkers match each answer). Edit this to change content.
- `sources.py`: citations. Links each thinker's position on each question to the chapter or passage where they say it, plus reading lists and the sources for the timeline facts. Free full texts wherever one exists.
- `lessons.py`: the Lessons tab. One entry per class worksheet (1.14 Hobbes & Locke, 1.15 Rousseau & Montesquieu, 2.2 Wollstonecraft): warm-up poll, which game questions to use, the witnessed/believed chart, primary source excerpts, apply-it scenarios, and the closing prompt. Copy an entry to add a lesson.
- `template.html`: the app's layout and code.
- `build.py`: rebuilds `society-game.html` from the other files.
- `data.json`: generated from `data.py`.

## Changing the questions or thinkers

```
python data.py
python build.py https://claude.ai/artifact/LJeBpPeWnVLut19NuN1fRK
```

## Class links

For a lesson, add `#lesson-` and the lesson number, for example `#lesson-1.14`. The Lessons tab has a Copy class link button for each one.


Add `#set-` and thinker codes to the end of the app's link so students start with only those thinkers, for example `#set-hob-loc-rou` for Hobbes, Locke and Rousseau. The teacher box on the start screen builds these for you.

## Netlify (public website)

The `netlify` folder holds `index.html`, the web version of the game. It works on any static host, and class links (`#set-...`) use the site's own address.

First time: sign in at https://app.netlify.com/drop and drag the `netlify` folder onto the page. Rename the site under Site configuration > Change site name.

To update later:

```
python data.py
python build_netlify.py
```

Then in Netlify open the site, go to Deploys, and drag the `netlify` folder onto the drop area at the bottom. The link stays the same.

## Streamlit (public website, alternative to Netlify)

The `streamlit` folder holds the Streamlit version: `streamlit_app.py`, `index.html` (the game) and `requirements.txt`. Class links there look like `https://your-app.streamlit.app/?go=lesson-1.14` or `?go=set-hob-loc-rou`; the teacher box and Lessons tab build them for you.

First time:
1. On GitHub, create a new repository (it can be public), then use Add file > Upload files to upload the three files from the `streamlit` folder.
2. Go to https://share.streamlit.io, sign in with GitHub, choose Create app, pick that repository, and set the main file to `streamlit_app.py`. Choose a site address, then Deploy.

To update later:

```
python data.py
python build_streamlit.py
```

Then upload the new `streamlit/index.html` to the GitHub repository. Streamlit redeploys on its own within a minute or two.
