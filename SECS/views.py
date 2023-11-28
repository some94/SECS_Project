from django.views.generic import View, TemplateView
from django.shortcuts import render


# -- TemplateView
class MainView(TemplateView):
    template_name = 'main.html'


# class MainView(View):
#     def get(self, request):
#         return render(request, 'main.html')
#
#     def post(self, request):
#         token = request.session.get('token', None)
#         name = request.session.get('name', None)
#
#         if token is not None:
#             return render(request, 'main.html', token)


class IntroduceView(TemplateView):
    template_name = 'introduce.html'
