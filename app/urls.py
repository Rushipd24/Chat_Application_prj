
from django.contrib import admin
from django.urls import path
from app.views import *
from app.views.user import *

urlpatterns = [
    # user
    path('get_user', get_user, name="get_user"),
    path('create_user', create_user, name="create_user"),
    path('update_user', update_user, name="update_user"),
    path('login_request', login_request, name="login_request"),
    path('user_logout', user_logout, name="user_logout"),
    path("CreateGrp", CreateGrp.as_view(), name="CreateGrp"),
    path('delete_user/<int:primary_key>', delete_user, name="delete_user"),
 ]