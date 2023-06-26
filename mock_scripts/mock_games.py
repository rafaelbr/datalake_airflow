import random
import string
import datetime
import psycopg2

# Conexão com o banco de dados PostgreSQL
conn = psycopg2.connect(
    host="",
    port="5432",
    database="gamedb",
    user="",
    password=""
)

cur = conn.cursor()

status = ['active', 'finished', 'cancelled']

# função para gerar um ID aleatório
def random_id(length=6):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def random_date():
    year = random.randint(2010, 2022)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return f"{year:04d}-{month:02d}-{day:02d}"

# lista de jogos
for i in range(1001):
    game_id = random_id()
    creation_date = datetime.datetime.now()
    end_date = creation_date + datetime.timedelta(days=1)
    query = "INSERT INTO games (game_id, game_name, game_start_date, game_end_date, game_status) VALUES ({}, '{}', TO_DATE('{}', 'YYYY-MM-DD HH24:MI:SS'), TO_DATE('{}', 'YYYY-MM-DD HH24:MI:SS'), '{}')".format(
        i, game_id, creation_date.strftime('%Y-%m-%d %H:%M:%S'), end_date.strftime('%Y-%m-%d %H:%M:%S'), random.choice(status))
    cur.execute(query)

# Finalizando a conexão
conn.commit()
cur.close()
conn.close()
