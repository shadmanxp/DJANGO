import sys
from math import ceil
from django.db.models import Count, Max
from django.core.paginator import Paginator
from .models import TblCatalog


def get_gender_list():
    gender_list = (TblCatalog.objects.values('gender')
                   .order_by('-gender')
                   .annotate(max_id=Max('gender'), count_id=Count('gender'))
                   .filter(count_id__gt=1)
                   )
    return gender_list


def get_collections():
    collections = TblCatalog.objects.all()
    return collections


def get_featured_products():
    featured_query_1 = "SELECT  top 6  ROW_NUMBER() OVER ( ORDER BY c.gender,c.category,c.sl ) AS RowNum, " \
                       "* FROM tbl_catalog c WHERE sl = (SELECT MIN(sl) FROM tbl_catalog WHERE ART_NO = c.ART_NO) " \
                       "order by NEWID() "
    featured_query_2 = "SELECT  RowConstrainedResult.*,n.art_count FROM ( SELECT  top 6  ROW_NUMBER() OVER ( ORDER BY " \
                       "c.gender, c.category,c.sl ) AS RowNum, * FROM tbl_catalog c WHERE sl = (SELECT MIN(sl) FROM " \
                       "tbl_catalog WHERE ART_NO = c.ART_NO) order by NEWID()) AS RowConstrainedResult left outer " \
                       "join (SELECT ART_NO, count(ART_NO) art_count FROM tbl_catalog c GROUP BY ART_NO ) n on " \
                       "RowConstrainedResult.ART_NO=n.ART_NO "
    ft_products = TblCatalog.objects.raw(featured_query_2)
    return ft_products


def get_gender_collection(gender):
    get_collections_query_1 = "select Cons.*,AC.art_count  FROM (SELECT * FROM tbl_catalog) AS Cons left outer join (" \
                              "SELECT  art_no, count(art_no) art_count FROM tbl_catalog c GROUP BY art_no) AC on  " \
                              "Cons.art_no = AC.art_no where Cons.GENDER='" + gender + "' "
    get_collections_query_2 = "SELECT  RowConstrainedResult.*,n.art_count FROM ( SELECT    ROW_NUMBER() OVER ( ORDER " \
                              "BY c.gender,c.category,c.sl ) AS RowNum, * FROM tbl_catalog c WHERE c.gender='" + \
                              gender + "' and sl = (SELECT MIN(sl) FROM tbl_catalog WHERE ART_NO = c.ART_NO)) AS " \
                                       "RowConstrainedResult left outer join (SELECT ART_NO, count(ART_NO) art_count " \
                                       "FROM tbl_catalog c WHERE c.gender='" + gender + "' GROUP BY ART_NO) n on " \
                                        "RowConstrainedResult.ART_NO=n.ART_NO WHERE RowNum >= 0 AND RowNum < 100 ORDER BY RowNum "
    gender_list = TblCatalog.objects.raw(get_collections_query_2)
    return gender_list


def get_category_list(gender):
    get_category_query = "select ROW_NUMBER() OVER ( ORDER BY C.category )  as SL,C.category from  (select category " \
                         "from tbl_catalog where gender='" + gender + "' group by category)  C "
    category_list = TblCatalog.objects.raw(get_category_query)
    return category_list


def get_category_collection(gender, category):
    get_category_collection_query = "SELECT  RowConstrainedResult.*,n.art_count FROM ( SELECT ROW_NUMBER() OVER ( " \
                                    "ORDER BY c.gender,c.category,c.sl ) AS RowNum, * FROM tbl_catalog c WHERE " \
                                    "c.gender='" + gender + "' and c.category='" + category + "' and sl = (SELECT MIN(sl) FROM " \
                                    "tbl_catalog WHERE ART_NO = c.ART_NO)) AS RowConstrainedResult left outer join (" \
                                    "SELECT ART_NO, count(ART_NO) art_count FROM tbl_catalog c WHERE c.gender='" + gender + "' " \
                                    "and c.category='" + category + "' GROUP BY ART_NO) n on " \
                                    "RowConstrainedResult.ART_NO=n.ART_NO WHERE RowNum >= 0 AND RowNum < 100 ORDER BY RowNum "
    category_list = TblCatalog.objects.raw(get_category_collection_query)
    return category_list


# def gender_collection_pagination(gender):
#     count = 0
#     page_count_list = []
#     gender_collection = get_gender_collection(gender)
#     for each in gender_collection:
#         count = count + 1
#     pages = ceil(count / 12)
#     for each in range(1, pages + 1, 1):
#         page_count_list.append(each)
#     return page_count_list

def get_gender_collection_pagination(gender):
    gender_collection = get_gender_collection(gender)
    collection = Paginator(gender_collection, 12)
    return collection


def get_category_collection_pagination(gender, category):
    category_collection = get_category_collection(gender, category)
    collection = Paginator(category_collection, 12)
    return collection

