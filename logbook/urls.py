from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from logbook.core import views as core_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^create_post/$', core_views.create_post , name='create_post'),
    url(r'^create_category/$', core_views.create_category , name='create_category'),
    url(r'^view_categories/$', core_views.view_categories , name='view_categories'),
    url(r'^view_posts/$', core_views.view_posts , name='view_posts'),
    url(r'^view_category/(?P<slug>[\w-]+)/$', core_views.view_category , name='view_category'),
    url(r'^view_post/(?P<slug>[\w-]+)/$', core_views.view_post , name='view_post'),
    url(r'^edit_post/(?P<slug>[\w-]+)/$', core_views.edit_post , name='edit_post'),
    url(r'^view_post/(?P<slug>[\w-]+)/delete/$', core_views.delete_post , name='delete_post'),
    url(r'^search_post/$', core_views.search_post , name='search_post'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
