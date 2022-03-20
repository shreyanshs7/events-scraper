from django.db import models

# Create your models here.
class Event(models.Model):

    class Meta:
        db_table = 'events'

    website = models.CharField(max_length=255)
    name = models.CharField(max_length=1024)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return '<{}>'.format(self.name)
