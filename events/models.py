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
    blocks = models.ManyToManyField(EventBloсk, related_name='bookings',
                                    blank=False)
    users = models.ManyToManyField(User, related_name='bookings',
                                   blank=False)

    def get_event(self):
        event = self.blocks.first().event
        return event

    def __str__(self):
        event = self.get_event()
        blocks = [block.title for block in self.blocks.all()]
        blocks_title = ', '.join(blocks)
        users = [user.username for user in self.users.all()]
        users_names = ', '.join(users)
        return (f'регистрация №{self.pk} на мероприятие {event}: '
                f'выбранные блоки {blocks_title}. '
                f'пользователи: {users_names}')
