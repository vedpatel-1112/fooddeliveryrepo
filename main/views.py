from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password, make_password
from .models import User, FoodItem, Order
 


# ================= ADMIN =================

def admin_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            admin = User.objects.get(email=email, is_admin=True)
            if check_password(password, admin.password):
                request.session['admin'] = admin.id
                return redirect('/admin-dashboard/')
        except User.DoesNotExist:
            pass

    return render(request, 'main/admin_login.html')


def admin_dashboard(request):
    if 'admin' not in request.session:
        return redirect('/admin-login/')
    return render(request, 'main/admin_dashboard.html')


def admin_users(request):
    if 'admin' not in request.session:
        return redirect('/admin-login/')
    users = User.objects.filter(is_admin=False)
    return render(request, 'main/admin_users.html', {'users': users})


def delete_user(request, id):
    if 'admin' not in request.session:
        return redirect('/admin-login/')
    User.objects.get(id=id).delete()
    return redirect('/admin-users/')


def admin_food(request):
    if 'admin' not in request.session:
        return redirect('/admin-login/')
    foods = FoodItem.objects.all()
    return render(request, 'main/admin_food.html', {'foods': foods})


def add_food(request):
    if 'admin' not in request.session:
        return redirect('/admin-login/')

    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        image = request.POST.get("image")  # local image path

        FoodItem.objects.create(
            name=name,
            price=price,
            image=image
        )
        return redirect('/admin-food/')

    return render(request, 'main/add_food.html')


def delete_food(request, id):
    if 'admin' not in request.session:
        return redirect('/admin-login/')
    FoodItem.objects.get(id=id).delete()
    return redirect('/admin-food/')


# ================= USER =================

def home(request):
    items = FoodItem.objects.all()
    return render(request, 'main/home.html', {'items': items})


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                request.session['user'] = user.id
                return redirect('/')
        except User.DoesNotExist:
            pass

    return render(request, 'main/login.html')


def signup_view(request):
    if request.method == "POST":
        name = request.POST.get("fullname")
        email = request.POST.get("email")
        password = request.POST.get("password")

        User.objects.create(
    full_name=name,
    email=email,
    password=make_password(password)
)

        return redirect('/login/')

    return render(request, 'main/signup.html')


# ================= CART =================

def add_to_cart(request, id):
    if 'user' not in request.session:
        return redirect('/login/')

    item = FoodItem.objects.get(id=id)
    cart = request.session.get('cart', {})

    if str(id) in cart:
        cart[str(id)]['qty'] += 1
    else:
        cart[str(id)] = {
            'name': item.name,
            'price': float(item.price),
            'qty': 1
        }

    request.session['cart'] = cart
    return redirect('/cart/')


def cart_view(request):
    if 'user' not in request.session:
        return redirect('/login/')

    cart = request.session.get('cart', {})
    total = 0

    for item in cart.values():
        item['item_total'] = item['price'] * item['qty']
        total += item['item_total']

    return render(request, 'main/cart.html', {
        'cart': cart,
        'total': total
    })


# ================= ORDER =================

def place_order(request):
    if 'user' not in request.session:
        return redirect('/login/')

    user = User.objects.get(id=request.session['user'])
    cart = request.session.get('cart', {})

    for item_id, item in cart.items():
        Order.objects.create(
            user=user,
            food_item=FoodItem.objects.get(id=item_id),
            quantity=item['qty'],
            total_price=item['price'] * item['qty']
        )

    request.session['cart'] = {}
    return render(request, 'main/order_success.html')


# ================= ADMIN ORDERS =================

def admin_orders(request):
    if 'admin' not in request.session:
        return redirect('/admin-login/')

    orders = Order.objects.all().order_by('-order_date')
    return render(request, 'main/admin_orders.html', {'orders': orders})

