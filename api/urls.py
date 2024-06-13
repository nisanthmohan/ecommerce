from django.urls import path
from api.views import signupview
from rest_framework.authtoken.views import ObtainAuthToken
from api.views import taskviewset
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("v2/task",taskviewset,basename="task")
urlpatterns = [
  path('register',signupview.as_view()),
  path("token",ObtainAuthToken.as_view()),
]+router.urls