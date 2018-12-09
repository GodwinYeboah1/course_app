from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CourseManager(models.Manager):

    def courseValidation(self, name, desc):
        response = {
            'user':None,
            'errors':[],
            'Valid': True
        }
        if len(name) <= 5:
            response['errors'].append("Name has to be greater then 5")
            response['Valid'] = False
        if len(desc) <= 15:
            response['errors'].append("desciption has to be greater then 15")
            response['Valid'] = False
        else:
            if response['Valid']:
                
                response['user']= Course.objects.create(
                    name = name,
                    desc = desc
                )

        return response
    

class Course(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now =True)
    objects = CourseManager()
