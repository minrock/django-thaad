# Generated by Django 3.0.5 on 2020-05-22 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interceptor', '0011_interceptorsession_creation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='interceptedrequest',
            name='matched_response',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='interceptor.InterceptorMockResponse'),
        ),
    ]
