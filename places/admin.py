from django.contrib import admin
from .models import Place, ImagesPlace


class ImagesPlaceInline(admin.TabularInline):
    model = ImagesPlace
    extra = 1


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
