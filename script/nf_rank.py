import json


def Countryconvert(code):
    with open("../countries.json", 'r', encoding="utf-8") as r:
        j = json.loads(r.read())
        for i in j:
            if code == i['iso2']:
                return i['translations']['cn'], i['emoji']
                
def Currencyconvert(code):
    with open("../countries.json", 'r', encoding="utf-8") as r:
        j = json.loads(r.read())
        for i in j:
            if code == i['currency']:
                return i['currency_symbol']


def exec():
    with open("../netflix.json", 'r', encoding="utf-8") as r:
        j = json.loads(r.read())
        countryList = {}
        for i in j:
            countryList[i['Code']] = i
            c,e = Countryconvert(i['Code'])
            countryList[i['Code']]['country'] = c
            countryList[i['Code']]['emoji'] = e
            countryList[i['Code']]['symbol'] = Currencyconvert(i['Currency'])

        jsObj = json.dumps(countryList)

        fileObject = open('api_ranking.json', 'w', encoding='utf-8')
        fileObject.write(jsObj)
        fileObject.close()


exec()
