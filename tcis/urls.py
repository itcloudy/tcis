#!/usr/bin/env python
# encoding: utf-8
"""tcis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static


urlpatterns = [
    # 系统后台
    url(r'^admin/', admin.site.urls),
    # 接口
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    # 项目管理
    url(r'^project/', include('project.urls', namespace='project', app_name='project manage')),
    # 项目bug管理
    url(r'^project_bug/', include('project_bug.urls', namespace='project_bug', app_name='project bug manage')),
    # 项目持续集成
    url(r'^project_ci/', include('project_ci.urls', namespace='project_ci',
                                 app_name='project continuous integration')),
    # 项目测试
    url(r'^project_test/', include('project_test.urls', namespace='project_test', app_name='project test')),
    # 绩效考核
    url(r'^performance_appraisal/', include('performance_appraisal.urls', namespace='performance_appraisal', app_name='performance appraisal')),

    # 基础
    url(r'', include('tcis_base.urls', namespace='tcis_base',
                       app_name='test continuous integration system base manage')),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
