from django.contrib import admin

from .models import Category, Location, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Настройка отображения модели Category в админке."""

    list_display = (
        "id",
        "title",
        "slug",
        "is_published",
        "created_at",
    )
    list_display_links = ("id", "title")
    search_fields = ("title", "description")
    list_filter = ("is_published", "created_at")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("created_at",)
    ordering = ("title",)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    """Настройка отображения модели Location в админке."""

    list_display = (
        "id",
        "name",
        "is_published",
        "created_at",
    )
    list_display_links = ("id", "name")
    search_fields = ("name",)
    list_filter = ("is_published", "created_at")
    readonly_fields = ("created_at",)
    ordering = ("name",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Настройка отображения модели Post в админке."""

    list_display = (
        "id",
        "title",
        "author",
        "category",
        "location",
        "pub_date",
        "is_published",
        "created_at",
    )
    list_display_links = ("id", "title")
    search_fields = ("title", "text", "author__username")
    list_filter = (
        "is_published",
        "category",
        "location",
        "author",
        "pub_date",
        "created_at",
    )
    readonly_fields = ("created_at",)
    date_hierarchy = "pub_date"
    ordering = ("-pub_date",)
    list_editable = ("is_published",)
    fieldsets = (
        (
            "Основная информация",
            {
                "fields": ("title", "text", "pub_date", "author"),
            },
        ),
        (
            "Дополнительные категории",
            {
                "fields": ("category", "location"),
            },
        ),
        (
            "Публикация",
            {
                "fields": ("is_published",),
            },
        ),
        (
            "Системные поля",
            {
                "fields": ("created_at",),
                "classes": ("collapse",),
            },
        ),
    )
