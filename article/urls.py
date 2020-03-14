from django.contrib import admin
from django.urls.conf import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from article import views

app_name='articles'


urlpatterns=[
    path('', views.ArticleListPostView.as_view()),
    path('<int:pk>', views.SingleArticleView.as_view()),
    path('apiauthtoken/', obtain_auth_token),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('admin/', admin.site.urls),
]