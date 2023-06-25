from lib.model_fields import CustomIntegerChoices
from django.utils.translation import gettext_lazy as _


class TicketStatusChoices(CustomIntegerChoices):

    TODO = 1, _('To do')
    IN_PROGRESS = 2, _('In Progress')
    DONE = 3, _('Done')
