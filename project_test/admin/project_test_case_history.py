#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:project_test_case_history.py
@date:2017/11/15 11:53
"""
from django.contrib import admin
from ..models import ProjectTestCaseHistory


@admin.register(ProjectTestCaseHistory)
class ProjectTestCaseHistoryAdmin(admin.ModelAdmin):
    list_display = ['case', 'user']

