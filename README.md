# 🐾 Pet Adoption & Rescue Platform

A full-stack web application and RESTful API built with Django and Django REST Framework (DRF) where users can browse available pets, submit adoption applications, and manage their requests, while admins can manage pet listings and review requests.

---

## 🚀 Features

### 1. User Features
* **Authentication:** User registration, login, logout, and profile management through Django Auth/Admin system[cite: 1, 8].
* **Pet Browsing & Search:** Users can view pet details (Name, Animal Type, Breed, Age, Gender, Location, Image, Adoption Status) and filter/search by name, type, gender, location, or status[cite: 1, 2].
* **Adoption Requests:** Logged-in users can apply to adopt available pets[cite: 3].

### 2. Admin Management
* Full administrative control over pet listings (Add, Edit, Delete, Update Status, Upload Images)[cite: 4, 5].
* Manage adoption applications (Approve/Reject requests)[cite: 5].

### 3. Business Logic Rules Applied
* **Rule 1:** Only pets with `Available` status can be applied for adoption[cite: 5].
* **Rule 2:** A user cannot submit multiple active pending requests for the same pet[cite: 5].
* **Rule 3:** When an admin approves an adoption application, the pet's status automatically updates to `Adopted`[cite: 6].

### 4. REST API Integration
* `GET /api/pets/` - List all pets with filtering and search parameters (`?search=`, `?animal_type=`, `?gender=`, `?location=`)[cite: 6].
* `GET /api/pets/<id>/` - Retrieve details of a specific pet[cite: 6].
* `POST /api/pets/` - Create a new pet entry (Admin)[cite: 6].
* `GET /api/adoptions/` - Retrieve adoption requests submitted by the logged-in user[cite: 6].
* `POST /api/adoptions/` - Submit a new adoption request[cite: 6].

---

## 🛠️ Tech Stack

* **Backend:** Python, Django 5.x[cite: 1]
* **API Framework:** Django REST Framework (DRF)[cite: 1, 6]
* **Database:** SQLite3[cite: 8]
* **Frontend:** Django Templates, HTML5, Bootstrap 5[cite: 1, 8]

---

## ⚙️ Installation & Setup Instructions

Follow these steps to run the project locally on your machine:

### 1. Clone the Repository
```bash
git clone [https://github.com/FahmidaMitu/pet_adoption_project.git](https://github.com/FahmidaMitu/pet_adoption_project.git)
cd pet-adoption-platform