from django.views.generic.list import ListView

from bookkeeper.models import Account


class AccountListView(ListView):

    model = Account

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accounts'] = Account.objects.filter(user=self.request.user.pk)
        return context

