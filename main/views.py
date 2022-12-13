from django.shortcuts import render, redirect
from openpyxl.workbook import Workbook
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import pandas as pd
import os
import openpyxl

# Create your views here.
def home(request):
    return render(request, 'index.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['psw']

        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            print('login')
            return redirect('profile')
        else:
            print('User Not Connected')


    return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['psw']

        user = User.objects.create_user(email=email, username=username, password=password)
    return render(request, 'reg.html')


def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        wb = openpyxl.load_workbook('Book1.xlsx')
        x = request.user.id
        # print(x)
        y = str(x)

        # getting a particular sheet by name out of many sheets
        worksheet = wb["Sheet1"]
        # print(worksheet)

        excel_data = list()
        # iterating over the rows and
        # getting value from each cell in row
        for row in worksheet.iter_rows(2):
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            excel_data.append(row_data)
        # print(row_data)
    # print(data)
    return render(request, 'profile.html', {'excel_data':excel_data, 'y': y})

