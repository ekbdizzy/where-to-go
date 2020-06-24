from django.contrib import admin
from django.utils.html import format_html

from .models import Place, ImagesPlace


class ImagesPlaceInline(admin.TabularInline):
    model = ImagesPlace
    extra = 1

    readonly_fields = ('preview',)
    fields = ('image', 'preview')

    def preview(self, obj):
        h = 'max-height:200px;'
        return format_html(f'<img src="{obj.image.url}" width=auto style={h} />')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    class Meta:
        model = Place

    list_display = (
        'title',
    )

    inlines = (ImagesPlaceInline,)


@admin.register(ImagesPlace)
class ImagesPlaceAdmin(admin.ModelAdmin):
    class Meta:
        model = ImagesPlace
