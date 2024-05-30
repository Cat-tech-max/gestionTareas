from django.shortcuts import render
from django.views import generic
from gestion.models import Task
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import PermissionRequiredMixin

def index(request): 

    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_Tasks = Task.objects.all().count()

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context = {'num_Tasks': num_Tasks},
    )
    
class TaskListView(generic.ListView):
    """Generic class-based view for a list of Tasks."""
    model = Task
    paginate_by = 10

class TaskDetailView(generic.DetailView):
    """Generic class-based detail view for a Task."""
    model = Task

class TaskCreate(PermissionRequiredMixin, CreateView):
    model = Task
    fields = ['id', 'description', 'status']
    permission_required = 'gestion.add_task'
    
class TaskUpdate(PermissionRequiredMixin, UpdateView):
    model = Task
    fields = ['id', 'description', 'status']
    permission_required = 'gestion.update_task'
    
class TaskDelete(PermissionRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('Tasks')

    def form_valid(self, form):
        try:
            self.object.delete()
            return HttpResponseRedirect(self.success_url)
        except Exception as e:
            return HttpResponseRedirect(
                reverse("Task-delete", kwargs={"pk": self.object.pk})
            )