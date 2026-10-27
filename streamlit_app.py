"""The Perfect Society on Streamlit. The whole game is index.html; this file just shows it.

Class links look like ...streamlit.app/?go=lesson-1.14 or ?go=set-hob-loc-rou.
"""
import json, pathlib, re
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="The Perfect Society", page_icon="⚖️", layout="wide", initial_sidebar_state="collapsed")
st.markdown("<style>#MainMenu, header, footer {visibility: hidden;} .block-container {padding: 0 !important; max-width: 100% !important;}</style>", unsafe_allow_html=True)

html = (pathlib.Path(__file__).parent / "index.html").read_text(encoding="utf-8")
go = st.query_params.get("go", "")
go = go if re.fullmatch(r"(set|lesson)-[a-z0-9.-]+", go or "") else ""
base = (st.context.url or "").split("?")[0]
html = html.replace("__LINK_BASE__", base.rstrip("/") + "/?go=" if base.startswith("http") else "")
html = html.replace("<!--START-->", f"<script>window.START_HASH = {json.dumps('#' + go if go else '')};</script>")
components.html(html, height=1400, scrolling=True)
