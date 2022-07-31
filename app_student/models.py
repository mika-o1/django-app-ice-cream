from django.contrib.auth.models import User
from django.db import models
from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator


# Create your models here.

class IceCreamCategory(models.Model):
    title = models.CharField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="Заголовок",
        verbose_name="Заголовок:",
        help_text='<small class="text-muted">это наш заголовок</small><hr><br>',

        max_length=250,
    )

    class Meta:
        app_label = 'app_student'
        ordering = ('title',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории мороженное'

    def __str__(self):  # возвращает строкове представление объекта
        return f'{self.title}'


class IceCreamLike(models.Model):
    like_value = models.IntegerField(  # BigIntegerField SmallIntegerField PositiveIntegerField ...
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="0",
        verbose_name="Like",
        help_text='<small class="text-muted">Like</small><hr><br>',

        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )
    user = models.ForeignKey(
        error_messages=False,
        primary_key=False,
        unique_for_date=False,
        unique_for_month=False,
        unique_for_year=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name='Пользователь',
        help_text='<small class="text-muted">Пользователь</small><hr><br>',

        to=User,
        on_delete=models.CASCADE,  # CASCADE SET_NULL DO_NOTHING
    )

    class Meta:
        app_label = 'app_student'
        ordering = ('like_value',)
        verbose_name = 'Лайк мороженного'
        verbose_name_plural = 'Лайки мороженного'

    def __str__(self):  # возвращает строкове представление объекта
        return f'{self.like_value}'


class IceCreamComment(models.Model):
    comment_text = models.CharField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="Текст комментария",
        verbose_name="Заголовок:",
        help_text='<small class="text-muted">Текст комментария</small><hr><br>',

        max_length=500,
    )
    user = models.ForeignKey(
        error_messages=False,
        primary_key=False,
        unique_for_date=False,
        unique_for_month=False,
        unique_for_year=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name='Пользователь',
        help_text='<small class="text-muted">Пользователь</small><hr><br>',

        to=User,
        on_delete=models.SET_NULL,  # CASCADE SET_NULL DO_NOTHING
    )

    class Meta:
        app_label = 'app_student'
        ordering = ('comment_text',)
        verbose_name = 'Комментарий к рецепту'
        verbose_name_plural = 'Комментарии к рецептам'

    def __str__(self):  # возвращает строкове представление объекта
        return f'{self.comment_text[:50:1]}'
