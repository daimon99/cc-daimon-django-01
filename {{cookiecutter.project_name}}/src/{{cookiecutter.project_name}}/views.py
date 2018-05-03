from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.shortcuts import render
import json
from . import models as m
# Create your views here.
import logging

log = logging.getLogger(__name__)


# class AnyJSONEncoder(DjangoJSONEncoder):
#     def default(self, o):
#         try:
#             return super().default(o)
#         except:
#             return repr(o)


# def match_all(request, path: str):
#     log.info('--> %s\n    [HEADERS]\n%s\n    [BODY]\n%s', path, json.dumps(request.META, cls=AnyJSONEncoder, indent=2),
#              request.body)

#     all_prefixs = m.PathRule.objects.all()
#     matched = None
#     for prefix in all_prefixs:
#         if path.startswith(prefix.path):
#             matched = prefix
#             break
#     if matched is None:
#         rv = """{"code": 0, "msg": "ok"}"""
#         ct = 'application/json'
#     else:
#         rv = matched.rv
#         ct = matched.content_type
#     log.info('<-- [%s] %s', ct, rv)
#     return HttpResponse(rv, content_type=ct)
