import sqlite3
database = "pythonsqlite.db"

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

def create_user(name):
    """
    Create a new name into the user table
    :param conn:
    :param name:
    :return: user id
    """    

    conn = create_connection(database)

    with conn:
	    sql = ''' INSERT OR IGNORE INTO utilizador(nome)
	              VALUES(?) '''
	    cur = conn.cursor()
	    cur.execute(sql, (name,))
	    return cur.lastrowid

def create_account(tipo,montante,name):
    """
    Create a new account
    :param conn:
    :param count:
    :return:
    """

    conn = create_connection(database)

    with conn:
		#user_id = create_user(name)
	    
	    sql = ''' INSERT INTO conta(tipo,montante,utilizador_id)
	              VALUES(?,?,?) '''
	    cur = conn.cursor()
	    cur.execute(sql, (tipo,montante,create_user(name),))
	    return cur.lastrowid

def saber_saldo(nome):

	conn = create_connection(database)

	with conn:
	    
		cur = conn.cursor()
		cur.execute("""
			SELECT DISTINCT montante
			FROM utilizador, conta
			WHERE utilizador_id =
			(SELECT utilizador.id
				FROM utilizador, conta
				WHERE nome = ?);
			""", (nome,))

		sal = cur.fetchone()

		if sal is None:
			return 0
		else:
			return str(sal).strip("()").strip(",")

	conn.close()

def atualizar_valores(nome, montante):

	conn = create_connection(database)

	with conn:
	    
		cur = conn.cursor()
		cur.execute("""
			UPDATE conta
			SET montante = ?
			WHERE utilizador_id =
			(SELECT utilizador.id
				FROM utilizador, conta
				WHERE nome = ?);
			""", (montante, nome,))
	
	conn.commit()
	conn.close()

'''def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = "pythonsqlite.db"
 
    sql_create_user_table = """CREATE TABLE IF NOT EXISTS utilizador (
                                    id integer PRIMARY KEY,
                           	        nome text NOT NULL
                            	); """

    sql_create_conta_table = """CREATE TABLE IF NOT EXISTS conta (
                                    id integer PRIMARY KEY,
                                    tipo text NOT NULL,
                                    montante integer NOT NULL,
                                    utilizador_id integer NOT NULL,
                                    FOREIGN KEY (utilizador_id) REFERENCES utilizador (id)
                                );"""
 
    # create a database connection
    conn = create_connection(database)
    if conn is not None:

        # create tables
        create_table(conn, sql_create_user_table)
        create_table(conn, sql_create_conta_table)

        # create a new user
        user = ('Pedro');
        user_id = create_user(conn, user)

        # account
        account_1 = ('Poupança', 300, user_id)
        # create account
        create_account(conn, account_1)
       
    else:
        print("Error! cannot create the database connection.")
'''

'''def main(e, c, d, n):
    database = "pythonsqlite.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn:

        # create a new user
        #user = ('Paulo')
        user_id = create_user(conn, n)

        # account
        account = (c, e, user_id)
        # create account
        create_account(conn, account)


if __name__ == '__main__':
    main()
'''