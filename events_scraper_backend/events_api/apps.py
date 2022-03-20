from django.apps import AppConfig

class EventsApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'events_api'

    def ready(self) -> None:
        super().ready()
        from django_q.tasks import async_task

        # Run background task to scrape events data parallely
        # async_task('events_api.workers.techmeme_events_scraper')
        # async_task('events_api.workers.computerworld_events_scraper')
