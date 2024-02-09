# LIBRARIES

import random
import os
import sys


# FUNCTION

def generate_board(lenght):
    # random for start position
    user_col = random.randint(0, lenght - 1)
    user_row = random.randint(0, lenght - 1)
    # random for exit position
    exit_col = random.randint(0, lenght - 1)
    exit_row = random.randint(0, lenght - 1)

    board = list(list(["⬜️"] * lenght) for a in range(lenght))
    board[user_row][user_col] = "⬛️"
    board[exit_row][exit_col] = "⛳️"
    return user_row, user_col, exit_col, exit_row, board


def show_board(board: list):
    for b in board:
        print("".join(map(str, b)))
    return


def movement(user_row, user_col, exit_col, exit_row, board, lenght):
    board[user_row][user_col] = "⬜️"
    available = ["N", "S", "E", "O"]
    position = input("\nOn vols anar? [N, S, E, O]  ")
    position = position.upper()

    if position in available:
        if position == "N":
            if (user_row - 1) < 0:
                print("\nOut of board")
                return movement(user_row, user_col, board, lenght)
            else:
                user_row -= 1
                user_col += 0
        elif position == "S":
            if (user_row + 1) >= lenght:
                print("\nFora del taulell")
                return movement(user_row, user_col, board, lenght)
            else:
                user_row += 1
                user_col += 0
        elif position == "E":
            if (user_col + 1) >= lenght:
                print("\nOut of board")
                return movement(user_row, user_col, board, lenght)
            else:
                user_row += 0
                user_col += 1
        else:  # pos = "O"
            if (user_col - 1) < 0:
                print("\nOut of board")
                return movement(user_row, user_col, board, lenght)
            else:
                user_row += 0
                user_col -= 1
        question(random.randint(0, 20))
        if user_row == exit_row and user_col == exit_col:
            return exit_game()
        else:
            return user_row, user_col
    else:
        print("Incorrect position [N, S, E, O]")
        return movement(user_row, user_col, board, lenght)


