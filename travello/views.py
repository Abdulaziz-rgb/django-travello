from django.shortcuts import render

# Create your views here.

from .models import Destination

def index(request):

    #? Getting static data
    # dest1 = Destination()
    # dest1.id = 1
    # dest1.name = 'Mumbai'
    # dest1.desc = 'The city never sleeps'
    # dest1.price = 1000
    # dest1.img = 'destination_1.jpg'
    # dest1.offer = False

    
    # dest2 = Destination()
    # dest2.id = 2
    # dest2.name = 'Dhaka'
    # dest2.desc = 'Biggest City'
    # dest2.price = 650
    # dest2.img = 'destination_2.jpg'
    # dest2.offer = True
    
    # dest3 = Destination()
    # dest3.id = 3
    # dest3.name = 'Kolkata'
    # dest3.desc = 'Garden City'
    # dest3.price = 100
    # dest3.img = 'destination_3.jpg'
    # dest3.offer = True
    
    # dests = [dest1, dest2, dest3]

    #! Getting data from database
    dests = Destination.objects.all()
    

    return render(request, 'index.html', {'dests': dests})
