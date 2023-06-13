from django.views.generic import TemplateView

# -- TemplateView
class MainView(TemplateView):
    template_name = 'main.html'

class IntroduceView(TemplateView):
    template_name = 'introduce.html'