## The script of the game goes in this file.

label variableDeclaration:
    
    #Variables
    init:
        $ fadein = Dissolve(0.3)
        $ fadeout = Dissolve(0.2)
        $ dfadeout = Dissolve(0.4)
    
    $ Confidence = 0
    $ Knowledge = 0
    $ Respect = 0
    $ Naibu_Affection = 10
    $ Tojai_Affection = 15
    $ Tai_Affection = 0
    $ Gekai_Affection = 0

    define RinName = "Armored Woman"
    define HuangName = "Eyepatch Man"
    define SuohName = "Red Armor Man"

    #Characters
    define Rin = DynamicCharacter("RinName", who_color = '#ffd700')
    define Huang = DynamicCharacter("HuangName", who_color = '#008400')
    define Suoh = DynamicCharacter("SuohName", who_color = '#ca0000')
    define Tojai = Character('Tojaiwa', who_color = '#ffffff')
    define Shichi = Character('Shichi', who_color = '#add8e6')
    define Naibu = Character('Naibu', who_color = "#3366ff")

    #Chara Pictures
    ##Rin
    image Rin yserious = "ch/rh/rin_happy.png"
    image Rin ySadSmile = "ch/rh/rin_happy.png"
    image Rin ySlightAngry = "ch/rh/rin_happy.png"
    image Rin yangry = "ch/rh/rin_happy.png"
   
    image Rin serious = "ch/rh/rin_happy.png"
    image Rin happy = "ch/rh/rin_happy.png"
    image Rin smiling = "ch/rh/rin_happy.png"
    image Rin surprised = "ch/rh/rin_happy.png"
    image Rin smug = "ch/rh/rin_happy.png"

    ##Naibu
    #image Naibu smiling 

    ##Tojai

    #Background Pictures
    image bg Black = "bg/black.png"
    image bg centralMeetingRoom = "#ffffff"
    image bg shichiRoom = "#fffffa"

    #Still Pictures
    image birthdaySurprise = "bg/black.png"

    #Sounds
    define audio.rustlingPaper = "<silence 0.5>"
    define audio.doorSlam = "<silence 0.5>"
    define audio.doorOpening = "<silence 0.5>"
    define audio.doorClosing = "<silence 0.5>"
    define audio.objectFall = "<silence 0.5>"
    define audio.silverware = "<silence 0.5>"
    define audio.walkingDownstairs = "<silence 0.5>"
    define audio.applauses = "<silence 0.5>"
    define audio.doorKnock = "<silence 0.5>"
    define audio.chair = "<silence 0.5>"
    define audio.silence = "<silence 1.0>"

    #Music
    define audio.serious = "<silence 0.5>"
    define audio.happy = "<silence 0.5>"
    define audio.refined = "<silence 0.5>"
    define audio.urban = "<silence 0.5>"
    define audio.tense = "<silence 0.5>"

    return

