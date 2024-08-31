from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('keymanager/signup/', views.signup, name='signup'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('resend_verification_email/', views.resend_verification_email, name='resend_verification_email'),
    path('keymanager/signin/', views.signin, name='signin'),
    path('keymanager/signout/', views.signout, name='signout'),
    path('keymanager/keylist/', views.keylist, name='keylist'),
    path('keymanager/keydetails/<int:id>/', views.keydetails, name='keydetails'),
    path('keymanager/password_reset_form/', views.password_reset_request, name='password_reset_form'),
    path('keymanager/password_reset_done/', views.password_reset_done, name='password_reset_done'),
    path('keymanager/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('keymanager/password_reset_complete/', views.password_reset_complete, name='password_reset_complete'),
    path('keymanager/change_password/', views.change_password, name='change_password',
         )
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'key_manager.views.custom_404'

