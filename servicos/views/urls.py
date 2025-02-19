from django.urls import path, include
from rest_framework.routers import DefaultRouter
from views import cadastraEvento_viewset, statusEvento_viewset

router = DefaultRouter()
router.register(r'cadastraLivro', cadastraEvento_viewset)
router.register(r'statusLivro', statusEvento_viewset)

urlpatterns = [
    path('', include(router.urls)),
]