## The game starts here.
label start:

    ## Show a background. This uses a placeholder by default, but you can add a
    ## file (named either "bg room.png" or "bg room.jpg") to the images
    ## directory to show it.
    label .scene1:

        scene bg Black
        with Dissolve(1.0)

        pause(2)

        play music serious
        play sound doorOpening
        scene bg centralMeetingRoom
        with Dissolve(1.0)

        "A circular meeting room stands in silence."
        "It stays in that emptiness for a couple of seconds before three doors open simultaneously from the sides and three tall figures enter the room."

        play sound doorClosing

        show Suoh at left
        with fadein

        "One is a tall, strong man in his early 40s."
        "His hair is so long that it can be seen from the sides of the helmet, his red eyes match the color of his armor."

        hide Suoh
        with fadeout

        show Huang at right
        with fadein

        "The second figure is a little shorter and noticeably older"
        "His experience is evident by the patch covering his left eye, but it is his right silver eye what retains the suffering of what he had been through,"

        hide Huang
        with fadeout

        show Rin yserious at center
        with fadeout

        "The third figure is a lady. She looks much younger compared to the men, but also more ferocious and cunning."
        "Her amber eyes look focused and serious, like every move she makes is coldly calculated."

        hide Rin
        with fadeout

        pause(0.2)

        "Each figure is followed by a different white-haired servant, each one formally-dressed and carrying a sword."
        play sound chair
        "These stay awkwardly on their feet behind their masters kneel take a seat, each warlord is at the same distance from the other two."

        pause(0.2)
        show Rin yserious at right
        with fadeout

        "The armored lady directs her vision towards the man with the eyepatch, then the man with the red armor"

        Rin "...Huang Senboshi-san..."
        Rin "...Suoh Amedu-san..."
        Rin "...I trust you both read the reason for this meeting in the letter I sent you."

        show Huang at left
        with fadein
        pause(0.3)

        Huang "The Senboshi Clan is willing to hear what you have to say, Rin-san. But we are not going to agree until a couple of matters have been solved. Especially between the Amedu and us."

        $ RinName = "Armored Woman (Rin Hinteru)"

        hide Huang
        with fadeout

        show Suoh at left
        with fadein
        pause(0.3)

        Suoh "The Amedu Clan is willing to listen to the proposal, but do not expect much after what the Hinteru did to my son."

        Rin "Suoh, he charged right to us in the middle of the battle."
        Rin "It is also very hypocritical of you to complain about that after what you did to {b}my{/b} son."
        Rin "Considering the situation the Senboshi have put you in, I would say I am being very generous in giving you the opportunity to sign this treaty, instead of letting the Senboshi crush you."

        $ RinName = "Rin Hinteru"
        $ HuangName = "Eyepatch Man (Huang Senboshi)"
        $ SuohName = "Red Armor Man (Suoh Amedu)"

        Suoh "We will not surrender. It’s just a matter of time for the tides to turn and when that happens this war will be ours."

        hide Rin
        with fadeout

        show Huang at right
        with fadein

        Huang "Keep dreaming punk."

        Suoh "What did you just call me?"

        Huang "A punk. You clearly have no idea of the situation your clan is into."

        Suoh "I am going to make you suffer like we did to your son, old man."

        Huang "What did you just say, you insolent piece of-?"

        show Rin ySlightAngry at center

        $ HuangName = "Huang Senboshi"
        $ SuohName = "Suoh Amedu"

        Rin "Enough of you two! I called you here to discuss peace, not for you to act like kids and settle your fights." with vpunch
        Rin "We all have lost someone in this chaos, deal with it."

        Huang "..."

        Suoh "..."

        hide Huang 
        hide Suoh
        with dfadeout

        Rin "I think we can all agree that the war have gone for too long."
        Rin "We took down the Ibuma to get rid of their abuses on Rigutochi and its components, but went right to killing each other after that."
        
        show Rin yserious

        Rin "I think it is time we finally end the chain of tragedy that we got into."
        Rin "Tojaiwa, papers"

        Tojai "Yes madam"
        
        play sound rustlingPaper

        "The white haired woman standing behind Rin hands her three envelopes. Rin takes them and puts the other two in the direction of each men."
        "The servant of each one slowly comes close to the papers and picks the respective envelope"

        show Suoh at left
        show Huang at right
        with Dissolve(0.5)

        pause(1.0)
        play sound rustlingPaper

        Rin "I will give you some minutes to skim over it before we start discussing them."

        "..."
        pause(5.0)

        Huang "You want to divide the country in four provinces? Why would you do that?"
        Huang "I would assume one is for the Senboshi and the other two for the Amedu and Hinteru"
        Huang "However, why would we need a fourth one?"

        Rin "It could serve as a middle ground where none of us has control over the other,"
        Rin "Much like the area where we stand now."

        Suoh "What about territory distribution?"
        Suoh "On behalf of the Amedu, I refuse to accept the deal if we get stuck with just what we have now."
        
        Huang "Because you are losing"

        Suoh "Would you just shut the-"

        Rin "The Hinteru are willing to negotiate some territorial disputes with the Amedu."
        Rin "However, we also would like that the Senboshi return a part of our territory they took recently"

        Huang "That is not something I can decide right now"

        Rin "And I do not expect you to, Huang-san."
        show Rin ySlightAngry
        Rin "But I demand a halt to the fight while we decide the terms under which a treaty is possible, if at all."

        Huang "We are not taking our military forces back, Rin-san."

        Suoh "Neither are the Amedu. We are not foolish to fall for such an obvious betrayal from the Hinteru."
        
        show Rin yserious

        Rin "I suppose the reputation of my husband has given everyone the wrong impression of the family."
        show Rin ySlightAngry
        Rin "We are honorable people, we always fulfill our part of the deal."
        Rin "And if that is not enough for you to trust me, let me make myself clear here:"
        Rin "I do not feel sympathy for the Amedu clan or the Senboshi clan."
        show Rin yangry
        Rin "Any esteem or respect I had for our comrades in the Rigu Revolution vanished the day I had to bury my firstborn"
        Rin "I could crush you both, just like my husband wanted, and take control of this whole island and make your families serve mine" with Dissolve(0.3)
        pause(1)
        show Rin yserious
        Rin "But I will not."
        Rin "Like I said, I am tired of this war. I lost most of my children because of it, and so have you two."
        Rin "We destroyed the lands we swore to fight for, we killed the friends that previously stood with us, we executed those who we swore to protect."
        show Rin yangry
        Rin "We are better than that!" with vpunch
        play music silence

        pause(0.3)

        Suoh "..."

        show Rin yserious

        pause(0.3)

        Huang "..."

        pause(0.3)

        Rin "So please..."
        show Rin ySadSmile
        extend "Help me stop this madness..."

        Huang "..."

        Suoh "..."

        Huang "This war has gone for too much. I will tell my troops to hold their positions as soon as we receive confirmation of yours doing the same."
        Huang "The Senboshi will read your proposal thoroughly and notify you of any clause we want to settle."

        Suoh "The Amedu will also read the proposal and order our troops to hold their position."
        Suoh "This better not be a trap or you will pay."

        Rin "...As the head of the Hinteru clan, and on behalf of my family"
        Rin "Thank you."

        scene bg Black
        with Dissolve(2.0)

        jump .scene2

        return
    
    label .scene2:
        scene bg Black

        show expression Text(_("{b}Rigged Heart{/b}"), size=100, yalign=0.5, xalign=0.5, drop_shadow=(2, 2)) as text
        with Fade(0.0, 3.0, 5.0)

        show expression Text(_("Act I"), size=70, yalign=0.5, xalign=0.5, drop_shadow=(0, 0)) as text
        with Fade(1.0, 2.0, 2.0)

        scene bg Black
        with Dissolve(1.0)

        play sound doorKnock
        pause (2.0)
        
        "..."

        play sound doorKnock

        "A knock on the wood wakes me up from my dream, but something covers my face."

        play sound objectFall

        scene bg shichiRoom with Dissolve(0.3)

        "The history book falls from my face to the ground as I stand up yawning."

        "I guess the book stopped sunlight from waking me up"

        play sound doorKnock

        Shichi "Coming!"
        pause (2.0)

        play sound doorKnock

        Shichi "I'm on my way, no need to be so hast-"

        play sound doorOpening

        show birthdaySurprise with vpunch

        play music happy

        "Family" "{b}Happy Birthday Shichi-kun!{/b}"
        
        Shichi "!!!"

        scene bg shichiRoom with Dissolve(1)

        show Rin happy at center with Dissolve(0.2)
        show Naibu at 

        Rin "Guess who just became an adult!"

        Naibu "Congratulations, onii-san"

        Tojai "Now you will not have to lie online anymore, Shichi-kun."

        menu:
            "How could I forget about this?":
                Rin "You were really focused on those exams"
                extend "...And we were also trying to surprise you."
                Shichi "Thank you mom. You are great."
                Rin "Hehehe I know"
            "This cake looks so good. Thank you everyone!":
                Naibu "We are glad that you like it Shichi, we worked on it all morning!"
                Tojai "I took the opportunity to to each Naibu-chan a thing or two about cake decoration too."
            "I totally saw that one coming":
                Tojai "Sure you did, cool guy."
                Naibu "You acting is awful, onii-san"
                Shichi "Okay, okay, I confess. You got me"
                "Gee Naibu, no need to be so harsh"
            "What's that supposed to mean?":
                Tojai "Oh, nothing at all."
                Tojai "Just the usual teenager things."
                Naibu "{i}*Giggles*{/i}"
                Shichi "H-hey don't give me that!" with vpunch






        return

    ## This ends the game.

    return
