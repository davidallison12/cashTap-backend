# cashTap-backend





**Associated Repos**
Frontend: https://github.com/davidallison12/cashTap-frontend
Backend: https://github.com/davidallison12/cashTap-backend
Twilio Backend: https://github.com/davidallison12/cashTap-twilio

**Deployed Links:**
Main Site: https://cashtap-frontend.herokuapp.com/
Backend:https://cashtap-backend.herokuapp.com/
Twilio: https://cashtap-backend.herokuapp.com/

cashTap was designed out of the thought of helping those who are in debt, start the journey to becoming debt free and becoming wealth builders. For many who live paycheck to paycheck, things such as Auto-Pay can be more of a burden than a helpful tool. Every penny counts and if one bill is taken early or one pay stub posts late, it can be a world of nightmares moving forward. 

cashTap hopes to be a a a simple, easy to use, alternative to the other bill apps out there. Built with Twilio, cashTap also has the ability to text you and alert you of the bills you have due. As someone, who very recently lived paycheck to paycheck, I know the experience of being forgetting a payment and suddenly remembeing all for it to be late. Well no more of that! 

**Why I Made It**
As someone, who very recently lived paycheck to paycheck, I know the experience of being forgetting a payment and suddenly remembeing all for it to be late. Well no more of that! 


Wireframes

![0e09f580-5214-11ec-8f51-c5e3e8a7b3cc](https://user-images.githubusercontent.com/25748411/146646740-127b30f1-0710-4c2b-a60c-d0066c9a444c.png)


Above are my wireframes for cashTap. I decided to keep these simple and minimalist in order to allow more of the design to come once things got built and underway. I decided to go more of a cards route for this app for an aesthetic purpose.


## User Stories


### MVP Goals
- As a user, I want to be able to register into the app 
- As a user, I want to be able to log into the app
- As a user, I want to be able to create a bill that only I can see on my account
- As a user, I want to be able to edit that bill 
- As a user, I want to be able to delete a bill I do not have anymore
- As a user, I want to be able to receive reminders on when my bills are due.
- As a user, I want to interact with the app on a responsive site

### Stretch Goals
- As a user, I want to be able to see my current bank balance
- As a user, I want to be able to text back to the app to receive additional notifications, such as current balance, or upcoming bills
- As a user, I want to receive alerts when money hits my account. 
- As a user, if my account is less than an upcoming bill, I want to receive a text message. 

Technologies Used
Django - Backend
React.js - Frontend
Node.js 
Express.js - Twilio Backend
Twilio
Heroku Deployment 
Bulma CSS
JWT Authentication Tokens



Approach
I approached this project through the use of the MVT(Model, Template, View) as layed out by the Django template. This is similar to the MVC(Model, View, Controller) framework.

Models
This app consists of two models, the Exercise Model and the Workout model.

Profile Model
The Profile Model is an extension of sorts to the user Model. While it is its own model, it has a one to one relationship with the Django default user model. 

![Screen Shot 2021-12-18 at 11 01 25 AM](https://user-images.githubusercontent.com/25748411/146647553-0edf1898-5373-4a2d-a20b-ff435fc8f771.png)


Bills
Bills is the main model used throughout the app. This model will track the type of bill it is, the company/entity it is owed to, the due date and the minimum payment. 

![Screen Shot 2021-12-18 at 11 03 36 AM](https://user-images.githubusercontent.com/25748411/146647628-497d4ef3-fbc5-449f-b976-1b61687b2b84.png)


**Authentication**
Authentication was created through the use of JWT Access Tokens. On the Django backend, this required update setting.py and adding quite a few parameters. Additionally, I used views to allow for REST capabilities and created two token routes in order to accept those requests. 

views.py
![Screen Shot 2021-12-18 at 11 11 14 AM](https://user-images.githubusercontent.com/25748411/146647830-59a44e60-54ba-4c00-a25f-df9d801aab3e.png)


url.py
![Screen Shot 2021-12-18 at 11 11 52 AM](https://user-images.githubusercontent.com/25748411/146647849-151f961b-fdb2-4a5d-862a-6bfa56a06a85.png)


On the frontend, a React Context file was used in order to allow the authentication materials to live outside of state. This is where the logic for for the fetch login and logout are along with adding the token to local storage. 

Authcontext.js - loginUser
![Screen Shot 2021-12-18 at 11 19 55 AM](https://user-images.githubusercontent.com/25748411/146648113-983f1586-da72-4584-9f3d-2406262ebc2a.png)

Authcontext.js - updateToken
![Screen Shot 2021-12-18 at 11 21 28 AM](https://user-images.githubusercontent.com/25748411/146648174-2c475453-07ca-4051-9329-f88eddff8c38.png)


**Twilio**
Twilio is another feature of this application. In cashTap's future stages, Twilio's text messaging service will be used to remind users of the upcoming bills and and account balance. 

server.js
![Screen Shot 2021-12-18 at 11 22 53 AM](https://user-images.githubusercontent.com/25748411/146648215-60a4e6f9-0059-4c5e-b405-ed1b16d08fd0.png)

Twilio Fetch Call
![Screen Shot 2021-12-18 at 11 24 23 AM](https://user-images.githubusercontent.com/25748411/146648260-eb01874a-6056-4c45-ab96-6e4422624c70.png)





Unsolved Problems
Some of my unsolved problems include:
- Unable to create a User on deployed version of app. Cors errors seem to be the issue.
- Increase Twilio functionality so users can text twilio for update on bills
- Unable to edit a user as well. Ii believe this is die to password being required and since it is not getting hashed on the backend once created, it is not registering through django password validation. 
- For a while, I was trying to launch the Twilio backend on the same heroku app as my React frontend. I would like to try to get that working if I can. 


**Special Thanks**
Thank you to my wonderful instructors Deja Yang, Matthew Gonczar, Joe Malatesta, Thiago Calvacante and Adonis Martin for the amazing experience over the last 6 months. Special shout out to my wonderful friends in SEI Bromeliad for all of your help and patience during the project!!!
