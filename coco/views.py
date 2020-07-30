from django.shortcuts import render

# relaciona la parte vista con el template home.html
def home(request, plantilla="home.html"):
    return render(request, plantilla);


def portada(request, plantilla="portada.html"):
    return render(request, plantilla);


def about(request, plantilla="about.html"):
    return render(request, plantilla);



def contact(request, plantilla="contact.html"):
    return render(request, plantilla);