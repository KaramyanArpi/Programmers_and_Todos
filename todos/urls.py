from django.urls import path, include
from rest_framework import routers
from .views import TodoViewSet, todo_paginate, todo_programmers

router = routers.SimpleRouter()
router.register(r'', TodoViewSet, basename="todos")

urlpatterns = [
    path("", include(router.urls)),
    path("paginate/", todo_paginate),
    path("<int:task_id>/programmers/", todo_programmers),
]
