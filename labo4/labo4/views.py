from django.shortcuts import render
from django.http.response import JsonResponse , HttpResponse

from django.views.decorators.csrf import csrf_exempt

from alarme.alarme import alarme

from alarme.models import MonSysteme, Zone

# Create your views here.

alarmedb = MonSysteme.objects.get(pk=1)


def index(request):
    return HttpResponse("Projet test accueil toto")

@csrf_exempt
def activationroute(request):
    if request.method == "POST":
        
        if alarme.systemStatus != 1:
            alarme.activer()
            alarmedb.etat = 1
            alarmedb.save()
            return JsonResponse({"ok":"oui"},safe=False)
        else:
            return JsonResponse({"ok":"activer deja"},safe=False)

@csrf_exempt
def desactivationroute(request):
    if request.method == "POST":
        if alarme.systemStatus != 0:
            alarme.desactiver()
            alarmedb.etat = 0
            alarmedb.save()
            return JsonResponse({"ok":"oui"},safe=False)
        else:
            return JsonResponse({"ok":"desactiver deja"},safe=False)   


@csrf_exempt
def reinitialisationroute(request):
    if request.method == "POST":
        if alarme.systemStatus != 0:
            alarme.reinitialiser()
            alarmedb.etat = 1
            alarmedb.save()
            return JsonResponse({"ok":"oui"},safe=False)
        else:
            return JsonResponse({"ok":"desactiver deja"},safe=False)
       


@csrf_exempt
def etatweb(request):
    if request.method == "GET":
        data = request.POST
        
        zone1 = Zone.objects.get(titre="Zone 1")
        zone2 = Zone.objects.get(titre="Zone 2")
        zone3 = Zone.objects.get(titre="Zone 3")
        zone4 = Zone.objects.get(titre="Zone 4")
        data = {
            "ok":"oui",
            "monalarme" : {
                "etat" :  alarme.systemStatus
            },
            "Zone1" : {
                "etat" : zone1.etat
            },
            "Zone2" : {
                "etat" : zone2.etat
            },
            "Zone3" : {
                "etat" : zone3.etat
            },
            "Zone4" : {
                "etat" : zone4.etat
            }
        }
    
        return JsonResponse(data,safe=False)
    