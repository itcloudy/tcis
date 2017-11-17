#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:permission.py
@date:2017/11/15 17:55
"""
from rest_framework import viewsets
from django.contrib.auth.models import Permission
from ..serializers import PermissionSerializer
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.decorators import list_route


class PermissionViewSet(viewsets.ModelViewSet):
    """
    用户权限
    """
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

    @list_route(["get"],
                permission_classes=[permissions.AllowAny])
    def get_all_permission(self, request):
        """
        过滤
        :return:
        """
        all_permissions = []
        for line in self.queryset:
            all_permissions.append({
                "id": line.id,
                "name": line.name
            })
        return Response(all_permissions, status=status.HTTP_200_OK)

    @list_route(["get"],
                permission_classes=[permissions.AllowAny])
    def translate_all_permission(self,  request):
        """
        翻译
        :return:
        """
        for permission in self.queryset:
            permission.name = permission.name.replace("Can add ", u"可创建:")
            permission.name = permission.name.replace("Can change ", u"可修改:")
            permission.name = permission.name.replace("Can delete ", u"可删除:")
            permission.save()

        return Response([], status=status.HTTP_200_OK)
