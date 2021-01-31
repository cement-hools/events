from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class EventBlok(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE,
                              related_name="bloks")
    cost = models.DecimalField(max_digits=6, decimal_places=0, default=0)


    def __str__(self):
        return self.title
