from django.contrib import admin
from django.contrib.auth.models import Group

from .models import User

admin.site.site_header = "Администрирование Simple API"
admin.site.index_title = "Добро пожаловать в Администрирование сайта"
admin.site.site_title = "Simple API Административный портал"


@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
        "is_active",
    )
    list_filter = (
        "email",
        "username",
    )
    search_fields = (
        "email",
        "username",
    )
    ordering = ("id",)


admin.site.unregister(Group)
