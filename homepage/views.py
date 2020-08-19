import subprocess

from django.shortcuts import render
from homepage.forms import CowForm
from homepage.models import Cow

def index(request):
    if request.method == "POST":
        form = CowForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            text = data.get("text")
            Cow.objects.create(
                text = text
            )
            cowsaid = subprocess.run(f'cowsay "{text}"', capture_output=True, shell=True).stdout.decode("utf-8").strip()
            form = CowForm()
            return render(request, "index.html", {"form": form, "subprocess": cowsaid})
    form = CowForm()
    return render(request, "index.html", {"form": form})

def history(request):
    cows = Cow.objects.all().order_by("-id")[:10]
    return render(request, "history.html", {"cowsays": cows})