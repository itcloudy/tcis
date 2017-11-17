#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:project.py
@date:2017/11/8 16:50
"""
from rest_framework import viewsets
from ..models import Project
from ..serializers import *
from rest_framework.decorators import list_route
from rest_framework import status, permissions
from rest_framework.response import Response


class ProjectViewSet(viewsets.ModelViewSet):
    """
    项目管理
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        """
        过滤
        :return:
        """
        check_child = self.request.query_params.get("check_child")
        project_id = self.request.query_params.get("project_id")
        if project_id:
            if check_child == "true":
                parent = Project.objects.get(id=project_id)
                self.queryset = self.queryset.filter(parent_left__gt=parent.parent_left,
                                                     parent_right__lt=parent.parent_right)
        return self.queryset

    @list_route(["get"],
                permission_classes=[permissions.AllowAny])
    def get_all_project(self, request):
        projects = Project.objects.all()
        project_list = []
        for project in projects:
            project_list.append({
                "id": project.id,
                "name": project.name
            })
        return Response(project_list, status=status.HTTP_200_OK)

