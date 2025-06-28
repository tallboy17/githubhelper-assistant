---
repo: donnemartin/system-design-primer
readme_filename: donnemartin_system-design-primer_README.md
stars: 308766
forks: 50890
watchers: 308766
contributors_count: 113
license: NOASSERTION
Header 1: The System Design Primer
Header 2: Availability patterns
Header 3: Availability in numbers
---
Availability is often quantified by uptime (or downtime) as a percentage of time the service is available.  Availability is generally measured in number of 9s--a service with 99.99% availability is described as having four 9s.  
#### 99.9% availability - three 9s  
| Duration            | Acceptable downtime|
|---------------------|--------------------|
| Downtime per year   | 8h 45min 57s       |
| Downtime per month  | 43m 49.7s          |
| Downtime per week   | 10m 4.8s           |
| Downtime per day    | 1m 26.4s           |  
#### 99.99% availability - four 9s  
| Duration            | Acceptable downtime|
|---------------------|--------------------|
| Downtime per year   | 52min 35.7s        |
| Downtime per month  | 4m 23s             |
| Downtime per week   | 1m 5s              |
| Downtime per day    | 8.6s               |  
#### Availability in parallel vs in sequence  
If a service consists of multiple components prone to failure, the service's overall availability depends on whether the components are in sequence or in parallel.  
###### In sequence  
Overall availability decreases when two components with availability < 100% are in sequence:  
```
Availability (Total) = Availability (Foo) * Availability (Bar)
```  
If both `Foo` and `Bar` each had 99.9% availability, their total availability in sequence would be 99.8%.  
###### In parallel  
Overall availability increases when two components with availability < 100% are in parallel:  
```
Availability (Total) = 1 - (1 - Availability (Foo)) * (1 - Availability (Bar))
```  
If both `Foo` and `Bar` each had 99.9% availability, their total availability in parallel would be 99.9999%.