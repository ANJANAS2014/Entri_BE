# Generated by Django 4.1.dev20211230073804 on 2021-12-30 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(blank=True, max_length=30)),
                ('middlename', models.CharField(blank=True, max_length=30, null=True)),
                ('lastname', models.CharField(blank=True, max_length=30, null=True)),
                ('starttime', models.TimeField()),
                ('endtime', models.TimeField()),
                ('is_interviewer', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddConstraint(
            model_name='users',
            constraint=models.UniqueConstraint(fields=('firstname', 'middlename', 'lastname'), name='unique_name'),
        ),
    ]
