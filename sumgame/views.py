import datetime
import random

from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
import ipdb


# Create your views here.
from sumgame.models import CommunityMember


def index(request):
    print(f"AAA request.user: {request.user}")
    # print(f"AAA type of user: {typeof(request.user)}")
    # breakpoint()
    # ipdb.set_trace()
    User


    community_member = CommunityMember.objects.get(id=request.user.id)
    if community_member.master_number_generation_date != datetime.datetime.now().date() or community_member.master_number is None:
        # CommunityMember.objects.filter(username=request.user.username).update(master_number=random.randint(1, 17))
        community_member.master_number = random.randint(1, 17)
        community_member.master_number_generation_date = datetime.datetime.date()
        community_member.save()

    print(f"AAA community_member.master_number_generation_date: {community_member.master_number_generation_date}")
    return HttpResponse(f"Welcome {community_member.username} :-). <br>"
                        f"you're at the game index. <br>"
                        f"your hobbies are: {[h.name for h in community_member.hobbies.all()]} <br>"
                        f"your master number for today is {community_member.master_number} <br>"
                        f"your community have 0 out of 100 points. (100 points will reward you with group prize <br>"
                        f"list of community members: {[c.username for c in CommunityMember.objects.all()]}"
                        f"<button>share your tasks and tasks progress! </button>"
                        f"your friend <friend> just finished task. clap him! | arrange a tizmoret 'kol hakavod' | else"
                        f"ubuntu level: 12")
