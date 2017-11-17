# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class ProjectConfig(AppConfig):
    name = 'project'
    verbose_name = u'项目'

    def ready(self):
        import project.signals

