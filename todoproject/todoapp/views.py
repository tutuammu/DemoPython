from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import TodoForm
from .models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView

class Listview(ListView):
    model=Task
    template_name='home.html'
    context_object_name='tik'
class Detailview(DetailView):
    model = Task
    template_name='detail.html'
    context_object_name = 'task'
class Updateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'tasks'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
class Deleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('Listview')

# Create your views here.
def add(request):
    tik = Task.objects.all()
    if request.method=="POST":
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        tasks=Task(name=name,priority=priority,date=date)
        tasks.save()
    return render(request,'home.html',{'tik':tik})
# def detail(request):
#
#     return render(request,'detail.html',
def delete(request,task_id):
    tasks=Task.objects.get(id=task_id)
    if request.method=="POST":
        tasks.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    tasks=Task.objects.get(id=id)
    f=TodoForm(request.POST or None,instance=tasks)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'tasks':tasks})