# tickets urls.py
from django.urls import path

from tickets.views import TicketsViewList, TicketsViewCreate, TicketsViewUpdate, TicketDeleteView

urlpatterns = [
    path('list/', TicketsViewList.as_view(), name="tickets_list"),
    path('create/', TicketsViewCreate.as_view(), name="tickets_create"),
    path('update/<int:pk>/', TicketsViewUpdate.as_view(), name="tickets_update"),
    path('<pk>/delete/', TicketDeleteView.as_view(), name="tickets_delete"),
]