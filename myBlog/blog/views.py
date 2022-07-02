from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy, reverse

# Create your views here.
def LikePostView(request, pk):
    post = get_object_or_404(Post, id=request.POST['postId'])
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('ArticleDetail', args=[str(pk)]))

class HomeView(ListView):
    model = Post
    template_name = 'blog/index.html'
    ordering = ['-pub_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'blog/categories.html', {'cat_menu_list': cat_menu_list})

def CategoryPostsView(request, cat):
    cat_posts = Post.objects.filter(category__icontains=cat.replace('-', ' '))
    return render(request, 'blog/category_posts.html', {'cat': cat.title().replace('-', ' '), 'cat_posts': cat_posts})

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)

        current_post = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = current_post.total_likes()

        liked = False
        if current_post.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class AddPostView(SuccessMessageMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'
    success_message = 'Post - | %(title)s | has been added successfully.'
    # fields = '__all__'
    # fields = ('title', 'content')

class AddCategoryView(SuccessMessageMixin, CreateView):
    model = Category
    template_name = 'blog/add_cat.html'
    fields = '__all__'

class UpdatePostView(SuccessMessageMixin, UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'blog/update_post.html'
    success_message = 'Your Post - | %(title)s | has been updated successfully.'

class DeletePostView(SuccessMessageMixin, DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('BlogHome')
    success_message = 'Your Post - | %(title)s | has been deleted successfully.'
