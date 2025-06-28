---
repo: bregman-arie/devops-exercises
readme_filename: bregman-arie_devops-exercises_README.md
stars: 76909
forks: 17266
watchers: 76909
contributors_count: 194
license: NOASSERTION
Header 2: Regex
---
Given a text file, perform the following exercises  
#### Extract  

Extract all the numbers  
- "\d+"
  

Extract the first word of each line  
- "^\w+"
Bonus: extract the last word of each line  
- "\w+(?=\W*$)" (in most cases, depends on line formatting)
  

Extract all the IP addresses  
- "\b(?:\d{1,3}\ .){3}\d{1,3}\b" IPV4:(This format looks for 1 to 3 digit sequence 3 times)
  

Extract dates in the format of yyyy-mm-dd or yyyy-dd-mm
  

Extract email addresses  
- "\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\ .[A-Za-z]{2,}\b"
  
#### Replace  

Replace tabs with four spaces
  

Replace 'red' with 'green'
