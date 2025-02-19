from django.urls import path, include
from rest_framework.routers import DefaultRouter
from views import cadastraLivro_viewset, statusLivro_viewset

router = DefaultRouter()
router.register(r'cadastraLivro', cadastraLivro_viewset)
router.register(r'statusLivro', statusLivro_viewset)

urlpatterns = [
    path('', include(router.urls)),
]
