from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import Flight,Passenger

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, "flight/index.html", {
        "flights": Flight.objects.all()
    })

def flight_view(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    return render(request, "flight/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flight=flight).all()
    })
    
def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger_id = int(request.POST["person"])
        passenger = Passenger.objects.get(pk=passenger_id)
        passenger.flight.add(flight)
        return redirect("flight_view", flight_id=flight_id)

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            return redirect("index")
        else:
            return render(request, "flight/login.html", {
                "message": "Invalid Username or Password",
            })
    return render(request, "flight/login.html")
    
def logout_view(request):
    logout(request)
    return render(request, "flight/login.html", {
        "logout": "Logged Out"
    })