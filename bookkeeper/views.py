from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from bookkeeper.models import Account


class AccountListView(LoginRequiredMixin, ListView):

    model = Account

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accounts'] = Account.objects.filter(user=self.request.user.pk)
        return context

class AccountCreateView(LoginRequiredMixin, CreateView):
    model = Account
    fields = ['account_name', 'description', 'initial_balance', 'creation_date']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('account-list')


class AccountUpdateView(LoginRequiredMixin, UpdateView):
    model = Account
    fields = ['account_name', 'description', 'initial_balance', 'creation_date']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('account-list')
