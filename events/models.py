from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Event(models.Model):
    """Мероприятие."""
    title = models.CharField(max_length=200)
    description = models.TextField()

    def total_cost(self):
        return sum([bloсk.cost for bloсk in self.bloсks.all()])

    def __str__(self):
        return self.title


class EventBloсk(models.Model):
    """Блоки мероприятия."""
    title = models.CharField(max_length=200)
    description = models.TextField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE,
                              related_name="bloсks")
    cost = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return self.title


class Booking(models.Model):
    """Регистрация пользователя на ммероприятие."""
    block = models.ManyToManyField(EventBloсk, related_name='bookings',
                                   null=False)
    user = models.ForeignKey(User, related_name='bookings',
                                on_delete=models.CASCADE)
