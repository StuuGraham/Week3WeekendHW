from app.models.choices import *
from app.models.player import *
class Game():

    def play_game(player1, player2):
        if player1.choice == Choice.Rock and player2.choice == Choice.Paper:
            return f"{player2.name} wins! Paper covers Rock!!"

        elif player1.choice == Choice.Rock and player2.choice == Choice.Scissors:
            return f"{player1.name} wins! Rock smashes Scissors!!"

        elif player1.choice == Choice.Paper and player2.choice == Choice.Rock:
            return f"{player1.name} wins! Paper covers Rock!!"

        elif player1.choice == Choice.Paper and player2.choice == Choice.Scissors:
            return f"{player2.name} wins! Scissors cuts Paper!!"

        elif player1.choice == Choice.Scissors and player2.choice == Choice.Rock:
            return f"{player2.name} wins! Rock smashes Scissors!!"

        elif player1.choice == Choice.Scissors and player2.choice == Choice.Paper:
            return f"{player1.name} wins! Scissors cuts Paper!!"

        elif player1.choice == player2.choice:
            return "It's a draw! Try again!"