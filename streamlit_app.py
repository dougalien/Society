"""The Perfect Society on Streamlit, a Dougalien Systems app. The whole game is index.html; this file just shows it.

Class links look like ...streamlit.app/?go=lesson-1.14 or ?go=set-hob-loc-rou.
"""
import json, pathlib, re
import streamlit as st
import streamlit.components.v1 as components
import dougalien_brand as brand

st.set_page_config(page_title="The Perfect Society • Dougalien Systems", page_icon=brand.page_icon("⚖️"), layout="wide", initial_sidebar_state="collapsed")
brand.apply_branding()
# The game fills the page under the branded header
st.html("<style>.block-container {padding: 3.75rem 0 0 !important; max-width: 100% !important;} footer {visibility: hidden;}</style>")

html = (pathlib.Path(__file__).parent / "index.html").read_text(encoding="utf-8")
go = st.query_params.get("go", "")
go = go if re.fullmatch(r"(set|lesson)-[a-z0-9.-]+", go or "") else ""
base = (st.context.url or "").split("?")[0]
html = html.replace("__LINK_BASE__", base.rstrip("/") + "/?go=" if base.startswith("http") else "")
# Light only, like the Streamlit theme around it (.streamlit/config.toml)
html = html.replace("<!--START-->", f"<script>window.START_HASH = {json.dumps('#' + go if go else '')}; document.documentElement.dataset.theme = 'light';</script>")
components.html(html, height=1400, scrolling=True)
