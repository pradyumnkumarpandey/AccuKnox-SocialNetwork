from django.urls import path  , include
from network.accounts.views import SignUp, Login, FindUsers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('signup',SignUp,basename="signup")
router.register('login',Login,basename="login")
router.register('users',FindUsers,basename="users")


urlpatterns = [
    path("", include(router.urls)),

]