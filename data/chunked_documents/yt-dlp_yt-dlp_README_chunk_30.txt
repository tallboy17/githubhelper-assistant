---
repo: yt-dlp/yt-dlp
readme_filename: yt-dlp_yt-dlp_README.md
stars: 116704
forks: 9228
watchers: 116704
contributors_count: 385
license: Unlicense
Header 1: USAGE AND OPTIONS
Header 2: SponsorBlock Options:
---
Make chapter entries for, or remove various segments (sponsor,
introductions, etc.) from downloaded YouTube videos using the
SponsorBlock API  
--sponsorblock-mark CATS        SponsorBlock categories to create chapters
for, separated by commas. Available
categories are sponsor, intro, outro,
selfpromo, preview, filler, interaction,
music_offtopic, poi_highlight, chapter, all
and default (=all). You can prefix the
category with a "-" to exclude it. See [1]
for descriptions of the categories. E.g.
--sponsorblock-mark all,-preview
[1] 
--sponsorblock-remove CATS      SponsorBlock categories to be removed from
the video file, separated by commas. If a
category is present in both mark and remove,
remove takes precedence. The syntax and
available categories are the same as for
--sponsorblock-mark except that "default"
refers to "all,-filler" and poi_highlight,
chapter are not available
--sponsorblock-chapter-title TEMPLATE
An output template for the title of the
SponsorBlock chapters created by
--sponsorblock-mark. The only available
fields are start_time, end_time, category,
categories, name, category_names. Defaults
to "[SponsorBlock]: %(category_names)l"
--no-sponsorblock               Disable both --sponsorblock-mark and
--sponsorblock-remove
--sponsorblock-api URL          SponsorBlock API location, defaults to
