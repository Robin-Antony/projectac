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
    path('privacy_policy',views.privacyPolicy,name='privacy_policy'),
    path('password_reset',views.passwordReset,name='password_reset'),
    path('reset_password_enter',views.reset,name='reset_password_enter'),
    path('edit_profile',views.editProfile,name='edit_profile'),
    path('help_page',views.helpPage,name='help_page'),
    path('carrier_page',views.carrierPage,name='carrier_page'),
    path('privacy_policy',views.privacyPolicy,name='privacy_policy'),
    path('terms_and_conditions',views.termsAndConditons,name='terms_and_conditions'),
    path('about_us',views.aboutUs,name='about_us'),
    path('what_we_do',views.whatWeDo,name='what_we_do'),
    path('why_us',views.WhyUs,name='why_us'),
    path('feedback',views.feedbackPage, name='feedback')
    
    ]