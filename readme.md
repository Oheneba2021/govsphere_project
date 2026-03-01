GovSphere

GovSphere is a civic engagement and governance transparency platform designed to help users track public projects and provide structured feedback in a centralized system.

The goal of this project is to create a digital space where projects can be documented, reviewed, and discussed through citizen feedback, improving visibility and accountability.

Project Overview

GovSphere allows authenticated users to:

Manage development projects

Attach supporting documents and media

Submit and review feedback tied to projects

Search and retrieve project or feedback data

This MVP focuses on the core interaction loop between projects and public feedback.

Features Implemented
Authentication

Custom login system

Access-controlled dashboard

Dashboard

Displays summarized database insights

Provides entry point to platform features

Project Management

Users can:

Add new projects

Edit existing projects

Delete projects

Search for projects

View project details

Attachments

Users can upload:

Images

PDF files

Word documents

These are linked directly to projects to support documentation and transparency.

Feedback System

Users can:

Add feedback to a project

Edit feedback

Delete feedback

Search for feedback by project name

Feedback includes:

Type

Priority

Ratings

Message

Anonymous option

Search Capabilities

The platform includes search functionality for:

Projects (by title, description, or location)

Feedback (by project name)

This improves discoverability and usability.

Technologies Used

Django

SQLite

HTML/CSS

Django ORM

Django Authentication System

Current Scope (MVP)

Within the 5-week sprint, the focus was on building a fully functional system that supports:

Project lifecycle management

Document attachment

Citizen-style feedback interaction

Search and retrieval

The system demonstrates a working governance interaction model.

Future Improvements

Planned enhancements include:

Data visualizations

Notification system

Role-based moderation

Public data integrations

Maps integration

Advanced analytics

Installation (Local Setup)
git clone <repo-url>
cd govsphere
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
Demo

A Loom walkthrough demonstrating the system features is available.

Author

Godwin Boakye