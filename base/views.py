from .models import Record
from .serializers import RecordSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import AddRecordForm, GetRecordForm

# front part

def main_page(request):
    recordAddForm = AddRecordForm(request.POST or None)
    recordGetForm = GetRecordForm(request.POST or None)
    if request.method == "POST":
        if recordAddForm.is_valid():
            record = recordAddForm.save()
            return HttpResponseRedirect(reverse('main'))
        if recordGetForm.is_valid():
            return HttpResponseRedirect(reverse('list', kwargs={"name": recordGetForm.cleaned_data['name']}))

    context = {'recordAddForm': recordAddForm,
               'recordGetForm': recordGetForm,}

    return render(request, "base/main.html", context)

def list_view(request, name):
    record_list = Record.objects.filter(name=name)
    if len(record_list) > 0:
        return render(request, "base/record_list.html", {"record_list":record_list})
    else:
        return HttpResponse('<h1>No such Names in book</h1>')

# rest api part

class RecordGet(generics.ListAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name',)

class RecordList(generics.ListCreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

class RecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    lookup_field = "name"
