from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView, View


class HomePage(TemplateView):
    template_name = "upload.html"


class UploadPage(View):
    def post(self, request):
        x = 1
        pass


