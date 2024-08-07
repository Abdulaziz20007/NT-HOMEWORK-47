class Karta:
    card = {'2': 1,'3': 2,'4': 3,'5': 4,'6': 5,'7': 6,'8': 7,'9': 8,'10': 9,'J': 10,'Q': 11,'K': 12,"A": 13}
    def __init__(self, player, card_name) -> None:
        self.player = player
        self.card_name = str(card_name).upper()

    def compare(self, user):
        if Karta.card[self.card_name] < Karta.card[user.card_name]:
            print(f"{user.player}ning {user.card_name} kartasi katta")
            print(f"{self.player}ning {self.card_name} kartasi kichik")
        elif Karta.card[self.card_name] > Karta.card[user.card_name]:
            print(f"{self.player}ning {self.card_name} kartasi katta")
            print(f"{user.player}ning {user.card_name} kartasi kichik")
        elif Karta.card[self.card_name] == Karta.card[user.card_name]:
            print("Ikkala kartalarham teng:", self.card_name)

player1 = Karta('Player1', 'K')
player2 = Karta('Player2', 'a')

player1.compare(player2)