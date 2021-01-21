from django.shortcuts import render
from django.shortcuts import render
from .models import Post

# Create your views here.
class IndexView(View):
  def get(self, request, *args, **kwargs):
    post_data = Post.objects.order_by("-id")
    return render(request, 'app/index.html', {
        'post_data': post_data,
    })