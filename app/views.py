from django.shortcuts import render,redirect
from app.models import Tasks
# Create your views here.





def index(request):
    
    if request.method=="POST":
        taskname=request.POST.get("taskname")
        if taskname:
            Tasks.objects.create(taskname=taskname)
        return redirect("/")

    tasks=Tasks.objects.all()
    context={'tasks':tasks}
    return render(request,'app/index.html',context)

def delete_task(request,id):
    tasks=Tasks.objects.get(id=id)
    tasks.delete()
    return redirect("/")

def update_task(request,id):
    tasks=Tasks.objects.get(id=id)
    
    if request.method=="POST":
        newname=request.POST.get("taskname")
        if newname:
            tasks.taskname=newname
            tasks.save()
        return redirect("/")
    context={"tasks":tasks}

    return render(request,"app/update.html",context)