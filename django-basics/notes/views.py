from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Notes
from django.http import Http404
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from .forms import NotesForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect
# Create your views here.

class NoteDeleteView(LoginRequiredMixin,DeleteView):
    model=Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'
    login_url = '/login'

class NoteUpdateView(LoginRequiredMixin,UpdateView):
    model = Notes
    # fields = ['title', 'note']
    success_url = '/smart/notes'
    form_class = NotesForm
    login_url = '/login'

class NoteCreateView(LoginRequiredMixin,CreateView):
    model = Notes
    # fields = ['title', 'note']
    success_url = '/smart/notes'
    form_class = NotesForm
    login_url = '/login'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NoteListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    template_name = 'notes/smart_notes.html'
    login_url = '/login'

    def get_queryset(self):
        return self.request.user.notes.all()

class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Notes
    context_object_name = "note"
    template_name = 'notes/note_detail.html'
    login_url = '/login'

# def list(request):
#     list_notes = Notes.objects.all()
#     return render(request, 'notes/smart_notes.html', {'notes':list_notes})

# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("The note does not exist")
#     return render(request, 'notes/note_detail.html', {'note':note})
