#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:department.py
@date:2017/11/9 16:49
"""
from django.contrib import admin

from ..models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    """
    用户后台信息管理
    """
    search_fields = ['name', "parent", "charge"]
    list_display = ['name',  "parent", "charge"]
    list_filter = ['name']

    fieldsets = [
        (u"基本信息",{
            'fields': ['name', 'parent', "charge"],
        }),
        (u"其他信息", {
            'fields': ['description'],
        }),

    ]
