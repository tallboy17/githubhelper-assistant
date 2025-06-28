---
repo: bregman-arie/devops-exercises
readme_filename: bregman-arie_devops-exercises_README.md
stars: 76909
forks: 17266
watchers: 76909
contributors_count: 194
license: NOASSERTION
Header 2: Mongo
---

What are the advantages of MongoDB? Or in other words, why choosing MongoDB and not other implementation of NoSQL?  
MongoDB advantages are as following:
- Schemaless
- Easy to scale-out
- No complex joins
- Structure of a single object is clear  
  

What is the difference between SQL and NoSQL?  
The main difference is that SQL databases are structured (data is stored in the form of
tables with rows and columns - like an excel spreadsheet table) while NoSQL is
unstructured, and the data storage can vary depending on how the NoSQL DB is set up, such
as key-value pair, document-oriented, etc.
  

In what scenarios would you prefer to use NoSQL/Mongo over SQL?  
* Heterogeneous data which changes often
* Data consistency and integrity is not top priority
* Best if the database needs to scale rapidly
  

What is a document? What is a collection?  
* A document is a record in MongoDB, which is stored in BSON (Binary JSON) format and is the basic unit of data in MongoDB.
* A collection is a group of related documents stored in a single database in MongoDB.
  

What is an aggregator?  
* An aggregator is a framework in MongoDB that performs operations on a set of data to return a single computed result.
  

What is better? Embedded documents or referenced?  
* There is no definitive answer to which is better, it depends on the specific use case and requirements. Some explanations : Embedded documents provide atomic updates, while referenced documents allow for better normalization.
  

Have you performed data retrieval optimizations in Mongo? If not, can you think about ways to optimize a slow data retrieval?  
* Some ways to optimize data retrieval in MongoDB are: indexing, proper schema design, query optimization and database load balancing.
  
##### Queries  

Explain this query: db.books.find({"name": /abc/})
  

Explain this query: db.books.find().sort({x:1})
  

What is the difference between find() and find_one()?  
* `find()` returns all documents that match the query conditions.
* find_one() returns only one document that matches the query conditions (or null if no match is found).
  

How can you export data from Mongo DB?  
* mongoexport
* programming languages
