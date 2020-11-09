import sqlite3

db = sqlite3.connect('project.db')
sql = db.cursor()

sql.execute('''CREATE TABLE IF NOT EXISTS users (
     name1 TEXT,
     name2 TEXT,
     turn1 TEXT,
     turn2 TEXT
)''')
db.commit()

user_input = input('Напишіть new щоб гра почалась: ')

if user_input == 'new':
     user1 = input("Введіть ім'я першого учасника: ")
     user2 = input("Введіть ім'я другого учасника: ")

while 1==1:
     user_input1 = input(f'Хід {user1}(напишіть stop щоб гра закінчилась(щоб закінчилось потрібно щоб stop написало двоє)): ')
     user_input2 = input(f'Хід {user2}(напишіть stop щоб гра закінчилась(щоб закінчилось потрібно щоб stop написало двоє)): ')
     sql.execute("INSERT INTO users VALUES (?,?,?,?)", (user1, user2, user_input1, user_input2))
     db.commit()
     if user_input1 == 'stop' or user_input2 == 'stop':
          print("Гра зупинилась.")
          break
     else:
          continue
           
else:
    print('Напишіть new щоб гра почалась')
