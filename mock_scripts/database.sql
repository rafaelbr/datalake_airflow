-- Players table
CREATE TABLE players (
  player_id SERIAL PRIMARY KEY,
  player_name VARCHAR(255),
  email_address VARCHAR(255),
  password VARCHAR(255),
  registration_date DATE,
  last_login_date DATE
);

-- Games table
CREATE TABLE games (
  game_id SERIAL PRIMARY KEY,
  game_name VARCHAR(255),
  game_start_date DATE,
  game_end_date DATE,
  game_winner INTEGER REFERENCES players(player_id),
  game_status VARCHAR(10)
);

-- Game Players table
CREATE TABLE game_players (
  game_player_id SERIAL PRIMARY KEY,
  game_id INTEGER REFERENCES games(game_id),
  player_id INTEGER REFERENCES players(player_id),
  join_date DATE,
  leave_date DATE
);

-- Characters table
CREATE TABLE characters (


);

-- Inventory table
CREATE TABLE inventory (
  inventory_id SERIAL PRIMARY KEY,
  item_name VARCHAR(255),
  item_quantity INTEGER,
  character_id INTEGER REFERENCES characters(character_id)
);

-- Currency table
CREATE TABLE currency (
  currency_id SERIAL PRIMARY KEY,
  currency_type VARCHAR(255),
  currency_amount INTEGER,
  player_id INTEGER REFERENCES players(player_id)
);

-- Events table
CREATE TABLE events (
  event_id SERIAL PRIMARY KEY,
  event_type VARCHAR(255),
  event_date DATE,
  player_id INTEGER REFERENCES players(player_id),
  game_id INTEGER REFERENCES games(game_id),
  character_id INTEGER REFERENCES characters(character_id)
);