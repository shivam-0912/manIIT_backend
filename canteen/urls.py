from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from canteen import views

urlpatterns =format_suffix_patterns( [

    path('all',views.canteen_list),#login a user
    path('<int:canteen_id>',views.canteen_detail),#singnup a user

])# -*- coding: utf-8 -*-

