# Unihaven
Unihaven_COMP3297

# Django Accommodation Management System

## Overview
This project is a web application for managing accommodation searches, reservations, and ratings. It is built using Django (Python 3.13) and relies on a local SQLite database for development and testing. **Note**: This version does not include landlord-related data or functionalities, which are planned for the next development cycle.

---

## Technology Stack
- **Backend**: Django 5.0
- **Database**: SQLite (local testing)
- **Database Tool**: [Navicat Premium 17](https://www.navicat.com) (for SQL management)
- **Python Version**: 3.13

---

## Key Features (Current Scope)
- Search accommodations by criteria (type, price, availability, etc.).
- View accommodation details (images, amenities, pricing).
- Reserve and cancel accommodations.
- Rate accommodations after a stay.
- Basic notifications for reservations and cancellations.

---

## Limitations
1. **No Landlord Functionality**  
   - Landlord data management (e.g., adding properties, managing bookings) is not implemented yet.  
   - Planned for the next development phase.

2. **Local Database Usage**  
   - Uses MySQL8 for local testing; no production-ready database setup.  
   - Lacks realistic sample data and data entry interfaces.  

3. **Missing Features**
   - No rate function for customers
   - No notifications for reservations and cancellations.
   - No user registration/login system (assumes pre-authenticated users).  
   - No payment gateway integration (reservations are mock-ups).  
---

## Setup Instructions

### Prerequisites
- Python 3.13
- Navicat Premium 17 (or any SQL client for database inspection)
- Git (optional)
