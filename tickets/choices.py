from lib.model_fields import CustomIntegerChoices


class TicketstatusChoices(CustomIntegerChoices):

    TODO = 1, 'todo'
    IN_PROGRESS = 2, 'in_progress'
    DONE = 3, 'done'
