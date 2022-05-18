from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail, get_connection
from django.http import HttpResponseRedirect
from .forms import ContactForm, UserRegisterForm
from .models import Category, Product
from django.contrib import messages


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all().order_by('-id')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {'category': category, 'categories': categories,
                                                      'products': products[:3]})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    return render(request, 'shop/product/detail.html', {'product': product})


def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Email Inquery'
            body = {
                'full_name': form.cleaned_data['full_name'],
                'subject': form.cleaned_data['subject'],
                'email_address': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = f"""
            From: {body['full_name']}\n
            Subject: {body['subject']}\n
            Email address: {body['email_address']}\n
            Message: {body['message']}\n
            """
            conn = get_connection('django.core.mail.backends.smtp.EmailBackend')
            send_mail(subject, message, body['email_address'], ['emiliyasart@gmail.com'], fail_silently=False,
                      connection=conn)
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'shop/contact.html', {'form': form, 'submitted': submitted})


def about_us(request):
    return render(request, 'shop/about_us.html', {})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! ')
            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
