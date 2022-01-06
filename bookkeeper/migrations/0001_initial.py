# Generated by Django 4.0.1 on 2022-01-06 19:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=50)),
                ('creation_date', models.DateTimeField(verbose_name='creation date')),
                ('initial_balance', models.DecimalField(decimal_places=2, max_digits=6)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('transaction_date', models.DateTimeField(verbose_name='date')),
                ('transaction_type', models.CharField(choices=[('C', 'credit'), ('D', 'debit')], default='D', max_length=1)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookkeeper.account')),
            ],
        ),
    ]