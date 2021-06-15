from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from mainapp.models import Sequence
from mainapp.models import Alignment


def compare_animal(request):
    template = loader.get_template('compare-animal.html')
    return HttpResponse(template.render(None, request))

def compare_data_collect(request):
    template = loader.get_template('compare-data-collect.html')
    return HttpResponse(template.render(None, request))

def compare_lowfatality(request):
    template = loader.get_template('compare-lowfatality.html')
    return HttpResponse(template.render(None, request))

def compare_mers_sars(request):
    template = loader.get_template('compare-mers-sars.html')
    return HttpResponse(template.render(None, request))

def compare_visualization(request):
    template = loader.get_template('compare-visualization.html')
    return HttpResponse(template.render(None, request))

def covid_data_collect(request):
    template = loader.get_template('covid-data-collect.html')
    return HttpResponse(template.render(None, request))

def covid_result(request):
    template = loader.get_template('covid-result.html')
    return HttpResponse(template.render(None, request))

def covid_sequence_alignment(request):
    template = loader.get_template('covid-sequence-alignment.html')
    return HttpResponse(template.render(None, request))

def covid_visualization(request):
    template = loader.get_template('covid-visualization.html')
    return HttpResponse(template.render(None, request))

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(None, request))

def intro_algorithm(request):
    template = loader.get_template('intro-algorithm.html')
    return HttpResponse(template.render(None, request))

def intro_team(request):
    template = loader.get_template('intro-team.html')
    return HttpResponse(template.render(None, request))

def execute(request):

    if request.method == "POST":
        name1 = request.POST['namecode1']
        name2 = request.POST['namecode2']

        if name1 == name2:
            return render(request, 'execute.html')

        sequence_obj1 = Sequence.objects.get(namecode=name1)
        sequence_obj2 = Sequence.objects.get(namecode=name2)
        alignment_obj = Alignment.objects.get(namecode1=name1, namecode2=name2)
        context = {'sequence_obj1': sequence_obj1, 'sequence_obj2': sequence_obj2, 'alignment_obj': alignment_obj}

        return render(request, 'execute.html', context)

    else:
        return render(request, 'execute.html')
