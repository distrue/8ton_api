# Generated by Django 2.2.7 on 2019-11-09 20:38

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('meta', jsonfield.fields.JSONField(default={})),
                ('keywords', jsonfield.fields.JSONField(default={})),
                ('posts', jsonfield.fields.JSONField(default={})),
            ],
        ),
    ]
