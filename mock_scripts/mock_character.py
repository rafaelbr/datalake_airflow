import random
import psycopg2

# Conexão com o banco de dados PostgreSQL
conn = psycopg2.connect(
    host="",
    port="5432",
    database="gamedb",
    user="",
    password=""
)


# Criação do cursor
cursor = conn.cursor()

# Dados para geração dos nomes
racas = ['Wolf', 'Fox', 'Rabbit']
classes = ['Warrior', 'Mage', 'Rogue']
nomes = ['Willy', 'Jack', 'Sophie', 'Luna', 'Charlie', 'Buddy', 'Daisy', 'Rocky', 'Bailey', 'Max']
sobrenomes = {
    'Wolf': ['Frost', 'Night', 'Moon', 'Storm', 'Shadow', 'Silver', 'Thunder', 'Wild'],
    'Fox': ['Bright', 'Dusk', 'Ember', 'Flame', 'Glow', 'Red', 'Russet', 'Scarlet'],
    'Rabbit': ['Hop', 'Swift', 'Bounce', 'Quick', 'Nimble', 'Hare', 'Flicker', 'Zigzag']
}

# Gerando 100 personagens aleatórios
for i in range(1, 1001):
    nome = random.choice(nomes)
    raca = random.choice(racas)
    classe = random.choice(classes)
    sobrenome = nome + ' ' + random.choice(sobrenomes[raca]) + raca.lower()
    nivel = random.randint(1, 10)
    player_id = random.randint(1, 1000)
    cursor.execute(f"INSERT INTO characters (character_id, player_id, character_name, character_race, character_class) VALUES ({i}, {player_id}, '{sobrenome}', '{raca}', '{classe}')")

# Finalizando a conexão
conn.commit()
cursor.close()
conn.close()
