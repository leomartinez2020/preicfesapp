# Generated by Django 4.1.3 on 2022-11-26 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='contenido',
            field=models.TextField(blank=True, null=True),
        ),
    ]
