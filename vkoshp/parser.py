from .models import Participant, Contest, Team
import requests

api = "http://codeforces.com/api/user.info?handles="


from bs4 import BeautifulSoup as BS


def chunks(l, n):
    n = max(1, n)
    return (l[i : i + n] for i in range(0, len(l) - n + 1, n))


def parse_soup(soup):
    contest = Contest(name="VKOSHP")
    contest.save()
    for table in soup.find_all("table", {"class": "regteams"}):
        menus = chunks(table.find_all("td"), 13)
        for tt in menus:
            try:
                team_name = BS(str(tt[0])).text.split(":")[1]
            except:
                team_name = "Без названия"
            try:
                team_city = BS(str(tt[0])).text.split(",")[0]
            except:
                team_city = ""
            try:
                team_region = BS(str(tt[3])).text
            except:
                team_region = ""
            team = Team(
                contest=contest, region=team_region, name=team_name, city=team_city
            )
            team.save()
            for i in range(7, 10):
                try:
                    member1 = BS(str(tt[i])).text
                except:
                    member1 = "???"
                Participant.objects.create(team=team, name=member1)


def parse_contest(url):
    soup = BS(requests.get(url).text)
    parse_soup(soup)


def parse_contest_file(file):
    soup = BS(file)
    parse_soup(soup)

def process_handles():
    url = api
    for participant in Participant.objects.all():
        url += participant.codeforces_handle + ";"
    print(url)
    x = requests.get(url).json()
    if x["status"] == "FAILED":
        print(x)
        return None
    for user, participant in zip(x["result"], Participant.objects.all()):
        participant.codeforces_rating = user["rating"]
        participant.save()


def process_handle(handle):
    x = requests.get(api + handle).json()
    try:
        return x["result"][0]
    except:
        return None


def get_rating(handle):
    return process_handle(handle)["rating"]
