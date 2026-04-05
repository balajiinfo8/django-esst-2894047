from django.shortcuts import render
from .models import Notes
from django.http import Http404
from django.views.generic import CreateView , ListView , DetailView , UpdateView , DeleteView
from django.db.models import Count 
from .forms import NotesForm 
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse 
from django.contrib.auth.mixins import LoginRequiredMixin

# add like upvote 
def add_like_views(request,pk):
    if request.method == 'POST':
        note =get_object_or_404(Notes, pk=pk)
        note.likes += 1 
        note.save()
        return HttpResponseRedirect(reverse('notes.detail', args=(pk,)))
    raise Http404("Invalid request method.")
    
# visibility change 
def change_visibility(request,pk):
    if request.method == "POST":
        note = get_object_or_404(Notes, pk=pk)
        note.is_public = not note.is_public 
        note.save()
        return HttpResponseRedirect(reverse('notes.detail', args=(pk,)))
    raise Http404("Invalid Request Method")

# DELETE 
class NotesDeleteView(DeleteView):
    model = Notes 
    success_url = '/smart/notes/'
    template_name = 'notes/notes_delete.html'
    
# UPDATE 
class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes/'
    form_class = NotesForm 

class NotesCreateView(CreateView):
    model = Notes
    success_url = '/smart/notes/'
    form_class = NotesForm
    login_url = 'login'

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user 
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NoteListView(ListView):
    model = Notes 
    context_object_name = "notes"
    template_name = 'notes/notes_list.html'
    login_url = 'login'

    def get_queryset(self):
        return self.request.user.notes.all()

class NotesDetailView(DetailView):
    model = Notes 
    context_object_name = "notes"

class PopularNotesListView(ListView):
    model = Notes 
    context_object_name = "notes"
    template_name = 'notes/notes_like.html'
    queryset = Notes.objects.filter(likes__gte=1)
