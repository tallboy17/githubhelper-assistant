---
repo: yt-dlp/yt-dlp
readme_filename: yt-dlp_yt-dlp_README.md
stars: 116704
forks: 9228
watchers: 116704
contributors_count: 385
license: Unlicense
Header 1: EXTRACTOR ARGUMENTS
---
Some extractors accept additional arguments which can be passed using `--extractor-args KEY:ARGS`. `ARGS` is a `;` (semicolon) separated string of `ARG=VAL1,VAL2`. E.g. `--extractor-args "youtube:player-client=tv,mweb;formats=incomplete" --extractor-args "twitter:api=syndication"`  
Note: In CLI, `ARG` can use `-` instead of `_`; e.g. `youtube:player-client"` becomes `youtube:player_client"`  
The following extractors use this feature:  
#### youtube
* `lang`: Prefer translated metadata (`title`, `description` etc) of this language code (case-sensitive). By default, the video primary language metadata is preferred, with a fallback to `en` translated. See youtube/_base.py for the list of supported content language codes
* `skip`: One or more of `hls`, `dash` or `translated_subs` to skip extraction of the m3u8 manifests, dash manifests and auto-translated subtitles respectively
* `player_client`: Clients to extract video data from. The currently available clients are `web`, `web_safari`, `web_embedded`, `web_music`, `web_creator`, `mweb`, `ios`, `android`, `android_vr`, `tv`, `tv_simply` and `tv_embedded`. By default, `tv,ios,web` is used, or `tv,web` is used when authenticating with cookies. The `web_music` client is added for `music.youtube.com` URLs when logged-in cookies are used. The `web_embedded` client is added for age-restricted videos but only works if the video is embeddable. The `tv_embedded` and `web_creator` clients are added for age-restricted videos if account age-verification is required. Some clients, such as `web` and `web_music`, require a `po_token` for their formats to be downloadable. Some clients, such as `web_creator`, will only work with authentication. Not all clients support authentication via cookies. You can use `default` for the default clients, or you can use `all` for all clients (not recommended). You can prefix a client with `-` to exclude it, e.g. `youtube:player_client=default,-ios`
* `player_skip`: Skip some network requests that are generally needed for robust extraction. One or more of `configs` (skip client configs), `webpage` (skip initial webpage), `js` (skip js player), `initial_data` (skip initial data/next ep request). While these options can help reduce the number of requests needed or avoid some rate-limiting, they could cause issues such as missing formats or metadata.  See #860 and #12826 for more details
* `player_params`: YouTube player parameters to use for player requests. Will overwrite any default ones set by yt-dlp.
* `player_js_variant`: The player javascript variant to use for signature and nsig deciphering. The known variants are: `main`, `tce`, `tv`, `tv_es6`, `phone`, `tablet`. Only `main` is recommended as a possible workaround; the others are for debugging purposes. The default is to use what is prescribed by the site, and can be selected with `actual`
* `comment_sort`: `top` or `new` (default) - choose comment sorting mode (on YouTube's side)
* `max_comments`: Limit the amount of comments to gather. Comma-separated list of integers representing `max-comments,max-parents,max-replies,max-replies-per-thread`. Default is `all,all,all,all`
* E.g. `all,all,1000,10` will get a maximum of 1000 replies total, with up to 10 replies per thread. `1000,all,100` will get a maximum of 1000 comments, with a maximum of 100 replies total
* `formats`: Change the types of formats to return. `dashy` (convert HTTP to DASH), `duplicate` (identical content but different URLs or protocol; includes `dashy`), `incomplete` (cannot be downloaded completely - live dash and post-live m3u8), `missing_pot` (include formats that require a PO Token but are missing one)
* `innertube_host`: Innertube API host to use for all API requests; e.g. `studio.youtube.com`, `youtubei.googleapis.com`. Note that cookies exported from one subdomain will not work on others
* `innertube_key`: Innertube API key to use for all API requests. By default, no API key is used
* `raise_incomplete_data`: `Incomplete Data Received` raises an error instead of reporting a warning
* `data_sync_id`: Overrides the account Data Sync ID used in Innertube API requests. This may be needed if you are using an account with `youtube:player_skip=webpage,configs` or `youtubetab:skip=webpage`
* `visitor_data`: Overrides the Visitor Data used in Innertube API requests. This should be used with `player_skip=webpage,configs` and without cookies. Note: this may have adverse effects if used improperly. If a session from a browser is wanted, you should pass cookies instead (which contain the Visitor ID)
* `po_token`:  Proof of Origin (PO) Token(s) to use. Comma seperated list of PO Tokens in the format `CLIENT.CONTEXT+PO_TOKEN`, e.g. `youtube:po_token=web.gvs+XXX,web.player=XXX,web_safari.gvs+YYY`. Context can be any of `gvs` (Google Video Server URLs), `player` (Innertube player request) or `subs` (Subtitles)
* `pot_trace`: Enable debug logging for PO Token fetching. Either `true` or `false` (default)
* `fetch_pot`: Policy to use for fetching a PO Token from providers. One of `always` (always try fetch a PO Token regardless if the client requires one for the given context), `never` (never fetch a PO Token), or `auto` (default; only fetch a PO Token if the client requires one for the given context)  
#### youtubepot-webpo
* `bind_to_visitor_id`: Whether to use the Visitor ID instead of Visitor Data for caching WebPO tokens. Either `true` (default) or `false`  
#### youtubetab (YouTube playlists, channels, feeds, etc.)
* `skip`: One or more of `webpage` (skip initial webpage download), `authcheck` (allow the download of playlists requiring authentication when no initial webpage is downloaded. This may cause unwanted behavior, see #1122 for more details)
* `approximate_date`: Extract approximate `upload_date` and `timestamp` in flat-playlist. This may cause date-based filters to be slightly off  
#### generic
* `fragment_query`: Passthrough any query in mpd/m3u8 manifest URLs to their fragments if no value is provided, or else apply the query string given as `fragment_query=VALUE`. Note that if the stream has an HLS AES-128 key, then the query parameters will be passed to the key URI as well, unless the `key_query` extractor-arg is passed, or unless an external key URI is provided via the `hls_key` extractor-arg. Does not apply to ffmpeg
* `variant_query`: Passthrough the master m3u8 URL query to its variant playlist URLs if no value is provided, or else apply the query string given as `variant_query=VALUE`
* `key_query`: Passthrough the master m3u8 URL query to its HLS AES-128 decryption key URI if no value is provided, or else apply the query string given as `key_query=VALUE`. Note that this will have no effect if the key URI is provided via the `hls_key` extractor-arg. Does not apply to ffmpeg
* `hls_key`: An HLS AES-128 key URI *or* key (as hex), and optionally the IV (as hex), in the form of `(URI|KEY)[,IV]`; e.g. `generic:hls_key=ABCDEF1234567980,0xFEDCBA0987654321`. Passing any of these values will force usage of the native HLS downloader and override the corresponding values found in the m3u8 playlist
* `is_live`: Bypass live HLS detection and manually set `live_status` - a value of `false` will set `not_live`, any other value (or no value) will set `is_live`
* `impersonate`: Target(s) to try and impersonate with the initial webpage request; e.g. `generic:impersonate=safari,chrome-110`. Use `generic:impersonate` to impersonate any available target, and use `generic:impersonate=false` to disable impersonation (default)  
#### vikichannel
* `video_types`: Types of videos to download - one or more of `episodes`, `movies`, `clips`, `trailers`  
#### youtubewebarchive
* `check_all`: Try to check more at the cost of more requests. One or more of `thumbnails`, `captures`  
#### gamejolt
* `comment_sort`: `hot` (default), `you` (cookies needed), `top`, `new` - choose comment sorting mode (on GameJolt's side)  
#### hotstar
* `res`: resolution to ignore - one or more of `sd`, `hd`, `fhd`
* `vcodec`: vcodec to ignore - one or more of `h264`, `h265`, `dvh265`
* `dr`: dynamic range to ignore - one or more of `sdr`, `hdr10`, `dv`  
#### instagram
* `app_id`: The value of the `X-IG-App-ID` header used for API requests. Default is the web app ID, `936619743392459`  
#### niconicochannelplus
* `max_comments`: Maximum number of comments to extract - default is `120`  
#### tiktok
* `api_hostname`: Hostname to use for mobile API calls, e.g. `api22-normal-c-alisg.tiktokv.com`
* `app_name`: Default app name to use with mobile API calls, e.g. `trill`
* `app_version`: Default app version to use with mobile API calls - should be set along with `manifest_app_version`, e.g. `34.1.2`
* `manifest_app_version`: Default numeric app version to use with mobile API calls, e.g. `2023401020`
* `aid`: Default app ID to use with mobile API calls, e.g. `1180`
* `app_info`: Enable mobile API extraction with one or more app info strings in the format of `/[app_name]/[app_version]/[manifest_app_version]/[aid]`, where `iid` is the unique app install ID. `iid` is the only required value; all other values and their `/` separators can be omitted, e.g. `tiktok:app_info=1234567890123456789` or `tiktok:app_info=123,456/trill///1180,789//34.0.1/340001`
* `device_id`: Enable mobile API extraction with a genuine device ID to be used with mobile API calls. Default is a random 19-digit string  
#### rokfinchannel
* `tab`: Which tab to download - one of `new`, `top`, `videos`, `podcasts`, `streams`, `stacks`  
#### twitter
* `api`: Select one of `graphql` (default), `legacy` or `syndication` as the API for tweet extraction. Has no effect if logged in  
#### stacommu, wrestleuniverse
* `device_id`: UUID value assigned by the website and used to enforce device limits for paid livestream content. Can be found in browser local storage  
#### twitch
* `client_id`: Client ID value to be sent with GraphQL requests, e.g. `twitch:client_id=kimne78kx3ncx6brgo4mv6wki5h1ko`  
#### nhkradirulive (NHK らじる★らじる LIVE)
* `area`: Which regional variation to extract. Valid areas are: `sapporo`, `sendai`, `tokyo`, `nagoya`, `osaka`, `hiroshima`, `matsuyama`, `fukuoka`. Defaults to `tokyo`  
#### nflplusreplay
* `type`: Type(s) of game replays to extract. Valid types are: `full_game`, `full_game_spanish`, `condensed_game` and `all_22`. You can use `all` to extract all available replay types, which is the default  
#### jiocinema
* `refresh_token`: The `refreshToken` UUID from browser local storage can be passed to extend the life of your login session when logging in with `token` as username and the `accessToken` from browser local storage as password  
#### jiosaavn
* `bitrate`: Audio bitrates to request. One or more of `16`, `32`, `64`, `128`, `320`. Default is `128,320`  
#### afreecatvlive
* `cdn`: One or more CDN IDs to use with the API call for stream URLs, e.g. `gcp_cdn`, `gs_cdn_pc_app`, `gs_cdn_mobile_web`, `gs_cdn_pc_web`  
#### soundcloud
* `formats`: Formats to request from the API. Requested values should be in the format of `{protocol}_{codec}`, e.g. `hls_opus,http_aac`. The `*` character functions as a wildcard, e.g. `*_mp3`, and can be passed by itself to request all formats. Known protocols include `http`, `hls` and `hls-aes`; known codecs include `aac`, `opus` and `mp3`. Original `download` formats are always extracted. Default is `http_aac,hls_aac,http_opus,hls_opus,http_mp3,hls_mp3`  
#### orfon (orf:on)
* `prefer_segments_playlist`: Prefer a playlist of program segments instead of a single complete video when available. If individual segments are desired, use `--concat-playlist never --extractor-args "orfon:prefer_segments_playlist"`  
#### bilibili
* `prefer_multi_flv`: Prefer extracting flv formats over mp4 for older videos that still provide legacy formats  
#### sonylivseries
* `sort_order`: Episode sort order for series extraction - one of `asc` (ascending, oldest first) or `desc` (descending, newest first). Default is `asc`  
#### tver
* `backend`: Backend API to use for extraction - one of `streaks` (default) or `brightcove` (deprecated)  
**Note**: These options may be changed/removed in the future without concern for backward compatibility  
