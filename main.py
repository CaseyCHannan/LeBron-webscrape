from grab import who_next 

url_points= "https://www.basketball-reference.com/leaders/pts_career.html"
url_rebounds = "https://www.basketball-reference.com/leaders/trb_career.html"
url_field_goals ="https://www.basketball-reference.com/leaders/fg_career.html"
url_assists = "https://www.basketball-reference.com/leaders/ast_career.html"
url_win_shares = "https://www.basketball-reference.com/leaders/ws_career.html"

# this is the HTML from the given URL

who_next(url_points, 'points')
who_next(url_rebounds, 'rebounds')
who_next(url_field_goals, 'field goals')
who_next(url_assists, 'assists')
who_next(url_win_shares, 'winshares')
