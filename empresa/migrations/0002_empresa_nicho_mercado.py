# Generated by Django 4.1.3 on 2022-11-09 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("empresa", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="empresa",
            name="nicho_mercado",
            field=models.CharField(
                choices=[
                    ("M", "Marketing"),
                    ("N", "Nutrição"),
                    ("D", "Design"),
                    ("T", "Tecnologia"),
                ],
                default=1,
                max_length=4,
            ),
            preserve_default=False,
        ),
    ]
