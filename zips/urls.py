from django.urls import include, path
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'zips', views.ZipViewSet, basename='zips')

urlpatterns = [
    path("vue", views.vue_page, name='vue_page'),
    path("vanilla", views.vanilla_page, name='vanilla_page'),

    path("", include(router.urls)),
]
