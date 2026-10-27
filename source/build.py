"""Builds society-game.html from template.html and data.json. Usage: python3 build.py [artifact_url]"""
import json, pathlib, sys
here = pathlib.Path(__file__).parent
data = json.loads((here / "data.json").read_text())
url = sys.argv[1] if len(sys.argv) > 1 else ""
html = (here / "template.html").read_text().replace("__DATA__", json.dumps(data, ensure_ascii=False)).replace("__URL__", url)
(here / "society-game.html").write_text(html)
