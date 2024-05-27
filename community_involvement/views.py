from django.shortcuts import render, redirect


def home(request):

    return render(request, "home.html", {"url": "home"})


def programs(request):

    return render(request, "programs.html", {"url": "programs", "title": "Programs"})


def projects(request):

    return render(request, "projects.html", {"url": "projects", "title": "Projects"})


