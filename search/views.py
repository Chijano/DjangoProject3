from django.shortcuts import render
from .models import SearchHistory
from .forms import SearchForm
from podcasts.models import Podcast, Episode


def search_view(request):
    form = SearchForm(request.GET)  # Get data from request
    podcasts = Podcast.objects.all()
    episodes = Episode.objects.all()

    if form.is_valid():
        query = form.cleaned_data.get("query")
        category = form.cleaned_data.get("category")
        language = form.cleaned_data.get("language")
        release_date = form.cleaned_data.get("release_date")

        if query:
            podcasts = podcasts.filter(title__icontains=query) | podcasts.filter(host__icontains=query)
            episodes = episodes.filter(title__icontains=query)

        if category:
            podcasts = podcasts.filter(category=category)

        if language:
            podcasts = podcasts.filter(language__icontains=language)

        if release_date:
            episodes = episodes.filter(release_date=release_date)

        # Save search history if user is logged in
        if request.user.is_authenticated and query:
            SearchHistory.objects.create(user=request.user, query=query)

    return render(request, "search/search_results.html", {
        "form": form,
        "podcasts": podcasts,
        "episodes": episodes,
    })
