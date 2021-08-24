import datetime
import random

import ipdb
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
import ipdb


# Create your views here.
from django.template.response import TemplateResponse
from django.views.generic import TemplateView

from sumgame.models import CommunityMember, Hobby

def get_number_list_from_stringified_list(stringified_list):
    return [int(number) for number in stringified_list[1:-1].split(',')]


def hobby_riddle(request):
    print(f"AAA riddle man: {request.GET.get('riddle_man_id')}")
    riddle_man = CommunityMember.objects.get(id=int(request.GET.get('riddle_man_id')))
    current_user = CommunityMember.objects.get(id=request.user.id)

    # ipdb.set_trace()

    if int(request.GET.get('answer')) in [hobby.id for hobby in riddle_man.hobbies.all()]: # riddle_man.hobbies
        print(f"AAA current_user.given_numbers before: {current_user.given_numbers}")
        # ipdb.set_trace()
        current_user_numbers_list = get_number_list_from_stringified_list(current_user.given_numbers)
        # ipdb.set_trace()
        current_user_numbers_set = set(current_user_numbers_list)
        current_user_numbers_set.add(riddle_man.master_number)

        current_user_numbers_list = list(current_user_numbers_set)
        # current_user_numbers_list.append(riddle_man.master_number)
        current_user.given_numbers = current_user_numbers_list
        current_user.save()

        # current_user.given_numbers[] (riddle_man.master_number)
        print(f"AAA current_user.given_numbers after: {current_user.given_numbers}")
        return HttpResponse(
            f"you're right! you earned the number {riddle_man.master_number} from {riddle_man.username} <br>"
            f"your numbers: {current_user.given_numbers}<br>"
            f'<a href="javascript:history.back()">Go Back</a>'
                            )


    else:
        return HttpResponse(f"this hobby is not written as the riddle man hobby")


class HomePageView(TemplateView):
    # template_name = "app/home.html"
    template_name = "heroic_app/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_message'] = 'Hello from Amitay'

        messages.info(self.request, "hello http://example.com")

        try:
            community_member = CommunityMember.objects.get(id=self.request.user.id)
            community_member_hobbies = [h.name for h in community_member.hobbies.all()]
            context['community_member'] = community_member
            context['all_hobbies'] = [h.name for h in community_member.hobbies.all()]


            if community_member.master_number_generation_date != datetime.datetime.now().date() or community_member.master_number is None:
                # CommunityMember.objects.filter(username=request.user.username).update(master_number=random.randint(1, 17))
                community_member.master_number = random.randint(1, 17)
                community_member.master_number_generation_date = datetime.date.today()
                community_member.save()


            print(
                f"AAA community_member.master_number_generation_date: {community_member.master_number_generation_date}")
            riddle_man = CommunityMember.objects.all()[1]
            context['riddle_man'] = riddle_man

            context['all_hobbies'] = [ho for ho in Hobby.objects.all()]

            # ipdb.set_trace()
            context['today'] = str(datetime.date.today())
            # context['all_hobbies'] = list(Hobby.objects.all())
            # context['Hobby'] = Hobby

            # return TemplateResponse(request, 'app/index.html')

        except Exception as e:
            print(f"AAA exception: {e}")
            if str(e) == "CommunityMember matching query does not exist.":
                return redirect('login')
            # else:
            #     return return_value
            # return HttpResponse("redirecting to login page...")

        return context


def index(request):
    print(f"AAA request.user: {request.user}")

    try:
        community_member = CommunityMember.objects.get(id=request.user.id)

        if community_member.master_number_generation_date != datetime.datetime.now().date() or community_member.master_number is None:
            # CommunityMember.objects.filter(username=request.user.username).update(master_number=random.randint(1, 17))
            community_member.master_number = random.randint(1, 17)
            community_member.master_number_generation_date = datetime.date.today()
            community_member.save()


        print(f"AAA community_member.master_number_generation_date: {community_member.master_number_generation_date}")
        riddle_man = CommunityMember.objects.all()[1]
        return TemplateResponse(request, 'app/index.html')

    except Exception as e:
        print(f"AAA exception: {e}")
        if str(e) == "CommunityMember matching query does not exist.":
            return redirect('login')
        # else:
        #     return return_value
        # return HttpResponse("redirecting to login page...")

def login(request):
    return HttpResponse("Welcome to login page")