import requests
from bs4 import BeautifulSoup
import csv

# Fonction pour extraire les citations d'une seule page
def scrape_page(page_url):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')
    return quotes

# URL de base
base_url = "https://quotes.toscrape.com"

# Préparation pour l'écriture dans un fichier CSV
results = []
for i in range(1, 6):  # Pour les cinq premières pages
    page_quotes = scrape_page(f"{base_url}/page/{i}/")
    for quote in page_quotes:
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        tags = [tag.text for tag in quote.find_all('a', class_='tag')]
        results.append([text, author, ', '.join(tags)])

# Écriture des résultats dans un fichier CSV
with open('results.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Text', 'Author', 'Tags'])
    writer.writerows(results)

print("Le fichier CSV a été créé avec succès.")

