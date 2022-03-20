from django.core.exceptions import ValidationError
from rest_framework.generics import ListAPIView

from events_api.models import Event
from events_api.serializers import EventSerializer
from events_scraper_backend.exception_middleware import assert_valid


# Create your views here.
class EventAPI(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def filter_queryset(self, queryset):
        query_params = dict(self.request.GET.items())
        if 'order' in query_params:
            order = query_params.pop('order')
            order = order.split(',')
        try:
            queryset = queryset.filter(**query_params)
        except ValidationError as error:
            assert_valid(False, error.messages)
        
        if 'order' in query_params:
            queryset = queryset.order_by(*order)
        return queryset


