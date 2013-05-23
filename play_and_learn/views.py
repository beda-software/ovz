# Create your views here.
from django.views.generic import ListView, DetailView
from models import ProfessionsLetter


class LetterList(ListView):
    model = ProfessionsLetter
    template_name = 'play_and_learn/letter_list.html'
    context_object_name = 'letters'


class ProfessionList(DetailView):
    model = ProfessionsLetter
    template_name = 'play_and_learn/profession_list.html'
    context_object_name = 'letter'
    slug_field = 'letter_slug'
