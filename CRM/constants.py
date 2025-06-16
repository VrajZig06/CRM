
# Django Constants Stuffs
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.db import IntegrityError
from django.urls import path,include
from django.contrib import admin
from django.contrib.auth.hashers import make_password,check_password
from django.utils import timezone
from django.core.paginator import Paginator


# Models stuffs
from person.models import Employee
from users.models import Users

# Other Extra Stuffs
import json
import jwt
import datetime
import time
import requests

# Messages
All_FIELDS_REQUIRED = "All fields are required"
COMPANY_OWNER_NOT_EXISTS = "Company Owner not found"
USER_WITH_SAME_EMAIL_EXISTS = 'Employee with this email already exists'
EMPLOYEE_CREATED = "Employee created successfully"
EMPLOYEE_UPDATED = "Employee Details are updated Successfully!"
EMPLOYEE_NOT_FOUND = "Employee Not Found."
EMPLOYEE_ID_REQUIRED = "Employee id required field."
EMPLOYEE_DELETED = "Employee Deleted Successfully!"
USER_ALREADY_EXISTS = "User Already Exists."
USER_CREATED_SUCCESSFULLY = "User Created Successfully"
PAYLOAD_REQUIRED = "Provide Payload to Login"
FAILED_ACCESS_TOKEN =  "Failed to Generate AccessToken."
TOKEN_REQUIRED = "Token Required"
EMAIL_PASSWORD_REQUIRED = "Email and Password Required"
USER_NOT_FOUND =  "User not Found."
UNAUTHORIZED_ACCESS = "Unauthorized Access to API"
INVALID_AUTHORIZATION_TOKEN = "Invalid Authorization Token"

# Databases Error Messages
DB_INTEGRITY_ERROR = "Database integrity error (possibly duplicate user ID or other constraint)"


# Global Error Messages 
SOMETHING_WENT_WRONG = "Something went wrong!"

# Base URL
BASE_URL = "api/v1/"

JWT_SECRET = "sashhdxuBFUYRTQ87745723584B7678Z676^&^&*^*%^3XBHQTKJGFGCAKKCGHSGGANXYUUCGHAGPUOQ8YBFHAGFYURCE"