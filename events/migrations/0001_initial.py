# Generated by Django 3.1.5 on 2021-01-31 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EventBloсk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('cost', models.DecimalField(decimal_places=0, default=0, max_digits=6)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bloсks', to='events.event')),
            ],
        ),
    ]
