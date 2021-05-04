from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import ArticlePost
from .form import ArticlePostForm
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login
# Create your views here.

def show_list(request):
    articles = ArticlePost.objects.all()
    context = {'articles' : articles}
    return render(request, 'article_list.html', context)
def show_detail(request, id):
    article = ArticlePost.objects.get(id=id)
    context = {'article' : article}
    return render(request, 'article_detail.html', context)
def article_submit(request):
    if request.method == "POST":
        article_post_form = ArticlePostForm(data=request.POST)
        # created a new instance of form
        if article_post_form.is_valid():
            # save() created a new instance of model, which is article
            new_article = article_post_form.save(commit=False)
            new_article.author = User.objects.get(id=request.user.id)
            new_article.save()
            return redirect("article:article_list")
        else:
            return HttpResponse("Error Form")
    else:
        # the request method is "GET"
        # which means I have to create a empty form
        # let it go to the html page, let the user input the info
        empty_article_post_form = ArticlePostForm()
        context = {'empty_article_post_form' : empty_article_post_form}
        return render(request, 'article_submit.html', context)
def article_delete(request, id):
    article = ArticlePost.objects.get(id=id)
    article.delete()
    return render(request, 'index_page.html')
def article_update(request, id):
    article = ArticlePost.objects.get(id = id)
    if request.method == "POST":
        new_form = ArticlePostForm(data = request.POST)
        if new_form.is_valid():
            article.title = request.POST['title']
            article.body = request.POST['body']
            article.save()
            return redirect("article:article_detail", id = id)
        else:
            return HttpResponse("Error Form")
    else:
        empty_article_post_form = ArticlePostForm()
        context = {'article' : article, 'empty_article_post_form' : empty_article_post_form}
        return render(request, 'article_update.html', context)
