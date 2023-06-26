import random
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

# lista de eventos
events_list = ['player_death', 'game_created', 'game_joined', 'character_created']

# gerando 100 eventos aleatórios
events = []
for i in range(1000):
    # selecionando aleatoriamente um evento da lista
    event_type = random.choice(events_list)
    # gerando uma data aleatória
    event_date = datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 30), hours=random.randint(1, 23), minutes=random.randint(1, 59), seconds=random.randint(1, 59))
    # gerando um jogador aleatório
    player_id = random.randint(1, 20)
    # gerando um jogo aleatório
    game_id = random.randint(1, 10)
    # gerando um personagem aleatório
    character_id = random.randint(1, 50)

    cur.execute("""
        INSERT INTO events (event_type, event_date, player_id, game_id, character_id)
        VALUES ('{}', '{}', {}, {}, {})
    """.format(event_type, event_date, player_id, game_id, character_id))
    conn.commit()

# Finalizando a conexão
cur.close()
conn.close()


