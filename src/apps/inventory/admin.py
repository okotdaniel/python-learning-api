from django.contrib import admin
from .models import Lesson, QuizQuestion, CodeChallenge, CodeSnippet, UserProgress, CodeReview

admin.site.register(Lesson)
   
admin.site.register(QuizQuestion)
  
admin.site.register(CodeChallenge)
  
admin.site.register(CodeSnippet)
   
admin.site.register(UserProgress)
  
admin.site.register(CodeReview)
  