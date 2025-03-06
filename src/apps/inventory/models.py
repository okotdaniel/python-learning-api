
from django.db import models
from django.contrib.auth.models import User

class Lesson(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()
    difficulty = models.CharField(max_length=20, choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced')
    ])
    order = models.IntegerField()
    category = models.CharField(max_length=50)
    code_examples = models.JSONField()  # Store array of code examples

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class QuizQuestion(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='quiz_questions', on_delete=models.CASCADE, null=True)
    question = models.TextField()
    code = models.TextField(null=True, blank=True)  # Optional code snippet
    options = models.JSONField()  # Store array of options
    correct_answer = models.TextField()
    explanation = models.TextField()
    difficulty = models.CharField(max_length=20, choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced')
    ])

    def __str__(self):
        return self.question[:50]  # First 50 characters of the question

class CodeChallenge(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    initial_code = models.TextField()  # Starting code template
    test_cases = models.JSONField()  # Array of test cases
    solution = models.TextField()
    difficulty = models.CharField(max_length=20, choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced')
    ])
    category = models.CharField(max_length=50)
    order = models.IntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class CodeSnippet(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    code = models.TextField()
    tags = models.JSONField()  # Array of tags for searching
    category = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True)
    challenge = models.ForeignKey(CodeChallenge, on_delete=models.CASCADE, null=True)
    completed = models.BooleanField(default=False)
    score = models.IntegerField(default=0)  # For quizzes and challenges
    completed_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [['user', 'lesson'], ['user', 'challenge']]

class CodeReview(models.Model):
    user = models.ForeignKey(User, related_name='submitted_reviews', on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, related_name='given_reviews', on_delete=models.CASCADE, null=True)
    code = models.TextField()
    description = models.TextField()
    feedback = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('in_review', 'In Review'),
        ('completed', 'Completed')
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Code Review by {self.user.username}"
