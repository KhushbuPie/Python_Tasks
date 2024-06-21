from django.shortcuts import render,redirect, get_object_or_404
from blog.models import Post, Comment, Category
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from blog.forms import CommentsForm
from django.db import connection
import time
from .models import PostWithDetails , Post
from .forms import PostForm


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('blog_index')  # Redirect to the index page after successful submission
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})

def like_post(request, post_id):
    if request.method == "POST":
        post =Post.get.objects(Post, id=post_id)
        post.like += 1
        post.save()
        return JsonResponse({'likes': post.like})
    return JsonResponse({'error': 'Invalid request'}, status=400)

    
def optimized_post_details(request, pk):
    post_details = PostWithDetails.objects.get(post_id=pk)
    context = {
        'post_details': post_details
    }
    return render(request, 'blog/post_details.html', context)

def optimized_post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'blog/optimized_post_list.html', context)
# Return all the post in order of when they created
# Before optimization
def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context)

# After optimization
def blog_index_A(request):
    posts = Post.objects.only('title', 'created_on').order_by("-created_on")
    context = {
        "posts":posts,
    }
    return render(request, "blog/index.html", context)

#Gives all the post of the particukar category
def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog/category.html",context)

#After optimization
def blog_category_A(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).only('title', 'created_on').order_by("-created_on").prefetch_related('categories')
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog/category.html", context)

# function returns the single post by primary key
def blog_details(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentsForm()
    if request.method == "POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body = form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": CommentsForm(),
    }
    return render(request, "blog/detail.html", context)

#After optimization
def blog_details_A(request, pk):
    post = Post.objects.only('title', 'body').select_related('categories').get(pk=pk)
    form = CommentsForm()
    if request.method == "POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
    comments = Comment.objects.filter(post=post).only('author', 'body', 'created_on')
    context = {
        "post": post,
        "comments": comments,
        "form": CommentsForm(),
    }
    return render(request, "blog/detail.html", context)

#Get the title with category
def title(request):
    posts = Post.objects.only('title').prefetch_related('categories')
    post_titles = []
    for post in posts:
        # categories = ", ".join ([category.name for category in post.categories.all()])
        post_titles.append((post.title, post.categories.name))
    context = {
        'post_titles': post_titles
    }

    return render(request,"blog/title.html" ,context)






# def explain_query(query):
#     query = "SELECT * FROM blog_post where UPPER(title) LIKE UPPER('%Post 1%') "
#     response = []
#     with connection.cursor() as cursor:
#         cursor.execute(f"EXPLAIN {query}")
#         for row in cursor.fetchall():
#             response.append(str(row))
#     return HttpResponse("<br>".join(response))
    
# def create_sample_date():
#     """create sample data foe testing"""
#     for i in range(1000):
#         Post.objects.create(title=f"Post {i}", body="Samle body")

# def measure_index_performance(request):
#     response_text = ""

#     #Droping the index if it exists
#     with connection.cursor() as cursor:
#         cursor.execute("DROP INDEX IF EXISTS blog_post_title")

#     create_sample_date()

#     # Measure query time without index
#     start_time = time.perf_counter()
#     posts = Post.objects.filter(title__icontains="Post 2").all()
#     end_time = time.perf_counter()
#     response_text += f"Query Time Without Index on title: {end_time - start_time} seconds \n"

#     # Create the index on title
#     with connection.cursor() as cursor:
#         cursor.execute("CREATE INDEX blog_post_title ON blog_post (title)")

#     #Measure query time with index
#     start_time = time.perf_counter()
#     posts = Post.objects.filter(title__icontains='Post 2').all()
#     end_time = time.perf_counter()
#     response_text += f"Query Time With Index on title:{end_time - start_time} seconds \n"

#     # Drop and analyze the query without index
#     with connection.cursor() as cursor:
#         cursor.execute("DROP INDEX IF EXISTS blog_post_title")
#         cursor.execute("EXPLAIN QUERY PLAN SELECT * FROM blog_post WHERE title LIKE '%Post 2'")
#         response_text += "Query Plan Without Index: \n"
#         for row in cursor.fetchall():
#             response_text +=f"{row}\n"

#     # Create and analyze the query with index
#     with connection.cursor() as cursor:
#         cursor.execute("CREATE INDEX blog_post_title ON blog_post (title)")
#         cursor.execute("EXPLAIN QUERY PLAN SELECT * FROM blog_post WHERE title LIKE '%Post 2%' ")
#         response_text += "Query Plan With Index: \n"
#         for row in cursor.fetchall():
#             response_text += f"{row}\n"

#     return HttpResponse(response_text, content_type="text/plain")

