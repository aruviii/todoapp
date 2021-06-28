from django.urls import path
from .views import (index,
	TaskList,
	DetailTaskList,
	CreateTaskList,
	UpdateTaskList,
	DeleteTaskList,
	CustomLoginView,
	SigninView
	)
from django.contrib.auth.views import LogoutView

urlpatterns =[

	path("index/",index,name="index"),
	path('tasks/',TaskList.as_view(),name="tasks"),
	path('tasks/<int:pk>/',DetailTaskList.as_view(),name="detail"),
	path('logout/',LogoutView.as_view(next_page='tasks'),name='logout'),
	path('login/',CustomLoginView.as_view(),name='login'),
	path('signin/',SigninView,name='signin'),
	path('tasks/create/',CreateTaskList.as_view(),name="create-task"),
	path('tasks/update/<int:pk>',UpdateTaskList.as_view(),name="update-task"),
	path('tasks/delete/<int:pk>',DeleteTaskList.as_view(),name="delete-task"),

]
