from django.views.generic import TemplateView


class EmberView(TemplateView):
    template_name = 'ember_client/ember_client.html'

ember_view = EmberView.as_view()
