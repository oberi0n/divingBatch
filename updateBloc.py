# Utilisez votre module utilitaire.
import connutils
import getInfoBloc
import datetime

def updateBloc(idEquipment,fabricant,numeroSerie,connection):
	
	#Récup des infos du bloc
	testData = getInfoBloc.getInfoBloc(fabricant, numeroSerie)
	
	if testData == "error":
		print("error")
	else:
		listData = testData.split(",")
		#listData = getInfoBloc.getInfoBloc(fabricant, numeroSerie).split(",")

		entretienDate=str(datetime.datetime.strptime(listData[0],"%d/%m/%Y"))
		status=str(listData[1])
		requalifDate=str(datetime.datetime.strptime(listData[2],"%d/%m/%Y"))

		sql = "update Equipment set dateDernierEntretien = '" + entretienDate + "', dateRequalif = '" + requalifDate + "', statutTIV = '" + status + "' where idEquipment = " + idEquipment 
		print("Mise à jour des infos du bloc ayant pour numéro de serie: " + numeroSerie)
		cursor = connection.cursor() 
		# Exécution sql
		cursor.execute(sql)  
		# Commit
		connection.commit()    
		print("Database mise à jour pour le bloc n°" + numeroSerie)

	