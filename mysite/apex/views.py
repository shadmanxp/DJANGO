from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.template import loader
from .list_dal import *
from .details_dal import *
from .cart_dal import *
from .orders_dal import *
from .accounts_dal import *
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from .models import TblCatalog
from .forms import *


def index(request):
    try:
        gender_list = get_gender_list()
        ft_products = get_featured_products()
        cart_items = get_cart_items(request)
        template = loader.get_template('apex/index.html')
        context = {
            'gender_list': gender_list,
            'featured_products': ft_products,
            'session_full_name': request.session.get('full_name', None),
            'session_user_email': request.session.get('user_email', None),
            'cart_count': len(cart_items),
        }
    except TblCatalog.DoesNotExist:
        raise Http404("Question does not exist")
    return HttpResponse(template.render(context, request))


def initial_list(request, gender, page):
    try:
        gender_list = get_gender_list()
        category_list = get_category_list(gender)
        cart_items = get_cart_items(request)
        # gender_collection = get_gender_collection(gender)
        gender_collection_pagination = get_gender_collection_pagination(gender)
        page_wise_gender_collection = gender_collection_pagination.page(page)
        page_has_next = page_wise_gender_collection.has_next()
        page_has_previous = page_wise_gender_collection.has_previous()
        try:
            page_next = page_wise_gender_collection.next_page_number()
        except:
            page_next = page
        try:
            page_previous = page_wise_gender_collection.previous_page_number()
        except:
            page_previous = 1
        template = loader.get_template('apex/list.html')
        context = {
            'gender_list': gender_list,
            # 'gender_collection': gender_collection,
            'gender': gender,
            'category_list': category_list,
            'page_wise_gender_collection': page_wise_gender_collection,
            'gender_collection_pagination': gender_collection_pagination,
            'gender_current_page': int(page),
            'gender_page_has_next': page_has_next,
            'gender_page_has_previous': page_has_previous,
            'gender_page_next': page_next,
            'gender_page_previous': page_previous,
            'session_full_name': request.session.get('full_name', None),
            'session_user_email': request.session.get('user_email', None),
            'cart_count': len(cart_items),

        }

    except TblCatalog.DoesNotExist:
        raise Http404("Page not found")
    return HttpResponse(template.render(context, request))


def further_list(request, gender, category, page):
    try:
        gender_list = get_gender_list()
        category_list = get_category_list(gender)
        category = category.strip()
        cart_items = get_cart_items(request)
        # category_collection = get_category_collection(gender, category)
        category_collection_pagination = get_category_collection_pagination(gender, category)
        page_wise_category_collection = category_collection_pagination.page(page)
        page_has_next = page_wise_category_collection.has_next()
        page_has_previous = page_wise_category_collection.has_previous()
        try:
            page_next = page_wise_category_collection.next_page_number()
        except:
            page_next = page
        try:
            page_previous = page_wise_category_collection.previous_page_number()
        except:
            page_previous = 1
        template = loader.get_template('apex/list.html')
        context = {
            'gender_list': gender_list,
            'gender': gender,
            'category': category,
            'category_list': category_list,
            # 'category_collection': category_collection,
            'page_wise_category_collection': page_wise_category_collection,
            'category_collection_pagination': category_collection_pagination,
            'category_current_page': int(page),
            'category_page_has_next': page_has_next,
            'category_page_has_previous': page_has_previous,
            'category_page_next': page_next,
            'category_page_previous': page_previous,
            'session_full_name': request.session.get('full_name', None),
            'session_user_email': request.session.get('user_email', None),
            'cart_count': len(cart_items),
        }

    except TblCatalog.DoesNotExist:
        raise Http404("Page not found")
    return HttpResponse(template.render(context, request))


def details(request, gender, category, art_no, leather_1):
    try:
        gender_list = get_gender_list()
        category_list = get_category_list(gender)
        cart_items = get_cart_items(request)
        list_by_art_no = get_list_by_art_no(art_no)
        product_details = get_details(art_no, leather_1)
        color_count = len(list(list_by_art_no))
        template = loader.get_template('apex/details.html')
        context = {
            'gender_list': gender_list,
            'gender': gender,
            'category': category,
            'category_list': category_list,
            'art_no': art_no,
            'list_by_art_no': list_by_art_no,
            'product_details': product_details,
            'color_count': color_count,
            'range': range(0, 5, 1),
            'session_full_name': request.session.get('full_name', None),
            'session_user_email': request.session.get('user_email', None),
            'cart_count': len(cart_items),
        }
    except TblCatalog.DoesNotExist:
        raise Http404("Page not found")
    return HttpResponse(template.render(context, request))


