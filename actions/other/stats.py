# import mysql.connector
# from mysql.connector import Error
# from time import sleep
# # from actions.launcher.license import License

# class Statistic:

#     def __init__(self):
#         pass


#     def IncrementStatistic():
#         try:
#             with open('data\\stat.txt', 'a+') as file:
#                 current_value = file.read()
#                 if current_value != "":
#                     new_value = int(current_value) + 1
#                 else:
#                     new_value = 1
                
#                 file.seek(0)
#                 file.write(str(new_value))
#         except Exception:
#             pass


    
#     def ReadTheNumber():
#          with open('data\\stat.txt', 'a+') as file:
#             try:
#                 current_value = file.read()
#                 if current_value != "":
#                     value = int(current_value) 
#                 else:
#                     value = 0
#                 return value
#             except Exception:
#                 pass
        

#     def sendToDataBase(self):
#         try:
#             self.__conn = mysql.connector.connect(
#                 host="65.21.108.149",
#                 user="script_user",
#                 port=3306,
#                 passwd="KDKjq[eri683kasknc9z2",
#                 database="lztc",
#                 # connect_timeout=60
#             )
#             username = License.get_username(self)

#             contest_count = Statistic.ReadTheNumber()

#             with self.__conn.cursor() as cursor:
#                 query = "SELECT contestsCount FROM statistic WHERE lzt_username = %s"
#                 cursor.execute(query, (username,))
#                 result = cursor.fetchone()
#                 if result:
#                     current_count = result[0]
#                 else:
#                     current_count = 0

#             contest_count += current_count

#             with self.__conn.cursor() as cursor:
#                 query = "UPDATE statistic SET contestsCount = %s WHERE lzt_username = %s"
#                 cursor.execute(query, (contest_count, username))
#             self.__conn.commit()
#             self.__conn.close()

#         except Error as ex:
#             pass
            




