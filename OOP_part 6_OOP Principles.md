# OOP Principles

## A Encapsulation 
Mechanism of restricting the direct access to some of our attributes in a program. <br>

eg. Like how we decided to only allow renaming of attributes for length less than 11

## B Abstraction
Mechanism that allows to only show the necessary attributes and hides the unnecessary attributes 

eg. we only want to show method "send email" but inside it, it contains 
connect(), prepare_body(), send(). However, we dont want all these inner functions to be
called, so we hide. --> abstraction process. <br>
--> done by adding __ when defined in the class method, <br>
eg. check out __connect
## C Inheritance

Mechanism to allow us to reuse the code across our classes by "inheriting"
We have gone through this in detail during this project

## D Polymorphism

Mechanism of using of a single type entity to represent different types in different scenarios
Take note that polymorphism and inheritance kind of come together, see the below eg.
Poly --> many, mophism --> forms

eg. in our project, apply_discount() was from parent class, but this method in parent class is applied to any objects that we build
so, it is actually practising polymorphism, handling diff types of object with a single parent class attribute

eg. checkout Keyboard class and the use of it as a child class