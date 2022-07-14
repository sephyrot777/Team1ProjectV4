from django.shortcuts import render, redirect
from django.views import View
from teams.models import Stadiums, Stadium


# Create your views here.


class TeamsView(View):
    def get(self, request):
        form = request.GET.dict()
        tbs = Stadium.objects.all()

        if (form != {}):
            team = Stadium.objects.get(based=form['based'])
        else:
            team = Stadium.objects.get(based='서울')
            print(team)

        context = {'tbs': tbs,
                   'stname': team.stname,
                   'opdate': team.opdate,
                   'based': team.based,
                   'hteam': team.hteam,
                   'accnum': format(team.accnum, ','),
                   'addr': team.location,
                   'addrstmp': team.addrstmp,
                   'addrkey': team.addrkey,
                   'url': team.url,
                   }

        return render(request, 'teams/stadium.html', context)


class OrganizationView(View):
    def get(self, request):
        return render(request, 'teams/organization.html')
