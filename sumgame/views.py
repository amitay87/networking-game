import datetime
import random

import ipdb
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
import ipdb


# Create your views here.
from sumgame.models import CommunityMember, Hobby

def hobby_riddle(request):
    print(f"AAA riddle man: {request.GET.get('riddle_man_id')}")
    riddle_man = CommunityMember.objects.get(id=int(request.GET.get('riddle_man_id')))
    current_user = CommunityMember.objects.get(id=request.user.id)

    # ipdb.set_trace()

    if int(request.GET.get('answer')) in [hobby.id for hobby in riddle_man.hobbies.all()]: # riddle_man.hobbies

        return HttpResponse(f"you're right!")
        request.user
    else:
        return HttpResponse(f"this hobby is not written as the riddle man hobby")

def index(request):
    print(f"AAA request.user: {request.user}")
    # return_value = None
    # print(f"AAA type of user: {typeof(request.user)}")
    # breakpoint()
    # ipdb.set_trace()
    User

    # print(f"AAA ")
    # breakpoint()
    try:
        community_member = CommunityMember.objects.get(id=request.user.id)

        if community_member.master_number_generation_date != datetime.datetime.now().date() or community_member.master_number is None:
            # CommunityMember.objects.filter(username=request.user.username).update(master_number=random.randint(1, 17))
            community_member.master_number = random.randint(1, 17)
            community_member.master_number_generation_date = datetime.date.today()
            community_member.save()


        print(f"AAA community_member.master_number_generation_date: {community_member.master_number_generation_date}")
        riddle_man = CommunityMember.objects.all()[1]
        return HttpResponse(f"Welcome {community_member.username} :-). <br>"
                            f"you're at the game index. <br>"
                            f"your hobbies are: {[h.name for h in community_member.hobbies.all()]} <br>"
                            f"your master number for today is {community_member.master_number} <br>"
                            f"numbers you earned today: {community_member.given_numbers}<br>"
                            f"sum of all of your numbers = {community_member.master_number + sum(map(int, str.split(community_member.given_numbers[1:-1], ',')))}<br>"
                            f"your community have 0 out of 100 points. (100 points will reward you with group prize <br>"
                            f"list of community members: {[c.username for c in CommunityMember.objects.all()]}<br>"
                            f"which of the following are hobbies of {riddle_man}? <br>"
                            f'<ul><li><a href="hobby_riddle?riddle_man_id={riddle_man.id}&answer={Hobby.objects.all()[0].id}">{Hobby.objects.all()[0]}</a></li>'
                            f'<li><a href="hobby_riddle?riddle_man_id={riddle_man.id}&answer={Hobby.objects.all()[1].id}">{Hobby.objects.all()[1]}</a></li>'
                            f'<li><a href="hobby_riddle?riddle_man_id={riddle_man.id}&answer={Hobby.objects.all()[2].id}">{Hobby.objects.all()[2]}</a></li>'
                            f'<li><a href="hobby_riddle?riddle_man_id={riddle_man.id}&answer={Hobby.objects.all()[3].id}">{Hobby.objects.all()[3]}</a></li></ul>'
                            f"<button>share your tasks and tasks progress! </button>"
                            f"your friend <friend> just finished task. clap him! | arrange a tizmoret 'kol hakavod' | else"
                            f"ubuntu level: 12")

    except Exception as e:
        print(f"AAA exception: {e}")
        if str(e) == "CommunityMember matching query does not exist.":
            return redirect('login')
        # else:
        #     return return_value
        # return HttpResponse("redirecting to login page...")

def login(request):
    return HttpResponse("Welcome to login page")