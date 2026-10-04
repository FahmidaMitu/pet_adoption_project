from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'api/pets', views.PetViewSet)
router.register(r'api/adoptions', views.AdoptionRequestViewSet, basename='adoption')

urlpatterns = [
    path('', views.pet_list, name='pet_list'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('pet/<int:pk>/', views.pet_detail, name='pet_detail'),
    path('pet/<int:pk>/apply/', views.apply_adoption, name='apply_adoption'),
    path('my-requests/', views.my_requests, name='my_requests'),
    path('', include(router.urls)),
]