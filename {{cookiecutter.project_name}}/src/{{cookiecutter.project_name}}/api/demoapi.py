# coding: utf-8

# from django.db import IntegrityError
# from django.db.transaction import atomic
# from django.utils import timezone
# from rest_framework import viewsets, decorators, request, serializers, response
# from .. import models as m

# import datetime


# class ProjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = m.Project
#         exclude = []


# class ProjectApi(viewsets.ModelViewSet):
#     queryset = m.Project.objects.all()
#     serializer_class = ProjectSerializer

#     @decorators.action(['GET'], detail=False)
#     def my_project(self, req: request.Request):
#         """我的项目"""
#         user = req.user
#         my_rank_list = m.Rank.objects.filter(user=user).all()
#         my_prj_list = [r.project for r in my_rank_list]
#         ser = ProjectSerializer(my_prj_list, many=True)
#         return response.Response(ser.data)
