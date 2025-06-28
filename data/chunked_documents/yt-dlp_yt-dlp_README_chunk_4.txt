---
repo: yt-dlp/yt-dlp
readme_filename: yt-dlp_yt-dlp_README.md
stars: 116704
forks: 9228
watchers: 116704
contributors_count: 385
license: Unlicense
Header 1: INSTALLATION
Header 2: UPDATE
---
You can use `yt-dlp -U` to update if you are using the release binaries  
If you installed with pip, simply re-run the same command that was used to install the program  
For other third-party package managers, see the wiki or refer to their documentation  
  
There are currently three release channels for binaries: `stable`, `nightly` and `master`.  
* `stable` is the default channel, and many of its changes have been tested by users of the `nightly` and `master` channels.
* The `nightly` channel has releases scheduled to build every day around midnight UTC, for a snapshot of the project's new patches and changes. This is the **recommended channel for regular users** of yt-dlp. The `nightly` releases are available from yt-dlp/yt-dlp-nightly-builds or as development releases of the `yt-dlp` PyPI package (which can be installed with pip's `--pre` flag).
* The `master` channel features releases that are built after each push to the master branch, and these will have the very latest fixes and additions, but may also be more prone to regressions. They are available from yt-dlp/yt-dlp-master-builds.  
When using `--update`/`-U`, a release binary will only update to its current channel.
`--update-to CHANNEL` can be used to switch to a different channel when a newer version is available. `--update-to [CHANNEL@]TAG` can also be used to upgrade or downgrade to specific tags from a channel.  
You may also use `--update-to ` (`/`) to update to a channel on a completely different repository. Be careful with what repository you are updating to though, there is no verification done for binaries from different repositories.  
Example usage:  
* `yt-dlp --update-to master` switch to the `master` channel and update to its latest release
* `yt-dlp --update-to stable@2023.07.06` upgrade/downgrade to release to `stable` channel tag `2023.07.06`
* `yt-dlp --update-to 2023.10.07` upgrade/downgrade to tag `2023.10.07` if it exists on the current channel
* `yt-dlp --update-to example/yt-dlp@2023.09.24` upgrade/downgrade to the release from the `example/yt-dlp` repository, tag `2023.09.24`  
**Important**: Any user experiencing an issue with the `stable` release should install or update to the `nightly` release before submitting a bug report:
```
# To update to nightly from stable executable/binary:
yt-dlp --update-to nightly

# To install nightly with pip:
python3 -m pip install -U --pre "yt-dlp[default]"
```