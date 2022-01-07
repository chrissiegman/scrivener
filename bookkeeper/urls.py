from django.urls import path

from bookkeeper.views import AccountListView, AccountCreateView, AccountUpdateView, AccountDeleteView, TransactionUpdateView, TransactionDeleteView, TransactionCreateView

urlpatterns = [
    path('', AccountListView.as_view(), name='account-list'),
    path('account/create/', AccountCreateView.as_view(), name='create-account-form'),
    path('account/edit/<pk>/', AccountUpdateView.as_view(), name='update-account-form'),
    path('account/delete/<pk>/', AccountDeleteView.as_view(), name='delete-account-form'),
    path('account/<int:account_id>/transaction/create/', TransactionCreateView.as_view(), name='create-transaction-form'),
    path('transaction/edit/<pk>/', TransactionUpdateView.as_view(), name='update-transaction-form'),
    path('transaction/delete/<pk>/', TransactionDeleteView.as_view(), name='delete-transaction-form'),
]
