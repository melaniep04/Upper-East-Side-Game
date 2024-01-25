print('''
                                        _._
                                     .-~ | ~-.
                                     |   |   |
                                     |  _:_  |                    .-:~--.._
                                   .-"~~ | ~~"-.                .~  |      |
                  _.-~:.           |     |     |                |   |      |
                 |    | `.         |     |     |                |   |      |
        _..--~:-.|    |  |         |     |     |                |   |      |
       |      |  ~.   |  |         |  __.:.__  |                |   |      |
       |      |   |   |  |       .-"~~   |   ~~"-.              |   |      |
       |      |   |  _|.--~:-.   |       |       |         .:~-.|   |      |
       |      A   | |      |  ~. |       |   _.-:~--._   .' |   |   |      |
       |      M   | |      |   | |       |  |   |     |  |  |   |   |      |
       |      C   | |      |   | |       |  |   |     |  |  |   |   |      |
       |      |   | |      |   | |       |  |   |     |  |  |   |   |      |
       |      9   | |      |   | |       |  |   |     |  |  |   |   |      |
       |      9   | |      |   | |       |  |   |     |  |  |   |   |      |
      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''') 
print("Hello Upper East Siders, Gossip Girl here.")
print("Looks like there's a mysterious new girl in town with a huge secret.") 
print('''She has a secret that everyone is dying to know. There is only one person she can trust, and she must find out who it is.''')
print('''If she tells the wrong person, she'll lose the game and be so embarrassed that she'll never see the light of day again. If she find the one trustworthy person, she'll win the game and become the most powerful It Girl in New York City.''')
print('''Everyone, make your next series of choices very wisely...''')
print("XOXO Gossip Girl")
print()
print("You're sitting at a coffee shop and notice Serena walks in.")
print("She comes up to you and asks if she can have a moment of your time.")
print("What do you say?")
answer1 = input("Type 'yes' or 'no'.")
if answer1 == "yes":
  print("She was sent there by Chuck to frame you for something. You lose.")
  exit()
else:
  print("She looks confused at your bold response, texts someone, and leaves.") 
print()
print("Later that day, you walk into a library and see Blair and Dan in the corner.")
print("Blair sees you, stands up, and waves you over to their table with a smile.")
print("Do you walk over to them and introduce yourself?")
answer2 = input("Type 'yes' or 'no'.")
if answer2 == "yes":
  print("You get along great so they invite you to a party they're hosting tonight!")
  print("Do you accept the invitation?")
  answer3 = input("Type 'yes' or 'no'.")
  if answer3 == "yes":
    print("Blair gives you her number and tells you to text her later for the address.")
  else:
    print("They judge you and think you're weird for rejecting the invite. You lose.")
    exit()
else:
  print("You walk away and they think you're rude for ignoring them. You lose.")
  exit()
print()
print("On your way home, you see Chuck get out of a taxi and walk up to you.")
print("He asks if you've seen Dan anywhere. He says it's an emergency regarding Rufus.")
print("Do you tell him that you just saw her at the library?")
answer4 = input("Type 'yes' or 'no'.")
if answer4 == "yes":
  print("He thanks you for your transparency and warns you to stay away from Blair.")
else:
  print("He scoffs and says he can tell that you're lying. You lose.")
  exit()
print()
print("You finally make it back to your apartment and hear a knock at your door.")
print("You look through the peephole and see Nate and Serena waiting outside.")
print("You're in the middle of cooking dinner. Do you answer the door?")
answer5 = input("Type 'yes' or 'no'.")
if answer5 == "yes":
  print("They ask you if you're going to Blair and Dan's party tonight.")
  print("Do you tell them about your plans?")
  answer6 = input("Type 'yes' or 'no'.")
  if answer6 == "yes":
    print("They say they'll see you there and leave.")
    print('''This reminds you to text Blair about the address. She sends it and says she's excited to see you there!''')
  else:
    print("They look at each other and tell you not to go under any circumstances.")
    print("They both leave.")
print("Suddenly, there's a new Gossip Girl blast.")
print('''It reads: Uh-oh. Looks like someone's idea isn't going as planned. See you tonight? I guess we'll see.''')
print()
print('''After seeing the Gossip Girl blast you start to get suspicious. Do you still want to go to the party?''')
answer7 = input("Type 'yes' or 'no'.")
if answer7 == "yes":
  print("You decide to get dressed and head over to the party.")
else:
  print("You decide to stay home and not go to the party. You lose.")
  exit()
print()
print("You arrive at the party and Nate immediately pulls you aside.")
print("He asks what you're doing here and if Chuck convinced you to come.")
print("At this point, you're extremely confused. What does Chuck have to do with this?")
print("Before you reply, Blair runs up to you. You notice she was talking with Chuck.")
print("Blair gets upset at Nate and insists that he leave you alone.")
print("Do you walk away and join the party with Blair?")
answer8 = input("Type 'yes' or 'no'.")
if answer8 == "yes":
  print("You have a great time with Blair. She invites you to chat on the balcony.")
  print("Do you go with her?")
  answer9 = input("Type 'yes' or 'no'.")
  if answer9 == 'yes':
    print("She wants to know if you're willing to tell her your big secret.")
    print("Do you tell her?")
    answer10 = input("Type 'yes' or 'no'.")
    if answer10 == 'yes':
      print("Gossip Girl sent a blast exposing your secret minutes after! You lose.")
      exit()
    else:
      print("You say you'll tell her later and go back inside.")
  else: 
    print("She gets defensive and tells you to leave. You lose.")
    exit()
else: 
  print("Blair gets offended but doesn't make a big deal of it. She walks away.")
print()
print("Near the end of the party, Dan pulls you aside. He asks if you're free to talk.")
print("Do you engage in a conversation with him?")
answer11 = input("Type 'yes' or 'no'.")
if answer11 == 'yes':
  print("He asks if you'll share your secret with him for book inspiration.")
  print("Apparently he has writer's block and says he'll never say it was your secret.")
  print("He promises he'll give you a percentage of his book revenue as well.")
  print("Do you trust him with your secret and tell him?")
  answer12 = input("Type 'yes' or 'no'.")
  if answer12 == 'yes':
    print('''He made your story into a book and no one ever found out! You also made hundreds of thousands of dollars from your percentage! You win!''')
  else:
    print("He would've genuinely protected your secret. You lose.")
    exit()
else:
  print("He gets bored and leaves. You lose.")
  exit()
