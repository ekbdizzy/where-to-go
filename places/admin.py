from django.contrib import admin
from .models import Place


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )

    class Meta:
        model = Place

    def __str__(self):
        return self.title
