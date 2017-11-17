#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:project_test_type.py
@date:2017/11/15 11:53
"""
from django.contrib import admin
from ..models import ProjectTestType


@admin.register(ProjectTestType)
class ProjectTestTypeAdmin(admin.ModelAdmin):
    list_display = ['name']

