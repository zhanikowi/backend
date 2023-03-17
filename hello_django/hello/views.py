from django.shortcuts import render

def index(request):
    return render(request, "welcome.html")
def search(request):
    name = request.GET.get("name")
    return render(request, "search.html", {"name": name})