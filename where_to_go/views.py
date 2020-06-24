from django.views.generic import TemplateView
from places.models import Place


class MainView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        places_data = [place.get_geojson() for place in Place.objects.all()]
        places_dict = {
            "type": "FeatureCollection",
            "features": places_data
        }

        context['places_json'] = places_dict
        return self.render_to_response(context)
