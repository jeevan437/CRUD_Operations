from django.shortcuts import render, redirect
from TaskApp.models import TaskDetailss
import datetime
# Create your views here.
def view_task_details(request):
    data = TaskDetailss.objects.all()
    return render(request, "TaskApp/task_details.html", {"data":data})

def view_home(request):
    return render(request, "TaskApp/home.html")

def view_register(request):
    if request.method == "POST":
        data = request.POST
        task = TaskDetailss(title = data.get("title"),
                            description = data.get("description"),
                            status = data.get("status"),
                            created_at = datetime.datetime.now())
        print(task)
        return redirect(view_task_details)
    return render(request, "TaskApp/register.html")

def view_delete(request, pid):
    task = TaskDetailss.objects.get(id = pid)
    task.delete()
    return redirect(view_task_details)

def view_update(request, pid):
    task = TaskDetailss.objects.get(id = pid)
    if request.method == "post":
        data = request.POST
        task.title = data.get("title")
        task.description = data.get("description")
        task.status = data.get("status")
        task.created_at = data.get("created")
        task.modified_at = data.get("modified")
        task.save()
        return redirect(view_task_details)
    return render(request, "TaskApp/update.html", {'data':task})