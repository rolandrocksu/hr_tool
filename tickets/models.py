from django.db import models
from .choices import TicketStatusChoices
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Ticket(models.Model):
    class Meta:
        db_table = 'ticket'
        verbose_name = _('Ticket')
        verbose_name_plural = _('Tickets')

    title = models.CharField(max_length=255)
    description = models.TextField(max_length=2000)
    status = models.IntegerField(
        choices=TicketStatusChoices.choices,
        default=TicketStatusChoices.TODO
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
