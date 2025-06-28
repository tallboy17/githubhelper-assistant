---
repo: nvbn/thefuck
readme_filename: nvbn_thefuck_README.md
stars: 92574
forks: 3717
watchers: 92574
contributors_count: 166
license: MIT
Header 1: The Fuck [![Version][version-badge]][version-link] [![Build Status][workflow-badge]][workflow-link] [![Coverage][coverage-badge]][coverage-link] [![MIT License][license-badge]](LICENSE.md)
Header 2: Creating your own rules
---
To add your own rule, create a file named `your-rule-name.py`
in `~/.config/thefuck/rules`. The rule file must contain two functions:  
```python
match(command: Command) -> bool
get_new_command(command: Command) -> str | list[str]
```  
Additionally, rules can contain optional functions:  
```python
side_effect(old_command: Command, fixed_command: str) -> None
```
Rules can also contain the optional variables `enabled_by_default`, `requires_output` and `priority`.  
`Command` has three attributes: `script`, `output` and `script_parts`.
Your rule should not change `Command`.  
**Rules api changed in 3.0:** To access a rule's settings, import it with
`from thefuck.conf import settings`  
`settings` is a special object assembled from `~/.config/thefuck/settings.py`,
and values from env (see more below).  
A simple example rule for running a script with `sudo`:  
```python
def match(command):
return ('permission denied' in command.output.lower()
or 'EACCES' in command.output)


def get_new_command(command):
return 'sudo {}'.format(command.script)

# Optional:
enabled_by_default = True

def side_effect(command, fixed_command):
subprocess.call('chmod 777 .', shell=True)

priority = 1000  # Lower first, default is 1000

requires_output = True
```  
More examples of rules,
utility functions for rules,
app/os-specific helpers.  
##### Back to Contents