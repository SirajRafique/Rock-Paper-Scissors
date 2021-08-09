# Rock Paper Scissors

## Introduction 

Welcome to my third project. A text based game, written completely in python for people of all ages.  

This is a classic game of rock, paper and scissors. The aim is to use logical considerations, compete and try to win against the computer.    

The command-line application has been deployed to a cloud-based platform. 

You can view it [here](https://sirajrafique.github.io/The-Language-Hub/) 

## Table of Contents
-----------------------------------------------------------------

* [1. UX](#UX) 
    * [1.1 User Goals](#user-goals) 
    * [1.2 Flow Chart](#flowchart) 
* [2. Technology Used](#technologyused) 
* [3. Testing](#testing) 
* [4. Bugs Discovered](#bugsdiscovered) 
* [5. Deployment](#deployment) 
* [6. End Product](#endproduct)

<a name="UX"></a>  
**1. UX**
---------

 <a name="user-goals"></a>           
**1.1 User Goals:** 

1. As a user, I want to be able to play a logical game.
2. As a user, I want to be able to play against the computer.
3. As a user, I want to be able to see the score.
4. As a site owner, I want to the user to know if there is empty or invalid input data.
5. As a site owner, I want the user to be able to end the game or continue playing. 

<a name="mockup"></a>
**1.2 Flow Chart:**

![image](https://user-images.githubusercontent.com/80712910/128757334-a95ba306-5e88-4f35-ac13-1e12f610c753.png)

<a name="technologyused"></a>
**2. Technologies Used**
---------------------

[*GO TO THE TOP*](#UX) <a name="UX"></a>

* Python
    
* GitHub

* Lucidchart 

* Heroku 

<a name="testing"></a> 
**3. Testing**
---------------------------------

[*GO TO THE TOP*](#UX) <a name="UX"></a>

Code passes through a linter (PEP8) with no issues.

![image](https://user-images.githubusercontent.com/80712910/128761745-99197890-7277-465b-a681-97c656bcf025.png)

Manually testing user goals: 



<a name="bugsdiscovered"></a>
**4. Bugs Discovered** 
--------------------------------

[*GO TO THE TOP*](#UX) <a name="UX"></a>
    
![image](https://user-images.githubusercontent.com/80712910/128760627-3e8363f6-5d90-4886-a52b-fd2c0a62a49b.png)

When passing the code through PEP8 the above error showed. 
This has now been fixed. I moved the code to a new line. 

<a name="deployment"></a>
**5. Deployment** 
--------------

[*GO TO THE TOP*](#UX) <a name="UX"></a>

The application was deployed via Heroku.

1. A python essential template was already created to get the project working in a mock terminal and out onto a webpage. 

2. We need to create a list of requirements that our project needs to run. 

3. In order for the project to run on Heroku, we need Heroku to install these dependencies. The list of dependencies will go in our requirements.txt file. 

4. Use the following command in the terminal 'pip3 freeze > requirements.txt'.


Heroku will use this file to import the dependencies that are required.
Log into or sign up to Heroku(it's free).
If signing up, you will need to wait and accept an authentication email.
Navigate to Dashboard.
Click "New" and select "create new app" from the drop-down menu. This is found in the upper right portion of the window.
Provide a name for your application, this needs to be unique, and select your region.
Click "Create App"



1.	First, Log into GitHub: Where the world builds software
2.	Once logged in, find repositories - could be on the left hand side or at the top. From the list, choose _Rock Paper Scissors_.
3.	From the menu items at the top of the page select settings.
4.	Scroll down to the GitHub pages section.
5.	Under source, click the drop-down menu labelled ‘None’ and select master branch. 
6.	On selecting master branch, the page is automatically refreshed, the website is now deployed.
7.	Scroll back down to the GitHub pages section to reference/retrieve the link. 

How to run this project locally and to clone the project into Gitpod:

1.	A GitHub account - create an account
2.	Use the chrome browser
3.	Install the Gitpod extensions for chrome
4.	Restart the browser
5.	Login to Gitpod with your Github account
6.	Navigate to the project GitHub repository
7.	Click the green Gitpod button top right-hand corner
8.	This will trigger a new Gitpod workspace to be created from the code where you can work locally
