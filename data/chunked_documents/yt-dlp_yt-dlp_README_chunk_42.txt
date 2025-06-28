---
repo: yt-dlp/yt-dlp
readme_filename: yt-dlp_yt-dlp_README.md
stars: 116704
forks: 9228
watchers: 116704
contributors_count: 385
license: Unlicense
Header 1: MODIFYING METADATA
---
The metadata obtained by the extractors can be modified by using `--parse-metadata` and `--replace-in-metadata`  
`--replace-in-metadata FIELDS REGEX REPLACE` is used to replace text in any metadata field using Python regular expression. Backreferences can be used in the replace string for advanced use.  
The general syntax of `--parse-metadata FROM:TO` is to give the name of a field or an output template to extract data from, and the format to interpret it as, separated by a colon `:`. Either a Python regular expression with named capture groups, a single field name, or a similar syntax to the output template (only `%(field)s` formatting is supported) can be used for `TO`. The option can be used multiple times to parse and modify various fields.  
Note that these options preserve their relative order, allowing replacements to be made in parsed fields and vice versa. Also, any field thus created can be used in the output template and will also affect the media file's metadata added when using `--embed-metadata`.  
This option also has a few special uses:  
* You can download an additional URL based on the metadata of the currently downloaded video. To do this, set the field `additional_urls` to the URL that you want to download. E.g. `--parse-metadata "description:(?Phttps?://www\.vimeo\.com/\d+)"` will download the first vimeo video found in the description  
* You can use this to change the metadata that is embedded in the media file. To do this, set the value of the corresponding field with a `meta_` prefix. For example, any value you set to `meta_description` field will be added to the `description` field in the file - you can use this to set a different "description" and "synopsis". To modify the metadata of individual streams, use the `meta_` prefix (e.g. `meta1_language`). Any value set to the `meta_` field will overwrite all default values.  
**Note**: Metadata modification happens before format selection, post-extraction and other post-processing operations. Some fields may be added or changed during these steps, overriding your changes.  
For reference, these are the fields yt-dlp adds by default to the file metadata:  
Metadata fields            | From
:--------------------------|:------------------------------------------------
`title`                    | `track` or `title`
`date`                     | `upload_date`
`description`,  `synopsis` | `description`
`purl`, `comment`          | `webpage_url`
`track`                    | `track_number`
`artist`                   | `artist`, `artists`, `creator`, `creators`, `uploader` or `uploader_id`
`composer`                 | `composer` or `composers`
`genre`                    | `genre` or `genres`
`album`                    | `album`
`album_artist`             | `album_artist` or `album_artists`
`disc`                     | `disc_number`
`show`                     | `series`
`season_number`            | `season_number`
`episode_id`               | `episode` or `episode_id`
`episode_sort`             | `episode_number`
`language` of each stream  | the format's `language`  
**Note**: The file format may not support some of these fields