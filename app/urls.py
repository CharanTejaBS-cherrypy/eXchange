from django.urls import path
from django.contrib.auth import views as auth_views
from .views import logout_view
from . import views
from .views import delete_product

urlpatterns = [
    path('', views.index, name='index'),
    path('buy/', views.buy, name='buy'),
    path('sell/', views.sell, name='sell'),
    path('account/', views.account, name='account'),
    path('saved/', views.saved_items, name='saved_items'),
    path('toggle_save_product/<int:product_id>/',
         views.toggle_save_product, name='toggle_save_product'),

    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', views.register, name='register'),


    # otp_verification
    # path('sell/', initiate_otp_verification, name='sell_product'),
    # path('verify-otp/', verify_otp, name='verify_otp'),


    path('delete_product/<int:product_id>/', delete_product, name='delete_product'),
    # path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),

]
