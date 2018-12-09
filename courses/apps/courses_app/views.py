from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Course,CourseManager
# Create your views here.
# main course
def main(req):
      
    content = {
        'allcourse':Course.objects.all()
    }
    return render(req,"courses_app/main.html", content)

def newCourse(req):
    name = req.POST['name']
    desc = req.POST['desc']
  
    response = Course.objects.courseValidation(name = name, desc=desc)

    if response["Valid"]:
        return redirect('/')
    else:
        for error_message in response['errors']:
            messages.add_message(req, messages.ERROR, error_message)
    return redirect('/')

# remove course
def remove(req, id):
    remCourse = Course.objects.get(id=id)
    content={
        'course': remCourse
    }
    return render(req,"courses_app/deletePage.html",content )
def destory(req, id):
    delcourse =Course.objects.get(id =id)
    delcourse.delete()
    return redirect('/')