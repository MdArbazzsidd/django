# Generated by Django 5.0.6 on 2024-05-26 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0005_alter_chaiverity_pirce'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chaiverity',
            name='pirce',
            field=models.IntegerField(default=20),
        ),
    ]
