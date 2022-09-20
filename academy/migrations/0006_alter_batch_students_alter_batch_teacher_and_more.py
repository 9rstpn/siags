# Generated by Django 4.0.4 on 2022-06-27 19:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('academy', '0005_batch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='students', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='batch',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='plan',
            name='messages',
            field=models.ManyToManyField(blank=True, to='academy.planmessage'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='electives',
            field=models.ManyToManyField(blank=True, related_name='semester_elective', to='academy.course'),
        ),
    ]
