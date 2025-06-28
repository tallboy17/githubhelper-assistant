---
repo: nvbn/thefuck
readme_filename: nvbn_thefuck_README.md
stars: 92574
forks: 3717
watchers: 92574
contributors_count: 166
license: MIT
Header 1: The Fuck [![Version][version-badge]][version-link] [![Build Status][workflow-badge]][workflow-link] [![Coverage][coverage-badge]][coverage-link] [![MIT License][license-badge]](LICENSE.md)
Header 2: Settings
---
Several *The Fuck* parameters can be changed in the file `$XDG_CONFIG_HOME/thefuck/settings.py`
(`$XDG_CONFIG_HOME` defaults to `~/.config`):  
* `rules` &ndash; list of enabled rules, by default `thefuck.const.DEFAULT_RULES`;
* `exclude_rules` &ndash; list of disabled rules, by default `[]`;
* `require_confirmation` &ndash; requires confirmation before running new command, by default `True`;
* `wait_command` &ndash; the max amount of time in seconds for getting previous command output;
* `no_colors` &ndash; disable colored output;
* `priority` &ndash; dict with rules priorities, rule with lower `priority` will be matched first;
* `debug` &ndash; enables debug output, by default `False`;
* `history_limit` &ndash; the numeric value of how many history commands will be scanned, like `2000`;
* `alter_history` &ndash; push fixed command to history, by default `True`;
* `wait_slow_command` &ndash; max amount of time in seconds for getting previous command output if it in `slow_commands` list;
* `slow_commands` &ndash; list of slow commands;
* `num_close_matches` &ndash; the maximum number of close matches to suggest, by default `3`.
* `excluded_search_path_prefixes` &ndash; path prefixes to ignore when searching for commands, by default `[]`.  
An example of `settings.py`:  
```python
rules = ['sudo', 'no_command']
exclude_rules = ['git_push']
require_confirmation = True
wait_command = 10
no_colors = False
priority = {'sudo': 100, 'no_command': 9999}
debug = False
history_limit = 9999
wait_slow_command = 20
slow_commands = ['react-native', 'gradle']
num_close_matches = 5
```  
Or via environment variables:  
* `THEFUCK_RULES` &ndash; list of enabled rules, like `DEFAULT_RULES:rm_root` or `sudo:no_command`;
* `THEFUCK_EXCLUDE_RULES` &ndash; list of disabled rules, like `git_pull:git_push`;
* `THEFUCK_REQUIRE_CONFIRMATION` &ndash; require confirmation before running new command, `true/false`;
* `THEFUCK_WAIT_COMMAND` &ndash; the max amount of time in seconds for getting previous command output;
* `THEFUCK_NO_COLORS` &ndash; disable colored output, `true/false`;
* `THEFUCK_PRIORITY` &ndash; priority of the rules, like `no_command=9999:apt_get=100`,
rule with lower `priority` will be matched first;
* `THEFUCK_DEBUG` &ndash; enables debug output, `true/false`;
* `THEFUCK_HISTORY_LIMIT` &ndash; how many history commands will be scanned, like `2000`;
* `THEFUCK_ALTER_HISTORY` &ndash; push fixed command to history `true/false`;
* `THEFUCK_WAIT_SLOW_COMMAND` &ndash; the max amount of time in seconds for getting previous command output if it in `slow_commands` list;
* `THEFUCK_SLOW_COMMANDS` &ndash; list of slow commands, like `lein:gradle`;
* `THEFUCK_NUM_CLOSE_MATCHES` &ndash; the maximum number of close matches to suggest, like `5`.
* `THEFUCK_EXCLUDED_SEARCH_PATH_PREFIXES` &ndash; path prefixes to ignore when searching for commands, by default `[]`.  
For example:  
```bash
export THEFUCK_RULES='sudo:no_command'
export THEFUCK_EXCLUDE_RULES='git_pull:git_push'
export THEFUCK_REQUIRE_CONFIRMATION='true'
export THEFUCK_WAIT_COMMAND=10
export THEFUCK_NO_COLORS='false'
export THEFUCK_PRIORITY='no_command=9999:apt_get=100'
export THEFUCK_HISTORY_LIMIT='2000'
export THEFUCK_NUM_CLOSE_MATCHES='5'
```  
##### Back to Contents