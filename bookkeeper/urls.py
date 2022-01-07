from django.urls import path

from bookkeeper.views import AccountListView, AccountCreateView, AccountUpdateView

urlpatterns = [
    path('', AccountListView.as_view(), name='account-list'),
    path('create/', AccountCreateView.as_view(), name='create-account-form'),
    path('edit/<pk>/', AccountUpdateView.as_view(), name='update-account-form'),
]
