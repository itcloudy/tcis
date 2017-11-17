#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:project_task.py
@date:2017/11/9 16:23
"""
from django.contrib import admin
from ..models import ProjectTask


@admin.register(ProjectTask)
class ProjectTaskAdmin(admin.ModelAdmin):
    """
    项目管理后台
    """
    search_fields = ["project", "name", "parent", "active", "handler", "state"]
    list_display = ["name", "project", "parent", "active", "handler", "state","start_time","end_time", 'real_end_time']
    list_filter = ['project', 'parent', "active", "handler", "state"]

    actions = ['set_disable', 'set_active']

    def set_disable(self, request, queryset):
        """
        设置项目任务无效
        :param request:
        :param queryset:
        :return:
        """
        queryset.update(is_active=False)

    set_disable.short_description = u'设置项目任务无效'

    def set_active(self, request, queryset):
        """
        设置项目任务有效
        :param request:
        :param queryset:
        :return:
        """
        queryset.update(is_active=True)

    set_active.short_description = u'设置项目任务有效'


