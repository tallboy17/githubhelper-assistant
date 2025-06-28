---
repo: bregman-arie/devops-exercises
readme_filename: bregman-arie_devops-exercises_README.md
stars: 76909
forks: 17266
watchers: 76909
contributors_count: 194
license: NOASSERTION
Header 2: Elastic
---

What is the Elastic Stack?  
The Elastic Stack consists of:  
* Elasticsearch
* Kibana
* Logstash
* Beats
* Elastic Hadoop
* APM Server  
Elasticsearch, Logstash and Kibana are also known as the ELK stack.
  

Explain what is Elasticsearch  
From the official docs:  
"Elasticsearch is a distributed document store. Instead of storing information as rows of columnar data, Elasticsearch stores complex data structures that have been serialized as JSON documents"
  

What is Logstash?  
From the blog:  
"Logstash is a powerful, flexible pipeline that collects, enriches and transports data. It works as an extract, transform & load (ETL) tool for collecting log messages."
  

Explain what beats are  
Beats are lightweight data shippers. These data shippers installed on the client where the data resides.
Examples of beats: Filebeat, Metricbeat, Auditbeat. There are much more.
  

What is Kibana?  
From the official docs:  
"Kibana is an open source analytics and visualization platform designed to work with Elasticsearch. You use Kibana to search, view, and interact with data stored in Elasticsearch indices. You can easily perform advanced data analysis and visualize your data in a variety of charts, tables, and maps."
  

Describe what happens from the moment an app logged some information until it's displayed to the user in a dashboard when the Elastic stack is used  
The process may vary based on the chosen architecture and the processing you may want to apply to the logs. One possible workflow is:  
1. The data logged by the application is picked by filebeat and sent to logstash
2. Logstash process the log based on the defined filters. Once done, the output is sent to Elasticsearch
2. Elasticsearch stores the document it got and the document is indexed for quick future access
4. The user creates visualizations in Kibana which based on the indexed data
5. The user creates a dashboard which composed out of the visualization created in the previous step
  
##### Elasticsearch  

What is a data node?  
This is where data is stored and also where different processing takes place (e.g. when you search for a data).
  

What is a master node?  
Part of a master node responsibilities:
* Track the status of all the nodes in the cluster
* Verify replicas are working and the data is available from every data node.
* No hot nodes (no data node that works much harder than other nodes)  
While there can be multiple master nodes in reality only of them is the elected master node.
  

What is an ingest node?  
A node which responsible for processing the data according to ingest pipeline. In case you don't need to use
logstash then this node can receive data from beats and process it, similarly to how it can be processed
in Logstash.
  

What is Coordinating only node?  
From the official docs:  
Coordinating only nodes can benefit large clusters by offloading the coordinating node role from data and master-eligible nodes. They join the cluster and receive the full cluster state, like every other node, and they use the cluster state to route requests directly to the appropriate place(s).  
  

How data is stored in Elasticsearch?  
* Data is stored in an index
* The index is spread across the cluster using shards
  

