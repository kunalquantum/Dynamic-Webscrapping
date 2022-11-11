import validators
import time
import webbrowser
import requests
from bs4 import BeautifulSoup


from win10toast_click import ToastNotifier


import sys



def get_score(team_name):
    search_team = team_name.split()
    search_team.append("live+cricket+score")
    search_team = "+".join(search_team)

    URL = f"https://www.google.com/search?q={search_team}"
    
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
    page = requests.get(URL, headers=header)

    soup = BeautifulSoup(page.content, 'lxml')
    scores = soup.find("div", class_="imso_mh__scr-sep")
    score_team_1 = scores.find(
        "div", class_="imspo_mh_cricket__first-score imspo_mh_cricket__one-innings-column-with-overs").text
    score_team_2 = scores.find(
        "div", class_="imspo_mh_cricket__second-score imspo_mh_cricket__one-innings-column-with-overs").text

    teams = soup.find_all(
        "div", class_="liveresults-sports-immersive__hide-element")
    team_list = []
    for t in teams:
        team_list.append(t.text)

    summary = soup.find(
        "div", class_="imso_mh__score-txt imso-ani imspo_mh_cricket__summary-sentence").text

    data = {
        "teams": team_list,
        "score_1": score_team_1,
        "score_2": score_team_2,
        "summary": summary
    }
    return data


print('Live Cricket Matches:')
print('=====================')
url = "http://static.cricinfo.com/rss/livescores.xml"
r = requests.get(url)
soup = BeautifulSoup(r.text,'lxml')

i = 1
for item in soup.findAll('item'):
 print(str(i) + '. ' + item.find('description').text)
 i = i + 1

links = []    
for link in soup.findAll('item'):
 links.append(link.find('guid').text)

print('Enter match number or enter 0 to exit:')
while True:
 try:
  userInput = int(input())
 except NameError:
  print('Invalid input. Try Again!')
  continue
 except SyntaxError:
  print('Invalid input. Try Again!')
 if userInput < 0 or userInput > 100:
  print('Invalid input. Try Again!')
  continue
 elif userInput == 0:
  sys.exit()      
 else:
  break
x=[]
for link in soup.findAll('item'):
  x.append(link.find('description').text)


url = links[userInput - 1]
r = requests.get(url)
soup = BeautifulSoup(r.text,'lxml')  




y=x[userInput-1]

def extract_alpha(string):
    alpha=[]

    for char in string:
        if char.isalpha():
            alpha.append(char)
    return alpha        
z=(extract_alpha(y))

xyz=''.join(z)


download_page1=f"https://www.google.com/search?q=live+cricket+score+{xyz}"
def yourfunction1():
    try:
        webbrowser.open(download_page1)
    except:
        print("failed")    

download_page2=url
def yourfunction2():
    try:
        webbrowser.open(download_page2)
    except:
        print("failed")   

    

while True:
            data = get_score(xyz)
            toaster = ToastNotifier() 
            toaster.show_toast(f"{data['teams'][0]} vs {data['teams'][1]}",
                            f"{data['teams'][0]} {data['score_1']} - {data['score_2']} {data['teams'][1]}\n{data['summary']}",
                            duration=5,
                            
                            callback_on_click=yourfunction1, ) 
            
            matchUrl = links[userInput - 1]
            r = requests.get(matchUrl)
            soup = BeautifulSoup(r.text,'lxml') 
            score = soup.findAll('title')      
            team_list = []
            for t in score:
                        team_list.append(t.text)
            toaster.show_toast(f"Full scoreboard",
                                f"{team_list}",
                                duration=5,
                                
                                callback_on_click=yourfunction2, )
            time.sleep(5)
               
