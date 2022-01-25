import pymysql.cursors   
# La fonction renvoie une connexion.
def getConnection(): 
    # Vous pouvez changer les arguments de la connexion.
#    connection = pymysql.connect(host='192.168.1.112',
#                                 user='divinguser',
#                                 password='za5ub33h',
#                                 database='equipment',
#                                 charset='utf8mb4',
#                                 cursorclass=pymysql.cursors.DictCursor)

    connection = pymysql.connect(host='192.168.1.45',
                                 user='divingbatch',
                                 password='za5ub33h',
                                 database='equipment',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)                                 
    return connection