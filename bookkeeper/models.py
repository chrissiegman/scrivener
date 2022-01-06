from django.db import models


class Account(models.Model):

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    account_name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    creation_date = models.DateTimeField('creation date')
    initial_balance = models.DecimalField(max_digits=6, decimal_places=2)

class Transaction(models.Model):

    CREDIT = 'C'
    DEBIT = 'D'
    TRANSACTION_TYPES = [
        (CREDIT, 'credit'),
        (DEBIT, 'debit'),
    ]

    account = models.ForeignKey('Account', on_delete=models.CASCADE)    
    description = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    transaction_date = models.DateTimeField('date')

    # there's probably a more appropriate way to handle this...
    transaction_type = models.CharField(
        max_length=1,
        choices=TRANSACTION_TYPES,
        default=DEBIT,
    )


    
