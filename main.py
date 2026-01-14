from graph.workflow import build_graph
from utils.logging_config import setup_logging
setup_logging()

logger = setup_logger()

def run_agents(payload: dict) -> dict:
    """
    Runs the LangGraph multi-agent workflow safely
    """
    try:
        logger.info("Starting multi-agent workflow")
        graph = build_graph()
        result = graph.invoke(payload)
        logger.info("Workflow completed successfully")
        return result
    except Exception as e:
        logger.error(f"Workflow failed: {e}")
        raise
