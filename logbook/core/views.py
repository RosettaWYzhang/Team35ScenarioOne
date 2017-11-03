from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from logbook.core.models import Entry, Category
from django.shortcuts import render_to_response, get_object_or_404
from logbook.core.forms import SignUpForm, EntryForm, CategoryForm
from django.views.generic import DeleteView
from django.core import urlresolvers
from django.utils import timezone


@login_required
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            username = signup_form.cleaned_data.get('username')
            raw_password = signup_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        signup_form = SignUpForm()
    return render(request, 'signup.html', {'signup_form': signup_form})

def view_post(request, slug):
    return render(request, 'view_post.html', {
                            'post': get_object_or_404(Entry, slug=slug)
                            })

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'view_category.html', {
                            'category': category,
                            'posts': Entry.objects.filter(category=category)[:5]
                            })

def create_post(request):
    if request.method == 'POST':
        post_form = EntryForm(request.POST)
        if post_form.is_valid():
            post = post_form.save()
            post.title = post_form.cleaned_data.get('title')
            post.slug = post_form.cleaned_data.get('slug')
            post.body = post_form.cleaned_data.get('body')
            post.url = post_form.cleaned_data.get('url')
            post.category = post_form.cleaned_data.get('category')
            post.date = timezone.now()
            post.save()
            return redirect('home')
    else:
        post_form = EntryForm()
    return render(request, 'create_post.html', {'post_form': post_form})

def edit_post(request, slug):
    if request.method == 'POST':
        my_record = Entry.objects.get(slug=slug)
        post_form = EntryForm(request.POST, instance=my_record)
        if post_form.is_valid():
            post_form.save()
            title = post_form.cleaned_data.get('title')
            slug = post_form.cleaned_data.get('slug')
            body = post_form.cleaned_data.get('body')
            url = post_form.cleaned_data.get('url')
            category = post_form.cleaned_data.get('category')
            return redirect('home')
    else:
        post_form = EntryForm(instance=my_record)
    return render(request, 'edit_post.html', {'title':my_record.title, 'instance': my_record, 'post_form': post_form})

def create_category(request):
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            title = category_form.cleaned_data.get('title')
            slug = category_form.cleaned_data.get('slug')
            return redirect('home')
    else:
        category_form = CategoryForm()
    return render(request, 'create_category.html', {'category_form': category_form})

def view_categories(request):
    categories = Category.objects.all()
    return render(request, 'view_categories.html', {'categories': categories})

def view_posts(request):
    posts = Entry.objects.all()
    return render(request, 'view_posts.html', {'posts': posts})

def delete_post(request, slug):
    instance = get_object_or_404(Entry, slug=slug)
    instance.delete()
    return render(request, 'view_posts.html')

def search_post(request):
    keyword = request.GET['q']
    posts = Entry.objects.filter(title__contains=keyword)
    return render(request, 'search_post.html', {'posts': posts})
