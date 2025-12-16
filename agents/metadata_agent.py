import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from tools.keyword_extractor import extract_keywords

def metadata_agent(state: dict) -> dict:
    """
    Agent: Metadata Recommender
    Uses Gemini LLM to suggest title and keywords
    """
    readme = state.get("readme", "")

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.4,
        google_api_key=os.getenv("GEMINI_API_KEY")
    )

    prompt = f"""
    You are an AI assistant helping improve AI project presentations.

    Based on the README below, suggest ONE concise project title.

    README:
    {readme}
    """

    response = llm.invoke([HumanMessage(content=prompt)])

    state["suggested_title"] = response.content.strip()
    state["suggested_tags"] = extract_keywords(readme)

    return state
