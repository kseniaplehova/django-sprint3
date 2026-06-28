from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from core.models import PublishedModel, TimeStampedModel

from .constants import (
    MAX_LENGTH_NAME,
    MAX_LENGTH_SLUG,
    MAX_LENGTH_STR,
    MAX_LENGTH_TITLE,
)

User = get_user_model()


class PostQuerySet(models.QuerySet):
    """Кастомный QuerySet для модели Post."""

    def published(self):
        """Фильтрует только опубликованные посты."""
        return self.filter(
            is_published=True,
            category__is_published=True,
            pub_date__lte=timezone.now(),
        )

    def with_related(self):
        """Подгружает связанные объекты."""
        return self.select_related("author", "location", "category")

    def ordered(self):
        """Сортирует по дате публикации (новые сверху)."""
        return self.order_by("-pub_date")


class PostManager(models.Manager):
    """Менеджер модели Post."""

    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()

    def with_related(self):
        return self.get_queryset().with_related()

    def ordered(self):
        return self.get_queryset().ordered()


class Category(PublishedModel, TimeStampedModel):
    title = models.CharField(
        "Заголовок",
        max_length=MAX_LENGTH_TITLE,
    )
    description = models.TextField(
        "Описание",
    )
    slug = models.SlugField(
        "Идентификатор",
        max_length=MAX_LENGTH_SLUG,
        unique=True,
        help_text=(
            "Идентификатор страницы для URL; разрешены символы "
            "латиницы, цифры, дефис и подчёркивание."
        ),
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "Категории"
        ordering = ("title",)

    def __str__(self):
        return self.title


class Location(PublishedModel, TimeStampedModel):
    name = models.CharField(
        "Название места",
        max_length=MAX_LENGTH_NAME,
    )

    class Meta:
        verbose_name = "местоположение"
        verbose_name_plural = "Местоположения"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Post(PublishedModel, TimeStampedModel):
    title = models.CharField(
        "Заголовок",
        max_length=MAX_LENGTH_TITLE,
    )
    text = models.TextField(
        "Текст",
    )
    pub_date = models.DateTimeField(
        "Дата и время публикации",
        help_text=(
            "Если установить дату и время в будущем — можно "
            "делать отложенные публикации."
        ),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Автор публикации",
    )
    location = models.ForeignKey(
        "Location",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Местоположение",
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        verbose_name="Категория",
    )

    objects = PostManager()

    class Meta:
        verbose_name = "публикация"
        verbose_name_plural = "Публикации"
        ordering = ("-pub_date",)
        default_related_name = "posts"

    def __str__(self):
        return self.title[:MAX_LENGTH_STR]
