from django.urls import path
from . import views

urlpatterns = [
     path('admin-login/', views.admin_login),
    path('admin-dashboard/', views.admin_dashboard),

    path('admin-users/', views.admin_users),
    path('delete-user/<int:id>/', views.delete_user),

    path('admin-food/', views.admin_food),
    path('add-food/', views.add_food),
    path('delete-food/<int:id>/', views.delete_food),
    
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),

   path('add-to-cart/<int:id>/', views.add_to_cart),
   path('cart/', views.cart_view),
   path('place-order/', views.place_order),
   path('admin-orders/', views.admin_orders),




]
