#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:project_member.py
@date:2017/11/10 11:49
"""
from rest_framework import serializers
from ..models import ProjectMember


class ProjectMemberSerializer(serializers.ModelSerializer):
    parent_left = serializers.IntegerField(read_only=True)
    parent_right = serializers.IntegerField(read_only=True)

    class Meta:
        model = ProjectMember
        depth = 1
        fields = "__all__"
