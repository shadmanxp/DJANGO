# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
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
    sl = models.AutoField(db_column='SL')  # Field name made lowercase.
    new_coll = models.IntegerField(db_column='NEW_COLL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_catalog'
