# Autogenerated config.py
#
# NOTE: config.py is intended for advanced users who are comfortable
# with manually migrating the config file on qutebrowser upgrades. If
# you prefer, you can also configure qutebrowser using the
# :set/:bind/:config-* commands without having to write a config.py
# file.
#
# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# Uncomment this to still load settings configured via autoconfig.yml
# config.load_autoconfig()

# Aliases for commands. The keys of the given dictionary are the
# aliases, while the values are the commands they map to.
# Type: Dict
c.aliases = {'code': 'spawn --userscript code', 'json': 'spawn --userscript json', 'list-downloads': 'spawn --userscript open_download', 'lyrics': 'spawn --userscript lyrics', 'pocket': 'open -t https://getpocket.com/edit?url={url}', 'q': 'close', 'qa': 'quit', 'video': 'spawn --userscript play-video', 'w': 'session-save', 'wq': 'quit --save', 'wqa': 'quit --save', 'youtube-dl': 'spawn --userscript youtube-dl'}

# Require a confirmation before quitting the application.
# Type: ConfirmQuit
# Valid values:
#   - always: Always show a confirmation.
#   - multiple-tabs: Show a confirmation if multiple tabs are opened.
#   - downloads: Show a confirmation if downloads are running
#   - never: Never show a confirmation.
c.confirm_quit = ['never']

# Find text on a page incrementally, renewing the search for each typed
# character.
# Type: Bool
c.search.incremental = True

# Which Chromium process model to use. Alternative process models use
# less resources, but decrease security and robustness. See the
# following pages for more details:    -
# https://www.chromium.org/developers/design-documents/process-models
# - https://doc.qt.io/qt-5/qtwebengine-features.html#process-models
# Type: String
# Valid values:
#   - process-per-site-instance: Pages from separate sites are put into separate processes and separate visits to the same site are also isolated.
#   - process-per-site: Pages from separate sites are put into separate processes. Unlike Process per Site Instance, all visits to the same site will share an OS process. The benefit of this model is reduced memory consumption, because more web pages will share processes. The drawbacks include reduced security, robustness, and responsiveness.
#   - single-process: Run all tabs in a single process. This should be used for debugging purposes only, and it disables `:open --private`.
c.qt.process_model = 'process-per-site'

# Time interval (in milliseconds) between auto-saves of
# config/cookies/etc.
# Type: Int
c.auto_save.interval = 10000

# Always restore open sites when qutebrowser is reopened.
# Type: Bool
c.auto_save.session = True

# Which cookies to accept. With QtWebEngine, this setting also controls
# other features with tracking capabilities similar to those of cookies;
# including IndexedDB, DOM storage, filesystem API, service workers, and
# AppCache. Note that with QtWebKit, only `all` and `never` are
# supported as per-domain values. Setting `no-3rdparty` or `no-
# unknown-3rdparty` per-domain on QtWebKit will have the same effect as
# `all`. If this setting is used with URL patterns, the pattern gets
# applied to the origin/first party URL of the page making the request,
# not the request URL.
# Type: String
# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
#   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
#   - never: Don't accept cookies at all.
config.set('content.cookies.accept', 'all', 'chrome-devtools://*')

# Which cookies to accept. With QtWebEngine, this setting also controls
# other features with tracking capabilities similar to those of cookies;
# including IndexedDB, DOM storage, filesystem API, service workers, and
# AppCache. Note that with QtWebKit, only `all` and `never` are
# supported as per-domain values. Setting `no-3rdparty` or `no-
# unknown-3rdparty` per-domain on QtWebKit will have the same effect as
# `all`. If this setting is used with URL patterns, the pattern gets
# applied to the origin/first party URL of the page making the request,
# not the request URL.
# Type: String
# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
#   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
#   - never: Don't accept cookies at all.
config.set('content.cookies.accept', 'all', 'devtools://*')

# Default encoding to use for websites. The encoding must be a string
# describing an encoding such as _utf-8_, _iso-8859-1_, etc.
# Type: String
c.content.default_encoding = 'utf-8'

