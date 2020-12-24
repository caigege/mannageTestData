# Create your views here.
# model/views.py
from django.http import HttpResponse
from django.shortcuts import render

from model.models import Book


def model_resp(request):
    # s = request.readlines()

    s = request.get_raw_uri()

    for i in range(5):
        print(i)
    print("*log* ", s)
    return HttpResponse(s)


def detail(request):
    book_list = Book.objects.order_by('pub_date')[:5]
    context = {'book_list1': book_list}
    print("-----*****--:"+str((book_list.all())[0].pub_date))

    return render(request, 'model/detail.html', context)


def detailChild(request):
    book_list = Book.objects.order_by('pub_date')
    context = {'book_list': book_list}

    return render(request, 'model/detailChild.html', context)


def test():
    print(1)
