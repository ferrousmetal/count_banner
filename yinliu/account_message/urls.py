from django.conf.urls import url
from .views import *

app_name = "account_message"

urlpatterns = [
    url(r'^douyinMessageAccount/', DouYinmessageView.as_view(), name='douyinMessageAccount'),
    url(r'^douyinCommentAccount/', DouYinCommentView.as_view(), name='douyinCommentAccount'),
    url(r'^quickHandMessageAccount/', QuickHandmessageView.as_view(), name='quickHandMessageAccount'),
    url(r'^quickHandCommentAccount/', QuickHandCommenteView.as_view(), name='quickHandCommentAccount'),
    url(r'^guimiQuanMessageAccount/', guimiQuanmessageView.as_view(), name='guimiQuanMessageAccount'),
    url(r'^guimiQuanCommentAccount/', guimiQuanCommentView.as_view(), name='guimiQuanCommentAccount'),
    url(r'^xiguaMessageAccount/', xiguamessageView.as_view(), name='xiguaMessageAccount'),
    url(r'^xiguaCommentAccount/', xiguaCommentView.as_view(), name='xiguaCommentAccount'),
    url(r'^showAccount/', ShowCountView.as_view(), name='showAccount'),
]
