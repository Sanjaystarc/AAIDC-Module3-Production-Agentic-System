import time
import random
import logging

logger = logging.getLogger(__name__)

def retry_with_exponential_backoff(func, retries=3, base_delay=1, max_delay=10):
    for attempt in range(retries):
        try:
            return func()
        except Exception as e:
            logger.error(f"Retry {attempt+1} failed: {e}")
            if attempt == retries - 1:
                raise
            sleep_time = min(base_delay * (2 ** attempt) + random.uniform(0, 0.5), max_delay)
            time.sleep(sleep_time)
