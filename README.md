<p><a href="https://dougalien.com"><img src="assets/dougalien_systems_logo.png" alt="Dougalien Systems" height="48"></a></p>

# The Perfect Society

A [Dougalien Systems](https://dougalien.com) app. Live at https://society.streamlit.app/

A political philosophy game for grades 10 and 11. Students answer questions about the ideal society, see their match against 21 thinkers, explore a history timeline, follow every match to the thinker's own words, and play lesson rounds that go with the class worksheets.

This repository runs on Streamlit Community Cloud:

- `streamlit_app.py`: the Streamlit app (main file).
- `index.html`: the whole game.
- `requirements.txt`: what Streamlit installs.
- `dougalien_brand.py`, `assets/`, `.streamlit/config.toml`: the Dougalien Systems look, shared with the other Dougalien apps.

Class links: `?go=lesson-1.14` opens a lesson round, and `?go=set-hob-loc-rou` starts the game with only those thinkers. The teacher box and Lessons tab build these for you.

`source/` holds the files the game is built from. To change content, edit `source/data.py`, `source/sources.py` or `source/lessons.py`, then run `python data.py` and `python build_streamlit.py` there, and copy `streamlit/index.html` over `index.html` here.
