from django.db.models.query_utils import Q
from django.forms.models import fields_for_model
from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Messages, Room, Topic
from Members.models import User ,Team
from .forms import RoomForm, MessageForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from Members.forms import createProfileUser, userForm
from App.models import Matches , Month , week
from Jobs.helpers import matchweekday

# Create your views here.


def home(request):
    
    winner = None
    match_winner = None
    week_id = week.objects.all().last()
    if Matches.objects.filter(week_id = week_id):
        match_winner = Matches.objects.get(week_id = week_id)
        if match_winner.yellow_team == 'win':
            winner = Team.objects.filter(name='Yellow Team').first()
            print(winner)

        elif match_winner.red_team == 'win':
            winner = Team.objects.filter(name='Red Team').first()
            print(winner)
        else:
            winner = 'Draw'   
    else:
        match_winner = Matches.objects.all().last()
        if match_winner:
            if match_winner.yellow_team == 'win':
                winner = 'Yellow team'
            elif match_winner.red_team == 'win':
                winner = 'red team'
            else:
                winner = 'Draw'   

    
   
   

    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)

    )
    topics = Topic.objects.all()[0:5]
    rooms_count = rooms.count()
    room_masseges = Messages.objects.filter(Q(room__topic__name__icontains=q))

    return render(request, "base/Home.html", {
        'rooms': rooms,
        'topics': topics,
        'rooms_count': rooms_count,
        'room_massages': room_masseges,
        'date' : matchweekday(),
        'winner': winner,
        'month_winner':Month.objects.all().last(),
         
    })


def room(request, pk):
    room = Room.objects.get(id=pk)
    room_masseges = room.messages_set.all().order_by('-created')
    participants = room.participants.all()
    form = MessageForm()
    if request.method == 'POST':
        massage = Messages.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body'),
            images=request.FILES.get('image_file'),
            video=request.FILES.get('videos')
        )
        massage.save()
        room.participants.add(request.user)
        return redirect('room', pk=room.id)
    context = {'room': room, 'form': form,
               'room_masseges': room_masseges, 'participants': participants,
              
               }
    return render(request, "base/room.html", context)


def userProfile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_massages = user.messages_set.all()
    topics = Topic.objects.all()

    context = {'user': user, 'rooms': rooms,
               'room_massages': room_massages, 'topics': topics
               }
    return render(request, 'base/profile.html', context)


@login_required(login_url='login')
def createRoom(request):
    form = RoomForm
    topics = Topic.objects.all()
    if request.method == "POST":
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description')
        )

        return redirect("home")
    context = {'form': form, 'topics': topics}
    return render(request, 'base/create-room.html', context)


@login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    topics = Topic.objects.all()
    if request.user != room.host:
        return HttpResponse(' you are not allowed here')

    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get('description')
        room.save()
        return redirect("home")

    context = {'form': form, "room": room, 'topics': topics}
    return render(request, 'base/create-room.html', context)


@login_required(login_url='login')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse(' you are not allowed here')

    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete_form.html', {'obj': room})


@login_required(login_url='login')
def deleteMassage(request, pk):
    massage = Messages.objects.get(id=pk)

    if request.user != massage.user:
        return HttpResponse(' you are not allowed here')

    if request.method == 'POST':
        massage.delete()
        return redirect('home')
    return render(request, 'base/delete_form.html', {'obj': massage})




def topicpage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Topic.objects.filter(name__icontains=q)
    context = {"topics": topics}
    return render(request, 'base/topics_mobile.html', context)


def activitypage(request):
    room_massages = Messages.objects.all()[0:5]
    context = {'room_massages': room_massages}

    return render(request, 'base/activity.html', context)
