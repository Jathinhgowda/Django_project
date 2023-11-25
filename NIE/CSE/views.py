from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')


def prodcts(request):
    return render(request, 'prodcts.html')

def service(request):
    return render(request, 'service.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')
from CSE.models import Student
def student(request):
    stu = Student.objects.all()
    context = {'stu': stu}
    return render(request, 'student.html', context)

from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

class Forms(CreateView):
    model = Student
    fields = "_all_"
    template_name = 'forms.html'
    success_url = '/'

class StudentList(ListView):
    model = Student
    template_name = 'stulist.html'

class StudentDetail(DetailView):
    model = Student
    template_name = 'studetail.html'

class StudentUpdate(UpdateView):
    model = Student
    fields = '_all_'
    template_name = 'stuupdate.html'
    success_url = '/'

class StudentDelete(DeleteView):
    model = Student
    template_name = 'studelete.html'
    success_url='/'
