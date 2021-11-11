from django.shortcuts import redirect, render
from posting.models import Article
from django.shortcuts import get_object_or_404
from django.views import View
from django.http import HttpResponse
from . import views
from posting.forms import CommentForm, CreateArticleForm
from django.contrib.auth.models import User

# Create your views here.


def allpost(request, id):
    datas = Article.objects.get(id=id)
    comments = datas.comments.all()[:3]
    print(comments)

    article_comment = None
    comment_form = CommentForm(request.POST)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            article_comment = comment_form.save(commit=False)
            article_comment.idea = data
            article_comment.save()
            comment_form = CommentForm()

    return render(request, 'details.html', {'data': comments, 'comment_form': comment_form, 'datas': datas, })


def home(request):
    posts = Article.objects.all()
    return render(request, 'index.html', {'post': posts})


def menu(request):
    return render(request, 'navigation.html')


# def post(request):
#     return render(request, 'post.html')


def createArticleView(request):
    forms = CreateArticleForm(request.POST or None)
    current_user = request.user.id
    print(current_user)
    new_form = None
    if request.method == 'POST':
        forms = CreateArticleForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            # new_form.Editor = current_user
            # new_form.save()
            return redirect('home')
    else:
        forms = CreateArticleForm()
    return render(request, 'post.html', {'new_form': forms})
        
