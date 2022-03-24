from django.http import HttpResponse, HttpResponseRedirect
from urllib import request
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from .models import Task
from .forms import TaskForm, EditTaskForm, TaskCompleteForm
from django.urls import reverse_lazy, reverse

class TaskTableView(ListView):
    model = Task
    template_name = 'task_table.html'
    paginate_by = 5

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Task.objects.filter(author=self.request.user, completed=False)
        else:
            return Task.objects.filter(session=self.request.session.session_key, completed=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['task_completed'] = Task.objects.filter(author=self.request.user, completed=True).count()
        else:
            context['task_completed'] = Task.objects.filter(session=self.request.session.session_key, completed=True).count()
        return context
    
    
    def get_template_names(self):
        if self.request.htmx:
            return 'partials/table_row.html'
        else:
            return 'task_table.html'
    
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            if not request.session.session_key:
                    request.session[None] = None
                    # self.request.session = request.session
            return super().get(request, *args, **kwargs)
        else:
            return super().get(request, *args, **kwargs)

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name= 'partials/task_form_create.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
            return super().form_valid(form)
        else:
            form.instance.session = self.request.session.session_key
            return super().form_valid(form)
        

class TaskDetailView(DetailView):
    model = Task
    template_name = 'partials/detail.html'

class EditTaskView(UpdateView):
    model = Task
    form_class = EditTaskForm
    template_name = 'partials/task_form_create.html'
    success_url = reverse_lazy('index')

class TaskCompleteView(UpdateView):
    model = Task
    form_class = TaskCompleteForm
    new_status = True
    success_url = reverse_lazy('response')

    def form_valid(self, form):
        if self.new_status:
            form.instance.completed = self.new_status
            return super().form_valid(form)
    
class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('index')

def response(request):
    return redirect('index')