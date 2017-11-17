#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:project_test.py
@date:2017/11/10 14:15
"""
from rest_framework import status, permissions
from rest_framework.decorators import list_route
from rest_framework import viewsets
from django.db.models import Count
from project.models import Project
from project_test.models import ProjectTest
from rest_framework.response import Response
from tcis_base.models import User
from ..serializers import *


class ProjectTestViewSet(viewsets.ModelViewSet):
    """
    项目管理
    """
    queryset = ProjectTest.objects.all()
    serializer_class = ProjectTestSerializer

    def get_queryset(self):
        project_id = self.request.query_params.get("project_id")
        type_id = self.request.query_params.get("type_id")
        if project_id:
            self.queryset = self.queryset.filter(project_id=project_id)
        if type_id:
            self.queryset = self.queryset.filter(type_id=type_id)

        return self.queryset

    @list_route(["get"],
                permission_classes=[permissions.AllowAny])
    def project_test_kanban(self, request):
        projects = Project.objects.all()
        project_list = []
        for project in projects:
            project_list.append({
                "id": project.id,
                "name": project.name
            })
        return Response(project_list, status=status.HTTP_200_OK)



