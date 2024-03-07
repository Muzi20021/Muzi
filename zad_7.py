import requests

class Brewery:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.brewery_type = data['brewery_type']
        self.address_1 = data['address_1']
        self.address_2 = data['address_2']
        self.address_3 = data['address_3']
        self.city = data['city']
        self.state_province = data['state_province']
        self.postal_code = data['postal_code']
        self.country = data['country']
        self.longitude = data['longitude']
        self.latitude = data['latitude']
        self.phone = data['phone']
        self.website_url = data['website_url']

    def __str__(self):
        return f"ID: {self.id}\nName: {self.name}\nType: {self.brewery_type}\n" \
               f"Address: {self.address_1}, {self.address_2}, {self.address_3}\n" \
               f"Location: {self.city}, {self.state_province}, {self.postal_code}, {self.country}\n" \
               f"Coordinates: {self.latitude}, {self.longitude}\n" \
               f"Phone: {self.phone}\nWebsite: {self.website_url}\n"

def fetch_breweries():
    base_url = "https://api.openbrewerydb.org/breweries"
    params = {'per_page': 20}

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def main():
    breweries_data = fetch_breweries()

    if breweries_data:
        breweries_list = [Brewery(data) for data in breweries_data]

        for brewery in breweries_list:
            print(brewery)

if __name__ == "__main__":
    main()
