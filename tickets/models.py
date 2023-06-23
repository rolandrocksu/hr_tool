from django.db import models
from .choices import TicketstatusChoices
from django.contrib.auth.models import User
# Create your models here.


class Tickets(models.Model):

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=2000)
    status = models.IntegerField(
        choices=TicketstatusChoices.choices,
        default=TicketstatusChoices.TODO
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')

    def __str__(self) -> str:
        return self.title
