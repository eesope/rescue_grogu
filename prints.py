"""
Prints information for a user throughout the game.
"""

from default_settings import make_board
from default_settings import make_character

# use font colour change package!!!


def print_grogu():
    print(
        r"""                          
        
        
             &%##%&&&&%.                           .%&&%%#%%##
               &%##%&%%%(&&@@@@&&&&%        ,&&&&&&&&&%#%%%%&%%%#%#%
                 &%&&&&&&&&&%#(*%&&@@@@&&&&&&&&&&&&&@&&##&&%#%###(#(#((%
                  &%&&&&&&&&&&&&&&%%&@&&&&&&@&&&&@@&@&&&&&&&&%&%#((#((((((&
                   &%%&&&&&&%%%&%#/##&&&&&&%&%%#%(#%&&&&&%%#////((%%#*//*//(#%%&%#%%%%%%%%%%%%%%##((#####%%(
                     ,&%%%&%%%%%/*#%&%&%&&.&  .  %(%&&@&%#/#%%#%#(//((/*/**/(##*..,,,,,*****///*//***(,**,
                         &&%%##(*%%%%&%%%&&  ,,    #%&&##/%# *,     */*,**,**....,*,**(/////(#((((*#%(
                             /%/#(%%%%&&&&%%%%&%%%&&%&&#*(##      .(/(*,,.......,,.,***(////((/((#%(
                                 &@&&&&@%&%&&&&%%&&&&%%%#(%%##((((#((/*,,  ..,,.,,****////%(###%/
                                       /(//*/,,(#%(%%%/,,,,**((((//*,*,. .*(/##/#(*.****,/.
                                   *%&#%#(//////(((###(*,,*,,*/***,,..*%##(///#,,,,
                              &&&%(((*.*,//(*/(///***,..  ....,(#%#%%/((%*****,,*,,
                              &%%%#%/(%(&%#(####((//,,/%%%%%#((#/%(%%#(**/,**,*, ,**
                               &&%%&%&%&&&%&&&%#/*,*,%&#%%(#((###(*/**/,*,,,,,..,*///**
                              %&&&&%%%%&&&&%##(. /%&&%#%(%/#(#((,*/*(*/,,,,. .,*/*,*,//(/./
                               *&%&&&&&&&&#(%#,,%&%%%%&%##(#%(((#/**..  .  ****,..*/((/(/*//%(#(/*
                                 &&%%&%#%%#%%/*%%%%%%%%#(/**,,*/(/.*  .,,/*,,,.,,*/(#(///,*(*,*/(%(,
                                 %#&%%%%&%%%/.#%&%%#.*((/(##***/(*. .*/*/*,,,,*/#/(##/**,*,.,*/#(###(/(
                                (######*%#&%(%%%/. .,##*/(#/* .. ..,,,,**,*,*/(//##(*.,,,.,**/((%##(%%%(/
                             #((//(((((((%%%%(, ,**//(#*,/. ...,,,*****#/**,((##(%%(.*,,.,/*(#(*(###%%%%/*
                          (((//*/**/((/(//****,*//*/*/,/*/,./*.*//**/***,,/(((((#(#*.,,.,,((/(#((((/(((/#(((/(/ 
                          """)


def print_board():
    board = make_board()
# how to print map in grid or any graphical way

print_board()


def print_character():
    print(make_character())


def start_game(user_name):
    print(f"{user_name}\n")

    print(r"""
    Your precious Grogu has been kidnapped by remnants of an evil empire. 
    They have ambitions to use Grogu’s mysterious powers to rule the galaxy. 
    But because young Grogu is still an apprentice to become a Mandalorian, 
    he lacks the power to defeat the villain on his own. 
    Who knows what disaster will befall Grogu if you don‘t save him quickly? 
    Right now, you must use both your intellect and brute strength to fight the villains and rescue Grogu, 
    who has been kidnapped at the edge of the galaxy. 
    The variety of weapons and sturdy armor you will acquire on this journey 
    will definitely help you in your duel with the villains. Show us your abilities to the fullest. 
    Now let’s go rescue Grogu!
    """)


def congrats_message(user_name):
    print(f"    Congratulations, {user_name}!\n")

    print(r"""
    You finally rescued Grogu! 
    For the first time in a very long time, he fell into a deep sleep in your arms. 
    Now, with your help, he can continue his training as a Mandalorian. 
    Thanks to your extraordinary courage and wisdom, the entire galaxy has been freed from the clutches of evil. 
    There are probably many people in other galaxies who need your help. 
    I can already hear the sound of the Razer Crest engine. 
    I am so sad to let you go, but I will remember you. Goodbye, our brave hero!
    """)