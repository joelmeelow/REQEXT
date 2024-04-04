from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Pharmmodels, PharmConverse, PharmMessages
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json


@csrf_exempt
@login_required
def index(request, pk):
    
    chat = get_object_or_404(PharmConverse, pk=pk)
    converse = PharmConverse.objects.filter(Item=chat.Item)
    pharms = PharmConverse.objects.all()
    messagee = PharmMessages.objects.filter(conversation=chat)
   
   

  
    
    context = {
        'converse': converse,
        'chat': chat,
        'pharms': pharms,
        
        
        
      
    }
    
    return render(request, 'care/index.html',  context)



@csrf_exempt
@login_required
def phar(request, pk):
    
    Item = get_object_or_404(Pharmmodels, pk=pk)
    print(Item.created_by)

    if Item.created_by == request.user:
        return redirect('patients:index')
    else:
        
        conversations = PharmConverse.objects.filter(Item=Item).filter(patient=request.user)
    
        
        if conversations:
            return redirect('care:index', pk=conversations.first().id)
        else:
            conversation = PharmConverse.objects.create(Item=Item, patient=request.user)
                
            conversation.save()
            return redirect('care:index', pk=conversation.id)



@csrf_exempt
@login_required
def send(request):
    

    if request.method == 'POST':
        pk = request.POST['conversation']
        content = request.POST['message']
        
        conversations = PharmConverse.objects.get(pk=pk)
        messaging = PharmMessages.objects.create(content=content, conversation=conversations, created_by=request.user)
    

        
        messaging.save()
        return HttpResponse('Message sent successfully')

       
@login_required
def getMessages(request, pk):
   

    message = PharmConverse.objects.get(pk=pk)
    messages = PharmMessages.objects.filter(conversation=message)

   
    return JsonResponse({"messages":list(messages.values())})

    
@csrf_exempt
@login_required
def inbox(request, pk):
    Item = get_object_or_404(Pharmmodels, pk=pk)
    print(Item.created_by)

 
    conversations = PharmConverse.objects.filter(Item=Item)
   
    context ={
        'conversations': conversations,
        'Item': Item
                }

    
    return render(request, 'care/converse.html', context)



    
    
