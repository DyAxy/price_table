import json


def Countryconvert(code):
    with open("../countries.json", 'r', encoding="utf-8") as r:
        j = json.loads(r.read())
        for i in j:
            if code == i['iso2']:
                return i['translations']['cn'], i['emoji']


def exec():
    with open("../netflix.json", 'r', encoding="utf-8") as r:
        j = json.loads(r.read())
        countrylist = []
        for i in j:
            if i['Currency'] != '':
                c, e = Countryconvert(i['Code'])
                tax = 1
                if i['Code'] == 'AR':
                    tax = 1.64
                content = {
                    'country': c,
                    'emoji': e,
                    'Code': i['Code'],
                    'Currency': i['Currency'],
                    'Basic': round(float(i['Basic'])*tax, 2),
                    'Standard': round(float(i['Standard'])*tax, 2),
                    'Premium': round(float(i['Premium'])*tax, 2),
                    'BasicCNY': round(float(i['BasicCNY'])*tax, 2),
                    'StandardCNY': round(float(i['StandardCNY'])*tax, 2),
                    'PremiumCNY': round(float(i['PremiumCNY'])*tax, 2),
                }
                countrylist.append(content)
        countrylist = sorted(countrylist, key=lambda i: i['PremiumCNY'])
        jsObj = json.dumps(countrylist)

        fileObject = open('api_ranking.json', 'w', encoding='utf-8')
        fileObject.write(jsObj)
        fileObject.close()


exec()
