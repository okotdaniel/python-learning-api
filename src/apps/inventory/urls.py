from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RegisterAPIView, LoginAPIView, UserViewSet, LessonViewSet, 
    QuizQuestionViewSet, CodeChallengeViewSet, CodeExecutionView,
    CodeSnippetViewSet, UserProgressViewSet, CodeReviewViewSet
)

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('lessons', LessonViewSet)
router.register('quiz-questions', QuizQuestionViewSet)
router.register('challenges', CodeChallengeViewSet)
router.register('snippets', CodeSnippetViewSet)
router.register('progress', UserProgressViewSet, basename='progress')
router.register('code-reviews', CodeReviewViewSet, basename='code-reviews')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('execute-code/', CodeExecutionView.as_view(), name='execute-code'),
]

