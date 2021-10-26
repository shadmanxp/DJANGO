from .details_dal import *
from datetime import date, datetime
from django.db import connections
import random


def get_cart_items(request):
    corrected_item_list = []
    try:
        cart_items = request.COOKIES['cart_items']
        split_items = cart_items.split(':')
        for each in split_items:
            if each is not "":
                corrected_item_list.append(each)
        return corrected_item_list
    except:
        return corrected_item_list


def get_cart_details(request, cart_items):
    cart_details = []
    for sl in cart_items:
        info_list = []
        cart_items_details = request.COOKIES['cart_' + sl.strip()]
        split_value = cart_items_details.split(':')
        sl = split_value[0]
        quantity = split_value[1]
        note = split_value[2]
        info_list.append(int(sl))
        info_list.append(quantity)
        info_list.append(note)
        cart_details.append(info_list)

    return cart_details


def get_cart_items_details(cart_items):
    items_details = []
    for sl in cart_items:
        item_detail = get_details_by_sl(sl)
        items_details.append(list(item_detail))
    return items_details


def get_total_pairs(request):
    total_pairs = 0
    cart_items = get_cart_items(request)
    for sl in cart_items:
        cart_items_details = request.COOKIES['cart_' + sl.strip()]
        split_value = cart_items_details.split(':')
        total_pairs = total_pairs + float(split_value[1])
    return total_pairs


def insert_order(request, cart_items):
    session_user_email = request.session.get('user_email', None)
    for each in cart_items:
        cart_items_details = request.COOKIES['cart_' + each.strip()]
        split_value = cart_items_details.split(':')
        quantity = float(split_value[1])
        note = split_value[2]
        item = get_details_by_sl(each)
        entry_date = date.today().strftime('%Y-%m-%d')
        cursor = connections['default'].cursor()
        for detail in item:
            insert_order_query = "insert into tbl_customer_order(ORDER_NO,PO_NO,QTY,NOTE,USER_EMAIL,ENTRY_DATE) values ('" \
                           + str(order_no_generator()) + "','" + str(detail.po_no) + "','" \
                           + str(quantity) + "','" + str(note) \
                           + "','" + str(session_user_email) + "','" \
                           + str(entry_date) + "')"
        cursor.execute(insert_order_query)


def order_no_generator():
    unique_id = '%6x' % random.getrandbits(12 * 6)
    entry_date = datetime.today().strftime('%Y-%m-%d-%H-%M')
    entry_date = entry_date.replace("-", "")
    order_no = entry_date+unique_id
    return order_no


# def get_cart_items_details(cart_items):
#     items_details = get_details_by_sl(cart_items)
#     return items_details
