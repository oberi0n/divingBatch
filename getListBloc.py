import connutils
import getInfoBloc
import updateBloc

#Main function

#Récuperation d'une connexion
connection = connutils.getConnection() 

sql = "Select idEquipment,libelle,marque,taille,numeroSerie,tag,dateAchat,dateDernierEntretien,fabriquant from Equipment where libelle = 'Bloc'" 

try :
    cursor = connection.cursor() 
    # Exécution de la requete
    cursor.execute(sql)  
    
    for row in cursor:
        idEquipment = row["idEquipment"]
        fabricant = row["fabriquant"]
        numeroSerie = row["numeroSerie"]
        
        if fabricant:
            updateBloc.updateBloc(str(idEquipment),fabricant,numeroSerie,connection)

finally:
    # Fermeture connexion
    connection.close()