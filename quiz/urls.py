from django.contrib import admin
from django.urls import path, include
from quiz.views import *

urlpatterns = [
    path('', Message.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('qv1/', include('qv1.urls')),
    path('message/', Message.as_view(), name='Message')
]
