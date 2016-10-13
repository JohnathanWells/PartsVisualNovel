## The script of the game goes in this file.

## Declare characters used by this game. The color argument colorizes the name
## of the character.

define Rin = Character('Armored Woman', who_color = '#ffd700')
define Huang = Character('Eyepatch Man', who_color = '#006400')
define Suoh = Character('Red Armor Man', who_color = '#8b0000')
define Tojai = Character('Tojaiwa', who_color = '#ffffff')
define Shichi = Character('Shichi', who_color = '#add8e6')

## The game starts here.

label start:

    ## Show a background. This uses a placeholder by default, but you can add a
    ## file (named either "bg room.png" or "bg room.jpg") to the images
    ## directory to show it.

    scene bg black

    ## This shows a character sprite. A placeholder is used, but you can replace
    ## it by adding a file named "eileen happy.png" to the images directory.

    ##show eileen happy

    ## These display lines of dialogue.

    "A circular meeting room stands in silence. It stays in that emptiness for a couple of seconds before three doors open simultaneously from the sides and three tall figures enter the room."

    "One is a tall, strong man in his early 40s. His hair is so long that it can be seen from the sides of the helmet, and his red eyes match the color of his armor,"

    "The second figure is a little shorter and noticeably older and wiser-looking. His experience is evident by the patch covering his left eye, but it is his right silver eye what retains the suffering of what he had been through,"

    "The third figure is a lady. She looks much younger compared to the men, but also more ferocious and cunning. Her amber eyes look focused and serious, like she is planning every step she takes."

    "The three figures are wearing armor, and each is one followed by a formally dressed white-haired servant carrying a sword. These stay awkwardly on their feet as their masters take a seat, each one from equal distance to the other two."

    "The lady directs her vision towards the man with the eyepatch, then the man with the red armor"

    show Rin at right
    with Dissolve(0.3)

    Rin "Huang Senboshi-san… Suoh Amedu-san… I trust you both read the reason for this meeting in the letter I send you."

    show Huang at left
    with Dissolve(0.3)
    pause(0.3)

    Huang "The Senboshi Clan is willing to hear what you have to say, Rin-san. But we are not going to agree until a couple of matters have been solved. Especially between the Amedu and us."

    $ Rin = Character('Armored Woman (Rin)', who_color = '#ffd700')

    hide Huang
    with Dissolve(0.2)

    show Suoh at left
    with Dissolve(0.3)

    Suoh "The Amedu Clan is willing to listen to the proposal, but do not expect much after what the Hinteru did to my son."

    Rin "Suoh, may I need to remind you what you did to my son? Considering the situation the Senboshi have put you in, I would say I am being very generous in giving you the opportunity to sign this treaty, instead of letting the Senboshi crush you."

    $ Rin = Character('Young Rin')
    $ Huang = Character('Eyepatch Man (Huang)', who_color = '#006400')
    $ Suoh = Character('Red Armor Man (Suoh)', who_color = '#8b0000')

    Suoh "We will not surrender. It’s just a matter of time for the tides to turn and when that happens this war will be ours."

    hide Rin
    with Dissolve(0.2)

    show Huang at right
    with Dissolve(0.3)

    Huang "Keep dreaming punk."

    Suoh "What did you just call me?"

    Huang "A punk. You clearly have no idea of the situation your clan is into."

    Suoh "I am going to make you suffer like we did to your son, old man."

    Huang "What did you just say, you insolent piece of-?"

    show Rin at center
    with Dissolve(0.1)

    $ Huang = Character('Huang', who_color = '#006400')
    $ Suoh = Character('Suoh', who_color = '#8b0000')

    Rin "Enough of you two!. I called you here to discuss peace, not for you to act like kids and settle your fights. We all have lost someone in this chaos, deal with it." with vpunch

    Huang "..."

    Suoh "..."

    hide Huang 
    with Dissolve(0.4)

    hide Suoh
    with Dissolve(0.4)

    Rin "I think we can all agree that the war have gone for too long. We took down the Ibuma to get rid of their abuses on Rigutochi and its components, but went right to killing each other after that. I think it is time we finally end the chain of tragedy that we got into."

    Rin "Tojaiwa, papers"

    Tojai "Yes madam"

    "The white haired woman standing behind Rin hands her three envelopes. Rin takes them and puts the other two in the direction of each men. The servant of both start walking in their direction but they stop them with a gesture"

    show Suoh at left
    with Dissolve(0.3)

    show Huang at right
    with Dissolve(0.3)

    ## This ends the game.

    return
