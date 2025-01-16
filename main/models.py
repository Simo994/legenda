from django.db import models

# Create your models here.

class Reservation(models.Model):
    name = models.CharField('Имя', max_length=100)
    phone = models.CharField('Телефон', max_length=20)
    email = models.EmailField('Email')
    date = models.DateField('Дата')
    time = models.TimeField('Время')
    guests = models.IntegerField('Количество гостей')
    message = models.TextField('Сообщение', blank=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} - {self.date} {self.time}'

class Feedback(models.Model):
    name = models.CharField('Имя', max_length=100)
    email = models.EmailField('Email')
    subject = models.CharField('Тема', max_length=200, default='Обратная связь')
    message = models.TextField('Сообщение')
    created_at = models.DateTimeField('Дата отправки', auto_now_add=True)
    is_read = models.BooleanField('Прочитано', default=False)

    class Meta:
        verbose_name = 'Сообщение обратной связи'
        verbose_name_plural = 'Сообщения обратной связи'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} - {self.subject}'
