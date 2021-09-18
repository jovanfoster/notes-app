from django.http import Http404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Note
from .forms import UserRegisterForm

@login_required
def index(request):
    user = request.user
    notes = user.notes.all().order_by('-date_created')
    return render(request, 'main/index.html', {'notes': notes})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            errors = 'Invalid login info'
    errors = ''
    return render(request, 'main/login.html', {'errors': errors})

def logout_view(request):
    logout(request)
    return render(request, 'main/logout_success.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    form = UserRegisterForm()

    return render(request, 'main/user_registration_form.html', {'form': form})      


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'text']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 

    
class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    fields = ['title', 'text']
    success_url = '/'

    # raises a 404 error if user is not the author of the note
    def dispatch(self, request, *args, **kwargs):
        note = self.get_object()
        if note.author != self.request.user:
            raise Http404("You are not allowed to edit this note")
        return super(NoteUpdateView, self).dispatch(request, *args, **kwargs)


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = '/'
