from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Sum

User = get_user_model()


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def summ(self):
        return sum([bloсk.cost for bloсk in self.bloсks.all()])
    # # @property
    # def summ(self):
    #     total = self.all().aggregate(valor=Sum('blocks'))
    #     return total.get('valor')

    def all_costs(self):
        pass

    def __str__(self):
        return self.title


class EventBloсk(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE,
                              related_name="bloсks")
    cost = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return self.title


class Booking(models.Model):
    block = models.ManyToManyField(EventBloсk, related_name='bookings')
    users = models.ManyToManyField(User, related_name='bookings')
