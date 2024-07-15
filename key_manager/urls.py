from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('keymanager/signup/', views.signup, name='signup'),
    path('keymanager/signin/', views.signin, name='signin'),
    path('keymanager/signout/', views.signout, name='signout'),
    path('keymanager/keylist/', views.keylist, name='keylist'),
    path('keymanager/keydetails/<int:id>/', views.keydetails, name='keydetails'),
    path('keymanager/password_reset/', views.password_reset_request, name='password_reset'),
    path('password_reset/done/', views.password_reset_done, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('reset/done/', views.password_reset_complete, name='password_reset_complete'),
    # path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    
                ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
