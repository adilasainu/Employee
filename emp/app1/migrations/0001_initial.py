# Generated by Django 5.1.1 on 2024-10-02 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp1',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('place', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('profile', models.ImageField(upload_to='images')),
                ('pdf', models.FileField(upload_to='pdf')),
            ],
        ),
    ]
