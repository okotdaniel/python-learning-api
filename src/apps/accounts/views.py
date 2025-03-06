import csv
import mimetypes
from functools import reduce
from operator import and_

from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.core.paginator import Paginator
from django.db import IntegrityError
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.http import Http404, JsonResponse, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.utils.html import strip_tags
from django.views import View
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes, api_view
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import NotFound
from django.db.models import Count
from .serializers import TestSerializer
from django.http import HttpResponse
import io

class GetAllUsersView(APIView):
    serializer_class = TestSerializer
    # permission_classes = [IsAuthenticated & (IsAdmin | IsSchoolAdmin)]

    # @staticmethod
    # def get_user_object(pk):
    #     try:
    #         return Account.objects.get(pk=pk)
    #     except Account.DoesNotExist:
    #         raise Http404

    @swagger_auto_schema(
        operation_description='Returns the content of a single user.',
        tags=['Account management'],
    )
    def get(self, request, *args, **kwargs):
        data, user = {}, self.get_user_object(kwargs.get('pk'))
        data['status'] = 200
        data['data'] = TestSerializer(user).data
        return Response(data)

