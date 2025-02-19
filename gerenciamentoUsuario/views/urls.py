from django.urls import path, include
from rest_framework.routers import DefaultRouter
from views import cadastrarPessoa_viewset, statusPessoa_viewset

router = DefaultRouter()
router.register(r'cadastraLivro', cadastrarPessoa_viewset)
router.register(r'statusLivro', statusPessoa_viewset)

urlpatterns = [
    path('', include(router.urls)),
]
