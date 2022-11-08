import requests

url_ddg = "https://api.duckduckgo.com"

president_list = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Jackson", "Buren", "Harrison", "Tyler",
                  "Polk", "Tylor", "Fillmore", "Pierce", "Buchanan", "Lincoln", "Johnson", "Grant", "Hayes", "Garfield",
                  "Arthur", "Cleveland", "Harrison", "Mckinley", "Roosevelt", "Taft", "Wilson", "Harding", "Coolidge",
                  "Hoover", "Truman", "Eisenhower", "Kennedy", "Johnson", "Nixon", "Ford", "Carter", "Reagan", "Bush",
                  "Clinton", "Obama", "Trump", "Biden"]

resp = requests.get(url_ddg + "/?q=presidents of the united states&" + "/?q=DuckDuckGo&format=json")
rsp_data = resp.json()

""" I tried using a list and comparing elements but I could not find a way to make it work. This was the easiest approach
I could think off."""


def test_ddg0():
    for key in rsp_data["RelatedTopics"]:
        assert "Washington" and "Adams" and "Jefferson" and "Madison", "Monroe" and "Jackson" and "Buren" and "Harrison" and \
                                                                       "Tyler" and "Polk" and "Tylor" and "Fillmore" and "Pierce" and "Buchanan" and "Lincoln" and "Johnson" and \
                                                                       "Grant" and "Hayes" and "Garfield" and "Arthur" and "Cleveland" and "Harrison" and "Mckinley" and "Roosevelt" and \
                                                                       "Taft" and "Wilson" and "Harding" and "Coolidge" and "Hoover" and "Truman" and "Eisenhower" and "Kennedy" and \
                                                                       "Johnson" and "Nixon" and "Ford" and "Carter" and "Reagan" and "Bush" and "Clinton" and "Obama" and "Trump" and "Biden" \
                                                                       in key['Text']