What is an Index?  
Index in Elasticsearch is in most cases compared to a whole database from the SQL/NoSQL world.
You can choose to have one index to hold all the data of your app or have multiple indices where each index holds different type of your app (e.g. index for each service your app is running).  
The official docs also offer a great explanation (in general, it's really good documentation, as every project should have):  
"An index can be thought of as an optimized collection of documents and each document is a collection of fields, which are the key-value pairs that contain your data"
  

Explain Shards  
An index is split into shards and documents are hashed to a particular shard. Each shard may be on a different node in a cluster and each one of the shards is a self contained index.
This allows Elasticsearch to scale to an entire cluster of servers.
  

What is an Inverted Index?  
From the official docs:  
"An inverted index lists every unique word that appears in any document and identifies all of the documents each word occurs in."
  

What is a Document?  
Continuing with the comparison to SQL/NoSQL a Document in Elasticsearch is a row in table in the case of SQL or a document in a collection in the case of NoSQL.
As in NoSQL a document is a JSON object which holds data on a unit in your app. What is this unit depends on the your app. If your app related to book then each document describes a book. If you are app is about shirts then each document is a shirt.
  

You check the health of your elasticsearch cluster and it's red. What does it mean? What can cause the status to be yellow instead of green?  
Red means some data is unavailable in your cluster. Some shards of your indices are unassigned.
There are some other states for the cluster.
Yellow means that you have unassigned shards in the cluster. You can be in this state if you have single node and your indices have replicas.
Green means that all shards in the cluster are assigned to nodes and your cluster is healthy.
  

True or False? Elasticsearch indexes all data in every field and each indexed field has the same data structure for unified and quick query ability  
False.
From the official docs:  
"Each indexed field has a dedicated, optimized data structure. For example, text fields are stored in inverted indices, and numeric and geo fields are stored in BKD trees."
  

What reserved fields a document has?  
* _index
* _id
* _type
  

Explain Mapping
  

What are the advantages of defining your own mapping? (or: when would you use your own mapping?)  
* You can optimize fields for partial matching
* You can define custom formats of known fields (e.g. date)
* You can perform language-specific analysis
  

Explain Replicas  
In a network/cloud environment where failures can be expected any time, it is very useful and highly recommended to have a failover mechanism in case a shard/node somehow goes offline or disappears for whatever reason.
To this end, Elasticsearch allows you to make one or more copies of your index’s shards into what are called replica shards, or replicas for short.
  

Can you explain Term Frequency & Document Frequency?  
Term Frequency is how often a term appears in a given document and Document Frequency is how often a term appears in all documents. They both are used for determining the relevance of a term by calculating Term Frequency / Document Frequency.
  

You check "Current Phase" under "Index lifecycle management" and you see it's set to "hot". What does it mean?  
"The index is actively being written to".
More about the phases here
  

What this command does? curl -X PUT "localhost:9200/customer/_doc/1?pretty" -H 'Content-Type: application/json' -d'{ "name": "John Doe" }'  
It creates customer index if it doesn't exists and adds a new document with the field name which is set to "John Dow". Also, if it's the first document it will get the ID 1.
  

What will happen if you run the previous command twice? What about running it 100 times?  
1. If name value was different then it would update "name" to the new value
2. In any case, it bumps version field by one
  

What is the Bulk API? What would you use it for?  
Bulk API is used when you need to index multiple documents. For high number of documents it would be significantly faster to use rather than individual requests since there are less network roundtrips.
  
##### Query DSL  

Explain Elasticsearch query syntax (Booleans, Fields, Ranges)
  

Explain what is Relevance Score
  

Explain Query Context and Filter Context  
From the official docs:  
"In the query context, a query clause answers the question “How well does this document match this query clause?” Besides deciding whether or not the document matches, the query clause also calculates a relevance score in the _score meta-field."  
"In a filter context, a query clause answers the question “Does this document match this query clause?” The answer is a simple Yes or No—no scores are calculated. Filter context is mostly used for filtering structured data"
  

Describe how would an architecture of production environment with large amounts of data would be different from a small-scale environment  
There are several possible answers for this question. One of them is as follows:  
A small-scale architecture of elastic will consist of the elastic stack as it is. This means we will have beats, logstash, elastcsearch and kibana.
A production environment with large amounts of data can include some kind of buffering component (e.g. Reddis or RabbitMQ) and also security component such as Nginx.
  
##### Logstash  

What are Logstash plugins? What plugins types are there?  
* Input Plugins - how to collect data from different sources
* Filter Plugins - processing data
* Output Plugins - push data to different outputs/services/platforms
  

What is grok?  
A logstash plugin which modifies information in one format and immerse it in another.
  

How grok works?
  

What grok patterns are you familiar with?
  

What is `_grokparsefailure?`
  

How do you test or debug grok patterns?
  

What are Logstash Codecs? What codecs are there?
  
##### Kibana  

What can you find under "Discover" in Kibana?  
The raw data as it is stored in the index. You can search and filter it.
  

You see in Kibana, after clicking on Discover, "561 hits". What does it mean?  
Total number of documents matching the search results. If not query used then simply the total number of documents.
  

What can you find under "Visualize"?  
"Visualize" is where you can create visual representations for your data (pie charts, graphs, ...)
  

What visualization types are supported/included in Kibana?
  

What visualization type would you use for statistical outliers
  

Describe in detail how do you create a dashboard in Kibana
  
#### Filebeat  

What is Filebeat?  
Filebeat is used to monitor the logging directories inside of VMs or mounted as a sidecar if exporting logs from containers, and then forward these logs onward for further processing, usually to logstash.
  

If one is using ELK, is it a must to also use filebeat? In what scenarios it's useful to use filebeat?  
Filebeat is a typical component of the ELK stack, since it was developed by Elastic to work with the other products (Logstash and Kibana). It's possible to send logs directly to logstash, though this often requires coding changes for the application. Particularly for legacy applications with little test coverage, it might be a better option to use filebeat, since you don't need to make any changes to the application code.
  

What is a harvester?  
Read here
  

True or False? a single harvester harvest multiple files, according to the limits set in filebeat.yml  
False. One harvester harvests one file.
  

What are filebeat modules?  
These are pre-configured modules for specific types of logging locations (eg, Traefik, Fargate, HAProxy) to make it easy to configure forwarding logs using filebeat. They have different configurations based on where you're collecting logs from.
  
#### Elastic Stack  

How do you secure an Elastic Stack?  
You can generate certificates with the provided elastic utils and change configuration to enable security using certificates model.
