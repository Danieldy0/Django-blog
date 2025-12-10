
from django.views import generic
from .models import Post

# View to list all published posts (Blog Index)
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    context_object_name = 'post_list' # Renames 'object_list' to 'post_list' in the template

# View to show a single post's details
class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
    # By default, it uses 'post' as the context object name.
