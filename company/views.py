from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from company.models import Company
from login.models import User
from login.views import auth


@auth
def companyC(request):
    user = request.session.get("user")

    company=Company.objects.filter(account=user).first()
    context={"companyHtml":company}



    return render(request,"model/company_Center.html",context)