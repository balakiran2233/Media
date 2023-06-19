from django.shortcuts import render,get_object_or_404,redirect
from .models import Article,Images,Comment
from .forms import ArticleCreateForm,UserLoginForm,UserRegisterForm,ArticleEditForm,CommentForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib import messages
from django.forms import modelformset_factory
import datetime as dt
date1=dt.datetime.now().date()

def articleList(request):
    article_list=Article.objects.all().order_by('-id')
    query1=request.GET.get('query')
    if query1:
        article_list=Article.objects.filter(
        Q(title__icontains=query1) |
        Q(author__username=query1) |
        Q(body__icontains=query1)
        )

    paginator=Paginator(article_list,10)
    page=request.GET.get('page')

    try:
        articles=paginator.page(page)
    except PageNotAnInteger:
        articles=paginator.page(1)
    except EmptyPage:
        articles=paginator.page(paginator.num_pages)


    return render(request,'articleList.html',{'articles':articles})

def like_article(request):
    aid=request.POST.get('article_id')
    article=get_object_or_404(Article,id=aid)

    if article.likes.filter(id=request.user.id).exists():
        article.likes.remove(request.user)
        is_liked=False
    else:
        article.likes.add(request.user)
        is_liked=True
    return HttpResponseRedirect(article.get_absolute_url())


def articleDetail(request,id,slug):
    article=get_object_or_404(Article,id=id,slug=slug)
    comments=Comment.objects.filter(article=article,reply=None).order_by('-id')
    is_liked=False
    is_favourite=False
    if article.likes.filter(id=request.user.id).exists():
        is_liked=True


    if article.favourite.filter(id=request.user.id).exists():
        is_favourite=True

    if request.method=='POST':
        comment_form=CommentForm(request.POST or None)
        if comment_form.is_valid:
            content=request.POST.get('content')
            reply_id=request.POST.get('comment_id')
            comment_qs=None
            if reply_id:
                comment_qs=Comment.objects.get(id=reply_id)
            comment=Comment.objects.create(article=article,user=request.user,content=content,reply=comment_qs)
            comment.save()
            return HttpResponseRedirect(article.get_absolute_url())
    else:
        comment_form=CommentForm()
    return render(request,'articleDetail.html',{
    'article':article,
    'is_liked':is_liked,
    'is_favourite':is_favourite,
    'total_likes':article.total_likes(),
    'comments':comments,
    'comment_form':comment_form,
    })



def article_create(request):
    ImageFormSet=modelformset_factory(Images,fields=('image',),extra=2)
    if request.method=='POST':
        form=ArticleCreateForm(request.POST)
        formset=ImageFormSet(request.POST or None,request.FILES or None)
        if form.is_valid() and formset.is_valid():
            title1=request.POST.get('title')
            body1=request.POST.get('body')
            article=Article(
            title=title1,
            body=body1,
            author=request.user,
            created_date=date1
            )
            article.save()

            for i in formset:
                try:

                    photo=Images(article=article,image=i.cleaned_data['image'])
                    photo.save()
                    return render('article_list')
                except Exception:
                    break

            messages.success(request,"New Article is created Successfully")
            return redirect('article_list')
    else:
        form=ArticleCreateForm()
        formset=ImageFormSet(queryset=Images.objects.none())
        return render(request,'articlecreate.html',{'form':form,'formset':formset})

def article_edit(request,id):
    article=get_object_or_404(Article,id=id)
    if request.method=='POST':
        form=ArticleEditForm(request.POST or None,instance=article)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(article.get_absolute_url())

    else:
        form=ArticleEditForm(instance=article)
        return render(request,'article_edit.html',{'form':form,'article':article})

def article_delete(request,id):
    article=get_object_or_404(Article,id=id)
    article.delete()
    messages.warning(request,'Article deleted Successfully')
    return redirect('article_list')


def favourite_article(request,id):
    aid=request.POST.get('article_id')
    article=get_object_or_404(Article,id=aid)
    if article.favourite.filter(id=request.user.id).exists():
        article.favourite.remove(request.user)
        is_favourite=False
    else:
        article.favourite.add(request.user)
        is_favourite=True
    return HttpResponseRedirect(article.get_absolute_url())

def article_favourite_list(request):
    user=request.user
    favourite_articles=user.favourite.all()
    context={
    'favourite_articles':favourite_articles
    }
    return render(request,'article_favourite_list.html',context)

def registerView(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            new_user=form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return redirect('loginView')
        else:
            return HttpResponse('Invalid Data')
    else:
        form=UserRegisterForm()
        return render(request,'registerform.html',{'form':form})

def loginView(request):
    if request.method=='POST':
        form=UserLoginForm(request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    messages.error(request,"Login Successful")
                    return redirect('article_list')
                else:
                    return HttpResponse('InActive Person')
            else:
                return HttpResponse('None')
        else:
            return HttpResponse('Incorrect Details..')
    else:
        form=UserLoginForm()
        return render(request,'loginform.html',{'form':form})


def logoutView(request):
    logout(request)
    messages.info(request,"Logout is Done")
    return redirect('article_list')

'''
<li class="fa fa-heart-o"></li>
'''
