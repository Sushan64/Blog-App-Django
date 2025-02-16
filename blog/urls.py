from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
  path('', views.post_list, name="post_list"),
  path('post/<int:pk>', views.post_details, name ="post_details"),
  path('post/new', views.post_new, name="post_new"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)