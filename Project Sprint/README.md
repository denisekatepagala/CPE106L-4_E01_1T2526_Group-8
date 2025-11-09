**Project Name: Accessible Transport Scheduler**
##
**01 FastAPI & SQLite**

This section serves as the backend server built with FastAPI and SQLite (using SQLModel). This manages Users, Drivers, and Ride Requests for an accessible transport scheduling system.
#
**1.Folder Structure**

01 Database & Backend

	- app/

		-- init.py
	
		-- main.py
	
		-- database.py
	
		-- models/
	
			--- init.py
	
			--- models.py
	
		-- routers/
		
			--- init.py
			
			--- users.py
			
			--- drivers.py
			
			--- ride_requests.py
		
	- database.db
#
**2. Installation & Setup Guide**

Step 1: Clone the repository

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
