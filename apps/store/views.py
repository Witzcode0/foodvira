from django.shortcuts import render, get_object_or_404
from apps.master.models import Contact, Blog, TeamMember
from apps.products.models import Product, ProductImages
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.
def index(request):
    products = Product.objects.order_by('-created_at')[:8]   # last 8 added products
    blogs = Blog.objects.order_by('-created_at')[:3]          # last 3 added blogs

    context = {
        'products': products,
        'blogs': blogs
    }
    return render(request, "store/index.html", context)

def products(request):
    products = Product.objects.order_by('-created_at')
    context = {
        'products':products
    }
    return render(request, "store/products.html", context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    context = {
        "product": product,
        "product_images": product.images.all()  # 🔥 BEST
    }
    print(context)
    return render(request, "store/product_details.html", context)

def blog(request):
    blogs  = Blog.objects.order_by('-created_at')
    context = {
        'blogs': blogs
    }
    return render(request, "store/blog.html", context)

def product_inquiry(request):
    products = Product.objects.order_by('-created_at')[:8]   # last 8 added products
    blogs = Blog.objects.order_by('-created_at')[:3]          # last 3 added blogs

    context = {
        'products': products,
        'blogs': blogs
    }
    return render(request, "store/index.html", context)


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    latest_blogs = Blog.objects.exclude(id=blog.id).order_by('-created_at')[:5]

    
    # Optional: increment view count
    # blog.views = blog.views + 1 if blog.views else 1
    # blog.save(update_fields=['views'])
    
    context = {
        'blog': blog,
        "latest_blogs":latest_blogs
    }
    return render(request, 'store/blog_detail.html', context)

def about(request):
    # Get all team members ordered by the 'order' field
    team_members = TeamMember.objects.all()
    
    context = {
        'team_members': team_members
    }
    
    return render(request, "store/about.html", context)

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