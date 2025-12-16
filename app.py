import streamlit as st
from utils.safety import validate_input
from main import run_agents

st.set_page_config(
    page_title="Agentic AI Project Reviewer",
    layout="centered"
)

st.title("🤖 Agentic AI Project Reviewer")
st.write("AAIDC Module 3 — Production-Ready Multi-Agent System")

readme_text = st.text_area(
    "Paste README or project description:",
    height=250,
    placeholder="Paste README.md content here..."
)

if st.button("Analyze"):
    try:
        clean_text = validate_input(readme_text)
        result = run_agents({"readme": clean_text})

        st.subheader("📘 Results")
        st.write("**Suggested Title:**", result.get("suggested_title"))
        st.write("**Suggested Tags:**", result.get("suggested_tags"))
        st.write("**Review Feedback:**", result.get("review_feedback"))

    except Exception as e:
        st.error(str(e))
