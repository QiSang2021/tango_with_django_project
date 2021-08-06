from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from datetime import datetime

from rango.models import Category, Page, Comment, Article
from rango.forms import PageForm,ArticleForm, CommentForm



# Create your views here.

def index(request):
    category_list = Category.objects.order_by('-brandname')[:10] # why not all?
    page_list = Page.objects.order_by('-views')[:3]

    context_dict = {}
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list
   
    return render(request, 'rango/index.html',context=context_dict)

def about(request):
    context_dict = {}
    return render(request, 'rango/about.html', context=context_dict)

def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request, 'rango/category.html', context=context_dict)

def show_page(request, page_name_slug):
    context_dict = {}
    try:
        page = Page.objects.get(slug=page_name_slug)
        clothname = Page.objects.filter(clothname=page.clothname)
        price = Page.objects.filter(price=page.price)
        description = Page.objects.filter(description=page.description)
        comments = Comment.objects.filter(page=page)
        context_dict['page'] = page
        context_dict['clothname'] = clothname
        context_dict['price'] = price
        context_dict['description'] = description
        context_dict['comments'] = comments
        context_dict['comment_form'] = CommentForm()
    except Page.DoesNotExist:
        context_dict['page'] = None
        context_dict['clothname'] = None
        context_dict['price'] = None
        context_dict['description'] = None
        context_dict['comment'] = None
    return render(request, 'rango/page.html', context=context_dict)

def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None
    if category is None:
        return redirect(reverse('rango:index'))

    form = PageForm()
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.typeAuto = 0
                page.save()
                return redirect(reverse('rango:show_category',kwargs={'category_name_slug':category_name_slug}))
        else:
            print(form.errors)

    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add_page.html', context=context_dict)

def submit_comment(request, page_name_slug):
    try:
        page = Page.objects.get(slug=page_name_slug)
    except Category.DoesNotExist:
        page = None
    if page is None:
        return redirect(reverse('rango:index'))

    data = {}
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            if page:
                comment = Comment()
                comment.page =  Page.objects.get(slug=page_name_slug)
                comment.author = request.user
                comment.text = form.cleaned_data['text']
                comment.save()
                # implement ajax
                data['status'] = 'SUCCESS'
                data['author'] = comment.author.username
                data['comtime'] = comment.comtime.strftime('%Y-%m-%d %H:%M:%S')
                data['text'] = comment.text

        else:
            data['status'] = 'ERROR'
            data['message'] = list(form.errors.values())[0]


    return JsonResponse(data) 

def profile(request):
    context_dict = {}
    articles = Article.objects.order_by('title')[:10]
    context_dict['article_list']=articles
    return render(request, 'rango/profile.html', context=context_dict)

def recommendation(request):
    context_dict = {}
    return render(request, 'rango/recommendation.html', context=context_dict)
def article(request):
    context_dict = {}
    article_list = Article.objects.order_by('title')[:10]
    context_dict['articles'] = article_list
    return render(request, 'rango/article.html', context=context_dict)

def show_article(request,article_title_slug):
    context_dict = {}
    try:
        article = Article.objects.get(slug=article_title_slug)
        context_dict['article'] = article
        context_dict['title'] = article.title
        context_dict['content'] = article.content
        context_dict['author'] = article.authorName
        context_dict['uploader'] = article.uploader
    except Category.DoesNotExist:
        context_dict['articles'] = None
    return render(request, 'rango/article_detail.html', context=context_dict)

def add_article(request):
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            # if article:
                curarticle = form.save(commit=False)
                # curarticle=article
                curarticle.uploader= request.user
                # curarticle.typeAuto = False
                curarticle.save()
                return redirect(reverse('rango:index'))
        else:
            print(form.errors)

    context_dict = {'form': form}
    return render(request, 'rango/add_article.html', context=context_dict)

def item(request):
    category_list = Category.objects.order_by('-brandname')[:10]  # why not all?
    page_list = Page.objects.order_by('-views')[:10]
    context_dict = {}
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list

    return render(request, 'rango/item.html', context=context_dict)

