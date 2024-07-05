from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

#Récuperation des infos d'un bloc dans la page TIV de la FFESSM
def getInfoBloc(fabId, numSerie): 
	try:
		print("Recuperation des infos du bloc ayant pour numéro de serie: " + numSerie)
		url = "https://tiv.ffessm.fr/InformationsBloc?FabricantId="+fabId+"&NumeroSerie="+numSerie

		req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})
		webpage = urlopen(req).read()
		page_soup = soup(webpage, "html.parser")

		page_soup = page_soup.find("div", {"id": "results"})
		sub_soup = page_soup.find("div", {"class": "form-group"})

		#Récuperation de la date de validité
		dateValide = sub_soup.find("div", {"class": "col-md-2"}).text.strip()

		#Récuperation du statut
		statutValide = 'NOK'
		for sub_heading in sub_soup.find_all("div", {"class": "col-md-4"}):
			if "alid" in sub_heading.text:
				statutValide = 'OK'

		#Récuperation de la date de qualification
		dateRequalif = page_soup.find("div", {"class": "col-md-3"}).text.strip()

		return dateValide + "," + statutValide + "," + dateRequalif
	except:
		return "error"