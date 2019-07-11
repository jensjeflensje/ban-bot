from django.shortcuts import render
from . import models


def home(request):
    bans = models.Ban.objects.order_by("-id").all()[:10]
    context = {"bans": bans}
    return render(request, "index.html", context)


def search(request):
    query = request.GET.get("q")
    bans_name = models.Ban.objects.filter(user_name__icontains=query).all()
    bans_id = models.Ban.objects.filter(user_id__icontains=query).all()
    bans = bans_name | bans_id
    context = {"bans": bans, "query": query}
    return render(request, "search.html", context)


def search_user(request, user_id):
    bans = models.Ban.objects.filter(user_id=user_id).all()
    context = {"bans": bans, "name": bans.last().user_name}
    return render(request, "search_user.html", context)