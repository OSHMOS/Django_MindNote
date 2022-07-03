from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("diary/info/", views.info, name="info"),
    path("diary/", views.PageListView.as_view(), name="page_list"),
    path("diary/write/", views.PageCreateView.as_view(), name="page_create"),
    path("diary/page/<int:pk>/", views.PageDetailView.as_view(), name="page_detail"),
    path(
        "diary/page/<int:pk>/update/",
        views.PageUpdateView.as_view(),
        name="page_update",
    ),
    path(
        "diary/page/<int:pk>/delete/",
        views.PageDeleteView.as_view(),
        name="page_delete",
    ),
]
