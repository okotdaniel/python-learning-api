import random
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.db.models import Q, QuerySet


# class Account(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(verbose_name="username", max_length=360, null=True, blank=True)
#     first_name = models.CharField(max_length=255, null=False, blank=False)
#     middle_name = models.CharField(max_length=255, null=True, blank=True)
#     last_name = models.CharField(max_length=255, null=False, blank=False)
#     email = models.EmailField(max_length=60, unique=True)
    
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username', 'first_name', 'middle_name', 'last_name']

#     # objects = BaseAccountManager()

#     class Meta:
#         constraints = [
           
#             models.UniqueConstraint(fields=['username'], condition=Q(nin__isnull=False), violation_error_message='Username already exists',
#                                     name='account_unique_username'),
#             models.UniqueConstraint(fields=['email'], condition=Q(phone_number__isnull=False),
#                                     violation_error_message='email already exists',
#                                     name='account_unique_email'),
#         ]

#     def __str__(self):
#         return "{} {}".format(str(self.first_name), str(self.last_name))

#     @property
#     def names(self):
#         return "{} {}".format(str(self.first_name), str(self.last_name))

#     # For checking permissions. to keep it simple all admin have ALL permissions
#     def has_perm(self, perm, obj=None):
#         return self.is_admin

#     # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
#     def has_module_perms(self, app_label):
#         return True


class Profile():
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, max_length=50, null=True, blank=True)
    passport_number = models.CharField(max_length=14, null=True, blank=True)
    nin = models.CharField(max_length=25, null=True, blank=True, verbose_name='ID Number')
    address = models.CharField(max_length=1000, null=True, blank=True, default='House, Bukoto Street')
    date_of_birth = models.DateField(verbose_name='Date of Birth', null=True, blank=True)
    # gender = models.CharField(max_length=10, null=True, blank=True, choices=GENDER)
    # school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True, blank=True)
    delegator_name = models.CharField(max_length=1000, null=True, blank=True)
    has_delegated_to = models.CharField(max_length=1000, null=True, blank=True)
    # image_url = models.ImageField(upload_to=upload_location, null=True, blank=True, max_length=500)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.name
    

