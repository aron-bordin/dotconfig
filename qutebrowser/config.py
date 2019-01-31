config.load_autoconfig()

config.source('nord-qutebrowser.py')

c.aliases['json'] = 'spawn --userscript json'
c.aliases['code'] = 'spawn --userscript code'
c.aliases['list-downloads'] = 'spawn --userscript open_download'
c.aliases['youtube-dl'] = 'spawn --userscript youtube-dl'
c.aliases['video'] = 'spawn --userscript play-video'
c.aliases['lyrics'] = 'spawn --userscript lyrics'

c.url.searchengines = {
    "DEFAULT":'https://google.com/search?q={}',
    "w": 'https://pt.wikipedia.org/wiki/={}',
    "W": 'https://pt.wikipedia.org/wiki/={}',
    "f": "https://www.facebook.com/search/top/?q={}&epa=SEARCH_BOX",
    "y": 'https://www.youtube.com/results?search_query={}',
    "l": "https://www.letras.mus.br/?q={}"
}

c.completion.timestamp_format = '%d-%m-%Y'
