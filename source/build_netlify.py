"""Builds the Netlify folder (netlify/index.html) from template.html and data.json. Usage: python3 build_netlify.py"""
import json, pathlib
here = pathlib.Path(__file__).parent
out = here / "netlify"
out.mkdir(exist_ok=True)
data = json.loads((here / "data.json").read_text())
# No fixed URL: class links use whatever address the page is served from.
html = (here / "template.html").read_text().replace("__DATA__", json.dumps(data, ensure_ascii=False)).replace("__URL__", "")
# The template is an artifact page fragment; give it a full document head for a plain web host.
head = '<!doctype html>\n<html lang="en">\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
(out / "index.html").write_text(head + html + "\n</html>\n", encoding="utf-8")
print("Wrote", out / "index.html")
