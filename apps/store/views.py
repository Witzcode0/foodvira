from django.shortcuts import render
from apps.master.models import Contact
from apps.products.models import Product, ProductImages
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.
def index(request):
    return render(request, "store/index.html")

def products(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request, "store/products.html", context)

def product_detail(request, product_id):
    # print(product_id)
    product = Product.objects.get(id=product_id)
    context = {
        "product": product
    }
    print(context)
    return render(request, "store/product_details.html", context)

def blog(request):
    return render(request, "store/blog.html")

def about(request):
    return render(request, "store/about.html")

def contact(request):
    if request.method == "POST":
        name_ = request.POST['name']
        email_ = request.POST['email']
        message_ = request.POST['message']
        print(name_, email_, message_)

        new_contact = Contact.objects.create(
            name = name_,
            email = email_,
            message = message_
        )
        new_contact.save()
        messages.success(request, "Your request submited successfully.")
        return redirect("contact")


    return render(request, "store/contact.html")