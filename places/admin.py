from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin

from .models import Place, ImagesPlace


class ImagesPlaceInline(SortableInlineAdminMixin, admin.TabularInline):
    model = ImagesPlace
    list_display = ('order', 'image', 'preview')
    readonly_fields = ('preview',)
    extra = 1

    def preview(self, obj):
        return format_html('<img src="{}" width=auto style=max-height:200px; />', obj.image.url)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    inlines = (ImagesPlaceInline,)


@admin.register(ImagesPlace)
class ImagesPlaceAdmin(admin.ModelAdmin):
    pass
