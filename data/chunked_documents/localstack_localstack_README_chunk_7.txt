---
repo: localstack/localstack
readme_filename: localstack_localstack_README.md
stars: 59419
forks: 4177
watchers: 59419
contributors_count: 426
license: NOASSERTION
Header 1: Overview
Header 2: Quickstart
---
Start LocalStack inside a Docker container by running:  
```bash
% localstack start -d

__                     _______ __             __
/ /   ____  _________ _/ / ___// /_____ ______/ /__
/ /   / __ \/ ___/ __ `/ /\__ \/ __/ __ `/ ___/ //_/
/ /___/ /_/ / /__/ /_/ / /___/ / /_/ /_/ / /__/ ,<
/_____/\____/\___/\__,_/_//____/\__/\__,_/\___/_/|_|

- LocalStack CLI: 4.5.0
- Profile: default
- App: 

[17:00:15] starting LocalStack in Docker mode 🐳               localstack.py:512
preparing environment                               bootstrap.py:1322
configuring container                               bootstrap.py:1330
starting container                                  bootstrap.py:1340
[17:00:16] detaching                                           bootstrap.py:1344
```  
You can query the status of respective services on LocalStack by running:  
```bash
% localstack status services
┏━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┓
┃ Service                  ┃ Status      ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━┩
│ acm                      │ ✔ available │
│ apigateway               │ ✔ available │
│ cloudformation           │ ✔ available │
│ cloudwatch               │ ✔ available │
│ config                   │ ✔ available │
│ dynamodb                 │ ✔ available │
...
```  
To use SQS, a fully managed distributed message queuing service, on LocalStack, run:  
```shell
% awslocal sqs create-queue --queue-name sample-queue
{
"QueueUrl": "
}
```  
Learn more about LocalStack AWS services and using them with LocalStack's `awslocal` CLI.