# Entri_BE
Steps to setup the application
  --Create a virtual environment
  --Install django and python
  --Install package requests(mentioned in requirements.txt file)
  --Now Go to the folder and run python manage.py runserver
  
 Have used sqlite db for storing the user details.(default django db)
 
 There are total 3 APIs
 1. To list the users.
 2. To register the user.(Need to send userdetails for eg{"firstname":"Anjana","middlename":"S","lastname":"candidate","is_interviewer":0,"starttime":"09:00","endtime":"12:00"}.
    The user name has to be unique.)
 4. To find the common timeslots.(Need to send userids as {"candidateid":1,"interviewerid":2})






 

  
 
