import requests


server = 'https://2238cf30.ngrok.io'


provinces= {1:'Khyber Pakhtunkhwa',
            2:'FATA',
            3:'Punjab',
            4:'Sindh',
            5:'Balochistan',
            6:'Islamabad',
            7:' Gilgit-Baltistan'}

def generateAreaForSindh(area_code):
    if(area_code<50):
        return 10
    elif(area_code<100):
        return 11
    elif(area_code<230):
        return 12
    elif(area_code<350):
        return 13
    elif(area_code<490):
        return 14
    elif(area_code<570):
        return 15
    elif(area_code<720):
        return 16
    elif(area_code<820):
        return 17
    elif(area_code<=999):
        return 18
    elif(area_code<3000):
        return 19
    elif(area_code<5000):
        return 20
    elif(area_code<7000):
        return 21
    elif(area_code<8500):
        return 22
    elif(area_code<=9900):
        return 23
    
    
def generateIDforProvince(province_num, area_code):
    if(province_num == 4):
        return generateAreaForSindh(area_code)
    else:
        return "This prototype only works for Sindh (province_num = 4)"

def districtGenerator(cnic):
    cnic_list = cnic.split("-")
    cnic_list = list(cnic)
    prov_code = int(cnic_list[0])
    code = int(''.join(cnic_list[1:5]))
    id_generated= generateIDforProvince(prov_code, code)
    query_district_id = server+'/api/district/{}'.format(id_generated)
    generatedDistrict = requests.get(query_district_id).json()
    return generatedDistrict
    
