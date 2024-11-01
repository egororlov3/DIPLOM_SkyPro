from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')

    phone = models.CharField(max_length=35, default='unknown', null=False, verbose_name='телефон')
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


class Reviews(models.Model):
    title = models.CharField(max_length=250, verbose_name='название')
    review = models.TextField(verbose_name='отзыв')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'
