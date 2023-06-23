from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView
from .forms import TicketsForm
from .models import Tickets


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
        tickets = Tickets.objects.filter(user=request.user)
        form = TicketsForm()
        return render(request, 'tickets/dashboard_view.html', {'form': form, 'tickets': tickets})


class TicketsViewUpdate(UpdateView):

    form_class = TicketsForm
    model = Tickets
    template_name = "tickets/edit_ticket.html"
    context_object_name = 'task'

    def get_object(self, queryset=None):
        task_id = self.kwargs.get('pk')
        return get_object_or_404(Tickets, id=task_id)

    def form_valid(self, form):
        form.save()
        return redirect('tickets_list')

