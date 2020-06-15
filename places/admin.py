from django.contrib import admin
from .models import Place, ImagesPlace


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    class Meta:
        model = Place

    list_display = (
        'title',
    )


@admin.register(ImagesPlace)
class ImagesPlaceAdmin(admin.ModelAdmin):
    class Meta:
        model = ImagesPlace
