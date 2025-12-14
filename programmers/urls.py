from django.urls import path, include
from rest_framework import routers
from .views import ProgrammerViewSet, programmer_paginate, programmer_todos

router = routers.SimpleRouter()
router.register(r'', ProgrammerViewSet, basename="programmers")

urlpatterns = [
    path("", include(router.urls)),
    path("paginate/", programmer_paginate),
    path("<int:programmer_id>/todos/", programmer_todos),
]
