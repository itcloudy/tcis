#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:project_task.py
@date:2017/11/10 11:49
"""

from rest_framework import serializers
from ..models import ProjectBug
from tcis_base.serializers import UserSerializer
from project.serializers import ProjectSerializer, ProjectTaskSerializer


class ProjectBugSerializer(serializers.ModelSerializer):
    handler = UserSerializer()
    tester = UserSerializer()
    checker = UserSerializer()
    project = ProjectSerializer()
    task = ProjectTaskSerializer()

    class Meta:
        model = ProjectBug
        depth = 1
        fields = "__all__"
