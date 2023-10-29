from django.shortcuts import render
from .models import *


def home(request):
    qidirish_sozi = request.GET.get("searched")
    togrisi = Togri.objects.filter(soz=qidirish_sozi)
    if togrisi:
        t = togrisi[0]
        n = Notogri.objects.filter(t_soz=t)
    else:
        n = Notogri.objects.filter(soz=qidirish_sozi)
        if n:
            t = n[0].t_soz
            n = Notogri.objects.filter(t_soz=t)

    content = {
        "togri": t,
        "notogrilar": n
    }
    return render(request, "result.html", content)
