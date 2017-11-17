#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:position.py
@date:2017/11/9 16:47
"""
from django.contrib import admin

from ..models import Position


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    """
    用户后台信息管理
    """
    search_fields = ['name']
    list_display = ['name', "description"]
    list_filter = ['name']

    fieldsets = [
        (None,{
            'fields': ['name', 'description'],
        }),

    ]

