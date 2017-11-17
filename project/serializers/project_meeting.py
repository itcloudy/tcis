#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:project_meeting.py
@date:2017/11/15 11:12
"""
from rest_framework import serializers
from ..models import ProjectMeeting
from .project import ProjectSerializer
from tcis_base.serializers import TcisMeetingSerializer


class ProjectMeetingSerializer(serializers.ModelSerializer):
    meeting = TcisMeetingSerializer()
    project = ProjectSerializer()

    class Meta:
        model = ProjectMeeting
        depth = 2
        fields = "__all__"
