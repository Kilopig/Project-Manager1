import json
import urllib



def showPrice(name):
    if name == "iphone":
        results = json.load(urllib.urlopen("http://www.pricetree.com/dev/api.ashx?pricetreeId=82044&apikey=7770AD31-382F-4D32-8C36-3743C0271699"))
    if name == "ipad":
        results = json.load(urllib.urlopen("http://www.pricetree.com/dev/api.ashx?pricetreeId=757&apikey=7770AD31-382F-4D32-8C36-3743C0271699"))
    if name == "fridge":
        results = json.load(urllib.urlopen("http://www.pricetree.com/dev/api.ashx?pricetreeId=122177&apikey=7770AD31-382F-4D32-8C36-3743C0271699"))
    if name == "microwave":
        results = json.load(urllib.urlopen("http://www.pricetree.com/dev/api.ashx?pricetreeId=124120&apikey=7770AD31-382F-4D32-8C36-3743C0271699"))
    if name == "laptop":
        results = json.load(urllib.urlopen("http://www.pricetree.com/dev/api.ashx?pricetreeId=123229&apikey=7770AD31-382F-4D32-8C36-3743C0271699"))
    if name == "tv":
        results = json.load(urllib.urlopen("http://www.pricetree.com/dev/api.ashx?pricetreeId=119307&apikey=7770AD31-382F-4D32-8C36-3743C0271699"))
    if name == "printer":
        results = json.load(urllib.urlopen("http://www.pricetree.com/dev/api.ashx?pricetreeId=124333&apikey=7770AD31-382F-4D32-8C36-3743C0271699"))
    if name == "camera":
        results = json.load(urllib.urlopen("http://www.pricetree.com/dev/api.ashx?pricetreeId=120752&apikey=7770AD31-382F-4D32-8C36-3743C0271699"))
    if name == "wash":
        results = json.load(urllib.urlopen("http://www.pricetree.com/dev/api.ashx?pricetreeId=122743&apikey=7770AD31-382F-4D32-8C36-3743C0271699"))
    return results["data"];
