# Generated by Django 4.2.5 on 2023-09-20 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_created_at_posts_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='AjaxList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('body', models.TextField()),
            ],
        ),
    ]
