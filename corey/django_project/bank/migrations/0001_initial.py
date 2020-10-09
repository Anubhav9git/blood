# Generated by Django 2.0.6 on 2020-10-05 19:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='bankreq',
            fields=[
                ('Hospital_Name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Address', models.CharField(max_length=100)),
                ('contact', models.IntegerField(max_length=10)),
                ('Units_of_A_Positive', models.IntegerField(max_length=2)),
                ('Units_of_A_Negative', models.IntegerField(max_length=2)),
                ('Units_of_B_Positive', models.IntegerField(max_length=2)),
                ('Units_of_B_Negative', models.IntegerField(max_length=2)),
                ('Units_of_O_Positive', models.IntegerField(max_length=2)),
                ('Units_of_O_Negative', models.IntegerField(max_length=2)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
