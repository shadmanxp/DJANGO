# Generated by Django 3.2.7 on 2021-10-13 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apex', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TblCustomerOrder',
            fields=[
                ('sl', models.AutoField(db_column='SL', primary_key=True, serialize=False)),
                ('order_no', models.CharField(blank=True, db_column='ORDER_NO', max_length=150, null=True)),
                ('po_no', models.CharField(blank=True, db_column='PO_NO', max_length=50, null=True)),
                ('qty', models.FloatField(blank=True, db_column='QTY', null=True)),
                ('note', models.CharField(blank=True, db_column='NOTE', max_length=3500, null=True)),
                ('user_email', models.CharField(blank=True, db_column='USER_EMAIL', max_length=150, null=True)),
                ('entry_date', models.DateField(blank=True, db_column='ENTRY_DATE', null=True)),
            ],
            options={
                'db_table': 'tbl_customer_order',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblMember',
            fields=[
                ('sl', models.AutoField(primary_key=True, serialize=False)),
                ('user_email', models.CharField(blank=True, max_length=150, null=True)),
                ('user_name', models.CharField(blank=True, max_length=100, null=True)),
                ('user_pass', models.CharField(blank=True, max_length=50, null=True)),
                ('company', models.CharField(blank=True, max_length=150, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateField(blank=True, null=True)),
                ('user_level', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'tbl_member',
                'managed': False,
            },
        ),
    ]
