# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class ProjectTestConfig(AppConfig):
    name = 'project_test'
    verbose_name = u'项目测试'

    def ready(self):
        import project_test.signals

