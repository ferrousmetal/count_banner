from django.shortcuts import render, redirect
from django.views.generic import View
from .models import *
from django.urls import reverse
import re, json
from django.http import JsonResponse, HttpResponse


class DouYinmessageView(View):
    """抖音计数器"""

    def get(self, request):
        num = DouyinMessageModel.objects.get(id=1)
        num.douyincount += 1
        num.save()
        return HttpResponse("私信加一")


class DouYinCommentView(View):
    """抖音计数器"""

    def get(self, request):
        num = DouyinMessageModel.objects.get(id=1)
        num.douyincount += 1
        num.save()
        return HttpResponse("评论加一")


class QuickHandmessageView(View):
    """快手计数器"""

    def get(self, request):
        num = QuickHandMessageModel.objects.get(id=1)
        num.quickhandcount += 1
        num.save()
        return HttpResponse("私信加一")


class QuickHandCommenteView(View):
    """快手计数器"""

    def get(self, request):
        num = QuickHandMessageModel.objects.get(id=1)
        num.quickhandcount += 1
        num.save()
        return HttpResponse("评论加一")


class guimiQuanmessageView(View):
    """闺蜜全计数器"""

    def get(self, request):
        num = QuickHandMessageModel.objects.get(id=1)
        num.quickhandcount += 1
        num.save()
        return HttpResponse("私信加一")


class guimiQuanCommentView(View):
    """闺蜜全数器"""

    def get(self, request):
        num = QuickHandMessageModel.objects.get(id=1)
        num.quickhandcount += 1
        num.save()
        return HttpResponse("评论加一")


class xiguamessageView(View):
    """闺蜜全计数器"""

    def get(self, request):
        num = QuickHandMessageModel.objects.get(id=1)
        num.quickhandcount += 1
        num.save()
        return HttpResponse("私信加一")


class xiguaCommentView(View):
    """闺蜜全数器"""

    def get(self, request):
        num = QuickHandMessageModel.objects.get(id=1)
        num.quickhandcount += 1
        num.save()
        return HttpResponse("评论加一")


class QuickHanaccountProfileView(View):
    """快手账号状态"""
    pass


class ShowCountView(View):
    "dmessagecount,dcommentcount;qmessagecount,qcommentcount,guimimessagecount,guimicommentcount,xiguamessagecount,xigaucommentcount"
    """显示计数"""
    "DouyinMessageModel,DouyinCommentModel,QuickHandMessageModel,QuickHandCommentModel,GuimiquanMessageModel,GuimiquanCommentModel,xihuaMessageModel,xihuaCommentModel"
    def get(self, request):
        dmessagecount = DouyinMessageModel.objects.get(id=1).dmessagecount
        dcommentcount = DouyinCommentModel.objects.get(id=1).dcommentcount
        qmessagecount = QuickHandMessageModel.objects.get(id=1).qmessagecount
        qcommentcount = QuickHandCommentModel.objects.get(id=1).qcommentcount
        guimimessagecount = GuimiquanMessageModel.objects.get(id=1).guimimessagecount
        guimicommentcount = GuimiquanCommentModel.objects.get(id=1).guimicommentcount
        xiguamessagecount = xiguaMessageModel.objects.get(id=1).xiguamessagecount
        xiguacommentcount = xiguaCommentModel.objects.get(id=1).xiguacommentcount

        return render(request, "shou_count.html", locals())
