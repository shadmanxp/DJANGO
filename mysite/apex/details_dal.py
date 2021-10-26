from .models import TblCatalog


def get_details(art_no, leather_1):
    get_details_query = "select * from tbl_catalog where art_no='" + art_no + "' and leather_1='" + leather_1 + "'"
    # get_details_query2= "SELECT  RowConstrainedResult.*,n.art_count FROM ( SELECT ROW_NUMBER() OVER ( ORDER BY " \
    #                     "c.gender,c.category,c.sl ) AS RowNum, * FROM tbl_catalog c"" WHERE c.ART_NO='" +art_no+ "' and c.leather_1='" +leather_1+ "' and sl = (SELECT MIN(sl) " \
    #                     "FROM tbl_catalog WHERE ART_NO = c.ART_NO)) AS RowConstrainedResult left outer join (SELECT ART_NO, count(ART_NO) art_count FROM" \
    #                    " tbl_catalog c WHERE c.ART_NO='" +art_no+ "' GROUP BY ART_NO) n on RowConstrainedResult.ART_NO=n.ART_NO WHERE RowNum >= 0 AND RowNum < 100 ORDER BY RowNum "

    product_details = TblCatalog.objects.raw(get_details_query)
    return product_details


def get_list_by_art_no(art_no):
    get_details_by_art_no_query = "select * from tbl_catalog where ART_NO='" + art_no + "'"

    product_by_art_no = TblCatalog.objects.raw(get_details_by_art_no_query)
    return product_by_art_no


def get_details_by_sl(sl):
    get_details_query = "select * from tbl_catalog where sl='" + sl + "'"
    product_details = TblCatalog.objects.raw(get_details_query)
    return product_details


def get_details_by_po_no(po_no):
    get_details_query = "select * from tbl_catalog where sl='" + po_no + "'"
    product_details = TblCatalog.objects.raw(get_details_query)
    return product_details

# def get_details_by_sl(sl):
#     get_details_query = "SELECT * FROM tbl_catalog WHERE sl IN (1,2,3)"
#     product_details = TblCatalog.objects.raw(get_details_query)
#     return product_details