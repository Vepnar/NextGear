from django.shortcuts import render,get_object_or_404
from .models import Channel



# Create your views here.
def index(request):
    latest_question_list = Channel.objects.order_by('-start_date')[:10]

    context = {'channel_list': latest_question_list,'radio':'radio'}
    return render(request, 'gids/index.html', context)

def info(request,id):
    channel = get_object_or_404(Channel,pk=id)
    return render(request,'gids/info.html',{'channel':channel})