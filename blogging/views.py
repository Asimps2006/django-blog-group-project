from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.utils import timezone
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blogging.forms import PostForm


def add_model(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.author = request.user
            model_instance.published_date = timezone.now()
            model_instance.save()
            return redirect("/")

    else:
        print(request.user)
        if request.user.is_anonymous:
            return redirect("../accounts/login/")
        form = PostForm()
        return render(request, "blogging/add.html", {"form": form})


def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")


# # and this view
# def list_view(request):
#     published = Post.objects.exclude(published_date__exact=None)
#     posts = published.order_by('-published_date')
#     template = loader.get_template('blogging/list.html')
#     context = {'posts': posts}
#     body = template.render(context)
#     return HttpResponse(body, content_type="text/html")

# def list_view(request):
#     published = Post.objects.exclude(published_date__exact=None)
#     posts = published.order_by('-published_date')
#     context = {'posts': posts}
#     return render(request, 'blogging/list.html', context)


class BlogListView(ListView):
    queryset = Post.objects.exclude(published_date__exact=None).order_by(
        "-published_date"
    )
    # posts = published.order_by('-published_date')
    template_name = "blogging/list.html"


# def detail_view(request, post_id):
#     published = Post.objects.exclude(published_date__exact=None)
#     try:
#         post = published.get(pk=post_id)
#     except Post.DoesNotExist:
#         raise Http404
#     context = {'post': post}
#     return render(request, 'blogging/detail.html', context)


class BlogDetailView(DetailView):
    queryset = Post.objects.exclude(published_date__exact=None)
    # exclude(published_date__exact=None)
    template_name = "blogging/detail.html"

    # def post(self, request, *args, **kwargs):
    #     try:
    #         post = self.get_object()
    #     except Post.DoesNotExist:
    #         raise Http404
    #     context = {'object': post}
    #     return render(request, 'blogging/detail.html', context)
