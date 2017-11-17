#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:project_task.py
@date:2017/11/10 14:15
"""
from rest_framework import viewsets
from ..models import ProjectMember,Project
from ..serializers import *


class ProjectMemberViewSet(viewsets.ModelViewSet):
    """
    项目管理
    """
    queryset = ProjectMember.objects.all()
    serializer_class = ProjectMemberSerializer

    def get_queryset(self):
        """
        过滤
        :return:
        """
        check_child = self.request.query_params.get("check_child")
        project_id = self.request.query_params.get("project_id")
        project_ids = [project_id]
        if check_child == 'true':
            project = Project.objects.get(id=project_id)
            projects = Project.objects.filter(parent_left__gte=project.parent_left, parent_right__lte=project.parent_right)
            project_ids = [line.id for line in projects]

        self.queryset = self.queryset.filter(project_id__in=project_ids)
        return self.queryset

