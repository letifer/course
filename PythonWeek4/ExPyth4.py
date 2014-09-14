from random import randint
import sys
class Card:
    """Карты, с возможностью сгенерить случайную,
        вычислением очков для 21, сравнением карт и
        представлением их пользователю"""
    suit_var = ["Spades","Hearts", "Clubs", "Diamonds"]
    rank_var = ["Ace","King", "Queen", "Jack", "10",\
                "9","8","7","6","5","4","3","2"]
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def value(self):
        if self.rank == "Ace":
            return 11
        elif self.rank == "King" or self.rank == "Queen"\
             or self.rank == "Jack":
            return 10
        else:
            return int(self.rank)
    def generate_random_card():
        x = randint(0,len(Card.suit_var) - 1)
        y = randint(0,len(Card.rank_var) - 1)
        l = Card(Card.suit_var[x],Card.rank_var[y])
        return l
    def card_eq(x,y):
        if x.rank == y.rank and x.suit == y.suit:
            return True
        else:
            return False
    def __str__(self):
        return "{0} of {1}".format(self.rank,self.suit)
class Deck(list):
    """Колода, с генератором случайной стандартной колоды,
        возможностью умножения на число для игры в 21
        с несколькими колодами (в игре не реализовано)"""
    deck_quant = 1
    def __append__(self,value):
        if isinstance(value,Card):
            return super().__append__(self,value)
        else:
            return "Not a card"
    def __contains__(self,value):
        for x in range(len(self)):
            if Card.card_eq(self[x],value):
                return True
            else:
                continue
            return False
    def generate_new_deck():
        new_deck = Deck()
        while len(new_deck) < 52:
            x = Card.generate_random_card()
            if x in new_deck:
                continue
            else:
                new_deck.append(x)
        return new_deck
    def __mul__(self,val):
        mult_deck = Deck()
        n = 0
        for i in range(len(self)):
            while n < val:
                mult_deck.append(self[i])
                n += 1
                continue
            n = 0
            continue
        return mult_deck
class Character:
    """Задаёт игроков (для дилера и игрока), с вытягиванием карты,
         оценкой руки и представлением руки пользователю"""
    name = "Dealer"
    deck = Deck.generate_new_deck()
    def __init__(self):
        self.hand = []
    def draw_card_deck(self):
        take = randint(0,len(self.deck) - 1)
        self.hand.append(self.deck[take])        
        print("{0} draws {1} \n".format(self.name,self.deck[take]))
        del self.deck[take]
    def hand_val(self):
        total = 0
        ace_cnt = 0
        for i in range(len(self.hand)):
            if Card.value(self.hand[i]) == 11:
                ace_cnt += 1
                total += Card.value(self.hand[i])
            else:
                total += Card.value(self.hand[i])
        if total > 21:
            total = total - 10 * ace_cnt
        return total
    def show_hand(self):
        print("{} hand is\n".format(self.name))
        for i in range(len(self.hand)):
            print(str(self.hand[i]) + "\n")
d = Character()
class Player(Character):
    """Игрок, с самой игрой"""
    def __init__(self,bank,cur_bet):
        self.hand = []
        self.bank = bank
        self.cur_bet = cur_bet
    name = ""
    def bank_show(self):
        print(self.bank)
    def leave(self):
        print\
("Congratulations! {0} wishes to return to the real world with {1} imaginary coins! \n"\
 .format(self.name,self.bank))
        p.bank = 0
        sys.exit(0)
    def start_round(self):
        """Начинает новый раунд, создавая новую колоду и обнуляя руки,
        игрок самостоятельно берёт карты и решает,когда закончить раунд"""
        d.deck = Deck.generate_new_deck()
        self.hand = []
        d.hand = []
        self.cur_bet = int(input("Enter your bet: \n"))
        if self.bank == 0:
            print("You got kicked out of casino for having no money!")
            self.leave()
        else:
            while self.cur_bet > self.bank :
                print("Inner voice of reason: you don't have enough money, only {} available \n"\
                  .format(self.bank))   
                self.cur_bet = int(input("Enter your bet: \n"))
                continue
            self.bank = self.bank - self.cur_bet
            d.draw_card_deck()
            print("To draw a card print draw\n")
            print("To stop drawing and finish the round print result\n")
    def result(self):
        """Добирает дилеру карты в руку, сравнивает с картами игрока
        и выдаёт результат, изменняя банк игрока в зависимости от исхода"""
        if self.hand_val() == 0:
            print("You need to start a game first and draw a card.\n")
        else:
            self.show_hand()
            if self.hand_val() > 21:
                print("Sorry, that's too much, you lost {0}, mr. {1}."\
                      .format(self.cur_bet, self.name))
            else:
                while d.hand_val() < 17:
                    d.draw_card_deck()
                d.show_hand()
                if d.hand_val() > 21:
                    print("You win {}! \n".format(self.cur_bet))
                    self.bank = self.bank + self.cur_bet * 2
                elif self.hand_val() ==  d.hand_val():
                    print("Deuce! You get your bet back!\n")
                    self.bank = self.bank + self.cur_bet
                elif self.hand_val() == 21:
                    print("Blackjack! You won {0}, mr. {1}!"\
                          .format(self.cur_bet * 1.5, self.name))
                    self.bank = self.bank + self.cur_bet * 2.5
                elif self.hand_val() > d.hand_val():
                    print("You win {}! \n".format(self.cur_bet))
                    self.bank = self.bank + self.cur_bet * 2
                else:
                    print("Casino wins. You lost {}\n".format(self.cur_bet))
            d.hand = []
        self.hand = []
        self.cur_bet = 0
    def help(self):
        #список команд с описанием
        print("Start - starts a new blackjack round\n")
        print("Draw - draws a new card\n")
        print("Hand - displays your current hand\n")
        print("Dealer - displays dealer's hand\n")
        print("Result - stop drawing and see if you could win the dealer\n")
        print("Leave - leave the casino with your money\n")
        print("Bank - displays your money left\n")
        print("Help - displays available commands")

p = Player(100,0)
Commands = {"start" : p.start_round,
            "draw" : p.draw_card_deck,
            "hand" : p.show_hand,
            "dealer" : d.show_hand,
            "result" : p.result,
            "leave" : p.leave,
            "bank" : p.bank_show,
            "help" : p.help,
}

p.name = input("Welcome to Blackjack 0.1a. What is your name, sir?\n")
print("To see commands - print help\n")
while(p.bank >= 0):
    #тут спасибо Balau за решение
  line = input("> ")
  args = line.split()
  if len(args) > 0:
    commandFound = False
    for c in Commands.keys():
      if args[0] == c[:len(args[0])]:
        Commands[c]()
        commandFound = True
        break
    if not commandFound:
      print("Incorrect command")
print("Thank you for playing the game!")


                    
        
    

        
