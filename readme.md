GovSphere

GovSphere is a civic engagement and governance transparency platform that enables citizens to view public projects, track their progress, and submit feedback directly to administrators.

This project is being developed as a 4-week MVP focused on proving the core transparency loop between citizens and government projects.

Project Goal (MVP)

The goal of this MVP is to demonstrate that:

Citizens can register and log in

Admins can create and manage government projects

Citizens can view projects and their locations

Citizens can submit feedback on projects

Admins can view that feedback

This proves the feasibility of a larger GovSphere platform.

Tech Stack

Backend: Django

Database: SQLite (development)

Frontend: Django Templates (initially)

Maps: Google Maps API (planned)

Deployment: (to be decided)

Django Apps Structure

The project is intentionally kept minimal and modular.

App	Responsibility
accounts	Custom user model and roles (citizen, admin)
projects	Government project data (title, budget, status, location)
feedback	Citizen feedback linked to projects
core	Dashboard, home views, shared templates
Database Models Implemented
User (accounts)

Custom user model

Role field: citizen or admin

Project (projects)

Title

Description

Budget

Status (pending, ongoing, completed)

Latitude & Longitude

Created by (admin)

Feedback (feedback)

Linked to project

Linked to user

Message

Timestamp

Progress Log
Completed

Django project and apps created

Custom user model implemented

Project and Feedback models implemented

Migrations successful

Django admin configured

Superuser created

Test data added through admin

In Progress

Views and templates for project listing

Authentication pages (login/register)

Pending

Project detail page with map

Feedback submission form

Admin feedback view

Basic data visualization

Deployment and documentation

How to Run the Project
git clone https://github.com/Oheneba2021/govsphere_project.git
cd govsphere
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


Visit:
http://127.0.0.1:8000/admin

4-Week Development Plan

Week 1: Setup, models, authentication
Week 2: Project management and listing
Week 3: Feedback system
Week 4: Testing, visualization, deployment, documentation