from django.contrib import admin
from django.urls.conf import path

from article import views

app_name='articles'


urlpatterns=[
    path('', views.ArticleListPostView.as_view()),
    path('<int:pk>', views.SingleArticleView.as_view()),
    path('admin/',admin.site.urls),
]