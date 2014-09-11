from random import randint
class Card(object):
    """Задаём карты, с возможностью сгенерить карту,
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
    """Задаём колоду, с генератором случайной стандартной колоды,
        возможностью умножения на число для игры в 21
        с несколькими колодами (в игре не реализовано"""
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
class Character(object):
    """Задаёт игроков (для дилера и игрока), с вытягиванием карты,
         оценкой руки и представлением руки пользователю"""
    name = "Dealer"
    deck = Deck.generate_new_deck()
    def __init__(self):
        self.hand = []
    def draw_card_deck(self,deck):
        take = randint(0,len(self.deck) - 1)
        self.hand.append(self.deck[take])        
        print("{0} draws {1} \n".format(self.name,self.deck[take]))
        del self.deck[take]
    def hand_val(self):
        total = 0
        for i in range(len(self.hand)):
            total += Card.value(self.hand[i])
        return total
    def show_hand(self):
        print("{} hand is\n".format(self.name))
        for i in range(len(self.hand)):
            print(str(self.hand[i]) + "\n")
d = Character()
class Player(Character):
    bank = 100
    #деньги на руках
    cur_bet = 0
    #текущая ставка
    name = ""
    """За неименим лучшего в голове, все случаи игры (по правилам из вики)
        со всеми коряками правил для упрощения вынесены в отдельные методы
        для упрощения чтения"""
    def bank_show(self):
        print(self.bank)
    def blackjack(self):
        #для блекджека
        print("Blackjack! You won {0}, mr. {1}!".\
              format(cur_bet * 1.5, self.name))
        self.bank = self.bank + self.cur_bet * 2.5
    def bj_retreat(self):
        #для ситуации с пасом при 10 и обычного выигрыша
        print("Alrighty, you win {0}, mr. {1}!".\
              format(self.cur_bet, self.name))
        self.bank = self.bank + self.cur_bet * 2
    def deal_win(self):
        print("Casino wins.")
    def much(self):
        print("Sorry, that's too much, you lost {0}, mr. {1}.".\
              format(self.cur_bet, self.name))
    def leave(self):
        print\
("Congratulations! {0} wishes to return to the real world with {1} imaginary coins! \n".\
              format(self.name,self.bank))
        p.bank = 0
    def deal_good(self):
        #расклад ситуации с 10 у дилера
        while True:
            n = input("Would you like to test your luck? print y or n")
            if n == "y":
                while d.hand_val < 17:
                    d.draw_card_deck(self.deck)
                    input()
                    if d.hand_val == 21:
                        d.show_hand()
                        print("Duece! You get your bet back!")
                        self.bank = self.bank + self.cur_bet
                        break
                    else:
                        d.show_hand()
                        self.blackjack
                        break
                    break
            elif n == "n":
                self.bj_retreat()
                break
            else:
                print("I'm sorry, mr. {}, what'd  you mean?".\
                      format(self.name))
                continue
    def bad_both(self):
        #расписывана ситуация "не зашло"
        while True:
            n = input("Would you like to draw another card? print y or n")
            if n == "y":
                self.draw_card_deck(self.deck)
                input()
                if self.hand_val() > 21:
                    self.show_hand()
                    self.much()
                    break
                else:
                    continue
            elif n == "n":
                while d.hand_val() < 17:
                    d.draw_card_deck(self.deck)
                    input()
                    continue
                d.show_hand()
                if d.hand_val() > 21:
                    self.bj_retreat()
                    break
                elif self.hand_val() > d.hand_val():
                    self.bj_retreat()
                    break
                elif self.hand_val() == d.hand_val():
                    print("Duece! You get your bet back!")
                    self.bank = self.bank + self.cur_bet
                    break
                else:
                    self.deal_win()
                    break
            else:
                print("I'm sorry, mr. {}, what'd  you mean?".\
                      format(self.name))
                continue

    def start_round(self):
        #общий цикл для игры, запускающий подварианты
        d.deck = Deck.generate_new_deck()
        self.cur_bet = int(input("Enter your bet: \n"))
        if self.cur_bet > self.bank or self.bank == 0:
            print("Inner voice of reason: you don't have enough money, just {} \n").\
                         format(self.bank)
        else:
            self.bank = self.bank - self.cur_bet
            self.draw_card_deck(self.deck)
            input()
            d.draw_card_deck(self.deck)
            input()
            self.draw_card_deck(self.deck)
            input()
            self.show_hand()
            input()
            if self.hand_val == 21 and d.hand_val < 10:
                self.blackjack()
            elif p.hand_val == 21:
                self.deal_good()
            else:
                 self.bad_both()
            self.hand = []
            d.hand = []
    def help(self):
        #список команд с описанием
        print("Start - starts a new blackjack round\n")
        print("Leave - leave the casino with your money\n")
        print("Bank - displays your money left\n")
        print("Help - displays available commands")

p = Player()
x = p.bank
Commands = {"start" : p.start_round,
            "leave" : p.leave,
            "bank" : p.bank_show,
            "help" : p.help,
}

p.name = input("Welcome to Blackjack 0.1a. What is your name, sir?\n")
print("To see commands - print help\n")
print\
("Don't forget to input something or press Enter to continue the game")
while(p.bank > 0):
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
 



                    
        
    

        
