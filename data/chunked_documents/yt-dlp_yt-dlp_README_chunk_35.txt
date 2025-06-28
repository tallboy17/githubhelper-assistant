---
repo: yt-dlp/yt-dlp
readme_filename: yt-dlp_yt-dlp_README.md
stars: 116704
forks: 9228
watchers: 116704
contributors_count: 385
license: Unlicense
Header 1: CONFIGURATION
Header 3: Authentication with netrc
---
You may also want to configure automatic credentials storage for extractors that support authentication (by providing login and password with `--username` and `--password`) in order not to pass credentials as command line arguments on every yt-dlp execution and prevent tracking plain text passwords in the shell command history. You can achieve this using a `.netrc` file on a per-extractor basis. For that, you will need to create a `.netrc` file in `--netrc-location` and restrict permissions to read/write by only you:
```
touch ${HOME}/.netrc
chmod a-rwx,u+rw ${HOME}/.netrc
```
After that, you can add credentials for an extractor in the following format, where *extractor* is the name of the extractor in lowercase:
```
machine  login  password 
```
E.g.
```
machine youtube login myaccount@gmail.com password my_youtube_password
machine twitch login my_twitch_account_name password my_twitch_password
```
To activate authentication with the `.netrc` file you should pass `--netrc` to yt-dlp or place it in the configuration file.  
The default location of the .netrc file is `~` (see below).  
As an alternative to using the `.netrc` file, which has the disadvantage of keeping your passwords in a plain text file, you can configure a custom shell command to provide the credentials for an extractor. This is done by providing the `--netrc-cmd` parameter, it shall output the credentials in the netrc format and return `0` on success, other values will be treated as an error. `{}` in the command will be replaced by the name of the extractor to make it possible to select the credentials for the right extractor.  
E.g. To use an encrypted `.netrc` file stored as `.authinfo.gpg`
```
yt-dlp --netrc-cmd 'gpg --decrypt ~/.authinfo.gpg' '
```