from .details_dal import *

def get_cart_items(request):
    corrected_item_list=[]
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
    items_details =[]
    for sl in cart_items:
        item_detail = get_details_by_sl(sl)
        items_details.append(list(item_detail))
    return items_details

# def get_cart_items_details(cart_items):
#     items_details = get_details_by_sl(cart_items)
#     return items_details
