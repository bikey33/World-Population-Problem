from django.shortcuts import render
from django.http import JsonResponse
from myapp.models import Country, Population
from myapp.forms import PopulationForm
# Create your views here.


def home(request):

    context = {}
    # Getting Each Cities and passing each city rows as context
    if request.method =="GET":
        pop = Population.objects.all()
        context = {'population': pop}
        return render(request,'home.html',context)

    return render(request,'home.html',{})


def get_total_populations(request):

    data_pop = []
    # Getting city and populations for a give country
    # Downward Querying
    country = Country.objects.all()
    for con in country:
        city_pop = con.population_set.all()
        total_population = 0
        for i in city_pop:
            # Sending Child Population with respect to each cities
            # in a list of dictionaries
            total_population = total_population + int(i.child_population) + int(i.man_population) + int(i.woman_population)
        data_pop.append({con.country: total_population})
        print(data_pop)
    return JsonResponse(data_pop, safe=False)


def get_data(request):

    data_pop =[]
    # Getting city and populations for a give country
    # Downward Querying
    country= Country.objects.get(id = 1)
    city_pop = country.population_set.all()
    for i in city_pop:
        # Sending Child Population with respect to each cities
        # in a list of dictionaries
        data_pop.append({i .city: i.child_population})
    print(data_pop)
    return JsonResponse(data_pop,safe= False)


def post_data(request):

    # Handling AJax Post Request
    if request.method == "POST":
        form = PopulationForm(request.POST)

        country = request.POST['country']
        print(country)
        con = Country()
        con.country = country
        con.save()
        city_name = request.POST['city']
        #print(city_name)
        male = request.POST['man_population']
        female = request.POST['woman_population']
        child = request.POST['child_population']
        try:
            city_p = Population(country = con,city=city_name, man_population=male, woman_population=female, child_population=child)
            city_p.save()
            # to send data back to template to render on table
            # After sucessfull posting of data
            city_pop= Population.objects.values()
            city_data = list(city_pop)
            # Get all objects as python dictionary using .values() methods
            print("Object is created sucessfully")
            return JsonResponse({'status': 'saved', 'city_data': city_data})

        except Exception as e:
            return JsonResponse({'status': e})
            print(e)

def help(request):
    pass
def get_plot_data(request):

    # Fuction to get values for showing them in graph
    if request.method =='POST':
        id = request.POST.get('sid')
        print(id)
        city_p = Population.objects.get(pk = id)
        data_pop = {'city':city_p.city, 'male':city_p.man_population, 'female':city_p.woman_population, 'child':city_p.child_population }
        print(data_pop)
        return JsonResponse(data_pop, safe=False)
    else:
        return JsonResponse({'status': 'failed'})
