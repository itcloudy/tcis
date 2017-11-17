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
from ..models import ProjectTask
from tcis_base.serializers import UserSerializer


class ProjectTaskSerializer(serializers.ModelSerializer):
    parent_left = serializers.IntegerField(read_only=True)
    parent_right = serializers.IntegerField(read_only=True)
    handler = UserSerializer()

    class Meta:
        model = ProjectTask
        depth = 1
        fields = "__all__"
