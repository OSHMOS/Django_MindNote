from django.urls import path, include
from diary.views import (
    page_list,
    info,
    page_create,
    page_detail,
    page_update,
    page_delete,
)

urlpatterns = [
    path("", page_list, name="page_list"),
    path("info/", info, name="info"),
    path("write/", page_create, name="page_create"),
    path("page/<int:page_id>/", page_detail, name="page_detail"),
    path("page/<int:page_id>/update/", page_update, name="page_update"),
    path("page/<int:page_id>/delete/", page_delete, name="page_delete"),
]
