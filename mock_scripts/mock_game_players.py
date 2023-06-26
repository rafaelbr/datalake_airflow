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

# lista de game_players
game_players_data = []

# gerar 1000 registros de game_players
for i in range(1, 1001):
    game_player_id = i + 1
    game_id = random.randint(1, 1000)
    player_id = random.randint(1, 1000)
    join_date = datetime.date(2022, random.randint(1, 12), random.randint(1, 28))
    leave_date = datetime.date(2022, random.randint(1, 12), random.randint(1, 28))
    if join_date > leave_date:
        join_date, leave_date = leave_date, join_date
    #game_players_data.append((game_player_id, game_id, player_id, join_date, leave_date))

    cur.execute("""
        INSERT INTO game_players (game_player_id, game_id, player_id, join_date, leave_date)
        VALUES ({}, {}, {}, TO_DATE('{}', 'YYYY-MM-DD'), TO_DATE('{}', 'YYYY-MM-DD'))
    """.format(game_player_id, game_id, player_id, join_date, leave_date))
    conn.commit()

# Finalizando a conexão

cur.close()
conn.close()
