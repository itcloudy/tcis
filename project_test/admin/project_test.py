#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:project_test.py
@date:2017/11/15 11:52
"""
from django.contrib import admin
from ..models import ProjectTest


@admin.register(ProjectTest)
class ProjectTestAdmin(admin.ModelAdmin):
    list_display = ['project', 'name', 'type']
