from ast import Del, Delete
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Page
from .forms import PageForm

# Create your views here.
def index(request):
    return render(request, "diary/index.html")


def info(request):
    return render(request, "diary/info.html")


class PageListView(ListView):
    model = Page
    paginate_by = 8


class PageDetailView(DetailView):
    model = Page


class PageCreateView(CreateView):
    model = Page
    form_class = PageForm

    def get_success_url(self):
        return reverse("page_detail", kwargs={"pk": self.object.id})


class PageUpdateView(UpdateView):
    model = Page
    form_class = PageForm

    def get_success_url(self):
        return reverse("page_detail", kwargs={"pk": self.object.id})


class PageDeleteView(DeleteView):
    model = Page

    def get_success_url(self):
        return reverse("page_list")
