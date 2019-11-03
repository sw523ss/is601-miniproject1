# Python 101: Definitions, Concepts and Examples

## How Python uses Indentation to control Flow

### In simple Terms:

Python uses indentation to control flow by defining a block of code. 

### Some Detail:

A code block starts with indentation and ends with the first unindented line. 
The amount of indentation must be consistent throughout that block. For instance, four whitespaces are used for indentation. 

### To visualize:

![indentation](./images/indentation.png)


---

## Don't Repeat Yourself

### In simple Terms:

The Don't Repeat Yourself principle states that duplication in logic should be eliminated via abstraction. 

### Some Detail:

Adding unnecessary code increases the amount of work required to maintain the software in the future. Duplicate code adds to technical debt. 
Duplication decreases the quality of the code. 

### To visualize:

Calculate BMI for three subjects. 

![Calculate BMI for Three Subjects](./images/DRYsample.png)

Use function to avoid repeating. 

![Use function to avoid DRY](./images/functiontoavoiddry.png)


---
## Design Patterns from Gang of Four

### In simple Terms:

Programmers faced with a number of recurring problems as they write object oriented code. To standardize the solutions to these problems, four software engineers, identified the most common patterns of problems that occur in object oriented programming. They formulated model solutions to these common problems in a book called “Design Patterns: Elements of Reusable Object-Oriented Software” aka “The Gang of Four (GoF)

### Some Detail:

### Classification of Design Patterns

**Creational Patterns**: These are concerned with creating objects.

**Structural Patterns**: These patterns describe relationship between objects.

**Behavioral Patterns**: Interaction between different objects. The strategy pattern aka “The Policy Pattern" is one of the most frequently used Behavioral Pattern. The main goal of this pattern is to enable a client class to choose between different algorithms or procedures to complete the same task. 

### To visualize:


---
## Class

### In simple Terms:

Python is an object oriented programming language.
A Class is like an object constructor, or a "blueprint" for creating objects.

### Some Detail:

To create a class, use the keyword class

### To visualize:

Python Class Demo: Write a Python program to convert an integer to a roman numeral.

![Class](./images/class.png)
---
## Object

### In simple Terms:

Object is simply a collection of data (variables) and methods (functions) that act on those data. 

The object() function returns an empty object.

You cannot add new properties or methods to this object.

This object is the base for all classes, it holds the built-in properties and methods which are default for all classes.

### Some Detail:

Syntax: object()

### To visualize:

Create Object: we use the class named myTime to create objects. 
Create an object t1, and print the value of t. 

![Object](./images/object.png)
---
## Static

### In simple Terms:

Static methods do not require object creation.

A static method can always be called, but is part of a class.

Method requires you to create an object: Not the case with static methods.


### Some Detail:

Static method
Create a class and add a method. You should explicitly define it’s a static method by adding @staticmethod.

Once you defined the class, you can call the methods directly.

This calls the method without creating an object. Unlike normal class methods, they do not have access to objects variables.

### To visualize:

![Static](./images/static.png)
---
## Property / Attribute

### In simple Terms:

### Some Detail:

### To visualize:


---
## Method

### In simple Terms:

### Some Detail:

### To visualize:


---
## Exception

### In simple Terms:

### Some Detail:

### To visualize:


---
## Unit Test

### In simple Terms:

### Some Detail:

### To visualize:


---
## Constructor

### In simple Terms:

### Some Detail:

### To visualize:


---
## Factory

### In simple Terms:

### Some Detail:

### To visualize:


---
## Decorator

### In simple Terms:

### Some Detail:

### To visualize:


---
## Extend Class

### In simple Terms:

### Some Detail:

### To visualize:


---
## CSV Files

### In simple Terms:

### Some Detail:

### To visualize:


---
## Reading Files

### In simple Terms:

### Some Detail:

### To visualize:


---

# Changelog

- [x] Create .md File for python 101 ~ Faisal
- [x] Added Headers for all items to be defined. ~Faisal
- [x] Added Link on README.md file ~ Faisal
- [x] How Python uses Indentation to control Flow ~Steven 
- [X] Don't Repeat Yourself ~Steven
- [X] Design Patterns from Gang of Four ~Steven 
- [X] Class ~Steven
- [X] Object ~Steven
- [X] Static ~Steven
- [ ] Property / Attribute
- [ ] Method 
- [ ] Exception
- [ ] Unit Test
- [ ] Constructor
- [ ] Factory 
- [ ] Decorator 
- [ ] Extend Class
- [ ] CSV Files 
- [ ] Reading Files 

