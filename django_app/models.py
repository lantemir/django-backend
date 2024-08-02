from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

class TextModel(models.Model):
    author = models.ForeignKey(
        verbose_name='Автор',
        to=User,
        on_delete=models.CASCADE,
    )
    text = models.CharField(
        verbose_name='Текст',
        max_length = 500,
    )
    created_datetime = models.DateTimeField(
        default=timezone.now,
        verbose_name='Время создания'
    )

    class Meta:
        app_label = 'django_app'
        ordering = ('text',)
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'      

    def __str__(self):  # возвращает строкове представление объекта
        return f'{self.text[0:30:1]}'
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    def __str__(self):
        return f'{self.user.username} Profile'


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        # тут происходит первое создание модели
        Profile.objects.create(user=instance) 
