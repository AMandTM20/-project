#ДЗ_5 Есть вопросы по синтаксису оператра  SQL("UPDATE client SET {}=%s WHERE client_id=%s").format(Identifier(key));
        #     """,(arg, client_id,)) в 4 функции. Так как для 7 функции тоже нужно импортировать SQL, Identifier
	# 					и там будут аналогичные вопросы, то я ее пока не начинал писать 
import psycopg2 
from psycopg2.sql import SQL, Identifier

#1 Функция, создающая структуру БД (таблицы).
def create_db(conn):
    cur.execute("""
                DROP TABLE IF EXISTS phone;
                DROP TABLE IF EXISTS client;

			  	CREATE TABLE IF NOT EXISTS client(
				client_id SERIAL PRIMARY KEY,
			 	firstname VARCHAR(20) NOT NULL,
			 	lastname VARCHAR(40) NOT NULL,
			 	email VARCHAR(40) NOT NULL UNIQUE);

			  	CREATE TABLE IF NOT EXISTS phone(
				phone_id SERIAL PRIMARY KEY,
				client_id INTEGER,
				phones INTEGER UNIQUE,
				CONSTRAINT fk
               	FOREIGN KEY(client_id)
               	    REFERENCES client(client_id)
               	        ON DELETE CASCADE);
    """)

#2.Функция, позволяющая добавить нового клиента.
def add_client(conn,cur, firstname, lastname, email, phone=None):

        cur.execute("""
            INSERT INTO client(firstname, lastname, email)
			VALUES(%s,%s,%s)
			RETURNING client_id, firstname, lastname, email;
	 		""", (firstname, lastname, email))
        print(cur.fetchone())
#3. Функция, позволяющая добавить телефон для существующего клиента.
def add_phone(conn,cur, client_id, phones ):
        cur.execute("""
            INSERT INTO phone(client_id, phones)
			VALUES(%s,%s)
			RETURNING phone_id, client_id, phones ;
			""", (client_id, phones ))
        print(cur.fetchone())

#4.Функция, позволяющая изменить данные о клиенте.

def change_client(conn, cur, client_id, firstname = None , lastname= None, email = None, phone=None):

    arg_list = {'name': firstname, "surname": lastname, 'e_mail': email}
    print("arg_list: ", arg_list)
    for key, arg in arg_list.items():
       if arg: # ТАК?:
            cur.execute(SQL("UPDATE client SET {}=%s WHERE client_id=%s").format(Identifier(key)), (arg, client_id))

        # if arg: 
#  # ИЛИ ТАК: cur.execute("""
        #             SQL("UPDATE client SET {}=%s WHERE client_id=%s").format(Identifier(key));
        #     """,(arg, client_id,))
        #    # print("arg: ", arg)

# def change_client(conn, cur, client_id, firstname =None, lastname=None, email=None,phone = None):
#     arg_list = {'name': firstname, 'surname': lastname, 'e_mail': email}
#     for key, arg in arg_list.items():
#         if arg: 
#  # ИЛИ ТАК:   conn.cur.execute(SQL("UPDATE Client SET {}=%s WHERE client_id=%s").format(Identifier(key)), (arg, client_id))
#5. Функция, позволяющая удалить телефон для существующего клиента.
def delete_phone(conn,cur, client_id, phones):

        cur.execute("""
            DELETE FROM phone WHERE client_id = %s and phones = %s;
                """, (client_id,phones))
        cur.execute("""
            SELECT * FROM phone;
            """)

#6. Функция, позволяющая удалить существующего клиента.
def delete_client(conn,cur, client_id):

        cur.execute("""
            DELETE FROM client WHERE client_id = %s;
                """, (client_id,))
        cur.execute("""
            SELECT * FROM client;
            """)

#7. Функция, позволяющая найти клиента по его данным: имени, фамилии, email или телефону.- НУЖНО ИЗМЕНИТЬ!
# функционал поиска стоило организовать так, чтобы была возможность найти клиента по любой комбинации параметров,
# а не по отдельным значениям каждого.
def find_client(conn, cur, firstname=None, lastname=None, email=None, phones=None):

        cur.execute("""
            SELECT c.client_id FROM client c
            JOIN phone p ON c.client_id = p.client_id
            WHERE  c.firstname = %s
            """,(firstname,))

        cur.execute("""
            SELECT c.client_id FROM client c
            JOIN phone p ON c.client_id = p.client_id
            WHERE  c.lastname = %s
            """, (lastname,))

        cur.execute("""
            SELECT c.client_id FROM client c
            JOIN phone p ON c.client_id = p.client_id
            WHERE  c.email = %s
            """, (email,))

        cur.execute("""
            SELECT c.client_id FROM client c
            JOIN phone p ON c.client_id = p.client_id
            WHERE  p.phones = %s
            """, (phones,))

with psycopg2.connect(database="clients_db", user="postgres", password="postgres") as conn:
    with conn.cursor() as cur:
        create_db(conn)
        add_client(conn,cur, 'Иван','Петров','ipiy@mailr.ru', phone=None)
        add_client(conn,cur, 'Петр','Иванов', 'pi@mailr.ru', phone=None)
        add_client(conn,cur,'Сидор', 'Сидоров', 'ss@mailr.ru', phone=None)
        add_client(conn,cur, 'Иван', 'Сидоров', 'is@mailr.ru', phone=None)
        add_client(conn,cur, 'Петр', 'Сидоров', 'ps@mailr.ru', phone=None)
        add_client(conn,cur, 'Алексей', 'Новиков', 'an@mailr.ru', phone = None)
        add_phone(conn,cur, 1, 8553552)
        add_phone(conn,cur,1,8653518)
        add_phone(conn,cur,2,8353757)
        add_phone(conn,cur,4,8124352)
        add_phone(conn,cur,4,8550059)
        add_phone(conn,cur,4,8553752)
        add_phone(conn,cur,5,8573585)
        add_phone(conn,cur,6,8599585)
        change_client(conn,cur, 1, name='Том', e_mail='a_tomas@mail.ru')
        delete_phone(conn,cur,4,8550059)
        delete_client(conn,cur, 3)
        f_find = find_client(conn, cur,'Петр', 'Иванов', '',8353757)
        print('f_find', f_find)
conn.close()



