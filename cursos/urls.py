from django.urls import path

from .views import CursoAPIview, AvaliacaoAPIView


urlpatterns = [
    path('cursos/', CursoAPIview.as_view(), name='cursos'),
    path('avaliacoes/', AvaliacaoAPIView.as_view(), name='avaliacoes'),
]