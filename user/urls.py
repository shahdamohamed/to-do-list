from django.urls import path
from .views import signup, Logout, Login

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]