def signup(request):
    gender_list = get_gender_list()
    cart_items = get_cart_items(request)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            insert_user_info(form_data)
            # return HttpResponseRedirect('/signup')
            context = {
                'gender_list': gender_list,
                'form': SignUpForm(),
                'from_data': form_data,
                'confirmation_message': 'Registration completed!',
                'session_full_name': request.session.get('full_name', None),
                'session_user_email': request.session.get('user_email', None),
                'cart_count': len(cart_items),
            }
        elif form.has_error('user_email', code=None):
            for error in form.errors['user_email']:
                email_error = error
                context = {
                    'gender_list': gender_list,
                    'form': SignUpForm(),
                    'email_error': email_error,
                    'denial_message': 'Registration not complete!',
                    'cart_count': len(cart_items),
                }
        elif form.has_error('conf_pass', code=None):
            for error in form.errors['conf_pass']:
                pass_error = error
            context = {
                'gender_list': gender_list,
                'form': SignUpForm(),
                'pass_error': pass_error,
                'denial_message': 'Registration not complete!',
                'cart_count': len(cart_items),
            }
    else:
        context = {
            'gender_list': gender_list,
            'form': SignUpForm(),
            'session_full_name': request.session.get('full_name', None),
            'session_user_email': request.session.get('user_email', None),
            'cart_count': len(cart_items),
        }
    template = loader.get_template('apex/signup.html')
    return HttpResponse(template.render(context, request))


def signin(request):
    gender_list = get_gender_list()
    cart_items = get_cart_items(request)
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            request.session.modified = True
            if request.POST.get('previous_page_ref'):
                previous_page_ref = request.POST.get('previous_page_ref', '/')
            else:
                previous_page_ref = '/'
            user_detail = get_user_email(form.cleaned_data.get('user_email'))
            for detail in user_detail:
                request.session['full_name'] = detail.user_name
                request.session['user_email'] = detail.user_email
            # print(request.session.get('full_name') , request.session.get('user_email'))
            return HttpResponseRedirect(previous_page_ref)
            # request.session.modified = True
        elif form.has_error('user_email', code=None):
            for error in form.errors['user_email']:
                email_error = error
                context = {
                    'gender_list': gender_list,
                    'form': SignInForm(),
                    'email_error': email_error,
                    'denial_message': 'Login attempt fail!',
                    'cart_count': len(cart_items),
                }
        elif form.has_error('user_pass', code=None):
            for error in form.errors['user_pass']:
                pass_error = error
            context = {
                'gender_list': gender_list,
                'form': SignInForm(),
                'pass_error': pass_error,
                'denial_message': 'Login attempt fail!',
                'cart_count': len(cart_items),
            }
    else:
        request_previous = request.META.get('HTTP_REFERER')
        if "signup" not in request_previous and "signin" not in request_previous:
            context = {
                'gender_list': gender_list,
                'form': SignInForm(),
                'session_full_name': request.session.get('full_name', None),
                'session_user_email': request.session.get('user_email', None),
                'previous_page': request_previous,
                'cart_count': len(cart_items),
            }
            print(request_previous)
        else:
            context = {
                'gender_list': gender_list,
                'form': SignInForm(),
                'session_full_name': request.session.get('full_name', None),
                'session_user_email': request.session.get('user_email', None),
                'cart_count': len(cart_items),
            }
    template = loader.get_template('apex/signin.html')
    return HttpResponse(template.render(context, request))


def changepassword(request):
    gender_list = get_gender_list()
    cart_items = get_cart_items(request)
    if request.method == 'POST':
        user_email = request.session.get('user_email', None)
        form = ChangePassForm(request.POST, user_email = request.session.get('user_email', None))
        if form.is_valid():
            form_data = form.cleaned_data
            change_password(user_email, form_data.get('conf_pass'))
            context = {
                'gender_list': gender_list,
                'form': ChangePassForm(),
                'session_full_name': request.session.get('full_name', None),
                'session_user_email': request.session.get('user_email', None),
                'cart_count': len(cart_items),
                'confirmation_message': 'Password Changed!',
            }
        elif form.has_error('old_pass', code=None):
            for error in form.errors['old_pass']:
                old_pass_error = error
                context = {
                    'gender_list': gender_list,
                    'form': ChangePassForm(),
                    'old_pass_error': old_pass_error,
                    'denial_message': 'Change password attempt fail!',
                    'cart_count': len(cart_items),
                }
        elif form.has_error('conf_pass', code=None):
            for error in form.errors['conf_pass']:
                conf_pass_error = error
            context = {
                'gender_list': gender_list,
                'form': ChangePassForm(),
                'conf_pass_error': conf_pass_error,
                'denial_message': 'Change password attempt fail!',
                'cart_count': len(cart_items),
            }
    else:
        context = {
            'gender_list': gender_list,
            'form': ChangePassForm(),
            'session_full_name': request.session.get('full_name', None),
            'session_user_email': request.session.get('user_email', None),
            'cart_count': len(cart_items),
        }

    template = loader.get_template('apex/changepassword.html')
    return HttpResponse(template.render(context, request))


def signout(request):
    request.session.modified = True
    if request.session['user_email']:
        del request.session['full_name']
        del request.session['user_email']
    return HttpResponseRedirect('/')


