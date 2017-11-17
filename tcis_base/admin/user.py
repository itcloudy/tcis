#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:user.py
@date:2017/11/9 9:31
"""
from django.contrib import admin

from ..models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    用户后台信息管理
    """
    search_fields = ['username', 'mobile', 'department', 'position']
    list_display = ['username', 'username_zh', 'department', 'position', 'mobile', 'is_active']
    list_filter = ['department', 'position']

    fieldsets = [
        (u'基本信息', {
            'fields': ['username', 'username_zh', 'is_active', 'email', 'mobile'],
        }),
        (u'部门信息', {
            'fields': ['department', 'position'],
        }),
        (u"权限信息", {
            'fields': ["groups"],
        })
    ]

    actions = ['set_disable', 'set_active']

    def set_disable(self, request, queryset):
        """
        设置用户无效
        :param request:
        :param queryset:
        :return:
        """
        queryset.update(is_active=False)

    set_disable.short_description = u'设置用户无效'

    def set_active(self, request, queryset):
        """
        设置用户有效
        :param request:
        :param queryset:
        :return:
        """
        queryset.update(is_active=True)

    set_active.short_description = u'设置用户有效'