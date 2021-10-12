from django.db import models

class TblCatalog(models.Model):
    pd_sl = models.FloatField(db_column='PD_SL', blank=True, null=True)  # Field name made lowercase.
    po_no = models.CharField(db_column='PO_NO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='GENDER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='CATEGORY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    last = models.CharField(db_column='LAST', max_length=255, blank=True, null=True)  # Field name made lowercase.
    art_no = models.CharField(db_column='ART_NO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    leather_1 = models.CharField(db_column='LEATHER_1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    leather_2 = models.CharField(db_column='LEATHER_2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lining_1 = models.CharField(db_column='LINING_1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lining_2 = models.CharField(db_column='LINING_2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    socks_design = models.CharField(db_column='SOCKS_DESIGN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sole = models.CharField(db_column='SOLE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    size = models.FloatField(db_column='SIZE', blank=True, null=True)  # Field name made lowercase.
    sl = models.AutoField(db_column='SL', primary_key=True)  # Field name made lowercase.
    new_coll = models.IntegerField(db_column='NEW_COLL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_catalog'

class TblMember(models.Model):
    sl = models.AutoField(primary_key=True)
    user_email = models.CharField(max_length=150, blank=True, null=True)
    user_name = models.CharField(max_length=100, blank=True, null=True)
    user_pass = models.CharField(max_length=50, blank=True, null=True)
    company = models.CharField(max_length=150, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateField(blank=True, null=True)
    user_level = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_member'

class TblCustomerOrder(models.Model):
    sl = models.AutoField(db_column='SL',primary_key=True)  # Field name made lowercase.
    order_no = models.CharField(db_column='ORDER_NO', max_length=150, blank=True, null=True)  # Field name made lowercase.
    po_no = models.CharField(db_column='PO_NO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='QTY', blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='NOTE', max_length=3500, blank=True, null=True)  # Field name made lowercase.
    user_email = models.CharField(db_column='USER_EMAIL', max_length=150, blank=True, null=True)  # Field name made lowercase.
    entry_date = models.DateField(db_column='ENTRY_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_customer_order'