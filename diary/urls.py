from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("diary/", views.page_list, name="page_list"),
    path("diary/info/", views.info, name="info"),
    path("diary/write/", views.page_create, name="page_create"),
    path("diary/page/<int:page_id>/", views.page_detail, name="page_detail"),
    path("diary/page/<int:page_id>/update/", views.page_update, name="page_update"),
    path("diary/page/<int:page_id>/delete/", views.page_delete, name="page_delete"),
]
