from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db.models.fields.related import ManyToManyField

User = get_user_model()
# Create your models here.
def user_directory_path(instance,filename):
    return 'blog/{0}/{1}'.format(instance.nombre,filename)


def event_directory_path(instance, filename):
    return 'courses/{0}/{1}'.format( instance.evn1, filename)
 

class Hotel(models.Model):
    nombre = models.CharField(max_length=20, help_text="Nombre del Hotel",null=False)
    own = models.ForeignKey(User,on_delete=models.CASCADE,help_text="Hotel admin",null=False)
    descripcion = models.CharField(max_length=100,help_text="Breve informacion")
    thumbnail = models.ImageField(upload_to=user_directory_path,blank=True,null=True)


    def __str__(self):
        return 'Hotel: '+self.nombre+' Dueño: '+ str(self.own)


class Eventos(models.Model):
    EVENT1='1'
    EVENT2='2'
    EVENT3='3'

    EV_HOT = (
        (EVENT1,'HIKING'),
        (EVENT2,'MOTOCR'),
        (EVENT3,'CAMPING'),
    )
    resp = models.ForeignKey(Hotel,on_delete=models.CASCADE,help_text="hotel : ",null=False)
    evn1 = models.CharField(max_length=10,choices=EV_HOT,help_text="Evento 1: ")
    descripcion = models.CharField(max_length=200,help_text="Breve informacion")
    thumbnail = models.ImageField(upload_to=event_directory_path,blank=True,null=True)


class customer(models.Model):
    name = models.CharField(max_length=30,null=False)
    last_name = models.CharField(max_length=30,null= False)
    def __str__(self):
        return 'Nombre : '+ self.name + ' Apellido : '+self.last_name


    
class Room(models.Model):
    ROOM = '1'
    ROOM2 = '2'
    ROOM3 = '4'

    CAPACITY_ROOM = (
        (ROOM,'1Bed'),
        (ROOM2,'2Bed'),
        (ROOM3,'3Bed'),
    )

    custom = ManyToManyField(customer,help_text="Nombre del huesped")
    number = models.IntegerField(help_text="Numero de habitacion")
    capacity = models.CharField(max_length=10,choices=CAPACITY_ROOM,default='1',blank=True,help_text="Numero de Camas")
    descripcion = models.CharField(max_length=100,help_text="Breve informacion")
    resposable = models.ForeignKey(Hotel,on_delete=models.CASCADE,help_text="Hotel admin")
    e1 = models.ForeignKey(Eventos,on_delete=models.CASCADE,related_name='E1',default='1',help_text="EVENTO 1")
    e2 = models.ForeignKey(Eventos,on_delete=models.CASCADE,related_name='E2',default='2',help_text="EVENTO 1")
    e3 = models.ForeignKey(Eventos,on_delete=models.CASCADE,related_name='E3',default='3',help_text="EVENTO 1")
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return 'Habitacion '+ str(self.number)+' Cliente: '+str(self.custom)+' Hotel: '+ str(self.resposable )




#class Booking(models.Model):
 #  usuario = models.ForeignKey(User,on_delete=models.CASCADE)