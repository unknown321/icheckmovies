# icheckmovies
parse public list on beta.icheckmovies.com and save it to json

python3, beautifulsoup4

used to parse https://beta.icheckmovies.com/lists/reddit+top+250/?showall=true

output:
```
  {
    "name": "The Great Dictator",
    "link": "/movies/the+great+dictator/",
    "length": "125min",
    "director": "Charles Chaplin",
    "imdb_link": "http://www.imdb.com/title/tt0032553/",
    "cover": "https://beta.icheckmovies.com/var/posters/medium/0/91.jpg",
    "genres": [
      "Drama",
      "Comedy",
      "War"
    ],
    "year": "1940"
  }
```
