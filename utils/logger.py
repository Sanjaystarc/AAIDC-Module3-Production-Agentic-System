import logging

def setup_logger():
    """
    Sets up application-wide logging
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )
    return logging.getLogger("agentic-system")
