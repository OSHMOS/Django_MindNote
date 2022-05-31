from django.shortcuts import render, redirect, get_object_or_404
from .models import Page
from .forms import PageForm

# Create your views here.
def index(request):
    return render(request, "diary/index.html")


def page_list(request):
    object_list = Page.objects.all()
    ctx = {"object_list": object_list}
    return render(request, "diary/page_list.html", ctx)


def info(request):
    return render(request, "diary/info.html")


def page_create(request):
    if request.method == "POST":
        form = PageForm(request.POST)
        if form.is_valid():
            new_page = form.save()
            return redirect("page_detail", page_id=new_page.id)
    else:
        form = PageForm()
    ctx = {"form": form}
    return render(request, "diary/page_form.html", ctx)


def page_detail(request, page_id):
    object = get_object_or_404(Page, id=page_id)
    ctx = {"object": object}
    return render(request, "diary/page_detail.html", ctx)


def page_update(request, page_id):
    object = get_object_or_404(Page, id=page_id)
    if request.method == "POST":
        form = PageForm(request.POST, instance=object)
        if form.is_valid():
            form.save()
            return redirect("page_detail", page_id=object.id)
    else:
        form = PageForm(instance=object)
    ctx = {"form": form}
    return render(request, "diary/page_form.html", ctx)


def page_delete(request, page_id):
    object = get_object_or_404(Page, id=page_id)
    if request.method == "POST":
        object.delete()
        return redirect("page_list")
    else:
        ctx = {"object": object}
        return render(request, "diary/page_confirm_delete.html", ctx)
