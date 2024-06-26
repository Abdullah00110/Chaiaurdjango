# Generated by Django 5.0.6 on 2024-05-30 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0003_chaivariety_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=500)),
            ],
        ),
    ]
