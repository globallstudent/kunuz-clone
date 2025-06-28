import logging
from celery import shared_task
from django.utils import timezone
from news.models import News

logger = logging.getLogger(__name__)

@shared_task
def publish_scheduled_news():
    now = timezone.now()
    # Find news scheduled for publish_at <= now and not active
    scheduled_news = News.objects.filter(is_active=False, publish_at__lte=now)
    count = scheduled_news.update(is_active=True)
    if count:
        logger.info(f"Published {count} scheduled news items at {now}.")
    return count
