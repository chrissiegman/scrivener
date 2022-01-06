from django.urls import path

from bookkeeper.views import AccountListView, AccountCreateView

urlpatterns = [
    path('', AccountListView.as_view(), name='account-list'),
    path('create/', AccountCreateView.as_view(), name='account-form'),
]
