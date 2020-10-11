from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .models import Place


def place_detail_view(request, place_id: int):
    place = get_object_or_404(Place, id=place_id)
    images = place.images.all()
    context = {
        "title": place.title,
        "imgs": [image.image.url for image in images],
        "description_short": place.short_description,
        "description_long": place.detailed_description,
        "coordinates": {
            "lat": place.latitude_coord,
            "lng": place.longitude_coord
        }
    }

    return JsonResponse(context,
                        encoder=DjangoJSONEncoder,
                        safe=False,
                        json_dumps_params={
                            'ensure_ascii': False,
                            'indent': 2
                        })
