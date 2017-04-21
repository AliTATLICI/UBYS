from django.conf.urls import url, include
from rest_framework import routers
from . import views
from django.contrib import admin
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns





router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    url(r'^obs/$', views.post_list, name='obs_ana_sayfa'),
    url(r'^obs/fakulte_myo', views.get_deneme, name='get_deneme'),
    url(r'^obs/dahil$', views.icerilen_sayfa),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^snippets/$', views.SnippetList.as_view()),

    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^test/', views.SnippetList.as_view()),
    url(r'^birimler/$', views.Fakulte_MYOList.as_view()),
]

#urlpatterns = format_suffix_patterns(urlpatterns)