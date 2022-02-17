from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from rareapi.views import register_user, login_user
from rareapi.views.category import CategoryView
from rareapi.views import PostView
from rareapi.views.rare_user import RareUserView
from rareapi.views.tag import TagsView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'categories', CategoryView, 'category')

router.register(r'posts', PostView, 'post')
router.register(r'tags', TagsView, 'tag')
router.register(r'users', RareUserView, 'user')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]

