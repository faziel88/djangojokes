from django.views.generic import Listview

from .models import Joke

class JokeListView(ListView):
    model = Joke