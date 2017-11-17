#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:project_test_case.py
@date:2017/11/15 11:53
"""
from django.contrib import admin
from ..models import ProjectTestCase


@admin.register(ProjectTestCase)
class ProjectTestCaseAdmin(admin.ModelAdmin):
    list_display = ['project', 'task', 'test', "name", "type"]

