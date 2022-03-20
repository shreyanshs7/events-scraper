from rest_framework.serializers import ModelSerializer

from events_api.models import Event

class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
