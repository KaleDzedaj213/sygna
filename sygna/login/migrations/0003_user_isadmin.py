# Generated by Django 4.1.7 on 2023-03-31 13:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("login", "0002_alter_user_email_alter_user_table"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="isAdmin",
            field=models.BooleanField(default=False),
        ),
    ]
