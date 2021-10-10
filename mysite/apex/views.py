from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.db.models import Count, Max, Q, FilteredRelation, F
import random

# from django.conf.urls.static import static

from .models import TblCatalog


# def NEWID():
#     filter_amount = 6
#     sl = (TblCatalog.objects
#           .values('art_no')
#           .annotate(art_count=Count('art_no'))
#           )
#     #SELECT [tbl_catalog].[ART_NO], COUNT_BIG([tbl_catalog].[ART_NO]) AS [art_count] FROM [tbl_catalog] GROUP BY [tbl_catalog].[ART_NO]
#     sl_list = list(sl)
#     random_no = random.sample(sl_list, filter_amount)
#     return random_no
def get_collections():
    collections = TblCatalog.objects.all()
    return collections


def get_gender_list():
    gender_list = (TblCatalog.objects.values('gender')
                   .order_by('-gender')
                   .annotate(max_id=Max('gender'), count_id=Count('gender'))
                   .filter(count_id__gt=1)
                   )
    return gender_list


def get_featured_products():
    featured_query_1= "SELECT  top 6  ROW_NUMBER() OVER ( ORDER BY c.gender,c.category,c.sl ) AS RowNum, * FROM tbl_catalog c WHERE sl = (SELECT MIN(sl) FROM tbl_catalog WHERE ART_NO = c.ART_NO) order by NEWID()"
    featured_query_2 = "SELECT  RowConstrainedResult.*,n.art_count FROM ( SELECT  top 6  ROW_NUMBER() OVER ( ORDER BY c.gender," \
            "c.category,c.sl ) AS RowNum, * FROM tbl_catalog c WHERE sl = (SELECT MIN(sl) FROM tbl_catalog WHERE " \
            "ART_NO = c.ART_NO) order by NEWID()) AS RowConstrainedResult left outer join (SELECT ART_NO, " \
            "count(ART_NO) art_count FROM tbl_catalog c GROUP BY ART_NO ) n on RowConstrainedResult.ART_NO=n.ART_NO "
    ft_products = TblCatalog.objects.raw(featured_query_2)
    return ft_products


def get_gender_collection(gender):
    get_collections_query_1 = "select Cons.*,AC.art_count  FROM (SELECT * FROM tbl_catalog) AS Cons left outer join (SELECT  art_no, " \
                                "count(art_no) art_count FROM tbl_catalog c GROUP BY art_no) AC on  Cons.art_no = AC.art_no where " \
                                "Cons.GENDER='" + gender + "' "
    get_collections_query_2= "SELECT  RowConstrainedResult.*,n.art_count FROM ( SELECT    ROW_NUMBER() OVER ( ORDER " \
                             "BY c.gender,c.category,c.sl ) AS RowNum, * FROM tbl_catalog c WHERE c.gender='" + gender + "' and " \
                             "sl = (SELECT MIN(sl) FROM tbl_catalog WHERE ART_NO = c.ART_NO)) AS RowConstrainedResult " \
                             "left outer join (SELECT ART_NO, count(ART_NO) art_count FROM tbl_catalog c WHERE " \
                             "c.gender='" + gender + "' GROUP BY ART_NO) n on RowConstrainedResult.ART_NO=n.ART_NO WHERE " \
                             "RowNum >= 0 AND RowNum < 100 ORDER BY RowNum "
    gender_collection = TblCatalog.objects.raw(get_collections_query_2)
    return gender_collection


def index(request):
    try:
        gender_list = get_gender_list()
        ft_products = get_featured_products()
        template = loader.get_template('apex/index.html')
        context = {
            'gender': gender_list,
            'featured_products': ft_products,
        }
    except TblCatalog.DoesNotExist:
        raise Http404("Question does not exist")
    return HttpResponse(template.render(context, request))

    # featured_products = (TblCatalog.objects.all()
    #                      .filter(Q(sl=NEWID()) | Q(sl=NEWID()) | Q(sl=NEWID()) | Q(sl=NEWID()) | Q(sl=NEWID()) )
    #                      )
    ####################################
    # filter_amount = 6
    # random_selected = (TblCatalog.objects
    #       .values('art_no')
    #       .annotate(art_count=Count('art_no'))
    #       .order_by()
    #       )
    # random_selected_list = list(random_selected)
    # random_no = random.sample(random_selected_list, filter_amount)
    # selected_list_art_no = []
    # selected_list_art_count = []
    # for each in random_no:
    #     selected_list_art_no.append(each.get('art_no'))
    #     selected_list_art_count.append(each.get('art_count'))
    #
    # featured_products = (TblCatalog.objects.all()
    #                      .filter(Q(art_no=selected_list_art_no[0]) |
    #                              Q(art_no=selected_list_art_no[1]) |
    #                              Q(art_no=selected_list_art_no[2]) |
    #                              Q(art_no=selected_list_art_no[3]) |
    #                              Q(art_no=selected_list_art_no[4]) |
    #                              Q(art_no=selected_list_art_no[5])
    #                              )
    #                      .annotate(art_count=Count('art_no'))
    #                      .order_by()
    #                      )


######################################################################################

def details(request, gender):
    try:
        gender_list = get_gender_list()
        gender_collection = get_gender_collection(gender)
        template = loader.get_template('apex/details.html')
        context = {
            'gender': gender_list,
            'gender_collection': gender_collection,
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
