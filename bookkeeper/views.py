from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from bookkeeper.models import Account, Transaction


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

class AccountDeleteView(LoginRequiredMixin, DeleteView):
    model = Account

    def get_success_url(self):
        return reverse('account-list')

class TransactionUpdateView(LoginRequiredMixin, UpdateView):
    model = Transaction 
    fields = ['description', 'amount', 'transaction_date', 'transaction_type']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('account-list')

class TransactionDeleteView(LoginRequiredMixin, DeleteView):
    model = Transaction 

    def get_success_url(self):
        return reverse('account-list')
