# Generated by Django 4.1.3 on 2022-12-23 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('N͓̽a͓̽m͓̽e͓̽', models.CharField(max_length=100)),
                ('քɦօռɛ', models.CharField(max_length=12)),
            ],
        ),
    ]
