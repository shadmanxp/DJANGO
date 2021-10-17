from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.template import loader
from .list_dal import *
from .details_dal import *
from .accounts_dal import *
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
# from django.conf.urls.static import static
from .models import TblCatalog
from .forms import *


def index(request):
    try:
        gender_list = get_gender_list()
        ft_products = get_featured_products()
        template = loader.get_template('apex/index.html')
        context = {
            'gender_list': gender_list,
            'featured_products': ft_products,
        }
    except TblCatalog.DoesNotExist:
        raise Http404("Question does not exist")
    return HttpResponse(template.render(context, request))


def initial_list(request, gender, page):
    try:
        gender_list = get_gender_list()
        category_list = get_category_list(gender)
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

        }

    except TblCatalog.DoesNotExist:
        raise Http404("Page not found")
    return HttpResponse(template.render(context, request))


def further_list(request, gender, category, page):
    try:
        gender_list = get_gender_list()
        category_list = get_category_list(gender)
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
        }

    except TblCatalog.DoesNotExist:
        raise Http404("Page not found")
    return HttpResponse(template.render(context, request))


def details(request, gender, category, art_no, leather_1):
    try:
        gender_list = get_gender_list()
        category_list = get_category_list(gender)
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
        }
    except TblCatalog.DoesNotExist:
        raise Http404("Page not found")
    return HttpResponse(template.render(context, request))


def signup(request):
    gender_list = get_gender_list()
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
            }
        elif form.has_error('user_email', code=None):
            for error in form.errors['user_email']:
                email_error = error
                context = {
                    'gender_list': gender_list,
                    'form': SignUpForm(),
                    'email_error': email_error,
                    'denial_message': 'Registration not complete!',
                }
        elif form.has_error('conf_pass', code=None):
            for error in form.errors['conf_pass']:
                pass_error = error
            context = {
                'gender_list': gender_list,
                'form': SignUpForm(),
                'pass_error': pass_error,
                'denial_message': 'Registration not complete!',
            }
    else:
        context = {
            'gender_list': gender_list,
            'form': SignUpForm(),
        }
    template = loader.get_template('apex/signup.html')
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
