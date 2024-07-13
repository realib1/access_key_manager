from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('reset_password/', views.reset_password, name='reset_password'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
