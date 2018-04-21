#!/usr/bin/python3
import bs4
import json

filename = "index.html"
output = 'result.json'

f = open(filename,'r')
html = f.read()
f.close()
soup = bs4.BeautifulSoup(html,'lxml')
types = ['rank-up','rank-neutral','rank-down','rank-new']
blocks = [{}]*250
for t in types:
    b = soup.find_all('div',{"class":"item media {}".format(t)})
    for bb in b:
        # first number is current rank, second is difference
        rank = filter(lambda x: bool(x), bb.find('div',{"class":"rank-numbers"}).text.replace(' ','').split('\n'))
        header_raw = bb.find('div',{'class':'col-sm-7 col-lg-8'})
        header = header_raw.find_all('a')
        link = header[0].attrs['href']
        name = header[0].text
        year = header[1].text
        details = header_raw.find('p',{"class": "compact"})
        length_candidates = details.text.split('·')
        length = ''
        for i in length_candidates:
            if 'min' in i:
                length = i.replace(' ','').strip('\n')
        director = details.find('a').text
        cover = 'https://beta.icheckmovies.com{}'.format(bb.find('img',{"class":"movie-cover"}).attrs['src'])
        imdb_link = bb.find('a',{"class":"external"}).attrs['href']
        genres_raw = bb.find('small',{"class":"compact"}).find_all('a')
        genres = []
        for g in genres_raw:
            genres.append(g.text)
        movie_info = {
            'cover': cover,
            'name': name,
            'link': link,
            'imdb_link': imdb_link,
            'genres': genres,
            'year': year,
            'length': length,
            'director': director
            }
        blocks[int(list(rank)[0]) - 1] = movie_info

f = open(output,'w')
f.write(json.dumps(blocks))
f.close()
