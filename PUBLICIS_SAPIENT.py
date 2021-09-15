import requests

def getPhoneNumber(country, phoneNumber):
    url="https://jsonmock.hackerrank.com/api/countries?name="+country
    responce=requests.get(url)
    if responce.status_code==200:
        data=responce.json()
        name=data['data'][0]['name']
        if name==country:
            code=data['data'][0]['callingCodes'][0]
            return " +" +code+" "+phoneNumber
        else:
            return "-1"    
    else:
        exit()


ans=getPhoneNumber("India", "9595959595")
print(ans)        
