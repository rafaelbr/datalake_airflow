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

# Gerando nomes aleatórios de itens
items = ['Sword', 'Shield', 'Potion', 'Wand', 'Staff', 'Bow', 'Arrow', 'Axe', 'Hammer', 'Helmet']

# Gerando dados fictícios para tabela de inventário
def generate_inventory_data(num_records):
    data = []
    for i in range(num_records):
        inventory_id = i
        item_name = random.choice(items)
        item_quantity = random.randint(1, 10)
        character_id = random.randint(1, 50)
        data.append((inventory_id, item_name, item_quantity, character_id))
    return data

# Gerando tipos aleatórios de moedas
currency_types = ['Gold', 'Silver', 'Copper']

# Gerando dados fictícios para tabela de moeda
def generate_currency_data(num_records):
    data = []
    for i in range(num_records):
        currency_id = i
        currency_type = random.choice(currency_types)
        currency_amount = random.randint(1, 1000)
        player_id = random.randint(1, 1000)
        data.append((currency_id, currency_type, currency_amount, player_id))
    return data

# Gerando dados fictícios para tabela de inventário
inventory_data = generate_inventory_data(100)

# Inserindo dados na tabela de inventário
cursor = conn.cursor()
for item in inventory_data:
    cursor.execute("INSERT INTO inventory (inventory_id, item_name, item_quantity, character_id) VALUES ({}, '{}', {}, {})"
                   .format(item[0], item[1], item[2], item[3]))
conn.commit()

# Gerando dados fictícios para tabela de moeda
currency_data = generate_currency_data(20)

# Inserindo dados na tabela de moeda
for currency in currency_data:
    cursor.execute("INSERT INTO currency (currency_id, currency_type, currency_amount, player_id) VALUES ({}, '{}', {}, {})"
                   .format(currency[0], currency[1], currency[2], currency[3]))
conn.commit()

# Encerrando conexão
cursor.close()
conn.close()
