from django.shortcuts import render
from .models import Zip
from .serializers import ZipSerializer
from rest_framework import viewsets


def vue_page(request):
    if request.method == "GET":
        return render(request, "vue-page.html")


def vanilla_page(request):
    if request.method == "GET":
        return render(request, "vanilla-page.html")


class ZipViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ZipSerializer
    
    def get_queryset(self):
        zip_code = self.request.query_params.get("zip_code")
        queryset = Zip.objects.filter(
            zip_code__startswith=zip_code
        )[:6]
        return queryset
