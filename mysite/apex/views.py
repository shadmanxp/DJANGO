from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.template import loader
from django.db.models import Count, Max

from .models import TblCatalog

def index(request):

    collections = TblCatalog.objects.order_by('-pd_sl')[:5]
    template = loader.get_template('apex/index.html')
    context = {
        'collections': collections,
    }
    return HttpResponse(template.render(context, request))

def detail(request, sl):

    try:
        collection = TblCatalog.objects.get(pk=sl)
    except TblCatalog.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'apex/detail.html', {'collection': collection})

def cart(request, sl):

    try:
        collection = TblCatalog.objects.get(pk=sl)
    except TblCatalog.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'apex/cart.html', {'collection': collection})

def gender_collections(request, gender):
    try:

        collection = TblCatalog.objects.all().filter(gender=gender)

    except TblCatalog.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'apex/index.html', {'collections': collection})



def gender(request):
    try:

        gender_list = (TblCatalog.objects.values('gender')
                       .order_by('gender')
                       .annotate(max_id=Max('gender'), count_id=Count('gender'))
                       .filter(count_id__gt=1)
                       )

        category_list = (TblCatalog.objects.values('category')
                   .order_by('category')
                   .annotate(max_id=Max('category'), count_id=Count('category'))
                   .filter(count_id__gt=1)
                   )


    except TblCatalog.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'apex/index.html', {'collections': '', 'gender':gender_list, 'categories': category_list})