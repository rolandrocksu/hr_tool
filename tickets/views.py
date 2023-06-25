from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView
from .forms import TicketsForm
from .models import Ticket
from .choices import TicketStatusChoices


class TicketsViewCreate(CreateView):

    form_class = TicketsForm

    def post(self, request, **kwargs):
        form = TicketsForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('tickets_list')


class TicketsViewList(ListView):

    def get(self, request, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')
        tickets = Ticket.objects.filter(user=request.user)
        form = TicketsForm()
        return render(
            request,
            'tickets/dashboard_view.html',
            {
                'form': form,
                'tickets': tickets,
                'tickets_status': TicketStatusChoices
            }
        )


class TicketsViewUpdate(UpdateView):

    form_class = TicketsForm
    model = Ticket
    template_name = "tickets/edit_ticket.html"
    context_object_name = 'task'

    def get_initial(self):
        initial = super().get_initial()
        obj = self.get_object()
        initial['title'] = obj.title
        initial['description'] = obj.description
        initial['status'] = obj.status
        return initial

    def get_object(self, queryset=None):
        task_id = self.kwargs.get('pk')
        return get_object_or_404(Ticket, id=task_id)

    def form_valid(self, form):
        form.save()
        return redirect('tickets_list')
