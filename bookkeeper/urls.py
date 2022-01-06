from django.urls import path

from bookkeeper.views import AccountListView

urlpatterns = [
    path('', AccountListView.as_view(), name='account-list'),
]
