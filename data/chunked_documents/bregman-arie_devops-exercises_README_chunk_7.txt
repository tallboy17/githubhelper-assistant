---
repo: bregman-arie/devops-exercises
readme_filename: bregman-arie_devops-exercises_README.md
stars: 76909
forks: 17266
watchers: 76909
contributors_count: 194
license: NOASSERTION
Header 2: Prometheus
---

What is Prometheus? What are some of Prometheus's main features?  
Prometheus is a popular open-source systems monitoring and alerting toolkit, originally developed at SoundCloud. It is designed to collect and store time-series data, and to allow for querying and analysis of that data using a powerful query language called PromQL. Prometheus is frequently used to monitor cloud-native applications, microservices, and other modern infrastructure.  
Some of the main features of Prometheus include:  
1. Data model: Prometheus uses a flexible data model that allows users to organize and label their time-series data in a way that makes sense for their particular use case. Labels are used to identify different dimensions of the data, such as the source of the data or the environment in which it was collected.  
2. Pull-based architecture: Prometheus uses a pull-based model to collect data from targets, meaning that the Prometheus server actively queries its targets for metrics data at regular intervals. This architecture is more scalable and reliable than a push-based model, which would require every target to push data to the server.  
3. Time-series database: Prometheus stores all of its data in a time-series database, which allows users to perform queries over time ranges and to aggregate and analyze their data in various ways. The database is optimized for write-heavy workloads, and can handle a high volume of data with low latency.  
4. Alerting: Prometheus includes a powerful alerting system that allows users to define rules based on their metrics data and to send alerts when certain conditions are met. Alerts can be sent via email, chat, or other channels, and can be customized to include specific details about the problem.  
5. Visualization: Prometheus has a built-in graphing and visualization tool, called PromDash, which allows users to create custom dashboards to monitor their systems and applications. PromDash supports a variety of graph types and visualization options, and can be customized using CSS and JavaScript.  
Overall, Prometheus is a powerful and flexible tool for monitoring and analyzing systems and applications, and is widely used in the industry for cloud-native monitoring and observability.  
  

In what scenarios it might be better to NOT use Prometheus?  
From Prometheus documentation: "if you need 100% accuracy, such as for per-request billing".
  

Describe Prometheus architecture and components  
The Prometheus architecture consists of four major components:  
1. Prometheus Server: The Prometheus server is responsible for collecting and storing metrics data. It has a simple built-in storage layer that allows it to store time-series data in a time-ordered database.  
2. Client Libraries: Prometheus provides a range of client libraries that enable applications to expose their metrics data in a format that can be ingested by the Prometheus server. These libraries are available for a range of programming languages, including Java, Python, and Go.  
3. Exporters: Exporters are software components that expose existing metrics from third-party systems and make them available for ingestion by the Prometheus server. Prometheus provides exporters for a range of popular technologies, including MySQL, PostgreSQL, and Apache.  
4. Alertmanager: The Alertmanager component is responsible for processing alerts generated by the Prometheus server. It can handle alerts from multiple sources and provides a range of features for deduplicating, grouping, and routing alerts to appropriate channels.  
Overall, the Prometheus architecture is designed to be highly scalable and resilient. The server and client libraries can be deployed in a distributed fashion to support monitoring across large-scale, highly dynamic environments
  

Can you compare Prometheus to other solutions like InfluxDB for example?  
Compared to other monitoring solutions, such as InfluxDB, Prometheus is known for its high performance and scalability. It can handle large volumes of data and can easily be integrated with other tools in the monitoring ecosystem. InfluxDB, on the other hand, is known for its ease of use and simplicity. It has a user-friendly interface and provides easy-to-use APIs for collecting and querying data.  
Another popular solution, Nagios, is a more traditional monitoring system that relies on a push-based model for collecting data. Nagios has been around for a long time and is known for its stability and reliability. However, compared to Prometheus, Nagios lacks some of the more advanced features, such as multi-dimensional data model and powerful query language.  
Overall, the choice of a monitoring solution depends on the specific needs and requirements of the organization. While Prometheus is a great choice for large-scale monitoring and alerting, InfluxDB may be a better fit for smaller environments that require ease of use and simplicity. Nagios remains a solid choice for organizations that prioritize stability and reliability over advanced features.
  

What is an Alert?
In Prometheus, an alert is a notification triggered when a specific condition or threshold is met. Alerts can be configured to trigger when certain metrics cross a certain threshold or when specific events occur. Once an alert is triggered, it can be routed to various channels, such as email, pager, or chat, to notify relevant teams or individuals to take appropriate action. Alerts are a critical component of any monitoring system, as they allow teams to proactively detect and respond to issues before they impact users or cause system downtime.
  

What is an Instance? What is a Job?  
In Prometheus, an instance refers to a single target that is being monitored. For example, a single server or service. A job is a set of instances that perform the same function, such as a set of web servers serving the same application. Jobs allow you to define and manage a group of targets together.  
In essence, an instance is an individual target that Prometheus collects metrics from, while a job is a collection of similar instances that can be managed as a group.
  

