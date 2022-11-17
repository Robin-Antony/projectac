from django.urls import path
from. import views

urlpatterns = [
    path('',views.index,name='index'),
    path('address',views.order,name='address'),
    path('order_page',views.orderPage,name='order_page'),
    path('staff_register',views.staffRegister,name='staff_register'),
    path('user_register',views.userRegister,name='user_register'),
    path('login_page',views.loginPage,name='login_page'),
    path('logout_page',views.logoutPage,name='logout_page'),
    path('order_status',views.orderStatus,name='order_status'),
    path('rating/<str:pk>/<str:phone>/',views.rating,name='rating'),
    path('staff_profile/<str:pk>/',views.staffProfile,name='staff_profile'),
    path('activate/<uidb64>/<token>',views.activate,name='activate'),
    path('reset/<uidb64>/<token>',views.reset,name='reset'),
    path('carrier_page',views.carrierPage,name='carrier_page'),
    path('privacy_policy',views.privacyPolicy,name='privacy_policy'),
    path('password_reset',views.passwordReset,name='password_reset'),
    path('reset_password_enter',views.reset,name='reset_password_enter'),
    path('edit_profile',views.editProfile,name='edit_profile'),
    
    ]