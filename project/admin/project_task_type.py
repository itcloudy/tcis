#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:project_task_type.py
@date:2017/11/15 12:42
"""
from django.contrib import admin
from ..models import ProjectTaskType


@admin.register(ProjectTaskType)
class ProjectTaskTypeAdmin(admin.ModelAdmin):
    """
    项目管理后台
    """
    list_display = ["name"]
