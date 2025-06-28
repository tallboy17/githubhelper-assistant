---
repo: nvbn/thefuck
readme_filename: nvbn_thefuck_README.md
stars: 92574
forks: 3717
watchers: 92574
contributors_count: 166
license: MIT
Header 1: The Fuck [![Version][version-badge]][version-link] [![Build Status][workflow-badge]][workflow-link] [![Coverage][coverage-badge]][coverage-link] [![MIT License][license-badge]](LICENSE.md)
Header 2: How it works
---
*The Fuck* attempts to match the previous command with a rule. If a match is
found, a new command is created using the matched rule and executed. The
following rules are enabled by default:  
* `adb_unknown_command` &ndash; fixes misspelled commands like `adb logcta`;
* `ag_literal` &ndash; adds `-Q` to `ag` when suggested;
* `aws_cli` &ndash; fixes misspelled commands like `aws dynamdb scan`;
* `az_cli` &ndash; fixes misspelled commands like `az providers`;
* `cargo` &ndash; runs `cargo build` instead of `cargo`;
* `cargo_no_command` &ndash; fixes wrong commands like `cargo buid`;
* `cat_dir` &ndash; replaces `cat` with `ls` when you try to `cat` a directory;
* `cd_correction` &ndash; spellchecks and corrects failed cd commands;
* `cd_cs` &ndash; changes `cs` to `cd`;
* `cd_mkdir` &ndash; creates directories before cd'ing into them;
* `cd_parent` &ndash; changes `cd..` to `cd ..`;
* `chmod_x` &ndash; adds execution bit;
* `choco_install` &ndash; appends common suffixes for chocolatey packages;
* `composer_not_command` &ndash; fixes composer command name;
* `conda_mistype` &ndash; fixes conda commands;
* `cp_create_destination` &ndash; creates a new directory when you attempt to `cp` or `mv` to a non-existent one
* `cp_omitting_directory` &ndash; adds `-a` when you `cp` directory;
* `cpp11` &ndash; adds missing `-std=c++11` to `g++` or `clang++`;
* `dirty_untar` &ndash; fixes `tar x` command that untarred in the current directory;
* `dirty_unzip` &ndash; fixes `unzip` command that unzipped in the current directory;
* `django_south_ghost` &ndash; adds `--delete-ghost-migrations` to failed because ghosts django south migration;
* `django_south_merge` &ndash; adds `--merge` to inconsistent django south migration;
* `docker_login` &ndash; executes a `docker login` and repeats the previous command;
* `docker_not_command` &ndash; fixes wrong docker commands like `docker tags`;
* `docker_image_being_used_by_container` &dash; removes the container that is using the image before removing the image;
* `dry` &ndash; fixes repetitions like `git git push`;
* `fab_command_not_found` &ndash; fixes misspelled fabric commands;
* `fix_alt_space` &ndash; replaces Alt+Space with Space character;
* `fix_file` &ndash; opens a file with an error in your `$EDITOR`;
* `gem_unknown_command` &ndash; fixes wrong `gem` commands;
* `git_add` &ndash; fixes *"pathspec 'foo' did not match any file(s) known to git."*;
* `git_add_force` &ndash; adds `--force` to `git add ...` when paths are .gitignore'd;
* `git_bisect_usage` &ndash; fixes `git bisect strt`, `git bisect goood`, `git bisect rset`, etc. when bisecting;
* `git_branch_delete` &ndash; changes `git branch -d` to `git branch -D`;
* `git_branch_delete_checked_out` &ndash; changes `git branch -d` to `git checkout master && git branch -D` when trying to delete a checked out branch;
* `git_branch_exists` &ndash; offers `git branch -d foo`, `git branch -D foo` or `git checkout foo` when creating a branch that already exists;
* `git_branch_list` &ndash; catches `git branch list` in place of `git branch` and removes created branch;
* `git_branch_0flag` &ndash; fixes commands such as `git branch 0v` and `git branch 0r` removing the created branch;
* `git_checkout` &ndash; fixes branch name or creates new branch;
* `git_clone_git_clone` &ndash; replaces `git clone git clone ...` with `git clone ...`
* `git_clone_missing` &ndash; adds `git clone` to URLs that appear to link to a git repository.
* `git_commit_add` &ndash; offers `git commit -a ...` or `git commit -p ...` after previous commit if it failed because nothing was staged;
* `git_commit_amend` &ndash; offers `git commit --amend` after previous commit;
* `git_commit_reset` &ndash; offers `git reset HEAD~` after previous commit;
* `git_diff_no_index` &ndash; adds `--no-index` to previous `git diff` on untracked files;
* `git_diff_staged` &ndash; adds `--staged` to previous `git diff` with unexpected output;
* `git_fix_stash` &ndash; fixes `git stash` commands (misspelled subcommand and missing `save`);
* `git_flag_after_filename` &ndash; fixes `fatal: bad flag '...' after filename`
* `git_help_aliased` &ndash; fixes `git help ` commands replacing  with the aliased command;
* `git_hook_bypass` &ndash; adds `--no-verify` flag previous to `git am`, `git commit`, or `git push` command;
* `git_lfs_mistype` &ndash; fixes mistyped `git lfs ` commands;
* `git_main_master` &ndash; fixes incorrect branch name between `main` and `master`
* `git_merge` &ndash; adds remote to branch names;
* `git_merge_unrelated` &ndash; adds `--allow-unrelated-histories` when required
* `git_not_command` &ndash; fixes wrong git commands like `git brnch`;
* `git_pull` &ndash; sets upstream before executing previous `git pull`;
* `git_pull_clone` &ndash; clones instead of pulling when the repo does not exist;
* `git_pull_uncommitted_changes` &ndash; stashes changes before pulling and pops them afterwards;
* `git_push` &ndash; adds `--set-upstream origin $branch` to previous failed `git push`;
* `git_push_different_branch_names` &ndash; fixes pushes when local branch name does not match remote branch name;
* `git_push_pull` &ndash; runs `git pull` when `push` was rejected;
* `git_push_without_commits` &ndash; creates an initial commit if you forget and only `git add .`, when setting up a new project;
* `git_rebase_no_changes` &ndash; runs `git rebase --skip` instead of `git rebase --continue` when there are no changes;
* `git_remote_delete` &ndash; replaces `git remote delete remote_name` with `git remote remove remote_name`;
* `git_rm_local_modifications` &ndash; adds `-f` or `--cached` when you try to `rm` a locally modified file;
* `git_rm_recursive` &ndash; adds `-r` when you try to `rm` a directory;
* `git_rm_staged` &ndash;  adds `-f` or `--cached` when you try to `rm` a file with staged changes
* `git_rebase_merge_dir` &ndash; offers `git rebase (--continue | --abort | --skip)` or removing the `.git/rebase-merge` dir when a rebase is in progress;
* `git_remote_seturl_add` &ndash; runs `git remote add` when `git remote set_url` on nonexistent remote;
* `git_stash` &ndash; stashes your local modifications before rebasing or switching branch;
* `git_stash_pop` &ndash; adds your local modifications before popping stash, then resets;
* `git_tag_force` &ndash; adds `--force` to `git tag ` when the tag already exists;
* `git_two_dashes` &ndash; adds a missing dash to commands like `git commit -amend` or `git rebase -continue`;
* `go_run` &ndash; appends `.go` extension when compiling/running Go programs;
* `go_unknown_command` &ndash; fixes wrong `go` commands, for example `go bulid`;
* `gradle_no_task` &ndash; fixes not found or ambiguous `gradle` task;
* `gradle_wrapper` &ndash; replaces `gradle` with `./gradlew`;
* `grep_arguments_order` &ndash; fixes `grep` arguments order for situations like `grep -lir . test`;
* `grep_recursive` &ndash; adds `-r` when you try to `grep` directory;
* `grunt_task_not_found` &ndash; fixes misspelled `grunt` commands;
* `gulp_not_task` &ndash; fixes misspelled `gulp` tasks;
* `has_exists_script` &ndash; prepends `./` when script/binary exists;
* `heroku_multiple_apps` &ndash; adds `--app ` to `heroku` commands like `heroku pg`;
* `heroku_not_command` &ndash; fixes wrong `heroku` commands like `heroku log`;
* `history` &ndash; tries to replace command with the most similar command from history;
* `hostscli` &ndash; tries to fix `hostscli` usage;
* `ifconfig_device_not_found` &ndash; fixes wrong device names like `wlan0` to `wlp2s0`;
* `java` &ndash; removes `.java` extension when running Java programs;
* `javac` &ndash; appends missing `.java` when compiling Java files;
* `lein_not_task` &ndash; fixes wrong `lein` tasks like `lein rpl`;
* `long_form_help` &ndash; changes `-h` to `--help` when the short form version is not supported
* `ln_no_hard_link` &ndash; catches hard link creation on directories, suggest symbolic link;
* `ln_s_order` &ndash; fixes `ln -s` arguments order;
* `ls_all` &ndash; adds `-A` to `ls` when output is empty;
* `ls_lah` &ndash; adds `-lah` to `ls`;
* `man` &ndash; changes manual section;
* `man_no_space` &ndash; fixes man commands without spaces, for example `mandiff`;
* `mercurial` &ndash; fixes wrong `hg` commands;
* `missing_space_before_subcommand` &ndash; fixes command with missing space like `npminstall`;
* `mkdir_p` &ndash; adds `-p` when you try to create a directory without a parent;
* `mvn_no_command` &ndash; adds `clean package` to `mvn`;
* `mvn_unknown_lifecycle_phase` &ndash; fixes misspelled life cycle phases with `mvn`;
* `npm_missing_script` &ndash; fixes `npm` custom script name in `npm run-script `;
* `npm_run_script` &ndash; adds missing `run-script` for custom `npm` scripts;
* `npm_wrong_command` &ndash; fixes wrong npm commands like `npm urgrade`;
* `no_command` &ndash; fixes wrong console commands, for example `vom/vim`;
* `no_such_file` &ndash; creates missing directories with `mv` and `cp` commands;
* `omnienv_no_such_command` &ndash; fixes wrong commands for `goenv`, `nodenv`, `pyenv` and `rbenv` (eg.: `pyenv isntall` or `goenv list`);
* `open` &ndash; either prepends ` to address passed to `open` or creates a new file or directory and passes it to `open`;
* `pip_install` &ndash; fixes permission issues with `pip install` commands by adding `--user` or prepending `sudo` if necessary;
* `pip_unknown_command` &ndash; fixes wrong `pip` commands, for example `pip instatl/pip install`;
* `php_s` &ndash; replaces `-s` by `-S` when trying to run a local php server;
* `port_already_in_use` &ndash; kills process that bound port;
* `prove_recursively` &ndash; adds `-r` when called with directory;
* `python_command` &ndash; prepends `python` when you try to run non-executable/without `./` python script;
* `python_execute` &ndash; appends missing `.py` when executing Python files;
* `python_module_error` &ndash; fixes ModuleNotFoundError by trying to `pip install` that module;
* `quotation_marks` &ndash; fixes uneven usage of `'` and `"` when containing args';
* `path_from_history` &ndash; replaces not found path with a similar absolute path from history;
* `rails_migrations_pending` &ndash; runs pending migrations;
* `react_native_command_unrecognized` &ndash; fixes unrecognized `react-native` commands;
* `remove_shell_prompt_literal` &ndash; removes leading shell prompt symbol `$`, common when copying commands from documentations;
* `remove_trailing_cedilla` &ndash; removes trailing cedillas `ç`, a common typo for European keyboard layouts;
* `rm_dir` &ndash; adds `-rf` when you try to remove a directory;
* `scm_correction` &ndash; corrects wrong scm like `hg log` to `git log`;
* `sed_unterminated_s` &ndash; adds missing '/' to `sed`'s `s` commands;
* `sl_ls` &ndash; changes `sl` to `ls`;
* `ssh_known_hosts` &ndash; removes host from `known_hosts` on warning;
* `sudo` &ndash; prepends `sudo` to the previous command if it failed because of permissions;
* `sudo_command_from_user_path` &ndash; runs commands from users `$PATH` with `sudo`;
* `switch_lang` &ndash; switches command from your local layout to en;
* `systemctl` &ndash; correctly orders parameters of confusing `systemctl`;
* `terraform_init.py` &ndash; runs `terraform init` before plan or apply;
* `terraform_no_command.py` &ndash; fixes unrecognized `terraform` commands;
* `test.py` &ndash; runs `pytest` instead of `test.py`;
* `touch` &ndash; creates missing directories before "touching";
* `tsuru_login` &ndash; runs `tsuru login` if not authenticated or session expired;
* `tsuru_not_command` &ndash; fixes wrong `tsuru` commands like `tsuru shell`;
* `tmux` &ndash; fixes `tmux` commands;
* `unknown_command` &ndash; fixes hadoop hdfs-style "unknown command", for example adds missing '-' to the command on `hdfs dfs ls`;
* `unsudo` &ndash; removes `sudo` from previous command if a process refuses to run on superuser privilege.
* `vagrant_up` &ndash; starts up the vagrant instance;
* `whois` &ndash; fixes `whois` command;
* `workon_doesnt_exists` &ndash; fixes `virtualenvwrapper` env name os suggests to create new.
* `wrong_hyphen_before_subcommand` &ndash; removes an improperly placed hyphen (`apt-install` -> `apt install`, `git-log` -> `git log`, etc.)
* `yarn_alias` &ndash; fixes aliased `yarn` commands like `yarn ls`;
* `yarn_command_not_found` &ndash; fixes misspelled `yarn` commands;
* `yarn_command_replaced` &ndash; fixes replaced `yarn` commands;
* `yarn_help` &ndash; makes it easier to open `yarn` documentation;  
##### Back to Contents  
The following rules are enabled by default on specific platforms only:  
* `apt_get` &ndash; installs app from apt if it not installed (requires `python-commandnotfound` / `python3-commandnotfound`);
* `apt_get_search` &ndash; changes trying to search using `apt-get` with searching using `apt-cache`;
* `apt_invalid_operation` &ndash; fixes invalid `apt` and `apt-get` calls, like `apt-get isntall vim`;
* `apt_list_upgradable` &ndash; helps you run `apt list --upgradable` after `apt update`;
* `apt_upgrade` &ndash; helps you run `apt upgrade` after `apt list --upgradable`;
* `brew_cask_dependency` &ndash; installs cask dependencies;
* `brew_install` &ndash; fixes formula name for `brew install`;
* `brew_reinstall` &ndash; turns `brew install ` into `brew reinstall `;
* `brew_link` &ndash; adds `--overwrite --dry-run` if linking fails;
* `brew_uninstall` &ndash; adds `--force` to `brew uninstall` if multiple versions were installed;
* `brew_unknown_command` &ndash; fixes wrong brew commands, for example `brew docto/brew doctor`;
* `brew_update_formula` &ndash; turns `brew update ` into `brew upgrade `;
* `dnf_no_such_command` &ndash; fixes mistyped DNF commands;
* `nixos_cmd_not_found` &ndash; installs apps on NixOS;
* `pacman` &ndash; installs app with `pacman` if it is not installed (uses `yay`, `pikaur` or `yaourt` if available);
* `pacman_invalid_option` &ndash; replaces lowercase `pacman` options with uppercase.
* `pacman_not_found` &ndash; fixes package name with `pacman`, `yay`, `pikaur` or `yaourt`.
* `yum_invalid_operation` &ndash; fixes invalid `yum` calls, like `yum isntall vim`;  
The following commands are bundled with *The Fuck*, but are not enabled by
default:  
* `git_push_force` &ndash; adds `--force-with-lease` to a `git push` (may conflict with `git_push_pull`);
* `rm_root` &ndash; adds `--no-preserve-root` to `rm -rf /` command.  
##### Back to Contents