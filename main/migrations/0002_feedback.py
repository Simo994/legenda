# Generated by Django 3.2.25 on 2025-01-16 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('subject', models.CharField(max_length=200, verbose_name='Тема')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')),
                ('is_read', models.BooleanField(default=False, verbose_name='Прочитано')),
            ],
            options={
                'verbose_name': 'Сообщение обратной связи',
                'verbose_name_plural': 'Сообщения обратной связи',
                'ordering': ['-created_at'],
            },
        ),
    ]
