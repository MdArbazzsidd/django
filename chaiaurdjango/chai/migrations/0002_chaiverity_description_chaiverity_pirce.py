# Generated by Django 5.0.6 on 2024-05-26 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaiverity',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='chaiverity',
            name='pirce',
            field=models.IntegerField(choices=[('20', '20'), ('50', '50'), ('60', '60'), ('100', '100'), ('160', '160')], default=20),
        ),
    ]
