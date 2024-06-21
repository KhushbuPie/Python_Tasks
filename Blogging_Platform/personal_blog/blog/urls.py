from django.urls import path
from . import views
from .views import optimized_post_list
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("post/<int:pk>/", views.blog_details, name="blog_detail"),
    path("category/<category>/", views.blog_category, name="blog_category"),
    # path('explain/', views.explain_query, name='explain_query'),
    # path('measure-index-performance/', measure_index_performance, name='measure_index_performance'),
    path('title/', views.title, name='title'),
    path('optimized-posts/', optimized_post_list, name='optimized_post_list'),
    path('add_post/', views.add_post, name='add_post'),
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
