# from django.shortcuts import render
# from rest_framework import views, response, status, request
# from .serializers import ProductSerializer
# from .models import Product


# import csv
# import mimetypes
# from functools import reduce
# from operator import and_

# from django.conf import settings
# from django.contrib.auth import authenticate
# from django.contrib.auth.decorators import login_required
# from django.core.mail import EmailMultiAlternatives
# from django.core.paginator import Paginator
# from django.db import IntegrityError
# from django.db.models import Q, Value
# from django.db.models.functions import Concat
# from django.http import Http404, JsonResponse, HttpResponse
# from django.shortcuts import render
# from django.template.loader import render_to_string
# from django.urls import reverse
# from django.utils.decorators import method_decorator
# from django.utils.html import strip_tags
# from django.views import View
# from drf_yasg import openapi
# from drf_yasg.utils import swagger_auto_schema
# from rest_framework import status
# from rest_framework.authtoken.models import Token
# from rest_framework.decorators import permission_classes, api_view
# from rest_framework.generics import GenericAPIView
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.pagination import PageNumberPagination
# from rest_framework.exceptions import NotFound
# from django.db.models import Count
# from django.http import HttpResponse
# import io


# class CreateProductView(GenericAPIView):
#     serializer_class = ProductSerializer
#     # permission_classes = [IsAuthenticated & (IsAdmin | IsSchoolAdmin | IsAdmin)]

#     @swagger_auto_schema(
#         operation_description='Create a new product.',
#         tags=['Product management'],
#     )
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data)
#         data = {}
#         if serializer.is_valid():
          
#             try:
#                 serializer.save()
#             except IntegrityError as ex:
#                 return Response({'error': ex.args}, status=status.HTTP_400_BAD_REQUEST)

#             data['status'] = status.HTTP_201_CREATED
#             data['message'] = f"Product added successfully."
#             data['data'] = serializer.data
#             return Response(data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class UpdateProductView(views.APIView):
#     serializer_class = ProductSerializer
#     # permission_classes = [IsAuthenticated]

#     @swagger_auto_schema(
#         operation_description='Update the details of logged in user.',
#         tags=['Product management'],
#     )
#     def put(self, request, *args, **kwargs):
        
#         data, product = {}, Product.objects.filter(id=kwargs("id")).user

#         serializer = self.serializer_class(product, data=request.data)

#         if serializer.is_valid():
#             try:
#                 serializer.save()
#             except IntegrityError as ex:
#                 return Response({'error': ex.args}, status=status.HTTP_400_BAD_REQUEST)
#             data['data'] = self.serializer_class(product).data
#             return Response(data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ViewProducts(views.APIView):
#     serializer_class = ProductSerializer 
#     # permission_classes = [IsAuthenticated & (IsAdmin | IsSchoolAdmin)]

#     @swagger_auto_schema(
#         operation_description='Returns the content of a single user.',
#         tags=['Product management'],
#     )
#     def get(self, request, *args, **kwargs):

#         data, product = {}, self.serializer_class(Product.objects.all())
#         data['status'] = 200
#         data['data'] = ProductSerializer(product).data
#         return Response(data)


# class ViewProductsById(views.APIView):
#     serializer_class = ProductSerializer 
#     # permission_classes = [IsAuthenticated & (IsAdmin | IsSchoolAdmin)]

#     @staticmethod
#     def get_user_object(pk):
#         try:
#             return Product.objects.get(pk=pk)
#         except Product.DoesNotExist:
#             raise Http404

#     @swagger_auto_schema(
#         operation_description='Returns the content of a single user.',
#         tags=['Product management'],
#     )
#     def get(self, request, *args, **kwargs):
#         data, product = {}, self.get_user_object(kwargs.get('pk'))
#         data['status'] = 200
#         data['data'] = ProductSerializer(product).data
#         return Response(data)


# class DeleteProductView(views.APIView):
#     pass 




from rest_framework import viewsets, permissions, status, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import (
    Lesson, QuizQuestion, CodeChallenge, CodeSnippet,
    UserProgress, CodeReview
)
from .serializers import (
    UserSerializer, RegisterSerializer, LessonSerializer, 
    QuizQuestionSerializer, CodeChallengeSerializer, 
    CodeChallengeDetailSerializer, CodeSnippetSerializer, 
    UserProgressSerializer, CodeReviewSerializer
)
import subprocess
import tempfile
import os

class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

