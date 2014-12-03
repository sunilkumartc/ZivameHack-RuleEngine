ZivameHack-RuleEngine
=====================
E-Commerce-Rule-Engine
======================

Rule Engine implemented in Python. 
The project came second in Zivame Hacakathon-2014.
The algorithm was designed and implemented in the 24 hour coding session. 



#ZivHack
November 15 - 16, 2014

Hacking etiquette
Please use the provided internet connection in a legally fitting manner. Don’t hack into secured resources or download illegal media content. If we find out about misuse we will disqualify you and your team. In the case of severe misdoing we will bring you to the attention of the authorities.

Premise Rules
There will be restrictions on accessing certain parts of the building (e.g. server rooms) so please be respectful and avoid those areas. 

Common sense etiquette
No force, violence, stealing will be tolerated.

Be thoughtful in the spirit of innovation and inclusiveness, there may be minors participating in the event, any content should not contain explicit content.

Be respectful to others.

Behave professionally. Remember that harassment and racist, sexist, or exclusionary jokes are not appropriate for this event.

Attendees violating these rules may be asked to leave the Hackathon at the sole discretion of the Hackathon organizers.

Be Awesome & Have Fun
Hack, meet new people, get creative, and have a good time. Getting something meaningful done within such a short amount of time can be stressful, but we'd like to encourage everyone to take a break every now and then to relax and enjoy the event.




Problem Statements


Problem A
Responsive Mobile Site/App

Build
A responsive optimized mobile shoe store. Build a category page, product page and a cart page. 

Product Attributes:
●	Main image
●	Other images
●	Categories (can be many)
●	Price (MRP)
●	Special Price (discounted price)
●	Description
●	Size (multiple)
●	Color (can be multiple per size)
●	Inventory (has to be per color, which is in turn per size)

Category Attribute:
●	Name

Technology
Node.js (preferred) / PHP / Python / Java

Database
Use a NoSQL database like MongoDB

Judging Criteria
Choice of Architecture 
NoSQL Schema
Application Performance








Problem B
Rule Engine

Build
A Rule Engine from scratch (do not use any available open source rule engine). We are expecting a User Interface for entering the rules.

Database schema
The sample database schema is given below

table_category
category_id
int(11)
category_name
      	varchar(100)

table_product
product_id
int(11)
product_name
varchar(100)
product_price
decimal(8,2)
product_special_price
decimal(8,2)

table_product_category
f_product_id
int(11)
f_category_id
int(11)

Input
The input to the rule engine is a set of products with its categories and special price.








The rule engine needs a set of conditions and a set of actions listed below.

Conditions
Cart total
Category id

Exclusions:
Category id

Actions
Free Shipping
% Discount
Flat Discount
Free Product

The conditions and exclusions can be grouped via brackets.

Samples
Input:
[
  {
    "product": {
      "id": "<product id>",
      "category_id": [
        "<comma separated category ids>"
      ],
      "price": "<price of product>"
    }
  },
  {
    "product": {
      "id": "<product id>",
      "category_id": [
        "<comma separated category ids>"
      ],
      "price": "<price of product>"
    }
  }
]




Rule

IF         
“cart total” [>/<] “predefined value”
AND/OR
“category is” [is] “predefined value”
AND/OR
“category id” [not] “predefined value”
THEN
[free shipping || %discount = “predefined value” || discount = “flat
          discount value” || free product = “product id”]

Example rules:

Rule 1

IF
{price > 1000 AND category_id in “200,201,200”}
THEN
 	{%discount = “20”}

Rule 2

IF
{cart_total > 5000}
OR
{price > 3000 AND category_id NOT IN “200,201,202”}
THEN
{discount = “1000”}


Judging Criteria
Correctness
Choice of algorithm(s)







Submission Guidelines
Direct your project to submissions+zivame@venturesity.com in the following format:
Name :
Link(s) to the application (zipped source code hosted on the web AND/OR github repository url AND/OR deployed application link) :
Usage instructions :














