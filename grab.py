from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# URL pages we will scraping (see image above)

url = "https://www.basketball-reference.com/leaders/trb_career.html"
# https://www.basketball-reference.com/leaders/fg_career.html
# url = "https://www.basketball-reference.com/leaders/ast_career.html"
#url = "https://www.basketball-reference.com/leaders/ws_career.html"
# url = "https://www.basketball-reference.com/leaders/pts_career.html"
# this is the HTML from the given URL
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

atags = soup.find_all('a')
nba_only = soup.find(id="all_nba")


brontag =  nba_only.find(href="/players/j/jamesle01.html")
# print(brontag)
bron_outer =brontag.find_parent('tr')
print(bron_outer)
print(f'I am the bron-outer a tag {bron_outer.a.string}')
bron_inner = bron_outer.find('td')
print(bron_inner)
print('\n')


next_up_outer = bron_outer.find_previous_sibling('tr')
print(next_up_outer)
print(f'i am the outer contents {next_up_outer.contents[-1].string} \n')
# print(f'I am the next-guy-outer a tag {next_up_outer.contents}')

next_up_inner = next_up_outer.find('td')
print(next_up_inner)
print(f'I am the next-guy-inner-contents {next_up_inner.contents}')


bron_id = int(bron_inner.contents[0].rstrip('.'))

bron_data_row= (bron_id - 1) #zero-indexed
next_up_data_row =bron_data_row - 1

print(int(bron_id))
# print(next_up_data_row)




# https://www.basketball-reference.com/leaders/pts_career.html

# <a href="/players/j/jamesle01.html">LeBron James</a>



# import requests
# from bs4 import BeautifulSoup as bs

# html = '''
# <tbody tabindex="0" class="yui-dt-data" id="yui_3_5_0_1_1408418470185_1650">
#       <tr id="yui-rec0" class="yui-dt-first yui-dt-even">
#            <td headers="yui-dt0-th-rank" class="rank yui-dt0-col-rank"></td>
#            </tr>
#       <tr id="yui-rec1" class="yui-dt-odd">...</tr>
#       <tr id="yui-rec2" class="yui-dt-even">...</tr>
#  </tbody>
#  '''
# soup = bs(html, 'lxml')
# soup.select('.yui-dt-data')


# https://stackoverflow.com/questions/25375351/beautifulsoup-unable-to-find-classes-with-hyphens-in-their-name

# from bs4 import BeautifulSoup

# htmlstring = """ <tbody tabindex="0" class="yui-dt-data" id="yui_3_5_0_1_1408418470185_1650">
#       <tr id="yui-rec0" class="yui-dt-first yui-dt-even">
#       <tr id="yui-rec1" class="yui-dt-odd">
#       <tr id="yui-rec2" class="yui-dt-even">"""


# soup = BeautifulSoup(htmlstring)
# Table = soup.find('tbody', attrs={'class': 'yui-dt-data'}) 
# print("Table:\n")
# print(Table)
# tr = Table.find('tr', attrs={'class': 'yui-dt-odd'}) 
# print("tr:\n")
# print(tr)
# outputs:

# Table:

# <tbody class="yui-dt-data" id="yui_3_5_0_1_1408418470185_1650" tabindex="0">
# <tr class="yui-dt-first yui-dt-even" id="yui-rec0">
# <tr class="yui-dt-odd" id="yui-rec1">
# <tr class="yui-dt-even" id="yui-rec2"></tr></tr></tr></tbody>
# tr:

# <tr class="yui-dt-odd" id="yui-rec1">
# <tr class="yui-dt-even" id="yui-rec2"></tr></tr>