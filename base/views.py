from django.shortcuts import render
from django.views.generic import (ListView,UpdateView ,
	DetailView ,
	CreateView ,
	DeleteView
	)
from .models import Task
from django.forms.models import model_to_dict
from django.contrib.auth.views import LoginView
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']


def index(request):
	if request.user.is_authenticated:
		return redirect('tasks')
	else :
		return render(request,"AR/index.html")


def SigninView(request):
	form = UserForm()
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("login")
	return render(request,"AR/signin.html",{'form':form})


class CustomLoginView(LoginView):
	template_name = "AR/login.html"
	fields = '__all__'
	def get_success_url(self):
		return reverse_lazy('tasks')


class TaskList(LoginRequiredMixin,ListView):
	model = Task
	template_name = 'AR/list.html'
	context_object_name = "tasks"
	def get_context_data(self,**kwargs):
		task_set = Task.objects.values()
		task_list = [entry for entry in task_set]
		context = super().get_context_data(**kwargs)
		context["task_list"] = task_list
		context["tasks"] = context["tasks"].filter(user=self.request.user)
		return context


class DetailTaskList(LoginRequiredMixin,DetailView):
	model = Task
	template_name = 'AR/detail.html'
	context_object_name = "details"


class CreateTaskList(LoginRequiredMixin,CreateView):
	model = Task
	template_name = 'AR/create.html'
	fields = '__all__'
	success_url = reverse_lazy('tasks')
	
	def form_valid(self,form):
		form.instance.user = self.request.user
		return super(CreateTaskList,self).form_valid(form)


class UpdateTaskList(LoginRequiredMixin,UpdateView):
	model = Task
	template_name = 'AR/create.html'
	fields = '__all__'
	success_url = reverse_lazy('tasks')


class DeleteTaskList(LoginRequiredMixin,DeleteView):
	model = Task
	template_name = 'AR/delete.html'
	success_url = reverse_lazy('tasks')
	context_object_name = "task"
