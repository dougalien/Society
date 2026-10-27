"""Builds the Streamlit folder (streamlit/index.html) from template.html and data.json. Usage: python3 build_streamlit.py

streamlit/streamlit_app.py shows index.html and fills in the class-link address when the app runs."""
import json, pathlib
here = pathlib.Path(__file__).parent
out = here / "streamlit"
out.mkdir(exist_ok=True)
data = json.loads((here / "data.json").read_text())
html = (here / "template.html").read_text().replace("__DATA__", json.dumps(data, ensure_ascii=False)).replace("__URL__", "__LINK_BASE__")
head = '<!doctype html>\n<html lang="en">\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n<!--START-->\n'
(out / "index.html").write_text(head + html + "\n</html>\n", encoding="utf-8")
print("Wrote", out / "index.html")
