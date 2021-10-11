from django.http import HttpResponse, Http404
from django.template import loader
from .list_dal import *
# from django.conf.urls.static import static
from .models import TblCatalog


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


def list(request, gender):
    try:
        gender_list = get_gender_list()
        gender = gender
        category_list = get_category_list(gender)
        gender_collection = get_gender_collection(gender)
        template = loader.get_template('apex/list.html')
        page_count_list = gender_collection_pagination(gender)
        context = {
            'gender_list': gender_list,
            'gender_collection': gender_collection,
            'gender': gender,
            'category_list': category_list,
            'page_count_list' : page_count_list,
        }

    except TblCatalog.DoesNotExist:
        raise Http404("Question does not exist")
    return HttpResponse(template.render(context, request))


def further_list(request, gender, category):
    try:
        gender_list = get_gender_list()
        gender = gender
        category_list = get_category_list(gender)
        category_collection = get_category_collection(gender, category)
        template = loader.get_template('apex/list.html')
        context = {
            'gender_list': gender_list,
            'gender': gender,
            'category_list': category_list,
            'category_collection': category_collection,
        }

    except TblCatalog.DoesNotExist:
        raise Http404("Question does not exist")
    return HttpResponse(template.render(context, request))

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
