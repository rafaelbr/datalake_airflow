import random
import string
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

# cursor para executar as operações no banco de dados
cursor = conn.cursor()


# lista de nomes comuns em inglês e português
names = ['John', 'Mary', 'João', 'Maria', 'David', 'Lucas', 'Sofia', 'Sophia', 'Emily', 'Miguel']
surnames = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor']

# função para gerar uma data aleatória de registro
def random_date():
    year = random.randint(2010, 2022)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return f"{year:04d}-{month:02d}-{day:02d}"

# função para gerar uma data aleatória de último login
def random_last_login(registration_date):
    year = int(registration_date[:4])
    month = int(registration_date[5:7])
    day = int(registration_date[8:10])
    days_since_registration = (2023 - year) * 365 + (4 - month) * 30 + (30 - day)
    print(days_since_registration)
    days_since_last_login = random.randint(1, days_since_registration)
    last_login = days_since_registration - days_since_last_login
    return f"TO_DATE('{registration_date}', 'YYYY-MM-DD') + {last_login}"

# gerar 100 jogadores
for i in range(1, 1001):
    # gerar um nome aleatório
    name = random.choice(names) + " " + random.choice(surnames)

    email_domains = ['gmail.com', 'hotmail.com', 'outlook.com', 'yahoo.com']

    email = name.lower().replace(" ", ".") + "@" + random.choice(email_domains)

    password = ''.join(random.choice(string.ascii_letters) for i in range(8))
    
    # gerar uma data de registro aleatória
    registration_date = random_date()
    
    # gerar uma data de último login aleatória
    last_login_date = random_last_login(registration_date)
    
    # inserir o jogador no banco de dados
    cursor.execute(f"INSERT INTO players (player_id, player_name, registration_date, last_login_date) VALUES ({i}, '{name}', TO_DATE('{registration_date}', 'YYYY-MM-DD'), {last_login_date})")

# commit das alterações no banco de dados
conn.commit()

# fechar o cursor e a conexão com o banco de dados
cursor.close()
conn.close()
