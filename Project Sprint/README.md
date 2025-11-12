**Project Name: Accessible Transport Scheduler**

This project is a ride booking system designed to provide safe and convenient transportation for elderly individuals and persons with accessibility needs. It allows users to request, track, and manage rides through an interface connected to a FastAPI and SQLite backend. The system promotes accessible and efficient mobility by enabling real time ride management and future integration of route optimization features.
##
*NOTE: Once the files are downloaded or the project is cloned, 
#
**01 Database & Backend | Member Assigned: Denise Pagala**

This section serves as the backend server built with FastAPI and SQLite (using SQLModel). This manages Users, Drivers, and Ride Requests for an accessible transport scheduling system.

#
**1. Installation & Setup Guide**

Step 1: Switch branches and choose "backend-mvp." Clone the repository

Step 2: Create environment 
ex.: For windows only: 

    python -m venv .venv 

    .venv\Scripts\activate

Step 3: Install dependencies

    pip install fastapi uvicorn sqlmodel

Step 4: Run the FastAPI server

    uvicorn app.main:app --reload
  
Note: You should see "INFO: Uvicorn running on http:..." If not working, try running it on CMD

Search in Browser: http://127.0.0.1:8000/docs

You should see the Swagger UI with all endpoints (/users/, /drivers/, /ride-requests/)

Step 5: Run unit tests (OPTIONAL)

    pip install pytest (Install if pytest not yet installed)
  
    pytest test_main.py
#
**-------------------------------------------------------- END FOR 01 Database & Backend -------------------------------------------------------**
#

**02 Frontend (FLET) | Member Assigned: Ralph Lam**

This is a simple Python app built with Flet. It simulates a basic transportation scheduler with three user roles: User, Driver, and Administrator.

- User Dashboard: Request rides and view ride history

- Driver Dashboard: Register drivers and view assigned rides
  
- Administrator Dashboard: Generate reports and view ride logs
#
**1. Setup Guide** 

Step 1: Install Flet

    pip install flet

Step 2: Run the App:

    python "Flet App.py"
#
**-------------------------------------------------------- END FOR 02 Frontend (FLET) -------------------------------------------------------**
#

**03 Algorithm & Analytics | Member Assigned: JM Esperanza**

This section...
#
**1.(Include Heading)** 
#
**-------------------------------------------------------- END FOR 03 Algorithm & Analytics -------------------------------------------------------**
#
