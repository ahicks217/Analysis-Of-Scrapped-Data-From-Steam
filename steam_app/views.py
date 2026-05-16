from django.shortcuts import render
from django.db.models import Q
from .models import SteamGame

def index(request):
    query = request.GET.get("q", "").strip()
    steam_data = SteamGame.objects.all()

    if query:
        filters = (
            Q(name__icontains=query) |
            Q(genres__name__icontains=query) |
            Q(publishers__name__icontains=query) |
            Q(developers__name__icontains=query)
        )

        # 🔥 Add ID lookup if the query is a number
        if query.isdigit():
            filters |= Q(id=int(query))

        steam_data = steam_data.filter(filters).distinct()

    return render(request, "index.html", {"steam_data": steam_data})