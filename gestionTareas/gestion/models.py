from django.db import models

# Create your models here.

from django.urls import reverse  # To generate URLS by reversing URL patterns
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from uuid import uuid4

class Task(models.Model):
    """Model representing a Task."""
    def generateUUID():
        return str(uuid4())
    id = models.UUIDField(primary_key=True, default=generateUUID, max_length=36, unique=True, editable=False, 
                          help_text="Valor unico por tarea")
    description = models.CharField(max_length=255, help_text="Introduce la descripción de la tarea")
    TASKS_STATUS = (
        ('P', 'Pendiente'),
        ('C', 'Completada'),
    )
    status = models.CharField(max_length=1, choices=TASKS_STATUS, blank=True, default='Pendiente', help_text='Estado de la tarea (Pendiente o Completada)')
    
    class Meta:
        ordering = ['status','description']

    def get_absolute_url(self):
        """Returns the url to access a particular Task record."""
        return reverse('Task-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.description
    
    

