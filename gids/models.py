from django.db import models

class Channel(models.Model):
    CHANNELS_TYPE = (
        ('radio', 'Radio'),
        ('television','Television')
    )

    title = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    channel = models.IntegerField(default=1)
    

    start_date = models.DateTimeField('start_date')
    end_date = models.DateTimeField('end_date')

    channel_type = models.CharField(max_length=20,choices=CHANNELS_TYPE, unique=True)

    def __str__(self):
        return self.title
