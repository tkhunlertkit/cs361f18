# Generated by Django 2.1.3 on 2019-03-13 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_user_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='new2',
            field=models.CharField(default='default', max_length=10),
            preserve_default=False,
        ),
    ]