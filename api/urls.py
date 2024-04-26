from django.urls import path, include
from api.views import CompanyViewSet, EmployeeViesSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'companies',CompanyViewSet)
router.register(r'employees',EmployeeViesSet)

urlpatterns = [
   path("", include(router.urls) )
]