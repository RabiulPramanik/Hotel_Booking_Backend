from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

roter = DefaultRouter()

roter.register("list", views.UserViewsets)

urlpatterns = [
    path('', include(roter.urls)),
    path('register/', views.UserRegistrationView.as_view(), name='registration'),
    path('active/<uid64>/<token>', views.activate, name="activate"),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout' ),
]
