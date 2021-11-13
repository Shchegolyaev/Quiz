from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from .views import QuestionViewSet, QuizViewSet

router = routers.DefaultRouter()

router.register(r'quiz', QuizViewSet)
router.register(r'question', QuestionViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]
