---
repo: bregman-arie/devops-exercises
readme_filename: bregman-arie_devops-exercises_README.md
stars: 76909
forks: 17266
watchers: 76909
contributors_count: 194
license: NOASSERTION
Header 2: SQL
Header 3: SQL Self Assessment
---

What is SQL?  
SQL (Structured Query Language) is a standard language for relational databases (like MySQL, MariaDB, ...).
It's used for reading, updating, removing and creating data in a relational database.
  

How is SQL Different from NoSQL  
The main difference is that SQL databases are structured (data is stored in the form of
tables with rows and columns - like an excel spreadsheet table) while NoSQL is
unstructured, and the data storage can vary depending on how the NoSQL DB is set up, such
as key-value pair, document-oriented, etc.
  

When is it best to use SQL? NoSQL?  
SQL - Best used when data integrity is crucial. SQL is typically implemented with many
businesses and areas within the finance field due to it's ACID compliance.  
NoSQL - Great if you need to scale things quickly. NoSQL was designed with web applications
in mind, so it works great if you need to quickly spread the same information around to
multiple servers  
Additionally, since NoSQL does not adhere to the strict table with columns and rows structure
that Relational Databases require, you can store different data types together.
  
##### Practical SQL - Basics  
For these questions, we will be using the Customers and Orders tables shown below:  
**Customers**  
Customer_ID | Customer_Name | Items_in_cart | Cash_spent_to_Date
------------ | ------------- | ------------- | -------------
100204 | John Smith | 0 | 20.00
100205 | Jane Smith | 3 | 40.00
100206 | Bobby Frank | 1 | 100.20  
**ORDERS**  
Customer_ID | Order_ID | Item | Price | Date_sold
------------ | ------------- | ------------- | ------------- | -------------
100206 | A123 | Rubber Ducky | 2.20 | 2019-09-18
100206 | A123 | Bubble Bath | 8.00 | 2019-09-18
100206 | Q987 | 80-Pack TP | 90.00 | 2019-09-20
100205 | Z001 | Cat Food - Tuna Fish | 10.00 | 2019-08-05
100205 | Z001 | Cat Food - Chicken | 10.00 | 2019-08-05
100205 | Z001 | Cat Food - Beef | 10.00 | 2019-08-05
100205 | Z001 | Cat Food - Kitty quesadilla | 10.00 | 2019-08-05
100204 | X202 | Coffee | 20.00 | 2019-04-29  

How would I select all fields from this table?  
Select * 
From Customers;
  

How many items are in John's cart?  
Select Items_in_cart 
From Customers 
Where Customer_Name = "John Smith";
  

What is the sum of all the cash spent across all customers?  
Select SUM(Cash_spent_to_Date) as SUM_CASH 
From Customers;
  

How many people have items in their cart?  
Select count(1) as Number_of_People_w_items 
From Customers 
where Items_in_cart > 0;
  

How would you join the customer table to the order table?  
You would join them on the unique key. In this case, the unique key is Customer_ID in
both the Customers table and Orders table
  

How would you show which customer ordered which items?  
Select c.Customer_Name, o.Item 
From Customers c 
Left Join Orders o 
On c.Customer_ID = o.Customer_ID;  
  

Using a with statement, how would you show who ordered cat food, and the total amount of money spent?  
with cat_food as ( 
Select Customer_ID, SUM(Price) as TOTAL_PRICE 
From Orders 
Where Item like "%Cat Food%" 
Group by Customer_ID 
) 
Select Customer_name, TOTAL_PRICE 
From Customers c 
Inner JOIN cat_food f 
ON c.Customer_ID = f.Customer_ID 
where c.Customer_ID in (Select Customer_ID from cat_food);  
Although this was a simple statement, the "with" clause really shines when
a complex query needs to be run on a table before joining to another. With statements are nice,
because you create a pseudo temp when running your query, instead of creating a whole new table.  
The Sum of all the purchases of cat food weren't readily available, so we used a with statement to create
the pseudo table to retrieve the sum of the prices spent by each customer, then join the table normally.
  

Which of the following queries would you use?  
```
SELECT count(*)                             SELECT count(*)
FROM shawarma_purchases                     FROM shawarma_purchases
WHERE                               vs.     WHERE
YEAR(purchased_at) == '2017'              purchased_at >= '2017-01-01' AND
purchased_at   
```
SELECT count(*)
FROM shawarma_purchases
WHERE
purchased_at >= '2017-01-01' AND
purchased_at 