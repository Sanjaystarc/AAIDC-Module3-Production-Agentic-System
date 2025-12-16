from langgraph.graph import StateGraph

from agents.repo_analyzer import repo_analyzer_agent
from agents.metadata_agent import metadata_agent
from agents.reviewer_agent import reviewer_agent


def build_graph():
    """
    Builds and compiles the LangGraph multi-agent workflow
    """

    # Shared state is a dictionary
    graph = StateGraph(dict)

    # Add agents as nodes
    graph.add_node("repo_analyzer", repo_analyzer_agent)
    graph.add_node("metadata_agent", metadata_agent)
    graph.add_node("reviewer_agent", reviewer_agent)

    # Define execution flow
    graph.set_entry_point("repo_analyzer")
    graph.add_edge("repo_analyzer", "metadata_agent")
    graph.add_edge("metadata_agent", "reviewer_agent")
    graph.set_finish_point("reviewer_agent")

    return graph.compile()
