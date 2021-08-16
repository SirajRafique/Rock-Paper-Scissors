# Rock Paper Scissors

## Introduction 

Rock Paper Scissors is a python terminal game, which runs in Code Institute's mock terminal on Heroku. 

A classic text based game for people of all ages.  

The aim is to use logical considerations, compete and try to win against the computer.  

To play, the user simply chooses from either rock, paper or scissors. 
Rock smashes scissors, paper eats rock and scissors cuts paper.

You can view it [here](https://ms3-rock-paper-scissors.herokuapp.com/) 

![image](https://user-images.githubusercontent.com/80712910/129610508-d2649a45-0a59-4a4e-812c-be31005993c2.png)

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
* [7. Credits](#credits)

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

I have manually tested this project by doing the following:

* Passed the code through a linter (PEP8) with no issues.

![image](https://user-images.githubusercontent.com/80712910/128761745-99197890-7277-465b-a681-97c656bcf025.png)

* Given invalid inputs, numbers when strings are expected, spelling mistakes and abbreviations. Error is shown as expected.

* Tested user stories in my local terminal and the Code Institute Heroku terminal - working as expected.  

### Validator testing 

PEP8 - No errors were returned from PEP8online.com

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

The application was deployed via Heroku. This is how:

1. A python essential template was already created to get the project working in a mock terminal and out onto a webpage. 

2. Use pip3 freeze > requirements.txt to import required dependencies. 

3. In order for the input method to work correctly make sure you add a new line character \n at the end of the text inside the input method.

4. Make sure your code is ready to be imported.

5. Create an account with Heroku - sign up for free and fill out the form. 

6. Confirm your email and accept the terms of service. 

7. Create a new app from the dashboard and name it. 

8. Add buildpack - python and nodejs in that order. 

9. Go to deploy section now and select github to connect your github and search for your repository.

10. Manual deploy branch and then select view. 


<a name="endproduct"></a>
**6. End Product** 
-----------

[*GO TO THE TOP*](#UX) <a name="UX"></a>

![image](https://user-images.githubusercontent.com/80712910/128779654-d19d8bb1-d9a1-4849-87f4-2dbbbec23cbd.png)

<a name="credits"></a>
**7. Credits** 
--------------------------------

[*GO TO THE TOP*](#UX) <a name="UX"></a>

Code Institute for the deployment terminal.