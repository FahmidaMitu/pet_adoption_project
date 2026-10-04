from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Pet, AdoptionRequest
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import PetSerializer, AdoptionRequestSerializer

# --- Authentication Views ---

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful! You are now logged in.")
            return redirect('pet_list')
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect('pet_list')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.info(request, "Logged out successfully.")
    return redirect('pet_list')

# --- Existing Web Views ---

def pet_list(request):
    pets = Pet.objects.all()
    search = request.GET.get('search')
    animal_type = request.GET.get('animal_type')
    gender = request.GET.get('gender')
    
    if search:
        pets = pets.filter(name__icontains=search)
    if animal_type:
        pets = pets.filter(animal_type__iexact=animal_type)
    if gender:
        pets = pets.filter(gender__iexact=gender)

    return render(request, 'pet_list.html', {'pets': pets})

def pet_detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    return render(request, 'pet_detail.html', {'pet': pet})

@login_required
def apply_adoption(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    
    if pet.status == 'Adopted':
        messages.error(request, "This pet is already adopted.")
        return redirect('pet_detail', pk=pk)
        
    if AdoptionRequest.objects.filter(user=request.user, pet=pet, status='Pending').exists():
        messages.error(request, "You already have a pending application for this pet.")
        return redirect('pet_detail', pk=pk)

    if request.method == 'POST':
        AdoptionRequest.objects.create(
            user=request.user,
            pet=pet,
            phone=request.POST.get('phone'),
            address=request.POST.get('address'),
            reason=request.POST.get('reason'),
            previous_pet_experience=bool(request.POST.get('experience')),
            message=request.POST.get('message')
        )
        messages.success(request, "Application submitted successfully!")
        return redirect('my_requests')

    return render(request, 'adoption_form.html', {'pet': pet})

@login_required
def my_requests(request):
    requests = AdoptionRequest.objects.filter(user=request.user)
    return render(request, 'my_requests.html', {'requests': requests})

# --- REST API Viewsets ---

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['animal_type', 'gender', 'location', 'status']
    search_fields = ['name', 'breed']

class AdoptionRequestViewSet(viewsets.ModelViewSet):
    serializer_class = AdoptionRequestSerializer

    def get_queryset(self):
        return AdoptionRequest.objects.filter(user=self.request.user)

# Web Pages Logic
def pet_list(request):
    pets = Pet.objects.all()
    search = request.GET.get('search')
    animal_type = request.GET.get('animal_type')
    gender = request.GET.get('gender')
    
    if search:
        pets = pets.filter(name__icontains=search)
    if animal_type:
        pets = pets.filter(animal_type__iexact=animal_type)
    if gender:
        pets = pets.filter(gender__iexact=gender)

    return render(request, 'pet_list.html', {'pets': pets})

def pet_detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    return render(request, 'pet_detail.html', {'pet': pet})

@login_required
def apply_adoption(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    
    # Rule 1: Adopted pet ke r adopt kora jabena
    if pet.status == 'Adopted':
        messages.error(request, "This pet is already adopted.")
        return redirect('pet_detail', pk=pk)
        
    # Rule 2: Ekei pet-er jonne ekjon user-er pending request thakle double application allowed na
    if AdoptionRequest.objects.filter(user=request.user, pet=pet, status='Pending').exists():
        messages.error(request, "You already have a pending application for this pet.")
        return redirect('pet_detail', pk=pk)

    if request.method == 'POST':
        AdoptionRequest.objects.create(
            user=request.user,
            pet=pet,
            phone=request.POST.get('phone'),
            address=request.POST.get('address'),
            reason=request.POST.get('reason'),
            previous_pet_experience=bool(request.POST.get('experience')),
            message=request.POST.get('message')
        )
        messages.success(request, "Application submitted successfully!")
        return redirect('my_requests')

    return render(request, 'adoption_form.html', {'pet': pet})

@login_required
def my_requests(request):
    requests = AdoptionRequest.objects.filter(user=request.user)
    return render(request, 'my_requests.html', {'requests': requests})

# REST API Viewsets
class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['animal_type', 'gender', 'location', 'status']
    search_fields = ['name', 'breed']

class AdoptionRequestViewSet(viewsets.ModelViewSet):
    serializer_class = AdoptionRequestSerializer

    def get_queryset(self):
        return AdoptionRequest.objects.filter(user=self.request.user)