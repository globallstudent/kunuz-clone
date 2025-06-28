import logging
from celery import shared_task

logger = logging.getLogger(__name__)

@shared_task
def test_celery_logging_task():
    logger.info("Celery test task executed!")
    return "Task completed and logged."
