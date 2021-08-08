# Generated by Django 3.1 on 2021-08-05 08:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animes', to=settings.AUTH_USER_MODEL),
        ),
    ]