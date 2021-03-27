from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from profiles.models import UserProfile
from products.models import Product
from .models import Wishlist
from django.contrib.auth.decorators import login_required


@login_required
def wishlist(request):
    """
    Get and display user's wishlist if they have one created or create one if
    they have not
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    wishlist, created = Wishlist.objects.get_or_create(user_profile=profile)
    wishlisted_products = Product.objects.filter(
        wishlist__user_profile=profile)

    context = {
        "profile": profile,
        "wishlisted_products": wishlisted_products,
    }

    return render(request, "wishlists/wishlist.html", context)


