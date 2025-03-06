from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    Lesson, QuizQuestion, CodeChallenge, CodeSnippet,
    UserProgress, CodeReview
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        read_only_fields = ['id']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'description', 'content', 'difficulty', 
                 'order', 'category', 'code_examples']

class QuizQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizQuestion
        fields = ['id', 'lesson', 'question', 'code', 'options', 
                 'correct_answer', 'explanation', 'difficulty']

class CodeChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeChallenge
        fields = ['id', 'title', 'description', 'initial_code', 'difficulty',
                 'category', 'order']
        # Note: We exclude test_cases and solution to prevent cheating

class CodeChallengeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeChallenge
        fields = ['id', 'title', 'description', 'initial_code', 'test_cases', 
                 'solution', 'difficulty', 'category', 'order']

class CodeSnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeSnippet
        fields = ['id', 'title', 'description', 'code', 'tags', 'category',
                 'created_at']

class UserProgressSerializer(serializers.ModelSerializer):
    lesson_title = serializers.CharField(source='lesson.title', read_only=True)
    challenge_title = serializers.CharField(source='challenge.title', read_only=True)

    class Meta:
        model = UserProgress
        fields = ['id', 'user', 'lesson', 'lesson_title', 'challenge',
                 'challenge_title', 'completed', 'score', 'completed_at']

class CodeReviewSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username', read_only=True)
    reviewer_username = serializers.CharField(source='reviewer.username', read_only=True)

    class Meta:
        model = CodeReview
        fields = ['id', 'user', 'user_username', 'reviewer', 'reviewer_username',
                 'code', 'description', 'feedback', 'status', 'created_at',
                 'updated_at']
