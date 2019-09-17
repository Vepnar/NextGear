from django.shortcuts import render
from .models import Channel



# Create your views here.
def index(request):
    latest_question_list = Channel.objects.order_by('-start_date')[:5]
    context = {'channel_list': latest_question_list}
    return render(request, 'gids/index.html', context)