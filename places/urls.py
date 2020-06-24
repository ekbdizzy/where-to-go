from django.urls import path
from .views import place_detail_view

app_name = 'place'

urlpatterns = [
    path('<int:place_id>/', place_detail_view, name='place')
]
