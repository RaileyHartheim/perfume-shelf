from django.db import models
from .choices import (
    GENDER_CHOICES,
    PERFUME_GROUP_CHOICES,
    SEASON_CHOICES,
    USAGE_CHOICES
)


class Perfume(models.Model):
    perfume_name = models.CharField(
        verbose_name='Название аромата',
        max_length=255,
        blank=False
    )
    brand = models.CharField(
        verbose_name='Бренд',
        max_length=255,
        blank=False
    )
    gender = models.CharField(
        verbose_name='Пол',
        choices=GENDER_CHOICES,
        default='Uncathegorized',
        max_length=50
    )
    perfume_group = models.CharField(
        verbose_name='Парфюмерное семейство',
        choices=PERFUME_GROUP_CHOICES,
        default='Uncathegorized',
        max_length=200
    )
    season = models.CharField(
        verbose_name='Сезонность',
        choices=SEASON_CHOICES,
        default='Uncathegorized',
        max_length=50
    )
    usage = models.CharField(
        verbose_name='Когда используется',
        choices=USAGE_CHOICES,
        default='Uncathegorized',
        max_length=100
    )
    top_notes = models.CharField(
        verbose_name='Верхние ноты',
        max_length=500,
        blank=True
    )
    middle_notes = models.CharField(
        verbose_name='Средние ноты',
        max_length=500,
        blank=True
    )
    base_notes = models.CharField(
        verbose_name='Ноты сердца',
        max_length=500,
        blank=True
    )
    image_url = models.URLField(
        verbose_name='Ссылка на изображение',
        default='/static/img/defaultimage.jpg'
    )
    have_it = models.BooleanField(
        verbose_name='Есть',
        default=False
    )
    had_it = models.BooleanField(
        verbose_name='Был',
        default=False
    )
    want_it = models.BooleanField(
        verbose_name='Хочу приобрести',
        default=False
    )
    test_it = models.BooleanField(
        verbose_name='Нужно попробовать',
        default=False
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['perfume_name', 'brand'],
                                    name='unique_perfume')
        ]
        ordering = ('pk',)
        verbose_name = 'Парфюм'

    def __str__(self):
        return f'{self.brand} — {self.perfume_name}'


class Comment(models.Model):
    perfume = models.ForeignKey(
        Perfume,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Парфюм'
    )
    text = models.TextField(
        verbose_name='Заметка',
        help_text='Здесь можно ввести текст заметки'
    )
    created = models.DateTimeField(
        verbose_name='Дата написания заметки',
        auto_now_add=True
    )

    class Meta:
        ordering = ('created',)
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
