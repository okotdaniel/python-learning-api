from django.urls import path
from .views import GetAllUsersView

app_name = 'account'

urlpatterns = [

    # Attendance
    path('view/', GetAllUsersView.as_view(), name='view_accounts'),
   
]