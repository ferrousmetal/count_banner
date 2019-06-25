from django.db import models


# Create your models here.

class DouyinMessageModel(models.Model):
    """抖音计数器"""
    dmessagecount = models.IntegerField(default=0, verbose_name="抖音私信计数器")


class DouyinCommentModel(models.Model):
    """抖音计数器"""
    dcommentcount = models.IntegerField(default=0, verbose_name="抖音私评论数器")


class QuickHandMessageModel(models.Model):
    """快手计数器"""
    qmessagecount = models.IntegerField(default=0, verbose_name="快手私信计数器")


class QuickHandCommentModel(models.Model):
    """快手计数器"""
    qcommentcount = models.IntegerField(default=0, verbose_name="快手评论计数器")


class GuimiquanMessageModel(models.Model):
    """闺蜜全计数器"""
    guimimessagecount = models.IntegerField(default=0, verbose_name="闺蜜私信计数器")


class GuimiquanCommentModel(models.Model):
    """闺蜜全计数器"""
    guimicommentcount = models.IntegerField(default=0, verbose_name="闺蜜评论数器")


class xiguaMessageModel(models.Model):
    """闺蜜全计数器"""
    xiguamessagecount = models.IntegerField(default=0, verbose_name="西瓜私信计数器")


class xiguaCommentModel(models.Model):
    """西瓜全计数器"""
    xiguacommentcount = models.IntegerField(default=0, verbose_name="西瓜评论数器")


class QuickHanaccountProfileModel(models.Model):
    """西瓜账号状态"""
    phone = models.CharField(max_length=11, verbose_name="手机号")
    password = models.CharField(max_length=20, verbose_name="账号密码")
    isUse = models.BooleanField(default=False, verbose_name="是否在使用")
    islock = models.BooleanField(default=False, verbose_name="是否封号")
