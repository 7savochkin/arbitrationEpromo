from django.views.generic import ListView, DetailView

from blog.models import Post


class PostListView(ListView):
    """List view for Post model"""
    queryset = Post.objects.all().filter(is_publish=True) # noqa
    paginate_by = 1

    template_name = 'pages/blog/blog_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    """Detail view for Post model"""
    model = Post
    template_name = 'pages/blog/blog_detail.html'
    context_object_name = 'post'