def question(n: int):
    # 100 questions by ChatGPT
    quest = [
        ["¿Quién escribió 'Cien años de soledad'?", "García Márquez"],
        ["¿Cuál es la capital de Japón?", "Tokio"],
        ["¿En qué año se fundó la Organización de las Naciones Unidas (ONU)?", "1945"],
        ["¿Cuál es el río más largo del mundo?", "Amazonas"],
        ["¿Quién pintó 'La Mona Lisa'?", "Da Vinci"],
        ["¿Cuándo comenzó la Revolución Francesa?", "1789"],
        ["¿Qué país es conocido como 'La Tierra del Sol Naciente'?", "Japón"],
        ["¿Cuál es la moneda oficial de Australia?", "Dólar australiano"],
        ["¿Quién fue el primer presidente de Estados Unidos?", "Washington"],
        ["¿En qué continente se encuentra el desierto del Sahara?", "África"],
        ["¿Cuál es el océano más grande del mundo?", "Pacífico"],
        ["¿Quién escribió 'Romeo y Julieta'?", "Shakespeare"],
        ["¿Cuál es la montaña más alta del mundo?", "Everest"],
        ["¿En qué año terminó la Segunda Guerra Mundial?", "1945"],
        ["¿Cuál es la capital de Italia?", "Roma"],
        ["¿Quién fue el líder espiritual de la India que predicó la no violencia?", "Gandhi"],
        ["¿Cuál es el sistema político de China?", "Comunismo"],
        ["¿Quién fue la reina de Egipto conocida por su relación con Marco Antonio y Julio César?", "Cleopatra"],
        ["¿En qué año se inauguró la Torre Eiffel en París?", "1889"],
        ["¿Cuál es el país más grande del mundo por área?", "Rusia"],
        ["¿Quién fue el primer hombre en llegar a la luna?", "Armstrong"],
        ["¿Qué famoso científico formuló la teoría de la relatividad?", "Einstein"],
        ["¿En qué año se descubrió América?", "1492"],
        ["¿Quién fue el líder surafricano que luchó contra el apartheid?", "Mandela"],
        ["¿Cuál es el principal componente del aire que respiramos?", "Oxígeno"],
        ["¿Cuál es la capital de Canadá?", "Ottawa"],
        ["¿Quién fue el autor de 'Don Quijote de la Mancha'?", "Cervantes"],
        ["¿Cuál es el océano más pequeño del mundo?", "Ártico"],
        ["¿Qué civilización construyó las pirámides en Egipto?", "Egipcia"],
        ["¿Cuál es el continente más poblado?", "Asia"],
        ["¿Quién fue el famoso líder militar y dictador francés durante las Guerras Napoleónicas?", "Napoleón"],
        ["¿Cuál es el segundo planeta más cercano al sol en nuestro sistema solar?", "Venus"],
        ["¿Qué ciudad es conocida como la 'Ciudad Eterna'?", "Roma"],
        ["¿Cuál es el país más poblado del mundo?", "China"],
        ["¿Quién pintó 'La Noche Estrellada'?", "Van Gogh"],
        ["¿Cuál es la capital de Rusia?", "Moscú"],
        ["¿Quién fue el fundador de Microsoft?", "Bill Gates"],
        ["¿Cuál es la moneda oficial de Japón?", "Yen"],
        ["¿En qué año se declaró la independencia de Estados Unidos?", "1776"],
        ["¿Quién fue el autor de 'El Principito'?", "Saint-Exupéry"],
        ["¿Cuál es el país más pequeño del mundo por área?", "Ciudad del Vaticano"],
        ["¿Quién fue el primer presidente de México?", "Hidalgo"],
        ["¿Cuál es el río más largo de Europa?", "Volga"],
        ["¿Qué país es conocido como 'La Tierra de los Faraones'?", "Egipto"],
        ["¿Cuál es la capital de Argentina?", "Buenos Aires"],
        ["¿Quién escribió '1984'?", "Orwell"],
        ["¿Cuál es la moneda oficial de Reino Unido?", "Libra esterlina"],
        ["¿En qué año se inauguró el Canal de Panamá?", "1914"],
        ["¿Quién fue la primera mujer en el espacio?", "Gagarin"],
        ["¿Cuál es la capital de España?", "Madrid"],
        ["¿Quién fue el famoso compositor de la 'Quinta Sinfonía'?", "Beethoven"],
        ["¿En qué país se celebró la primera Copa Mundial de la FIFA?", "Uruguay"],
        ["¿Cuál es la capital de China?", "Pekín"],
        ["¿Quién escribió 'Matar a un ruiseñor'?", "Harper Lee"],
        ["¿En qué año se firmó la Declaración de Independencia de Estados Unidos?", "1776"],
        ["¿Quién fue el líder de la Revolución Rusa en 1917?", "Lenin"],
        ["¿Cuál es la capital de Canadá?", "Ottawa"],
        ["¿Quién fue el famoso pintor mexicano conocido por sus obras surrealistas?", "Frida Kahlo"],
        ["¿En qué año se produjo la caída del Muro de Berlín?", "1989"],
        ["¿Quién fue el líder de la Revolución Cubana?", "Fidel Castro"],
        ["¿Cuál es la capital de Sudáfrica?", "Pretoria"],
        ["¿Quién fue la última reina de Francia antes de la Revolución Francesa?", "María Antonieta"],
        ["¿En qué año se inauguró el Canal de Suez?", "1869"],
        ["¿Quién fue el filósofo griego considerado el padre de la filosofía occidental?", "Sócrates"],
        ["¿Cuál es la capital de Australia?", "Canberra"],
        ["¿Quién fue el líder militar y político de la antigua Roma conocido por cruzar los Alpes con elefantes?",
         "Aníbal"],
        ["¿En qué año se estableció la Declaración Universal de Derechos Humanos?", "1948"],
        ["¿Quién fue el primer emperador de China?", "Qin Shi Huang"],
        ["¿Cuál es la capital de India?", "Nueva Delhi"],
        ["¿Quién fue el famoso físico británico conocido por su teoría de la relatividad general?", "Stephen Hawking"],
        ["¿En qué año se celebró la primera Olimpiada moderna?", "1896"]]

    print("\nAnswer below question!\n")
    print("-" * 15)
    q = input(f"{quest[n][0]}   \n")
    print("-" * 15)
    if q.lower() == quest[n][1].lower():
        return
    else:
        print("\n🛑 Wrong answer!")
        return question(random.randint(0, 20))


def exit_game():
    print()
    print("🎊" * 9)
    print("  You rock!!")
    print("🎊" * 9)
    sys.exit()


# MAIN

if __name__ == "__main__":

    lenght = 10
    user_row, user_col, exit_col, exit_row, board = generate_board(lenght)
    while True:
        print("\n")
        show_board(board)
        user_row, user_col = movement(user_row, user_col, exit_col, exit_row, board, lenght)
        board[user_row][user_col] = "⬛️"
        os.system('clear')
