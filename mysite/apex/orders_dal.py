from .models import TblCustomerOrder, TblCatalog
from .details_dal import *

def get_orders(request):
    session_user_email = request.session.get('user_email', None)
    get_order_query = "select * from tbl_customer_order where USER_EMAIL='" + session_user_email + "'"
    orders = TblCustomerOrder.objects.raw(get_order_query)
    return orders

def get_order_item_details(orders):
    list_string = ""
    for each in orders:
        list_string = list_string + "'" + each.po_no + "',"
    list_string = list_string + "''"
    get_items_query = "select * from tbl_catalog where PO_NO in (" + list_string + ")"
    order_items = TblCatalog.objects.raw(get_items_query)
    return order_items