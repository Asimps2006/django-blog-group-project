from django.urls import path

# from blogging.views import detail_view
# from blogging.views import list_view
from blogging.views import BlogListView, BlogDetailView, add_model
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", BlogListView.as_view(), name="blog_index"),
    path("add/", add_model, name="add_post"),
    path("posts/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
