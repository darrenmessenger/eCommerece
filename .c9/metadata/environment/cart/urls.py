{"filter":false,"title":"urls.py","tooltip":"/cart/urls.py","undoManager":{"mark":1,"position":1,"stack":[[{"start":{"row":0,"column":0},"end":{"row":21,"column":85},"action":"insert","lines":["from django.shortcuts import get_object_or_404","from products.models import Product","","","def cart_contents(request):","    \"\"\"","    Ensures that the cart contents are available when rendering","    every page","    \"\"\"","    cart = request.session.get('cart', {})","","    cart_items = []","    total = 0","    product_count = 0","    ","    for id, quantity in cart.items():","        product = get_object_or_404(Product, pk=id)","        total += quantity * product.price","        product_count += quantity","        cart_items.append({'id': id, 'quantity': quantity, 'product': product})","    ","    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}"],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":21,"column":85},"action":"remove","lines":["from django.shortcuts import get_object_or_404","from products.models import Product","","","def cart_contents(request):","    \"\"\"","    Ensures that the cart contents are available when rendering","    every page","    \"\"\"","    cart = request.session.get('cart', {})","","    cart_items = []","    total = 0","    product_count = 0","    ","    for id, quantity in cart.items():","        product = get_object_or_404(Product, pk=id)","        total += quantity * product.price","        product_count += quantity","        cart_items.append({'id': id, 'quantity': quantity, 'product': product})","    ","    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}"],"id":2},{"start":{"row":0,"column":0},"end":{"row":8,"column":1},"action":"insert","lines":["","from django.conf.urls import url","from .views import view_cart, add_to_cart, adjust_cart","","urlpatterns = [","    url(r'^$', view_cart, name='view_cart'),","    url(r'^add/(?P<id>\\d+)', add_to_cart, name='add_to_cart'),","    url(r'^adjust/(?P<id>\\d+)', adjust_cart, name='adjust_cart'),","]"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":2,"column":28},"end":{"row":2,"column":28},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1575929139227,"hash":"7989c7c416fa06238de6c1fda82779912adffebf"}