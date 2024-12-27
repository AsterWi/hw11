import requests

response = requests.get("https://nationalbank.kz/en/exchangerates/ezhednevnye-oficialnye-rynochnye-kursy-valyut")
response_text = response.text

response_parse = response_text.split("<tr>")

exch_rate = None

for parse_elem in response_parse:
    l = parse_elem.find("USD")
    if l != -1:
        for parse_elem2 in parse_elem.split():
            if len(parse_elem2) >=5:
                if parse_elem2[4] in "0123456789":
                    parse_elem2 = parse_elem2.replace("<td>", "")
                    parse_elem2 = parse_elem2.replace("</td>", "")
                    exch_rate = parse_elem2

exch_rate = float(exch_rate)

amount = int(input("Hello, please enter the amount in tenge to convert to us dollar: "))
print(f"The amount in dollars is: {amount*exch_rate}")
