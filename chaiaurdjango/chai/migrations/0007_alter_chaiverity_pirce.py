# Generated by Django 5.0.6 on 2024-05-26 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0006_alter_chaiverity_pirce'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chaiverity',
            name='pirce',
            field=models.IntegerField(default=0),
        ),
    ]
