from django.shortcuts import render
from .models import Page

# Create your views here.
def page_list(request):
    object_list = Page.objects.all()
    ctx = {"object_list": object_list}
    return render(request, "diary/page_list.html", ctx)


def info(request):
    pass


def page_create(request):
    pass


def page_detail(request, page_id):
    object = Page.objects.get(id=page_id)
    ctx = {"object": object}
    return render(request, "diary/page_detail.html", ctx)


def page_update(request):
    pass


def page_delete(request):
    pass