# Value to send in the `Accept-Language` header. Note that the value
# read from JavaScript is always the global value.
# Type: String
c.content.headers.accept_language = 'en-US,en'

# When to send the Referer header. The Referer header tells websites
# from which website you were coming from when visiting them. No restart
# is needed with QtWebKit.
# Type: String
# Valid values:
#   - always: Always send the Referer.
#   - never: Never send the Referer. This is not recommended, as some sites may break.
#   - same-domain: Only send the Referer for the same domain. This will still protect your privacy, but shouldn't break any sites. With QtWebEngine, the referer will still be sent for other domains, but with stripped path information.
c.content.headers.referer = 'same-domain'

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
c.content.headers.user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}', 'https://web.whatsapp.com/')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0', 'https://accounts.google.com/*')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36', 'https://*.slack.com/*')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0', 'https://docs.google.com/*')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0', 'https://drive.google.com/*')

# Enable host blocking.
# Type: Bool
c.content.host_blocking.enabled = True

# Load images automatically in web pages.
# Type: Bool
config.set('content.images', True, 'chrome-devtools://*')

# Load images automatically in web pages.
# Type: Bool
config.set('content.images', True, 'devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome-devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome://*/*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'qute://*/*')

# Allow locally loaded documents to access remote URLs.
# Type: Bool
c.content.local_content_can_access_remote_urls = True

# Allow websites to record audio/video.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
config.set('content.media_capture', True, 'https://web.whatsapp.com')

# Allow websites to record audio/video.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
config.set('content.media_capture', True, 'https://whereby.com')

# Allow websites to show notifications.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
config.set('content.notifications', True, 'https://calendar.google.com')

# Allow websites to show notifications.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
config.set('content.notifications', True, 'https://web.whatsapp.com')

# Allow websites to show notifications.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
config.set('content.notifications', True, 'https://www.buscape.com.br')

# Allow websites to show notifications.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
config.set('content.notifications', True, 'https://www.youtube.com')

# Allow pdf.js to view PDF files in the browser. Note that the files can
# still be downloaded by clicking the download button in the pdf.js
# viewer.
# Type: Bool
c.content.pdfjs = True

# Enable plugins in Web pages.
# Type: Bool
c.content.plugins = True

# Allow websites to register protocol handlers via
# `navigator.registerProtocolHandler`.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
config.set('content.register_protocol_handler', True, 'https://*.google.com/*')

# Allow websites to register protocol handlers via
# `navigator.registerProtocolHandler`.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
config.set('content.register_protocol_handler', True, 'https://*.gooogle.com/*')

# List of user stylesheet filenames to use.
# Type: List of File, or File
c.content.user_stylesheets = 'custom.css'

# Number of commands to save in the command history. 0: no history / -1:
# unlimited
# Type: Int
c.completion.cmd_history_max_items = 1000

# Format of timestamps (e.g. for the history completion). See
# https://sqlite.org/lang_datefunc.html for allowed substitutions.
# Type: String
c.completion.timestamp_format = '%d-%m-%Y'

# A list of patterns which should not be shown in the history. This only
# affects the completion. Matching URLs are still saved in the history
# (and visible on the qute://history page), but hidden in the
# completion. Changing this setting will cause the completion history to
# be regenerated on the next start, which will take a short while.
# Type: List of UrlPattern
c.completion.web_history.exclude = ['https://*.google.com/+']

# Number of URLs to show in the web history. 0: no history / -1:
# unlimited
# Type: Int
c.completion.web_history.max_items = 10000

# Execute the best-matching command on a partial match.
# Type: Bool
c.completion.use_best_match = True

# Directory to save downloads to. If unset, a sensible OS-specific
# default is used.
# Type: Directory
c.downloads.location.directory = '/home/aron/Downloads'

# Prompt the user for the download location. If set to false,
# `downloads.location.directory` will be used.
# Type: Bool
c.downloads.location.prompt = True

# Which categories to show (in which order) in the :open completion.
# Type: FlagList
# Valid values:
#   - searchengines
#   - quickmarks
#   - bookmarks
#   - history
c.completion.open_categories = ['history', 'searchengines', 'quickmarks', 'bookmarks']

# Editor (and arguments) to use for the `open-editor` command. The
# following placeholders are defined:  * `{file}`: Filename of the file
# to be edited. * `{line}`: Line in which the caret is found in the
# text. * `{column}`: Column in which the caret is found in the text. *
# `{line0}`: Same as `{line}`, but starting from index 0. * `{column0}`:
# Same as `{column}`, but starting from index 0.
# Type: ShellCommand
c.editor.command = ['vim-termitef', '{file}']

# Comma-separated list of regular expressions to use for 'next' links.
# Type: List of Regex
c.hints.next_regexes = ['\\bnext\\b', '\\bproximo\\b', '\\bpróximo\\b', '\\bmais\\b', '\\bcontinuar\\b', '\\bmore\\b', '\\bnewer\\b', '\\b[>→≫]\\b', '\\b(>>|»)\\b', '\\bcontinue\\b']

# Comma-separated list of regular expressions to use for 'prev' links.
# Type: List of Regex
c.hints.prev_regexes = ['\\bprev(ious)?\\b', '\\bback\\b', '\\bolder\\b', '\\b[<←≪]\\b', '\\b(<<|«)\\b', '\\banterior\\b', '\\bvoltar\\b']

# Make characters in hint strings uppercase.
# Type: Bool
c.hints.uppercase = True

# Automatically enter insert mode if an editable element is focused
# after loading the page.
# Type: Bool
c.input.insert_mode.auto_load = True

# Enable smooth scrolling for web pages. Note smooth scrolling does not
# work with the `:scroll-px` command.
# Type: Bool
c.scrolling.smooth = False

# Languages to use for spell checking. You can check for available
# languages and install dictionaries using scripts/dictcli.py. Run the
# script with -h/--help for instructions.
# Type: List of String
# Valid values:
#   - af-ZA: Afrikaans (South Africa)
#   - bg-BG: Bulgarian (Bulgaria)
#   - ca-ES: Catalan (Spain)
#   - cs-CZ: Czech (Czech Republic)
#   - da-DK: Danish (Denmark)
#   - de-DE: German (Germany)
#   - el-GR: Greek (Greece)
#   - en-AU: English (Australia)
#   - en-CA: English (Canada)
#   - en-GB: English (United Kingdom)
#   - en-US: English (United States)
#   - es-ES: Spanish (Spain)
#   - et-EE: Estonian (Estonia)
#   - fa-IR: Farsi (Iran)
#   - fo-FO: Faroese (Faroe Islands)
#   - fr-FR: French (France)
#   - he-IL: Hebrew (Israel)
#   - hi-IN: Hindi (India)
#   - hr-HR: Croatian (Croatia)
#   - hu-HU: Hungarian (Hungary)
#   - id-ID: Indonesian (Indonesia)
#   - it-IT: Italian (Italy)
#   - ko: Korean
#   - lt-LT: Lithuanian (Lithuania)
#   - lv-LV: Latvian (Latvia)
#   - nb-NO: Norwegian (Norway)
#   - nl-NL: Dutch (Netherlands)
#   - pl-PL: Polish (Poland)
#   - pt-BR: Portuguese (Brazil)
#   - pt-PT: Portuguese (Portugal)
#   - ro-RO: Romanian (Romania)
#   - ru-RU: Russian (Russia)
#   - sh: Serbo-Croatian
#   - sk-SK: Slovak (Slovakia)
#   - sl-SI: Slovenian (Slovenia)
#   - sq: Albanian
#   - sr: Serbian
#   - sv-SE: Swedish (Sweden)
#   - ta-IN: Tamil (India)
#   - tg-TG: Tajik (Tajikistan)
#   - tr-TR: Turkish (Turkey)
#   - uk-UA: Ukrainian (Ukraine)
#   - vi-VN: Vietnamese (Viet Nam)
c.spellcheck.languages = ['pt-BR']

# When to show the statusbar.
# Type: String
# Valid values:
#   - always: Always show the statusbar.
#   - never: Always hide the statusbar.
#   - in-mode: Show the statusbar when in modes other than normal mode.
c.statusbar.show = 'always'

# Padding (in pixels) for the statusbar.
# Type: Padding
c.statusbar.padding = {'bottom': 0, 'left': 0, 'right': 0, 'top': 0}

# Position of the status bar.
# Type: VerticalPosition
# Valid values:
#   - top
#   - bottom
c.statusbar.position = 'bottom'

# List of widgets displayed in the statusbar.
# Type: List of String
# Valid values:
#   - url: Current page URL.
#   - scroll: Percentage of the current page position like `10%`.
#   - scroll_raw: Raw percentage of the current page position like `10`.
#   - history: Display an arrow when possible to go back/forward in history.
#   - tabs: Current active tab, e.g. `2`.
#   - keypress: Display pressed keys when composing a vi command.
#   - progress: Progress bar for the current page loading.
c.statusbar.widgets = ['keypress', 'url', 'scroll', 'history', 'progress']

# Open new tabs (middleclick/ctrl+click) in the background.
# Type: Bool
c.tabs.background = True

# Mouse button with which to close tabs.
# Type: String
# Valid values:
#   - right: Close tabs on right-click.
#   - middle: Close tabs on middle-click.
#   - none: Don't close tabs using the mouse.
c.tabs.close_mouse_button = 'middle'

# Position of new tabs opened from another tab. See
# `tabs.new_position.stacking` for controlling stacking behavior.
# Type: NewTabPosition
# Valid values:
#   - prev: Before the current tab.
#   - next: After the current tab.
#   - first: At the beginning.
#   - last: At the end.
c.tabs.new_position.related = 'last'

# Position of the tab bar.
# Type: Position
# Valid values:
#   - top
#   - bottom
#   - left
#   - right
c.tabs.position = 'top'

# Which tab to select when the focused tab is removed.
# Type: SelectOnRemove
# Valid values:
#   - prev: Select the tab which came before the closed one (left in horizontal, above in vertical).
#   - next: Select the tab which came after the closed one (right in horizontal, below in vertical).
#   - last-used: Select the previously selected tab.
c.tabs.select_on_remove = 'next'

# When to show the tab bar.
# Type: String
# Valid values:
#   - always: Always show the tab bar.
#   - never: Always hide the tab bar.
#   - multiple: Hide the tab bar if only one tab is open.
#   - switching: Show the tab bar when switching tabs.
c.tabs.show = 'multiple'

# Format to use for the tab title. The following placeholders are
# defined:  * `{perc}`: Percentage as a string like `[10%]`. *
# `{perc_raw}`: Raw percentage, e.g. `10`. * `{current_title}`: Title of
# the current web page. * `{title_sep}`: The string ` - ` if a title is
# set, empty otherwise. * `{index}`: Index of this tab. * `{id}`:
# Internal tab ID of this tab. * `{scroll_pos}`: Page scroll position. *
# `{host}`: Host of the current web page. * `{backend}`: Either
# ''webkit'' or ''webengine'' * `{private}`: Indicates when private mode
# is enabled. * `{current_url}`: URL of the current web page. *
# `{protocol}`: Protocol (http/https/...) of the current web page. *
# `{audio}`: Indicator for audio/mute status.
# Type: FormatString
c.tabs.title.format = '{audio}{index}: {current_title} {perc}'

# Width (in pixels or as percentage of the window) of the tab bar if
# it's vertical.
# Type: PercOrInt
c.tabs.width = '25%'

# Width (in pixels) of the progress indicator (0 to disable).
# Type: Int
c.tabs.indicator.width = 3

# Shrink pinned tabs down to their contents.
# Type: Bool
c.tabs.pinned.shrink = True

# Page to open if :open -t/-b/-w is used without URL. Use `about:blank`
# for a blank page.
# Type: FuzzyUrl
c.url.default_page = 'https://google.com'

# Open base URL of the searchengine if a searchengine shortcut is
# invoked without parameters.
# Type: Bool
c.url.open_base_url = False

# Search engines which can be used via the address bar.  Maps a search
# engine name (such as `DEFAULT`, or `ddg`) to a URL with a `{}`
# placeholder. The placeholder will be replaced by the search term, use
# `{{` and `}}` for literal `{`/`}` braces.  The following further
# placeholds are defined to configure how special characters in the
# search terms are replaced by safe characters (called 'quoting'):  *
# `{}` and `{semiquoted}` quote everything except slashes; this is the
# most   sensible choice for almost all search engines (for the search
# term   `slash/and&amp` this placeholder expands to `slash/and%26amp`).
# * `{quoted}` quotes all characters (for `slash/and&amp` this
# placeholder   expands to `slash%2Fand%26amp`). * `{unquoted}` quotes
# nothing (for `slash/and&amp` this placeholder   expands to
# `slash/and&amp`).  The search engine named `DEFAULT` is used when
# `url.auto_search` is turned on and something else than a URL was
# entered to be opened. Other search engines can be used by prepending
# the search engine name to the search term, e.g. `:open google
# qutebrowser`.
# Type: Dict
c.url.searchengines = {'DEFAULT': 'https://google.com/search?q={}', 'w': 'https://pt.wikipedia.org/wiki/={}', 'W': 'https://pt.wikipedia.org/wiki/={}', 'f': 'https://www.facebook.com/search/top/?q={}&epa=SEARCH_BOX', 'y': 'https://www.youtube.com/results?search_query={}', 'l': 'https://www.letras.mus.br/?q={}'}

# Page(s) to open at the start.
# Type: List of FuzzyUrl, or FuzzyUrl
c.url.start_pages = 'https://google.com'

# Format to use for the window title. The same placeholders like for
# `tabs.title.format` are defined.
# Type: FormatString
c.window.title_format = '{perc}{current_title}{title_sep}'

# Text color of the completion widget. May be a single color to use for
# all columns or a list of three colors, one for each column.
# Type: List of QtColor, or QtColor
c.colors.completion.fg = '#d8dee9'

# Background color of the completion widget for odd rows.
# Type: QssColor
c.colors.completion.odd.bg = '#3b4252'

# Background color of the completion widget for even rows.
# Type: QssColor
c.colors.completion.even.bg = '#3b4252'

# Foreground color of completion widget category headers.
# Type: QtColor
c.colors.completion.category.fg = '#e5e9f0'

# Background color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.bg = '#2e3440'

# Top border color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.border.top = '#2e3440'

# Bottom border color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.border.bottom = '#2e3440'

# Foreground color of the selected completion item.
# Type: QtColor
c.colors.completion.item.selected.fg = '#eceff4'

# Background color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.bg = '#4c566a'

# Top border color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.border.top = '#4c566a'

# Bottom border color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.border.bottom = '#4c566a'

# Foreground color of the matched text in the completion.
# Type: QtColor
c.colors.completion.match.fg = '#ebcb8b'

# Color of the scrollbar handle in the completion view.
# Type: QssColor
c.colors.completion.scrollbar.fg = '#e5e9f0'

# Color of the scrollbar in the completion view.
# Type: QssColor
c.colors.completion.scrollbar.bg = '#3b4252'

# Background color for the download bar.
# Type: QssColor
c.colors.downloads.bar.bg = '#2e3440'

# Color gradient stop for download backgrounds.
# Type: QtColor
c.colors.downloads.stop.bg = '#b48ead'

# Color gradient interpolation system for download backgrounds.
# Type: ColorSystem
# Valid values:
#   - rgb: Interpolate in the RGB color system.
#   - hsv: Interpolate in the HSV color system.
#   - hsl: Interpolate in the HSL color system.
#   - none: Don't show a gradient.
c.colors.downloads.system.bg = 'none'

# Foreground color for downloads with errors.
# Type: QtColor
c.colors.downloads.error.fg = '#e5e9f0'

# Background color for downloads with errors.
# Type: QtColor
c.colors.downloads.error.bg = '#bf616a'

# Font color for hints.
# Type: QssColor
c.colors.hints.fg = '#2e3440'

# Background color for hints. Note that you can use a `rgba(...)` value
# for transparency.
# Type: QssColor
c.colors.hints.bg = '#ebcb8b'

# Font color for the matched part of hints.
# Type: QtColor
c.colors.hints.match.fg = '#5e81ac'

# Text color for the keyhint widget.
# Type: QssColor
c.colors.keyhint.fg = '#e5e9f0'

# Highlight color for keys to complete the current keychain.
# Type: QssColor
c.colors.keyhint.suffix.fg = '#ebcb8b'

# Background color of the keyhint widget.
# Type: QssColor
c.colors.keyhint.bg = '#3b4252'

# Foreground color of an error message.
# Type: QssColor
c.colors.messages.error.fg = '#e5e9f0'

# Background color of an error message.
# Type: QssColor
c.colors.messages.error.bg = '#bf616a'

# Border color of an error message.
# Type: QssColor
c.colors.messages.error.border = '#bf616a'

# Foreground color of a warning message.
# Type: QssColor
c.colors.messages.warning.fg = '#e5e9f0'

# Background color of a warning message.
# Type: QssColor
c.colors.messages.warning.bg = '#d08770'

# Border color of a warning message.
# Type: QssColor
c.colors.messages.warning.border = '#d08770'

# Foreground color of an info message.
# Type: QssColor
c.colors.messages.info.fg = '#e5e9f0'

# Background color of an info message.
# Type: QssColor
c.colors.messages.info.bg = '#88c0d0'

# Border color of an info message.
# Type: QssColor
c.colors.messages.info.border = '#88c0d0'

# Foreground color for prompts.
# Type: QssColor
c.colors.prompts.fg = '#e5e9f0'

# Border used around UI elements in prompts.
# Type: String
c.colors.prompts.border = '1px solid #2e3440'

# Background color for prompts.
# Type: QssColor
c.colors.prompts.bg = '#434c5e'

# Background color for the selected item in filename prompts.
# Type: QssColor
c.colors.prompts.selected.bg = '#4c566a'

# Foreground color of the statusbar.
# Type: QssColor
c.colors.statusbar.normal.fg = '#e5e9f0'

# Background color of the statusbar.
# Type: QssColor
c.colors.statusbar.normal.bg = '#2e3440'

# Foreground color of the statusbar in insert mode.
# Type: QssColor
c.colors.statusbar.insert.fg = '#3b4252'

# Background color of the statusbar in insert mode.
# Type: QssColor
c.colors.statusbar.insert.bg = '#a3be8c'

# Foreground color of the statusbar in passthrough mode.
# Type: QssColor
c.colors.statusbar.passthrough.fg = '#e5e9f0'

# Background color of the statusbar in passthrough mode.
# Type: QssColor
c.colors.statusbar.passthrough.bg = '#5e81ac'

# Foreground color of the statusbar in private browsing mode.
# Type: QssColor
c.colors.statusbar.private.fg = '#e5e9f0'

# Background color of the statusbar in private browsing mode.
# Type: QssColor
c.colors.statusbar.private.bg = '#4c566a'

# Foreground color of the statusbar in command mode.
# Type: QssColor
c.colors.statusbar.command.fg = '#e5e9f0'

# Background color of the statusbar in command mode.
# Type: QssColor
c.colors.statusbar.command.bg = '#434c5e'

# Foreground color of the statusbar in private browsing + command mode.
# Type: QssColor
c.colors.statusbar.command.private.fg = '#e5e9f0'

# Background color of the statusbar in private browsing + command mode.
# Type: QssColor
c.colors.statusbar.command.private.bg = '#434c5e'

# Foreground color of the statusbar in caret mode.
# Type: QssColor
c.colors.statusbar.caret.fg = '#e5e9f0'

# Background color of the statusbar in caret mode.
# Type: QssColor
c.colors.statusbar.caret.bg = '#b48ead'

# Foreground color of the statusbar in caret mode with a selection.
# Type: QssColor
c.colors.statusbar.caret.selection.fg = '#e5e9f0'

# Background color of the statusbar in caret mode with a selection.
# Type: QssColor
c.colors.statusbar.caret.selection.bg = '#b48ead'

# Background color of the progress bar.
# Type: QssColor
c.colors.statusbar.progress.bg = '#e5e9f0'

# Default foreground color of the URL in the statusbar.
# Type: QssColor
c.colors.statusbar.url.fg = '#e5e9f0'

# Foreground color of the URL in the statusbar on error.
# Type: QssColor
c.colors.statusbar.url.error.fg = '#bf616a'

# Foreground color of the URL in the statusbar for hovered links.
# Type: QssColor
c.colors.statusbar.url.hover.fg = '#88c0d0'

# Foreground color of the URL in the statusbar on successful load
# (http).
# Type: QssColor
c.colors.statusbar.url.success.http.fg = '#e5e9f0'

# Foreground color of the URL in the statusbar on successful load
# (https).
# Type: QssColor
c.colors.statusbar.url.success.https.fg = '#a3be8c'

# Foreground color of the URL in the statusbar when there's a warning.
# Type: QssColor
c.colors.statusbar.url.warn.fg = '#d08770'

# Background color of the tab bar.
# Type: QssColor
c.colors.tabs.bar.bg = '#4c566a'

# Color for the tab indicator on errors.
# Type: QtColor
c.colors.tabs.indicator.error = '#bf616a'

# Color gradient interpolation system for the tab indicator.
# Type: ColorSystem
# Valid values:
#   - rgb: Interpolate in the RGB color system.
#   - hsv: Interpolate in the HSV color system.
#   - hsl: Interpolate in the HSL color system.
#   - none: Don't show a gradient.
c.colors.tabs.indicator.system = 'none'

# Foreground color of unselected odd tabs.
# Type: QtColor
c.colors.tabs.odd.fg = '#e5e9f0'

# Background color of unselected odd tabs.
# Type: QtColor
c.colors.tabs.odd.bg = '#4c566a'

# Foreground color of unselected even tabs.
# Type: QtColor
c.colors.tabs.even.fg = '#e5e9f0'

# Background color of unselected even tabs.
# Type: QtColor
c.colors.tabs.even.bg = '#4c566a'

# Foreground color of selected odd tabs.
# Type: QtColor
c.colors.tabs.selected.odd.fg = '#e5e9f0'

# Background color of selected odd tabs.
# Type: QtColor
c.colors.tabs.selected.odd.bg = '#2e3440'

# Foreground color of selected even tabs.
# Type: QtColor
c.colors.tabs.selected.even.fg = '#e5e9f0'

# Background color of selected even tabs.
# Type: QtColor
c.colors.tabs.selected.even.bg = '#2e3440'

# Default font families to use. Whenever "default_family" is used in a
# font setting, it's replaced with the fonts listed here. If set to an
# empty value, a system-specific monospace default is used.
# Type: List of Font, or Font
c.fonts.default_family = ['Venetian 301', 'Hack Nerd Font Mono']

# Font used in the completion widget.
# Type: Font
c.fonts.completion.entry = '10pt "Hack Nerd Font Mono"'

# Font used in the completion categories.
# Type: Font
c.fonts.completion.category = 'bold 10pt "Hack Nerd Font Mono"'

# Font used for the debugging console.
# Type: Font
c.fonts.debug_console = '10pt "Hack Nerd Font Mono"'

# Font used for the downloadbar.
# Type: Font
c.fonts.downloads = '10pt "Hack Nerd Font Mono"'

# Font used for the hints.
# Type: Font
c.fonts.hints = 'bold 10pt "Hack Nerd Font Mono"'

# Font used in the keyhint widget.
# Type: Font
c.fonts.keyhint = '10pt "Hack Nerd Font Mono"'

# Font used for error messages.
# Type: Font
c.fonts.messages.error = '10pt "Hack Nerd Font Mono"'

# Font used for info messages.
# Type: Font
c.fonts.messages.info = '10pt "Hack Nerd Font Mono"'

# Font used for warning messages.
# Type: Font
c.fonts.messages.warning = '10pt "Hack Nerd Font Mono"'

# Font used for prompts.
# Type: Font
c.fonts.prompts = '10pt "Hack Nerd Font Mono"'

# Font used in the statusbar.
# Type: Font
c.fonts.statusbar = '10pt "Hack Nerd Font Mono"'

# Font used for selected tabs.
# Type: Font
c.fonts.tabs.selected = '10pt "Hack Nerd Font Mono"'

# Font used for unselected tabs.
# Type: Font
c.fonts.tabs.unselected = '10pt "Hack Nerd Font Mono"'

# Font family for standard fonts.
# Type: FontFamily
c.fonts.web.family.standard = '"Hack Nerd"'

# Font family for fixed fonts.
# Type: FontFamily
c.fonts.web.family.fixed = '"Hack Nerd"'

# Font family for serif fonts.
# Type: FontFamily
c.fonts.web.family.serif = '"Hack Nerd"'

# Font family for sans-serif fonts.
# Type: FontFamily
c.fonts.web.family.sans_serif = '"Hack Nerd"'

# Font family for cursive fonts.
# Type: FontFamily
c.fonts.web.family.cursive = '"Hack Nerd"'

# Font family for fantasy fonts.
# Type: FontFamily
c.fonts.web.family.fantasy = '"Hack Nerd"'

# Default font size (in pixels) for regular text.
# Type: Int
c.fonts.web.size.default = 16

# Hard minimum font size (in pixels).
# Type: Int
c.fonts.web.size.minimum = 6

# This setting can be used to map keys to other keys. When the key used
# as dictionary-key is pressed, the binding for the key used as
# dictionary-value is invoked instead. This is useful for global
# remappings of keys, for example to map Ctrl-[ to Escape. Note that
# when a key is bound (via `bindings.default` or `bindings.commands`),
# the mapping is ignored.
# Type: Dict
c.bindings.key_mappings = {'<Ctrl+6>': '<Ctrl+^>', '<Ctrl+Enter>': '<Ctrl+Return>', '<Ctrl+j>': '<Return>', '<Ctrl+m>': '<Return>', '<Ctrl+[>': '<Escape>', '<Enter>': '<Return>', '<Shift+Enter>': '<Return>', '<Shift+Return>': '<Return>'}

# Bindings for normal mode
config.bind(',A', 'set content.headers.user_agent "Googlebot/2.1 (+http://www.google.com/bot.html)";; reload')
config.bind(',F', 'open --tab {primary}')
config.bind(',H', 'open -t https://google.com')
config.bind(',O', 'spawn --userscript history --tab')
config.bind(',V', 'video')
config.bind(',a', 'set content.headers.user_agent "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36";; reload')
config.bind(',c', 'code')
config.bind(',f', 'open {primary}')
config.bind(',h', 'open https://via.hypothes.is/{url}')
config.bind(',j', 'json')
config.bind(',l', 'lyrics')
config.bind(',o', 'spawn --userscript history')
config.bind(',p', 'pocket')
config.bind(',s', 'set-cmd-text :buffer 0')
config.bind(',t', 'open --tab https://translate.google.com/#auto/nl/{primary}')
config.bind(',v', 'hint links run video {hint-url}')
config.bind(',yd', 'spawn --userscript youtube-dl')
config.bind('J', 'tab-prev')
config.bind('K', 'tab-next')
config.bind(',b', 'spawn --userscript qute-bitwarden')
