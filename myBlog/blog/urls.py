from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryListView, CategoryPostsView, LikePostView

urlpatterns = [
    path('', HomeView.as_view(), name="BlogHome"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="ArticleDetail"),
    path('add_post/', AddPostView.as_view(), name="AddPost"),
    path('add_cat/', AddCategoryView.as_view(), name="AddCategory"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="UpdatePost"),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name="DeletePost"),
    path('categories/', CategoryListView, name="Categories"),
    path('category/<str:cat>', CategoryPostsView, name="CategoryPosts"),
    path('like/<int:pk>', LikePostView, name="LikePost"),
]
