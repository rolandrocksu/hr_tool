from django.contrib import admin
from .models import Ticket


# Register your models here.
@admin.register(Ticket)
class TicketsAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at')
