from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from .models import Product, UserProfile
from .forms import ProductForm, UserProfileForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login



@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id, seller=request.user)
    product.delete()
    return redirect('account')  # Redirect back to the account page after deletion



# Register View


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create UserProfile instance for the new user
            UserProfile.objects.create(user=user)
            login(request, user)  # Log the user in after registration
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})

# Home (Index) View


def index(request):
    return render(request, 'index.html')

# Buy Page


@login_required
def buy(request):
    products = Product.objects.all()
    saved_products = request.user.saved_products.values_list('id', flat=True)
    return render(request, 'buy.html', {'products': products ,'saved_products': saved_products})

# Sell Page


@login_required
def sell(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            return redirect('buy')
    else:
        form = ProductForm()
    return render(request, 'sell.html', {'form': form})

# Account Page
# @login_required
# def account(request):
#     user_profile, created = UserProfile.objects.get_or_create(user=request.user)
#     return render(request, 'account.html', {'user_profile': user_profile})

# Account Page with Edit Option


@login_required
def account(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    products_sold = Product.objects.filter(seller=request.user)  # Get products sold by the user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('account')  # Refresh the page to show updated data
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'account.html', {
        'user_profile': user_profile,
        'form': form,
        'products_sold': products_sold  # Pass sold products to the template
    })


# Saved Items


@login_required
def saved_items(request):
    saved_products = request.user.userprofile.saved_products.all()
    return render(request, 'saved.html', {'saved_products': saved_products})

# Save or Unsave a Product


@login_required
def toggle_save_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if product in user_profile.saved_products.all():
        user_profile.saved_products.remove(product)
        print(f"Removed {product.name} from saved products.")
    else:
        user_profile.saved_products.add(product)
        print(f"Added {product.name} to saved products.")

    return redirect('saved_items') 


@login_required
def logout_view(request):
    logout(request)
    return redirect('index')
    
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from .models import Product

# @csrf_exempt
# def delete_product(request, product_id):
#     if request.method == 'DELETE':
#         try:
#             product = Product.objects.get(id=product_id, owner=request.user)
#             product.delete()
#             return JsonResponse({'message': 'Product deleted successfully.'}, status=204)
#         except Product.DoesNotExist:
#             return JsonResponse({'error': 'Product not found.'}, status=404)
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)
#     return JsonResponse({'error': 'Invalid request.'}, status=400)
