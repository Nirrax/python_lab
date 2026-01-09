import requests
import xml.dom.minidom as xml

def get_data():
    url = "https://api.nbp.pl/api/cenyzlota/2025-12-01/2025-12-31?format=xml"
    response = requests.get(url)
    data = response.text
    dom = xml.parseString(data)
    return dom

def parse_data(data):
    results = []

    for node in data.getElementsByTagName("CenaZlota"):
        date = node.getElementsByTagName("Data")[0].firstChild.nodeValue
        price = node.getElementsByTagName("Cena")[0].firstChild.nodeValue
        results.append((date, float(price)))

    return results

def calc_avg(data):
    total = sum(price for _, price in data)
    return total / len(data)

def print_data(data):
    for date, price in data:
        print(f"{date}: {price:.2f} zł")
    print(f"Average price: {calc_avg(data):.2f} zł")

data = get_data()
data = parse_data(data)
print_data(data)
