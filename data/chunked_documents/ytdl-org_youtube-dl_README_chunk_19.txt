---
repo: ytdl-org/youtube-dl
readme_filename: ytdl-org_youtube-dl_README.md
stars: 136243
forks: 10379
watchers: 136243
contributors_count: 388
license: Unlicense
Header 1: CONFIGURATION
Header 3: Authentication with `.netrc` file
---
You may also want to configure automatic credentials storage for extractors that support authentication (by providing login and password with `--username` and `--password`) in order not to pass credentials as command line arguments on every youtube-dl execution and prevent tracking plain text passwords in the shell command history. You can achieve this using a `.netrc` file on a per extractor basis. For that you will need to create a `.netrc` file in your `$HOME` and restrict permissions to read/write by only you:
```
touch $HOME/.netrc
chmod a-rwx,u+rw $HOME/.netrc
```
After that you can add credentials for an extractor in the following format, where *extractor* is the name of the extractor in lowercase:
```
machine  login  password 
```
For example:
```
machine youtube login myaccount@gmail.com password my_youtube_password
machine twitch login my_twitch_account_name password my_twitch_password
```
To activate authentication with the `.netrc` file you should pass `--netrc` to youtube-dl or place it in the configuration file.  
On Windows you may also need to setup the `%HOME%` environment variable manually. For example:
```
set HOME=%USERPROFILE%
```