from .models import TblMember
from datetime import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.forms import ModelForm


def get_country_list():
    country = [('NULL', 'Select a country....'),
               ('Australia', 'Australia'),
               ('Austria', 'Austria'),
               ('Belgium', 'Belgium'),
               ('Bosnia And Herzegovina', 'Bosnia And Herzegovina'),
               ('Canada', 'Canada'),
               ('China', 'China'),
               ('Colombia', 'Colombia'),
               ('Czech Republic', 'Czech Republic'),
               ('Denmark', 'Denmark'),
               ('Estonia', 'Estonia'),
               ('Finland', 'Finland'),
               ('France', 'France'),
               ('Germany', 'Germany'),
               ('Greece', 'Greece'),
               ('Hong Kong', 'Hong Kong'),
               ('Hungary', 'Hungary'),
               ('India', 'India'),
               ('Ireland', 'Ireland'),
               ('Italy', 'Italy'),
               ('Japan', 'Japan'),
               ('Republic Of Korea', 'Republic Of Korea'),
               ('Latvia', 'Latvia'),
               ('Libyan Arab Jamahiriya', 'Libyan Arab Jamahiriya'),
               ('Lithuania', 'Lithuania'),
               ('Netherlands', 'Netherlands'),
               ('Norway', 'Norway'),
               ('Pakistan', 'Pakistan'),
               ('Poland', 'Poland'),
               ('Romania', 'Romania'),
               ('Russian Federation', 'Russian Federation'),
               ('Saudi Arabia', 'Saudi Arabia'),
               ('Singapore', 'Singapore'),
               ('Slovakia', 'Slovakia'),
               ('Slovenia', 'Slovenia'),
               ('Spain', 'Spain'),
               ('Sweden', 'Sweden'),
               ('Switzerland', 'Switzerland'),
               ('Taiwan', 'Taiwan'),
               ('Province Of China', 'Province Of China'),
               ('Turkey', 'Turkey'),
               ('Ukraine', 'Ukraine'),
               ('United Arab Emirates', 'United Arab Emirates'),
               ('United Kingdom', 'United Kingdom'),
               ('United State', 'United State')
               ]

    return country

def get_user_email(user_email):

    get_user_email_query = "select ROW_NUMBER() OVER (ORDER BY user_email) as sl, user_email from tbl_member where " \
                           "user_email='" + user_email.strip() + "' "
    user_email = TblMember.objects.raw(get_user_email_query)
    return len(user_email)

def insert_user_info(form_data):
    created_at = datetime.today().strftime('%Y-%m-%d')

    insert_query = "insert into tbl_member(user_email,user_name,user_pass,company,country,created_at) values('"+form_data.get('user_email')+"','"+form_data.get('user_name')+"','"+form_data.get('user_pass')+"','"+form_data.get('company')+"','"+form_data.get('country')+"','"+created_at+"')"

    TblMember.objects.raw(insert_query)