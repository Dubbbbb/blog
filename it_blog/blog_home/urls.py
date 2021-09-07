from django.urls import path
from blog_home.views import blog_page

urlpatterns = [
    path("", blog_page, name="blogs_page"),
]
