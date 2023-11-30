import requests
import json

def search_place(api_key, place):
    base_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"
    inputtype = "textquery"
    fields = "name,formatted_phone_number"
    locationbias = "ipbias"

    request_url = f"{base_url}input={place}&inputtype={inputtype}&fields={fields}&locationbias={locationbias}&key={api_key}"

    res = requests.get(request_url)
    data = json.loads(res.text)

    return data

api_key = "AIzaSyAekIrOAKyr1sWpnuAihL0_Jtt8dkCLly4"

hotel_list = [
    "White castle",
    "Mihilaka holiday homes",
    "OYO Barasti beach resort",
    "Indi lesiure",
    "Claremont suits",
    "Saffron beach hotel",
    "Fisherman villa",
    "The white hotel",
    "Taprobana wadduwa",
    "Maresia beach hotel",
    "Anjayu vila",
    "Dhammika beach palace",
    "The villa by contemporary ceylon",
    "Reef Sri Lanka",
    "Summer breeze at reef Sri Lanka",
    "Ocean ripples resort",
    "Clive garden luxury boutique Hotel and Spa",
    "Ayana sea",
    "Villa ocean view",
    "Serendiya beach hotel",
    "The privilege ayurveda beach",
    "Larn’s villa",
    "Ocean queen hotel wadduwa",
    "Sun view beach",
    "Oak ray haridra beach resort",
    "Siddalepa ayrveda health resort",
    "The beach villa ceylon bungalows",
    "The kenrish hotel",
    "Shalimar beach hotel",
    "Caltura beach villa",
    "Turyaa kalutara",
    "Turyaa",
    "The cod father seafood",
    "Happy cocos",
    "Green shadow beach",
    "White house villa waskaduwa",
    "Sea sand villa",
    "Austro lanka waskaduwa",
    "Mermaid hotel and club",
    "Club hotel beach resort and spa",
    "Hibiscus beach hotel",
    "Coco royal beach resort",
    "Paradise waskaduwa",
    "Sun view beach",
    "Royal palms beach hotel",
    "Coffee shop by tangerine beach",
    "Tangerine beach hotel",
    "Ritz gate kalutara",
    "Pradeep villa",
    "Villa whispering shells",
    "Sunshine beach",
    "Candle house",
    "Amssler beach stay hotel",
    "Karl holiday bungalow",
    "Kalido beach villa",
    "Garden beach hotel kalutara",
    "Grand royal",
    "Hotel ocean spray",
    "Royal oshin hotel",
    "Panaroma hotel",
    "Mahakumara White house hotel",
    "Laya beach hotel",
    "Citrus waskaduwa"
]

with open("hotel_numbers.txt", "w") as file:
    for hotel in hotel_list:
        data = search_place(api_key, hotel)
        if 'candidates' in data and data['candidates']:
            hotel_data = data['candidates'][0]
            name = hotel_data.get('name', '')
            phone = hotel_data.get('formatted_phone_number', "Can't find")
            file.write(f"{name}: {phone}\n")
        else:
            file.write(f"{hotel}: Can't find\n")
