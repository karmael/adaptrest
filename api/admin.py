import logging

from django.contrib import admin
from djangoql.admin import DjangoQLSearchMixin

from api.models import User

logger = logging.getLogger()


class BaseAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    ordering = ('id',)
    list_per_page = 10
    list_display = []
    readonly_fields = ['created_at', 'updated_at']


@admin.register(User)
class UserAdmin(BaseAdmin):
    ordering = ('google_id',)
    list_display = [f.name for f in User._meta.fields]
    readonly_fields = []
    can_delete = False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False