What core metrics types Prometheus supports?
Prometheus supports several types of metrics, including:  
1. Counter: A monotonically increasing value used for tracking counts of events or samples. Examples include the number of requests processed or the total number of errors encountered.  
2. Gauge: A value that can go up or down, such as CPU usage or memory usage. Unlike counters, gauge values can be arbitrary, meaning they can go up and down based on changes in the system being monitored.  
3. Histogram: A set of observations or events that are divided into buckets based on their value. Histograms help in analyzing the distribution of a metric, such as request latencies or response sizes.  
4. Summary: A summary is similar to a histogram, but instead of buckets, it provides a set of quantiles for the observed values. Summaries are useful for monitoring the distribution of request latencies or response sizes over time.  
Prometheus also supports various functions and operators for aggregating and manipulating metrics, such as sum, max, min, and rate. These features make it a powerful tool for monitoring and alerting on system metrics.
  

What is an exporter? What is it used for?
The exporter serves as a bridge between the third-party system or application and Prometheus, making it possible for Prometheus to monitor and collect data from that system or application.  
The exporter acts as a server, listening on a specific network port for requests from Prometheus to scrape metrics. It collects metrics from the third-party system or application and transforms them into a format that can be understood by Prometheus. The exporter then exposes these metrics to Prometheus via an HTTP endpoint, making them available for collection and analysis.  
Exporters are commonly used to monitor various types of infrastructure components such as databases, web servers, and storage systems. For example, there are exporters available for monitoring popular databases such as MySQL and PostgreSQL, as well as web servers like Apache and Nginx.  
Overall, exporters are a critical component of the Prometheus ecosystem, allowing for the monitoring of a wide range of systems and applications, and providing a high degree of flexibility and extensibility to the platform.
  

Which Prometheus best practices?
Here are three of them:  
1. Label carefully: Careful and consistent labeling of metrics is crucial for effective querying and alerting. Labels should be clear, concise, and include all relevant information about the metric.  
2. Keep metrics simple: The metrics exposed by exporters should be simple and focus on a single aspect of the system being monitored. This helps avoid confusion and ensures that the metrics are easily understandable by all members of the team.  
3. Use alerting sparingly: While alerting is a powerful feature of Prometheus, it should be used sparingly and only for the most critical issues. Setting up too many alerts can lead to alert fatigue and result in important alerts being ignored. It is recommended to set up only the most important alerts and adjust the thresholds over time based on the actual frequency of alerts.
  

How to get total requests in a given period of time?
To get the total requests in a given period of time using Prometheus, you can use the *sum* function along with the *rate* function. Here is an example query that will give you the total number of requests in the last hour:  
```
sum(rate(http_requests_total[1h]))
```
In this query, *http_requests_total* is the name of the metric that tracks the total number of HTTP requests, and the *rate* function calculates the per-second rate of requests over the last hour. The *sum* function then adds up all of the requests to give you the total number of requests in the last hour.  
You can adjust the time range by changing the duration in the *rate* function. For example, if you wanted to get the total number of requests in the last day, you could change the function to *rate(http_requests_total[1d])*.
  

What HA in Prometheus means?  
HA stands for High Availability. This means that the system is designed to be highly reliable and always available, even in the face of failures or other issues. In practice, this typically involves setting up multiple instances of Prometheus and ensuring that they are all synchronized and able to work together seamlessly. This can be achieved through a variety of techniques, such as load balancing, replication, and failover mechanisms. By implementing HA in Prometheus, users can ensure that their monitoring data is always available and up-to-date, even in the face of hardware or software failures, network issues, or other problems that might otherwise cause downtime or data loss.
  

How do you join two metrics?
In Prometheus, joining two metrics can be achieved using the *join()* function. The *join()* function combines two or more time series based on their label values. It takes two mandatory arguments: *on* and *table*. The on argument specifies the labels to join *on* and the *table* argument specifies the time series to join.  
Here's an example of how to join two metrics using the *join()* function:  
```
sum_series(
join(
on(service, instance) request_count_total,
on(service, instance) error_count_total,
)
)
```
In this example, the *join()* function combines the *request_count_total* and *error_count_total* time series based on their *service* and *instance* label values. The *sum_series()* function then calculates the sum of the resulting time series
  

How to write a query that returns the value of a label?
To write a query that returns the value of a label in Prometheus, you can use the *label_values* function. The *label_values* function takes two arguments: the name of the label and the name of the metric.  
For example, if you have a metric called *http_requests_total* with a label called *method*, and you want to return all the values of the *method* label, you can use the following query:  
```
label_values(http_requests_total, method)
```  
This will return a list of all the values for the *method* label in the *http_requests_total* metric. You can then use this list in further queries or to filter your data.
  

How do you convert cpu_user_seconds to cpu usage in percentage?
To convert *cpu_user_seconds* to CPU usage in percentage, you need to divide it by the total elapsed time and the number of CPU cores, and then multiply by 100. The formula is as follows:  
```
100 * sum(rate(process_cpu_user_seconds_total{job=""}[])) by (instance) / ( * )
```  
Here, ** is the name of the job you want to query, ** is the time range you want to query (e.g. *5m*, *1h*), and ** is the number of CPU cores on the machine you are querying.  
For example, to get the CPU usage in percentage for the last 5 minutes for a job named *my-job* running on a machine with 4 CPU cores, you can use the following query:  
```
100 * sum(rate(process_cpu_user_seconds_total{job="my-job"}[5m])) by (instance) / (5m * 4)
```
