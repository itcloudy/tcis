#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:project_task.py
@date:2017/11/10 14:15
"""
from rest_framework import status, permissions
from rest_framework.decorators import list_route
from rest_framework import viewsets
from django.db.models import Count
from project.models import Project
from ..models import ProjectBug
from rest_framework.response import Response
from tcis_base.models import User
from ..serializers import *


class ProjectBugViewSet(viewsets.ModelViewSet):
    """
    项目管理
    """
    queryset = ProjectBug.objects.all()
    serializer_class = ProjectBugSerializer

    def get_queryset(self):
        """
        过滤
        :return:
        """

        project_id = self.request.query_params.get("project_id")
        if project_id:
            self.queryset = self.queryset.filter(project__id=project_id)

        check_child = self.request.query_params.get("check_child")
        project_id = self.request.query_params.get("project_id")
        if project_id:
            project_ids = [project_id]
            if check_child == 'true' :
                project = Project.objects.get(id=project_id)
                projects = Project.objects.filter(parent_left__gte=project.parent_left,
                                                  parent_right__lte=project.parent_right)
                project_ids = [line.id for line in projects]

            self.queryset = self.queryset.filter(project_id__in=project_ids)
        return self.queryset

    @list_route(["get"],
                permission_classes=[permissions.AllowAny])
    def project_bug_kanban(self, request):
        """
        获得项目任务情况
        :param request:
        :return:
        """
        handler_level = {}
        handler_state = {}
        legend = []
        series_data = []
        handlers = []
        handler_ids = []
        other = u"未指定"
        handler_info = {
            "None": other
        }
        project_id = request.query_params.get("project_id")
        check_child = request.query_params.get("check_child")
        project_ids = [project_id]
        if check_child == "true":
            parent = Project.objects.get(id=project_id)
            projects = Project.objects.filter(parent_left__gte=parent.parent_left, parent_right__lte=parent.parent_right)
            project_ids = [line.id for line in projects]

        results = ProjectBug.objects.filter(project__id__in=project_ids).values_list("state", 'handler_id',
                                                                                 'level').annotate(Count('id'))
        for result in results:
            handler = "%s" % result[1]
            state_key = "%s_%s" % (handler, result[0])
            level_key = "%s_%s" % (handler, result[2])
            handler_state[state_key] = handler_state.get(state_key, 0) + result[3]
            handler_level[level_key] = handler_state.get(level_key, 0) + result[3]
            handlers.append(handler)
            # 用户ID
            if result[1]:
                handler_ids.append(result[1])
        handlers = list(set(handlers))
        handlers_num = len(handlers)
        # 获得用户信息
        users = User.objects.filter(id__in=handler_ids)
        for user in users:
            handler_info["%s" % user.id] = user.username_zh or user.username
        for state_tuple in ProjectBug.STATES:
            state = state_tuple[0]
            state_data = [0 for l in range(handlers_num)]
            for i in range(handlers_num):
                state_key = "%s_%s" % (handlers[i], state)
                state_data[i] = handler_state.get(state_key, 0)
            series_data.append({
                "name": state_tuple[1],
                "type": "bar",
                "stack": u"状态",
                'data': state_data
            })
            legend.append(state_tuple[1])

        for level_tuple in ProjectBug.LEVELS:
            level = level_tuple[0]
            level_data = [0 for l in range(handlers_num)]
            for i in range(handlers_num):
                level_key = "%s_%s" % (handlers[i], level)
                level_data[i] = handler_level.get(level_key, 0)
            series_data.append({
                "name": level_tuple[1],
                "type": "bar",
                "stack": u"级别",
                'data': level_data
            })
            legend.append(level_tuple[1])

        x_axis = ["" for i in range(handlers_num)]
        for i in range(handlers_num):
            x_axis[i] = handler_info.get(handlers[i], other)

        result_data = {
            'series': series_data,
            'x_axis': x_axis,
            'legend': legend
        }
        return Response(result_data, status=status.HTTP_200_OK)