def addToCart(request, sl):
    if request.method == "POST":
        response = HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        quantity = request.POST.get("quantity", "")
        note = request.POST.get("note", "")
        try:
            value = request.COOKIES['cart_' + sl]
            split_value = value.split(':')
            previous_quantity = split_value[1]
            quantity = float(quantity) + float(previous_quantity)
        except:
            print("Cookie not found")
        try:
            cart_items = request.COOKIES['cart_items']
            if sl not in cart_items:
                cart_items = cart_items + sl
                response.set_cookie('cart_items', cart_items + ':')
        except:
            print("cookie not found")
            response.set_cookie('cart_items', sl + ':')
        response.set_cookie('cart_' + sl.strip(), sl.strip() + ':' + str(quantity) + ':' + note.strip())
    else:
        pass
    return response


def removeFromCart(request, sl):
    # if request.method == "POST":
    response = HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    response.delete_cookie('cart_' + sl.strip())
    cart_items = request.COOKIES['cart_items']
    cart_items = cart_items.replace(sl+":", "")
    response.set_cookie('cart_items', cart_items)
    return response

def updateCart(request, sl):
    if request.method == "POST":
        quantity = request.POST.get("quantity_"+sl, "")
        note = request.POST.get("note_"+sl, "")
        response = HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        response.set_cookie('cart_' + sl.strip(), sl.strip() + ':' + str(quantity) + ':' + note.strip())
    return response


def cart(request):
    try:
        gender_list = get_gender_list()
        cart_items = get_cart_items(request)
        cart_details = get_cart_details(request, cart_items)
        items_details = get_cart_items_details(cart_items)
        total_pairs = get_total_pairs(request)
        template = loader.get_template('apex/cart.html')
        context = {
            'gender_list': gender_list,
            'session_full_name': request.session.get('full_name', None),
            'session_user_email': request.session.get('user_email', None),
            'items_details': items_details,
            'cart_details': cart_details,
            'cart_count': len(cart_items),
            'total_pairs': total_pairs,

        }
    except TblCatalog.DoesNotExist:
        raise Http404("Page not found")
    return HttpResponse(template.render(context, request))


def placeOrder(request):
    try:
        cart_items = get_cart_items(request)
        insert_order(request, cart_items)
        gender_list = get_gender_list()
        template = loader.get_template('apex/cart.html')
        context = {
            'gender_list': gender_list,
            'session_full_name': request.session.get('full_name', None),
            'session_user_email': request.session.get('user_email', None),
            'cart_count': len(cart_items),
            'order_message': 'ORDER PLACED',
        }
    except TblCatalog.DoesNotExist:
        raise Http404("Page not found")
    response = HttpResponse(template.render(context, request))
    for sl in cart_items:
        response.delete_cookie('cart_' + sl.strip())
        response.delete_cookie('cart_items')
    return response

def viewOrders(request):
    try:
        gender_list = get_gender_list()
        cart_items = get_cart_items(request)
        orders = get_orders(request)
        order_item_details = get_order_item_details(orders)
        template = loader.get_template('apex/orders.html')
        context = {
            'gender_list': gender_list,
            'session_full_name': request.session.get('full_name', None),
            'session_user_email': request.session.get('user_email', None),
            'cart_count': len(cart_items),
            'orders': orders,
            'order_item_details': order_item_details,
        }
    except TblCatalog.DoesNotExist:
        raise Http404("Page not found")
    return HttpResponse(template.render(context, request))


# def signup(request):
#     try:
#         gender_list = get_gender_list()
#         country_list = get_country_list()
#         # password_validation.validate_password(password, self.instance)
#         template = loader.get_template('apex/signup.html')
#         context = {
#             'gender_list': gender_list,
#             'country_list': country_list,
#         }
#     except TblCatalog.DoesNotExist:
#         raise Http404("Page not found")
#     return HttpResponse(template.render(context, request))
#
# def user_save(request):
#
#     fullName=request.POST["fullName"]
#     if (len(fullName)<4) :
#
#
#         print (fullName)
#     pass


# def detail(request, sl):
#
#     try:
#         collection = TblCatalog.objects.get(pk=sl)
#     except TblCatalog.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'apex/detail.html', {'collection': collection})

# def cart(request, sl):
#
#     try:
#         collection = TblCatalog.objects.get(pk=sl)
#     except TblCatalog.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'apex/cart.html', {'collection': collection})

# def gender_collections(request, gender):
#     try:
#
#         collection = TblCatalog.objects.all().filter(gender=gender)
#
#     except TblCatalog.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'apex/index.html', {'collections': collection})

# def gender(request):
#     try:
#         gender_list = (TblCatalog.objects.values('gender')
#                        .order_by('gender')
#                        .annotate(max_id=Max('gender'), count_id=Count('gender'))
#                        .filter(count_id__gt=1)
#                        )
#
#         category_list = (TblCatalog.objects.values('category')
#                    .order_by('category')
#                    .annotate(max_id=Max('category'), count_id=Count('category'))
#                    .filter(count_id__gt=1)
#                    )
#     except TblCatalog.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'apex/index.html', {'collections': '', 'gender':gender_list, 'categories': category_list})
