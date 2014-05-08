from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'zncviewer.views.index', name='home'),
    url(r'^login/', 'zncviewer.views.login_user', name='login_user'),
    url(r'^logs/$', 'zncviewer.views.logs', name="logs"),
    url(r'^logs/(?P<filename>(.)+)', 'zncviewer.views.show_log', name="log")
]
