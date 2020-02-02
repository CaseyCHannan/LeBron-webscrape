from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import inflect
p = inflect.engine()


def who_next(url, stat ):
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')

    #atags = soup.find_all('a')
    nba_only = soup.find(id="all_nba")
    
    brontag =  nba_only.find(href="/players/j/jamesle01.html")
    # print(brontag)
    bron_outer =brontag.find_parent('tr')
    # print(bron_outer)
    bron_inner = bron_outer.find('td')

    bron_stat_string = bron_outer.find_all('td')[-1].string
    next_up_outer = bron_outer.find_previous_sibling('tr')
    next_up_name = next_up_outer.a.string

    
    if '.' in  bron_stat_string:
        bron_stat = float(bron_outer.find_all('td')[-1].string)
        next_up_stat = float(next_up_outer.contents[-1].string)
        stat_diff = round((next_up_stat - bron_stat + 0.01),2)
    else:
        bron_stat = int(bron_outer.find_all('td')[-1].string)
        next_up_stat = int(next_up_outer.contents[-1].string)
        stat_diff = (next_up_stat - bron_stat + 1) 

    
    bron_place = int(bron_inner.contents[0].rstrip('.')) 
    next_up_ord = p.ordinal(bron_place - 1) #zero-index
    print(f'LeBron James has {bron_stat} career {stat}')
    print(f"he needs {stat_diff} {stat}")
    print(f'to surpass {next_up_name}\'s {next_up_stat} {stat} for {next_up_ord} place all time\n')

    return str(bron_stat)