class LoginAPIView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
            'email': user.email
        })

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return User.objects.all()
        return User.objects.filter(id=user.id)

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=['get'])
    def by_category(self, request):
        category = request.query_params.get('category', None)
        if category:
            lessons = self.queryset.filter(category=category)
            serializer = self.get_serializer(lessons, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def by_difficulty(self, request):
        difficulty = request.query_params.get('difficulty', None)
        if difficulty:
            lessons = self.queryset.filter(difficulty=difficulty)
            serializer = self.get_serializer(lessons, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class QuizQuestionViewSet(viewsets.ModelViewSet):
    queryset = QuizQuestion.objects.all()
    serializer_class = QuizQuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = QuizQuestion.objects.all()
        lesson_id = self.request.query_params.get('lesson_id', None)
        if lesson_id is not None:
            queryset = queryset.filter(lesson_id=lesson_id)
        return queryset

class CodeChallengeViewSet(viewsets.ModelViewSet):
    queryset = CodeChallenge.objects.all()
    serializer_class = CodeChallengeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return CodeChallengeDetailSerializer
        return CodeChallengeSerializer

    @action(detail=False, methods=['get'])
    def by_category(self, request):
        category = request.query_params.get('category', None)
        if category:
            challenges = self.queryset.filter(category=category)
            serializer = self.get_serializer(challenges, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def by_difficulty(self, request):
        difficulty = request.query_params.get('difficulty', None)
        if difficulty:
            challenges = self.queryset.filter(difficulty=difficulty)
            serializer = self.get_serializer(challenges, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class CodeExecutionView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        code = request.data.get('code')
        if not code:
            return Response({"error": "No code provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Execute the Python code in a safe environment
        try:
            with tempfile.NamedTemporaryFile(suffix='.py', delete=False) as temp:
                temp_path = temp.name
                temp.write(code.encode())
            
            # Run with timeout for safety
            result = subprocess.run(
                ['python', temp_path], 
                capture_output=True, 
                text=True, 
                timeout=5
            )
            
            os.unlink(temp_path)  # Clean up
            
            return Response({
                'stdout': result.stdout,
                'stderr': result.stderr,
                'returncode': result.returncode
            })
        except subprocess.TimeoutExpired:
            return Response({
                'error': 'Code execution timed out',
                'stdout': '',
                'stderr': 'Execution took too long and was terminated.',
                'returncode': 1
            }, status=status.HTTP_408_REQUEST_TIMEOUT)
        except Exception as e:
            return Response({
                'error': str(e),
                'stdout': '',
                'stderr': str(e),
                'returncode': 1
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CodeSnippetViewSet(viewsets.ModelViewSet):
    queryset = CodeSnippet.objects.all()
    serializer_class = CodeSnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        queryset = CodeSnippet.objects.all()
        category = self.request.query_params.get('category', None)
        tags = self.request.query_params.get('tags', None)
        
        if category:
            queryset = queryset.filter(category=category)
        
        if tags:
            tag_list = tags.split(',')
            for tag in tag_list:
                queryset = queryset.filter(tags__contains=[tag])
                
        return queryset

class UserProgressViewSet(viewsets.ModelViewSet):
    serializer_class = UserProgressSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return UserProgress.objects.filter(user=user)
    
    @action(detail=False, methods=['post'])
    def update_progress(self, request):
        user = request.user
        lesson_id = request.data.get('lesson_id')
        challenge_id = request.data.get('challenge_id')
        completed = request.data.get('completed', False)
        score = request.data.get('score', 0)
        
        if not lesson_id and not challenge_id:
            return Response({"error": "Must provide either lesson_id or challenge_id"}, 
                            status=status.HTTP_400_BAD_REQUEST)
        
        if lesson_id:
            progress, created = UserProgress.objects.get_or_create(
                user=user, 
                lesson_id=lesson_id,
                defaults={'completed': completed, 'score': score}
            )
            if not created:
                progress.completed = completed
                progress.score = score
                progress.save()
        elif challenge_id:
            progress, created = UserProgress.objects.get_or_create(
                user=user, 
                challenge_id=challenge_id,
                defaults={'completed': completed, 'score': score}
            )
            if not created:
                progress.completed = completed
                progress.score = score
                progress.save()
                
        serializer = self.get_serializer(progress)
        return Response(serializer.data)

class CodeReviewViewSet(viewsets.ModelViewSet):
    serializer_class = CodeReviewSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return CodeReview.objects.all()
        else:
            # Regular users can only see their own submitted reviews or reviews they're assigned to
            return CodeReview.objects.filter(user=user) | CodeReview.objects.filter(reviewer=user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user, status='pending')
    
    @action(detail=True, methods=['post'])
    def assign_reviewer(self, request, pk=None):
        if not request.user.is_staff:
            return Response({"error": "Only staff can assign reviewers"}, 
                           status=status.HTTP_403_FORBIDDEN)
        
        review = self.get_object()
        reviewer_id = request.data.get('reviewer_id')
        
        if not reviewer_id:
            return Response({"error": "No reviewer_id provided"}, 
                           status=status.HTTP_400_BAD_REQUEST)
        
        try:
            reviewer = User.objects.get(id=reviewer_id)
            review.reviewer = reviewer
            review.status = 'in_review'
            review.save()
            serializer = self.get_serializer(review)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({"error": "Reviewer not found"}, 
                           status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=True, methods=['post'])
    def submit_feedback(self, request, pk=None):
        review = self.get_object()
        
        # Check if user is the assigned reviewer
        if review.reviewer != request.user and not request.user.is_staff:
            return Response({"error": "Only the assigned reviewer can submit feedback"}, 
                           status=status.HTTP_403_FORBIDDEN)
        
        feedback = request.data.get('feedback')
        if not feedback:
            return Response({"error": "No feedback provided"}, 
                           status=status.HTTP_400_BAD_REQUEST)
        
        review.feedback = feedback
        review.status = 'completed'
        review.save()
        
        serializer = self.get_serializer(review)
        return Response(serializer.data)
