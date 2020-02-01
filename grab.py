from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# URL pages we will scraping (see image above)

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
    bron_stat = bron_outer.find_all('td')[-1].string
    print(f'I am {bron_outer.a.string}')
    print(f'I have {bron_stat} {stat}\n')

    next_up_outer = bron_outer.find_previous_sibling('tr')
    next_up_name = next_up_outer.a.string
    next_up_stat = next_up_outer.contents[-1].string
    print(f'I am {next_up_name}')
    print(f'i have {next_up_stat} {stat} \n')

    #next_up_inner = next_up_outer.find('td')
    
    bron_id = int(bron_inner.contents[0].rstrip('.'))
    bron_data_row= (bron_id - 1) #zero-indexed

    print(int(bron_id))
    return
