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
        $ Sheru_Closeness = 10
        $ ToldNaibuYouWereGay = False

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
    define Sheru = Character('Sheryoku', who_color = "#cccccc")
    define Kogan = Character('Kogan', who_color = "#336699")

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
    image Rin sadSmile = "ch/rh/rin_happy.png"
    image Rin angry = "ch/rh/rin_happy.png"
    image Rin annoyed_b = "ch/rh/rin_happy.png"

    ##Naibu
    
    #image Naibu smiling 

    ##Tojai


    #Background Pictures
    image bg Black = "bg/black.png"
    image bg centralMeetingRoom = "#ffffff"
    image bg HinteruMeetingRoom = "#000000"
    image bg shichiRoom = "#fffffa"
    image bg hall = "#aaffff"
    image bg limoInside = "#ffbbff"
    image bg commercialArea = "#999999"
    image bg NaibuRoom = "#ff0066"

    #Still Pictures
    image birthdaySurprise = "bg/black.png"
    image ShichiOrigins1 = "bg/black.png"
    image ShichiOrigins2 = "bg/black.png"
    image ShichiOrigins3 = "bg/black.png"

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
    define audio.calmed = "<silence 0.5>"

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
        "..."

        play music serious
        play sound doorOpening
        scene bg centralMeetingRoom
        with Dissolve(1.0)

        "{b}Location: Old Ibuma Mansion in the center of Rigutochi.{/b}"
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
        Rin "We took down the Ibuma to get rid of their abuses on Rigutochi and the Components, but went right to killing each other after that."
        
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
        "{b}Location: Hinteru Mansion, Shichi's Room{/b}"
        pause(5)

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

        show Rin happy at center
        show Naibu happy at left
        show Tojai smiling at right
        with Dissolve(0.4)

        Rin "Guess who just became an adult!"

        Naibu "Congratulations, onii-san"

        Tojai "Now you will not have to lie online anymore, Shichi-kun."

        show Rin smiling
        show Naibu smiling
        show Tojai smiling

        menu:
            "\"How could I forget about this?\"":
                Rin "You were really focused on those exams"
                extend "...And we were also trying to surprise you."
                Shichi "Thank you mom. You are great."
                Rin "Hehehe I know"
            "\"This cake looks so good. Thank you everyone!\"":
                Naibu "We are glad that you like it Shichi, we worked on it all morning!"
                Tojai "I took the opportunity to to each Naibu-chan a thing or two about cake decoration too."
            "\"I totally saw that one coming\"":
                show Tojai smug
                Tojai "Sure you did, cool guy."
                Naibu "You acting is awful, onii-san"
                Shichi "Okay, okay, I confess. You got me"
                "Gee Naibu, no need to be so harsh"
                $ Confidence -= 1
            "\"What's that supposed to mean?\"":
                show Tojai smug
                show Naibu giggling
                Tojai "Oh, nothing at all."
                Tojai "Just the usual teenager things."
                Naibu "{i}*Giggles*{/i}"
                Shichi "H-hey don't give me that!" with vpunch

        show Rin smiling
        show Naibu smiling
        show Tojai smiling

        Rin "We will celebrate with the rest of the family at seven, the servants are preparing the main hall for that."

        Rin "Relax for a bit, we will go get your kimono soon"

        Naibu "You will finally get to use Dad's. That's great Shichi!"

        Shichi "Hehe I guess it is"

        Tojai "Come on Shichi-kun, it means a lot. No need to be modest about it"

        "Tojai is right. I should feel honored, all things considered"

        Rin "Well, let's not distract him for too long shall we?"

        Rin "We will leave you do your thing, Shichi. Tojai and I have some stuff to do"

        Tojai "We will talk to you later"

        Shichi "Alright, see you later. Thank you!"

        show Rin happy

        Rin "Don't mention it."

        hide Rin
        hide Tojai
        with Dissolve(0.3)

        show Naibu smiling at center
        with move

        Shichi "Thank you Naibu, I really appreciate this."

        Naibu "You are welcome."

        extend "But if you want to repay me, I bet the cake is delicious."

        "Of course there was something she would get from all this. Should I comply?"

        menu:
            "Let her eat the whole cake.":
                Shichi "Okay, okay. You can eat the whole cake"
                show Naibu surprised
                Naibu "Are...Are you sure? We made it for you Shichi. Mom wouldn't let me eat it all and leave you nothing"
                Shichi "It's fine, I don't feel very hungry anyway and I am sure there will be more tonight."
                Naibu "Oh..."
                show Naibu happy
                extend "Thank you very much Shichi"
                Shichi "Don't mention it. Enjoy your cake, I'm going to take a shower."
                Naibu "Sure! See you later."
                scene bg Black
                with Dissolve(0.6)
                play sound silverware
                $ Naibu_Affection += 2

            "Eat the whole cake.":
                "Before she can say anything I take the whole cake and eat it quickly in front of her."
                play sound silverware
                play sound silverware
                show Naibu surprised
                Naibu "!!!"
                show Naibu surprised
                Naibu "Okay then, I guess it's your cake after all."
                Shichi "If it serves as any consolation, it was delicious."
                Naibu "Glad you enjoyed it."
                Shichi "I'll go take a shower now. See ya."
                Naibu "See ya."
                scene bg Black
                with Dissolve(0.6)
                "I leave to the bathroom."
                $ Confidence += 1

            "Eat a piece of the cake and let her have the rest.":
                Shichi "I am not that hungry, I'll just eat a piece and you can eat the rest"
                show Naibu happy
                Naibu "Thank you onii-san"
                play sound silverware
                "I take a portion of the cake and slowly eat it. It's sweet, soft and it melts in my mouth."
                Shichi "This is pretty good. Nice job Naibu"
                show Naibu blushed
                Naibu "Thank you, it's the first time I try cooking something like this"
                Shichi "I'll go take a shower now. Enjoy the rest of the cake."
                show Naibu happy
                Naibu "Mhmm~"
                scene bg Black
                with Dissolve(0.6)
                $ Naibu_Affection += 1

            "Share it with her.":
                Shichi "Why don't we share the cake?"
                show Naibu smiling
                Naibu "Sure. Have a spoon."
                "Naibu passes me a spoon and we start eating the cake"
                play sound silverware
                Naibu "Did you have any cool dreams last night?"
                Shichi "Studied so hard I had a dream about history."
                show Naibu awkwardly
                Naibu "You should probably take a rest from the studying."
                Shichi "I know, I know. But this professor wants to test us in our first day of school about every single class last year and it's worth like hald of our grade."
                show Naibu surprised
                Naibu "Oh, that's just cruel"
                Shichi "Yeah, I know."
                Shichi "Did you have any dreams last night?"
                show Naibu smiling
                Naibu "I had one with Dad"
                Shichi "Huh... Did you rest well?"
                scene bg Black
                with Dissolve(0.6)
                "We keep talking for a little longer while we finish the cake. Then I say goodbye before leaving to take a shower."
                $ Naibu_Affection += 3
            
        play music refined

        "I take a hot shower and put on my regular clothes before going downstairs."

        scene bg hall

        "I hear the sound of steps and tables being moved as I get closer to the hall."
        "From the top of the stair, I can see half a dozen servants doing the decoration and preparations for the events."
        "Every servant is dressed in formal clothing according to their role as butler or maid."
        "I never considered my birthday this important, but I guess under my conditions it's kind of a big deal."
        "Just as I was reaching the bottom, I notice Tojai and my mother talking at the base of the stairs."

        show Rin serious at left
        show Tojai serious at right
        with Dissolve(0.4)

        Tojai "Why do you still invite them? You know how they are, Rin-san."
        Rin "I don't have a choice, Tojai. As the head of the Hinteru Clan, I am expected to-"
        "Mom cuts her speech the moment she notices me walking down the stairs."

        play sound walkingDownstairs
        show Rin smiling

        Rin "You ready, Shichi?"
        "I nod. Tojaiwa makes a deep sigh."
        Tojai "I will go and help the cooks. Say hello to Sheru-chan on my behalf."

        hide Tojai 
        with Dissolve(1)
        show Rin smiling at center 
        with move

        Shichi "Did something happen?"
        Rin "Don't worry about it. Let's go."

        scene bg Black
        with Dissolve(1.5)

        jump .scene3

        return
    
    label .scene3:
        "{b}Location: Hinteru Limo, driving through the Prefecture of Heiwa{/b}"
        pause(2)
        scene bg limoInside
        show Rin serious at left
        with Dissolve(2)

        "My mother and I are seated in the back of the limo."
        "A white-haired servant is sitting in front of us, in the driver seat."
        "We are both in silence, not saying anything to the other. It has been this in the car for as long as I remember."
        "During my infancy, I thought she just didn't like to deal with me when there was no one to impress."
        "That she didn't like me."
        "I was a terrible son during my teenage years, I came to believe that maybe she hated me."
        "It is just so bizarre to see her warm and motherly in front of others, and then cold and serious when it's just the two of us."
        "Eventually, I asked Tojai about it. If someone knew why my mother was like that with me, it was her."
        
        scene bg Black 
        with Dissolve(1)

        "She giggled at my question."
        Tojai "She doesn't hate you Shichi! She was like that before you arrived."
        Shichi "Really?"
        Tojai "Rin-san has been through a lot. She lost too many friends and family members during the war."
        Tojai "Sons, daughters, brothers, sisters, her parents, her husband..."
        Tojai "She tries to hide it, she tries to act like everything is fine..."
        extend "But I don't think she has recovered to this day."
        "Tojai looked gloomier than I had ever seen her before and crossed her arms in front of her chest."
        Tojai "I believe that to this day... she still lives in fear. In fear of someone going after Naibu or you."
        Tojai "She is more relaxed when she is with you two, or in the house. But the moment she has to go out..."
        Tojai "Well, she becomes distant and paranoid."
        "I stood in silence, at fault of words. Tojai smiled at me."
        Tojai "It was actually worse before you arrived, you know?"
        Tojai "I hope that clears it up."

        scene bg limoInside

        "Driver" "We have arrived, Rin-Sama"
        Rin "Thank you Shinji. Wait for us in the car, this will not take long."
        "Driver" "Understood, Rin-Sama."

        play music urban
        scene bg commercialArea
        show Sheru smiling at center
        show Rin smiling at left
        with Dissolve(1.5)

        Sheru "Greetings Hinteru-san, the kimono is almost ready. Please grant us a couple of additional minutes."
        Rin "I am confident the wait will be worth it."
        
        show Sheru happy

        Sheru "Oh, it will most certainly be. You know my quality."
        Shichi "Hey Sheru"
        menu:
            "\"Nothing for your bro?\"":
                Sheru "Come on Shichi, I am just trying to be polite here."
                
            "\"I'm here too you know.\"":
                Sheru "Ladies first Shichi, especially if she's the head of the Hinteru Clan."

        menu:
            "Fist-bump Sheryoku.":
                "I walk towards Sheru, we fist-bump like when we were younger."
                show Sheru smiling
                Sheru "Habby birthday pal."
                $ Sheru_Closeness += 1
                Shichi "Thanks Sheru"

            "Be sassy.":
                Shichi "Well, now you will have to answer to me too."
                Sheru "I hear you mean."
                Sheru "Happy Birthday!"
                Shichi "Thank you."
                $ Confidence += 1
                $ Respect += 1
        Shichi "I swear every time I talk to you it feels that you are older than me."
        show Sheru smug
        Sheru "Well, that's because I spend my days working in the forge and moving stuff around instead of being a hermit."
        Shichi "H-hey most of the time I am studying you know!"
        Sheru "Yeah, like half of it."
        show Rin smiling
        Rin "The other half you are just being lazy."
        Shichi "Mom not you too!" with vpunch

        scene bg Black
        with Dissolve(1.5)

        "We talk for a little longer before Sheru's coworkers bring us the kimono"
        "I say goodbye to Sheru and get in the car with mom."

        jump .scene4

        return

    label .scene4:
        play music refined
        scene bg hall
        "{b}Location: Hinteru Mansion, Dining Hall{/b}"
        pause(5)

        "A couple of hours later I am in the hall. The celebration has been going for a while."
        "I am wearing the kimono we picked up earlier."
        "Every member of the Hinteru Clan was invited, but of course many had better things to do."
        "I received every guess that attends, as I was instructed to."
        "After it seemed clear no one else was arriving I give myself the permission to sit down with my family."
        "To pass time I..."

        $ ReadBookInMeeting = False

        menu:
            "Talk to relatives about economics.":
                $ Respect += 2
                "I talk to my uncles and aunts about the economics in Rigutochi and the way the Hinteru are handling the competition with the Amedu and Senboshi."
                "They recognize my knowledge on the topic."
                "I get to know of a drop in the price of Woolget."
            "Talk to relatives about meaningless topics.":
                $ Respect += 1
                "I talk to my cousins and some of my uncles and aunts about meaningless topics, like sports and celebrities."
                "They clearly enjoy talking about it, as I barely get to say anything."
            "Read a book.":
                $ Respect -= 1
                $ ReadBookInMeeting = True
                "I avoid contact with my relatives in any way and start reading a novel."
                "The story takes place during The Great War and is about the a Component that left to fight in it."
                "No one makes any attempt to talk to me, but I can see Tojai with the border of my eye."
                "She certainly does not approve of my isolation."
                "Should I stop reading?"
                menu:
                    "Try to make conversation with some relative.":
                        "I put my book down and strike a conversation with a cousin about politics."
                        "He doesn't seem very interested but reciprocates the action nonetheless."
                        $ Respect += 1
                    "Continue reading book.":
                        $ Knowledge += 1
                        $ Respect -= 1
                        "I ignore Tojai and go back to my reading."
            "Walk around to certify everyone is enjoying themselves.":
                $ Respect += 2
                "I walk around the hall asking my relatives if they are enjoying themselves."
                "Most of them insist that they like the meal and the ambience."
                "They also insist that I should not worry abour it, since \"Thats what servants are for\" but I insist."
                "I receive a lot of compliments about how much I have grown and participate in many quick chats before I go back to my seat."
            
        "When the clock hits midnight, the sound of a bell makes the whole room go into silence."
        "In the middle of the room stands a small scaffold, and on top of it is my mother with a microphone in front of her."

        show Rin smiling at center
        with Dissolve(0.4)

        Rin "Good evening everyone, I hope you are all enjoying this small formal party. Do not worry, I will not take much of your time."
        show Rin serious
        Rin "Today we are celebrating two things:"
        Rin "The first one is that it has been almost twenty years since the Three Clans signed the Rigutochi Peace Treaty."
        Rin "I know it is still a couple of days early, but it is worth to conmemorate it now by keeping a minute of silence for those who perished among the violence and distress."
        Rin "Let us all pray for their souls to rest peacefully and find light in the aftermath of this wonderful adventure we call life."
        play music silence
        "The whole hall is in complete silence. Most people have their eyes closed for a minute with their hands together, even Naibu and Tojai."
        "I do the same."
        pause(1)
        "..."
        pause(2)
        "... ..."
        pause(3)
        "... ... ..."
        pause(1)
        show Rin sadSmile
        Rin "Thank you."
        show Rin smiling
        play music refined
        Rin "Our second celebration is a happier one."
        Rin "We are celebrating the day Shichi-san, my eldest son, reaches maturity."
        Rin "Please give him a round of applause, I think he deserves them."
        play sound applauses
        "The atmosphere feels more serious and cold after the silence, but it recovers some warmth as the applauses of the clan fills the room."
        "I can't help myself but smile and feel a little proud."
        "Loud Voice" "Cut the crap Rin"
        play music silence
        show Rin surprised

        show Tojai serious at left
        with Dissolve(0.5)
        Tojai "I warned her..."
        play music tense
        "Uncle Kogan stands from his seat. His wife and children stay sitting in silence."
        show Rin serious
        "Based on the way they don't try to stop him, it looks like they are supporting whatever he's saying."
        show Kogan at right
        with Dissolve(0.5)
        Kogan "We all know why you did this Rin. You just want to give the impression that Shichi is worth of his status."
        Kogan "You can fool yourself if you want, but don't try to fool us."
        Kogan "First you finish the war with the Senboshi and the Amedu, even though victor was practically ours."
        Kogan "Then you give them part of our territory to make them accept peace and another piece for that stupid city in the middle of the island-"
        Rin "Heiwa"
        Kogan "-from which only private companies are benefiting."
        Rin "I assure you, we have more interests there than you may think."
        Kogan "Interests you have refused to prove to us, because we are not the ones that handle that part of Rigurochi."
        Kogan "For all we know, you could be doing deals with the Amedu and Senboshi to keep this... artificial peace for longer."
        Kogan "And there is nothing we can do about it!"
        Rin "I can promise that i-"
        Kogan "You can promise a lot of things, Rin, but there is little you can prove as it stands now."
        Kogan "You are managing this family with such a lack of tradition and culture and dignity that I can't help but feel that you have turned our clan into a business."
        Rin "..."
        Kogan "And as if that wasn't enough, then you impose that regulation to allow servants to gain their freedom."
        Kogan "What the hell were you thinking?!"
        Rin "These regulations were recommended by the UN, we had to integrate them to avoid international conflicts."
        Kogan "You agreed to all of them too soon and with minor resistance."
        Kogan "So I was not surprised at all when you made use of them the way you did."
        Rin "I made very clear my reasons for freeing Tojaiwa-san during the ceremony."
        Rin "She earned it."
        Kogan "She did do her job as intended, I agree. But that's not what insults me the most."
        Kogan "No, Rin, my problem is that you did not only took her status as a servant,"
        Kogan "But {b}gave her our honorous last name{/b}. You gave a mere servant the right to call herself a Hinteru just because she did her damn job!"
        show Tojai angry at center 
        show Rin serious at left
        with move
        "Kogan took a quick step forward to express his anger."
        "Tojai sprung herself from her seat to right next to the scaffold, blood in her eyes as she took her right hand close to the scabbard of her katana."
        "For a fraction of a second I could see a muderous intent dawn on her face and her own conscience holding it back."
        "Fortunately, a gesture from my mother made Tojai stop in her place and stand firmly. Limiting herself to coldly look at Kogan."
        Kogan "Look at her! She is a bulgar peasant and hasn't even learned to behave properly in high society. She is a savage wi-"
        Rin "Kogan, I must order you to stop insulting Tojaiwa-san this precise instant or I will have to show you the way out."
        show Kogan angrier
        Kogan "Are you threating us with kicking us out?! You cannot be serious!"
        Rin "I am completely serious Kogan. Behave yourself."
        Rin "If you have a problem with how I have handled things I must ask that we talk in private about those matters and that you refrain from using insults against me or anyone else."
        Kogan "You {b}cannot{/b} kick us out Rin. This house was {i}mine{/b} before you settled up here. It only became your home when my brother decided to marry a lowly peasant."
        Kogan "{size=+2}If he was alive, he would not have allowed any of this.{/size}"
        Kogan "{size=+4}We would have crushed the Amedu and the Senboshi,{/size}"
        Kogan "{size=+6}He would have kept the servants as what they are,{/size}"
        Rin "{b}Kogan that's enough{/b}"
        Kogan "{size=+8}He would not have allowed foreigners to profit from our country,{/size}"
        if ReadBookInMeeting == True:
            Kogan "{size=+9}He would have made sure his heir was polite and charismatic,{/size}"
        Kogan "{size=+9}and above everything else-{/size}"
        show Rin angry
        Rin "{b}{size=+8} Kogan that's enough!{/size}{/b}"
        Kogan "{size=+10}{b}He would not have allowed some random foreigner kid found in the woods to become the new head of the family!{\b}{/size}" with vpunch
        play music silence
        pause(1)
        "..."
        pause(1)
        "... ..."
        pause(2)
        "... ... ..."
        pause(1)
        "The whole room drowned in silence. The atmosphere so tense it could almost be cut with a knife."
        "My mother stayed in silence in the middle of the room, looking at Kogan with an intense hatred I had never seen in her before."
        hide Rin
        show Naibu surprised at left
        with Dissolve(0.5)
        "Naibu took her hands to her mouth in surprised and looked alternatively between me and the rest of the room."
        "Tojaiwa looked uncomfortable, but kept her eyes pointed directly at Kogan."
        "He stayed there, looking at my mother defiantly, like someone who just won a battle."
        "The worst part, is that he kind of did."
        scene bg Black 
        hide Naibu
        hide Rin
        hide Tojai
        with Dissolve(1)

        "Of course everyone knew I was adopted, that could be seen the moment anyone compared the color of my eyes to the amber in the rest of the Hinteru."
        "In fact, no matter who you compared me to, there was not a single clan in the island that had a similar eye color, or match of features as me."
        "I was either the product of some crazy mix with some mutation, or not a Component at all."
        "Either case, that made me completely unfit as the new leader of the Hinteru Clan, or any clan for that matter."
        "Fortunately, with the crazy amount of clans and families in Rigutochi, you would have to actively look for comparisons to confirm this as a fact."
        "No one else in the family cared enough to take the time to do some research on that."
        "My mom did it when she found me, and couldn't find anything, so we had a plan:"
        "No one would know where they found me, if someone asked we would make up an excuse."
        
        scene ShichiOrigins1
        with Dissolve(0.3)

        "I was found in a cave outside of a farm, in Hinteru's territory."
        "The local farmers noticed someone was stealing food from them and requested the military police to investigate."
        "One of them saw a shadow in the woods and was ready to shot it when it noticed the shape."
        "Turns out seven-year-old me had been feeding on crop and animals from local farms all this time, living in a cave deep in the woods."

        scene ShichiOrigins2
        with Dissolve(0.3)

        "I don't remember how I came to be there, or what happened to my original parents."
        "I do remember the first time I was brought to Rin. I was caged and handcuffed, scared of what she might do to me."
        "I was still scared when they forced me to stay in a room with a soft-white-bouncy thing in a corner,"
        "even more scared when they forced me to wear some sort of soft layer over my skin."

        scene ShichiOrigins3
        with Dissolve(0.3)

        "Rin would send someone everyday, and that someone would show me white rectangular tables with colors mixed, meant to represent things."
        "That someone would also make noises I have never heard before, over and over again until they were stuck in my head."
        "There was this sound she made that I liked a lot: "
        "\"Shichi\""
        "At some point it stuck and that became my name."
        "Of course, I eventually understood that it was the japanese word for seven, and while growing up I regretted to have made that my name."
        "After my first year, I understood the situation I was in and how fortunate I was."

        scene bg Black
        with Dissolve(0.5)

        "I understood that I was but a lost child, lucky enough to be found by someone who missed many."
        "I understood that I owed my life that the family that took me in, that I could never repay my debt."
        "I understood that I needed to blend in with the rest of the Hinteru and become one of them,"
        "and so I did."
        pause(1)
        "However, the secret of my origin could never be revealed."
        "So my mother, Tojaiwa and I kept it hidden from everybody else."

        scene bg hall
        show Rin serious at left
        show Tojai serious at center
        show Kogan angry at right
        with Dissolve(0.5)

        "Not that it mattered anymore."
        pause(2)
        "The room was still, in silence."
        "I could feel Naibu's eyes fixated on me, having just discovered the truth along with everybody else in the room."
        Kogan "You thought you could keep it hidden, but I had my suspicions from the very beginning."
        Kogan "It took a while, but I came to the definitive conslusion that this man here, Shichi, is not only not a Hinteru from birth, but not even a Component."
        Rin "D-{nw}"
        Kogan "I do have proof of these assumptions, and I will make sure to provide it to anyone interested in corroboration of my claims."
        "Tojai looked at my mother with a serious look on her face. I knew that look very well, it was the \"We need to talk later\" look."
        Rin "Kogan, I request that you leave this instant."
        Kogan "Or what?"
        Rin "Or I will have to use force to take you out of my house. I am sure Tojaiwa-san would love to show you the way out."
        "Tojai took her hand to the grip of her sword and drew a small smile on her face."
        "Kogan looked at her and tried to act dismissive about it, but his eyes revealed a glance of fear."
        Kogan "That won't be necessary, we were just leaving."
        Rin "Good. Take haste."
        "Kogan directed another look at Tojai, she responded by defiantly drawing part of her sword out."
        "That was all it took for Kogan and his whole family to almost run towards the exit and dissapear into the night."
        hide Kogan 
        with Dissolve(1)
        show Tojai serious at left
        show Rin serious at center
        with move

        play music refined

        Rin "With that out of the way..."
        Rin "I dont think I need to remind you all of the current situation."
        Rin "You may remember me better as only the wife of the old Hinteru Clan leader, but that was a long time ago ago."
        Rin "As the leader of this family, I will not tolerate any insubordination or insults towards me or any other member of this family."
        Rin "I will have to impart more severe measures next time this happens."
        
        "Mom let out a deep sigh, full of tension and contained anger. Then she came close to the microphone one last time."

        Rin "Enjoy the rest of the night."
        hide Rin 
        hide Tojai
        with Dissolve(0.3)
        
        "She then stepped down the scaffold as the hall slowly recovered its life, though this time with an uncomfortable atmosphere of hostility and hypocrisy."
        "My mother walked towards the stairs, with Tojai closely following her behind."
        "I jumped from my seat and followed them."
        "I almost didn't notice Naibu following right behind me."

        jump .scene5

        return

    label .scene5:
        scene bg HinteruMeetingRoom
        play music calmed
        show Naibu sad at left
        show Rin serious at center
        show Tojai serious at right
        with fadein

        "{b}Location: Hinteru Mansion, Meeting Room{/b}"
        pause(2)

        Tojai "It was a bad idea to invite them, Rin-san."
        Rin "I didn't have a choice Tojai. Kogan's family is still the second most important in the clan."
        Tojai "Well, it's not like we look any better now."
        "Mother doesn't respond. Had it been us who said that and she would not be so calmed."
        "She directs her eyes to Naibu who is sitting in silence next to me."
        Tojai "After how he insulted us tonight, I kind of wish we could excute him."
        Rin "Sweet goodnes Tojai, no. We don't do things that way anymore."
        Tojai "I know. Never said that we should, said that I wish we could."
        Tojai "He has tested our patience for too long too."
        "My mother sighs and looks at me now."
        show Rin sadSmile
        Rin "Sichi, are you okay?"
        Shichi "Huh? Why do you ask?"
        show Rin smiling
        Rin "You haven't said anything since we were in the hall."
        
        menu:
            "\"Yeah I'm fine. I'm just really tense.\"":
                show Tojai sadSmile
                Tojai "Indeed... Kogan certainly complicated the matters for us."
                show Rin serious
                Rin "I don't think the rest of the family is thinking very fondly of you now."
                show Tojai serious
                Tojai "They were prepared to accept you as the heir, but now suddenly they refuse because you are not a Component."
                show Tojai angry
                Tojai "Hypocrites."
            "\"I am a little scared to be honest.\"":
                $ Confidence -= 1
                $ Tojai_Affection += 2
                show Tojai smiling
                "Tojai smiles at me, then she walks around the table and hugs me."
                Tojai "We all are, Shichi-kun; do not feel embarrassed."
                "After saying that she lets go and stand by my side."
                show Rin serious
                Rin "We will find a way around it, don't worry."
            "Ignore the question and redirect it to Naibu.":
                $ Confidence += 1
                $ Naibu_Affection += 1
                Shichi "Naibu, you have been stranely silent. Is there something you want to tell us?"
            "\"I'm fine, what about you two?\"":
                $ Tojai_Affection += 1
                $ Confidence += 1
                show Tojai surprised
                show Rin smiling
                show Tojai happy
                "Tojai looks surprised at me and starts laughing."
                Shichi "...What? Did I say something funny?"
                Rin "{i}Giggles{/i}"
                Shichi "...Uh do I have something on my face?"
                Tojai "Hehehe nothing like that."
                show Tojai smiling
                Tojai "You are just really cute."
                Shichi "I-I am not cute!"
                Rin "Sure you aren't."
                Tojai "Shichi-kun, I have received worse insults before, and that is not counting my time as a servant."
                Tojai "The words that hurt the most are the ones that come from people you are close to."
                Tojai "People like Kogan can-"
                Rin "Tojai, Naibu is here" with vpunch
                Tojai "-eat trash."
                "I start laughing at the situation and they do the same."
            
        "Naibu's voice suddenly makes everything go silent."
        show Naibu sad
        Naibu "Why...?"
        play music silence
        pause(1)
        Shichi "What?"
        show Naibu angry
        show Tojai surprised
        show Rin surprised
        Naibu "You never told me you were not from Rigutochi!"
        Naibu "You never told me you don't know where you are from!"
        Naibu "I didn't know any of this before today!"
        "..."
        "... ..."
        Naibu "I thought you trusted me Shichi..."
        "She then turned towards Tojaiwa"
        Naibu "And you... you know me well."
        Naibu "I know how to keep a secret."
        show Tojai serious
        Tojai "..."
        "Naibu then directed her watery eyes towards my mother."
        "She didn't have the change to say anything."
        show Rin serious
        Rin "Silence."
        show Naibu sadSmile
        "Naibu instictively went mute."
        "She was motionless in her seat like if my mother had petrified her with her scary judemental eyes."
        Rin "You have to understand, it was very important information that could tun our whole political stand."
        Rin "We were trying to find the right moment to tell you but-"
        show Naibu angry
        Naibu "What about anytime huh? I was not going to tell anyone, I never do."
        Rin "Naibu, it was-"
        "For the first time ever, Naibu defied my mother by standing up and not letting her finish."
        Naibu "You always think of Shichi as your heir, mom."
        Naibu "But you keep forgetting something:"
        Naibu "I am a Hinteru too."
        Naibu "I am your last biological daughter for crying out loud!"
        Naibu "I am just as prepared to handle sensitive information as he is."
        Naibu "Why couldn't you just tell me?!"
        Rin "..."
        Naibu "You stand there talking about how people only think of you as the husband of a dead leader..."
        Naibu "But all you do is treat me like the sister of the next one..."
        
        hide Naibu
        with fadeout
        
        "Naibu then turned around and left the room, closing the door behind her with a {i}slam{/i}"
        with fadeout

        "Neither Tojai or my mother went behind her."
        Rin "..."
        Rin "I know that, Naibu...But..."
        Shichi "Huh?"
        Tojai "If she ever wanted the throne for herself, she could take it with that information."
        Rin "...That's the real reason why we never told her."
        
        menu:
            "\"That's... a pretty pessimistic way to look at it. \"":
                Rin "It is. But that's how politics work."
                Rin "Why do you think Kogan did this? He wants to make us look shady so he and his family can take the lead."
                Tojai "We know Naibu is not like him... but..."
                Rin "The risk always exists."
                Rin "Not to say we want to keep you as the heir. If she ever proved herself over you, she would have earned it."
                Tojai "But giving her information like that would be a big advantage."
                Shichi "..."
                $ Knowledge += 1
            "Stay silent":
                "My mother sighs."
        
        $ ADick = False

        menu:
            "\"Is no one going to talk to her?\"":
                Rin "We will only make it worse if we try to reason with her now."
                Rin "I will talk to her tomorrow."
                "Tojai nodded clearly uncomfortable with the situation."
            "\"We should let her alone for tonight...\"":
                Tojai "Agreed."
                Rin "Mhmm."
            "Ignore the situation and try to go back to the issue at hand.":
                Shichi "What will we do with Kogan then? Do you have any plans?"
                "Both my mother and Tojaiwa looked at me with clear dissaproval and walked towards the door."
                Rin "I have things to do downstairs. We will talk about that tomorrow."
                Rin "Good night Shichi."
                hide Rin
                with fadeout
                Tojai "I feel a little sleepy, I will go to my room. Good night Shichi-kun"
                hide Tojai
                with fadeout
                "I am left alone in the room feeling like an idiot."
                $ Confidence -= 1
                $ Respect -= 1
                $ Tojai_Affection -= 1
                $ ADick = True
        
        "..."
        menu:
            "Go after Naibu yourself.":
                $ Confidence += 1
                if ADick == False:
                    Shichi "I will go talk to her"
                    Rin "Shichi, you shouldn't..."
                    Shichi "It's fine. I know what to say."
                    "Mother sighed."
                    Rin "Okay. I will go back downstairs. We will talk about this whole thing tomorrow."
                    Tojai "I will accompany you then."
                    Shichi "Alright."
                    Shichi "Good night Mom,"
                    Shichi "Good night Tojai."
                    show Rin sadSmile
                    Rin "Good night Shichi. Good luck with your sister."
                    Tojai "Do not keep yourselves awake for too long."
                    Shichi "Promised."
                    
                    hide Rin
                    hide Tojai
                    with fadeout
                else:
                    "I stay in the room for a little longer and decide to go after Naibu."
                
                "I leave the room and go in direction of Naibu's"
                pause(3)
                jump .scene5b
            "Go to your room.":
                $ Confidence -= 1
                if ADick == False:
                    "I sigh and stand up."
                    Shichi "I will go to my room now. I need some rest."
                    Rin "We will go down until everyone is gone."
                    Tojai "Good night Shichi-kun."
                    Shichi "Good night Mom. Good night Tojai."
                scene bg Black
                hide Tojai
                hide Rin
                with fadeout
                "I go to my room and lay on my bed."
                "I feel nervous, not sure of what will happen now."
                "I stay awake for hours before my body finally falls asleep."
                jump .scene6
        return

    label .scene5b:
        play music calmed
        "I stand in front of Naibu's door."
        "I can feel a knot in my throat, product of my nervousness."
        menu:
            "Knock on the door.":
                play sound doorKnock
                "I knock on her door and wait for a short time."
                "..."
                "No response."
                play sound doorKnock
                "I knock again and wair a little longer."
                "..."
                "..."
                "Still no response."
                play sound doorOpening
                "I turn the knob and open the door slowly."
            "Tell her you're going to enter.":
                Shichi "Naibu"
                "..."
                "No response"
                Shichi "Naibu, I'm going in."
                "..."
                "Still no response."
                "I take that as a permission and open the door slowly."
                play sound doorOpening
            "Enter without asking.":
                "I open the door without telling her in advance."
                play sound doorOpening
        scene bg NaibuRoom
        show Naibu sad
        with fadein

        Naibu "Hi..."
        "Naibu is sitting on her bed, hugging a pillow."
        "Bellow her, there is a pair of faint lines from tears."
        "Her cute and charming face looks frowned and gloomy. Her sight avoids my prescence."
        
        menu:
            "\"I'm sorry we never told you\"":
                "She darts her eyes quickly at me for a couple of seconds before taking them off me again."
                menu:
                    "Lie about why you didn't tell her.":
                        label C5b211:
                            Shichi "To be honest, we thought you were too young and you would tell someone at some point."
                            Naibu "I wouldn't have..."
                            Shichi "We couldn't take any risks. You saw what happened."
                            Naibu "..."
                            "Naiby stays silent for a bit. She is clearly mad but more understanding."
                            Naibu "I want everyone to stop treating me like a kid."
                            Naibu "You should have told me, Shichi."
                            Shichi "You are right, I should have."
                            Naibu "I was thinking about telling you tomorrow, once the risks were minimized."
                            "Naibu sighs and puts her pillow down."
                            menu:
                                "\"I am sorry\"":
                                    #show Naibu smiling
                                    "Naibu looks at me, smiling sadly."
                                    Naibu "I am sorry I reacted that way too."
                                    Naibu "You are still my onii-san. Thank you for coming here."
                                    $ Naibu_Affection += 3
                                    "I smile to her."
                                    Shichi "That's what siblings are for."
                                    "She giggles and we hug shortly."
                                    Naibu "I am a little tired now. I think I will go to sleep." 
                                    
                                    label .C5b2111:
                                        menu:
                                            "\"Sure thing. I will do the same, good night!\"":
                                                $ Naibu_Affection += 1
                                                Naibu "Good night!"
                                            
                                                scene bg Black
                                                hide Naibu
                                                with fadeout
                                                
                                                "I leave her room and go to mine, more relaxed."
                                                "I change, lay on my bed and fall asleep shortly after."
                                                jump .scene6
                                            
                                            "\"Want me to sleep with you?\"":
                                                $ Naibu_Affection -= 1
                                                #show Naibu b_surprised
                                                Naibu "W-what?!"
                                                "Naibu blushes intensely."
                                                Naibu "{b}You are such a pervert!{/b}"
                                                
                                                scene bg Black
                                                hide Naibu
                                                with fadeout

                                                "Naibu hits me with her pillow and literally kicks me out of her room."
                                                "I go to my room, hurting from the kicks."
                                                "I drop myself on the bed, bothered by having screwed it up like that, and fall asleep shortly after."
                                                jump .scene6

                                        return

                                "Pat her head.":
                                    "I pat Naibu on the head."
                                    #show Naibu b_annoyed
                                    Naibu "..."
                                    "She is clearly annoyed but doesn't complain."
                                    Naibu "I am sorry I acted that way..."
                                    Naibu "But I just told you to not treat me like a kid."
                                    Shichi "You are still my little sister."
                                    Naibu "I-I guess..."
                                    $ Naibu_Affection += 2
                                    #show Naibu b_angry
                                    Naibu "A-anyway you should stop, I need to go to sleep now."
                                    jump .C5b2111

                                "Hug her.":
                                    "I move towards Naibu and cover her with my arms in a hug."
                                    "She stays responseless for a couple of seconds, not having expected my action."
                                    "She finally returns the hug to me."
                                    "We stay like that for a couple of seconds. Then we separate and I see that she's blushing."
                                    #show Naibu smiling_b
                                    Naibu "T-thank you."
                                    Naibu "I needed that."
                                    $ Naibu_Affection += 3
                                    Shichi "Anytime, onee-chan."
                                    #show Naibu smiling
                                    "She smiles to me and giggles."
                                    Naibu "I should go to sleep now, onii-san."
                                    jump .C5b2111

                                "Throw her out of the bed.":
                                    "I suddenly push Naibu out of the bed."
                                    $ Naibu_Affection -= 2
                                    play sound objectFall
                                    #show Naibu surprised
                                    "She awkwardly falls to the floor dumbfounded." with vpunch
                                    #show Naibu angry
                                    Naibu "W-what the hell?!"
                                    "I laugh as she stands up. Then she throws a pillow to my face and kicks me to the floor."
                                    scene bg Black 
                                    hide Naibu
                                    with fadeout
                                    "She keeps kicking me in the floor without stopping."
                                    "I try to cover myself but" with vpunch
                                    extend "she keeps" with vpunch
                                    extend " kicking." with vpunch
                                    "I eventually manage to escape and leave her room."
                                    "I limp to my room, feeling the pain of her kicks all over my body."
                                    Shichi "She is "
                                    extend "{b}ouch{/b} stronger than I" with vpunch
                                    extend "{b}ouch{/b} thought..." with vpunch
                                    "I drop o my bed groaning from the pain and fall asleep."
                                    jump .scene6
                                    
                            return

                    "Say you wanted to protect her.":
                        Shichi "I just wanted to protect you."
                        show Naibu angry
                        Naibu "Oh, come on. At least don't act like a cliche. How would not telling me protect me?"
                        label .C5b212:
                            menu:
                                "\"Someone may have tortured you to get that information.\"":
                                    Naibu "..."
                                    #show Naibu serious
                                    Naibu "I can't believe you said something so stupid."
                                    Naibu "You know that wouldn't have happened. It's just too unlikely."
                                    $ Naibu_Affection -= 2
                                    "She throws her pillow at my face and get under the bedsheets."
                                    hide Naibu
                                    with fadeout
                                    Naibu "Get out."
                                    Shichi "Naibu..."
                                    Naibu "{b}Get {\b}"
                                    extend "{b}Out{\b}"
                                    "I sigh and leave her room."
                                    scene bg Black
                                    with fadein
                                    Shichi "I should have left her alone..."
                                    "I walk to my room and get in my bed"
                                    "Eventually, I fall asleep while I look at the ceiling thinking of what I could have done better."
                                    jump .scene6
                                "\"I didn't want you to feel betrayed.\"":
                                    #show Naibu angry
                                    Naibu "Yeah, because that worked out really well."
                                    Naibu "Try giving me a better answer now."
                                    jump .C5b212
                                "\"I did't want you to feel ashamed of your brother\"":
                                    jump .C5b22
                                "Tell her she was too young to understand.":
                                    jump .C5b211

                            return
                    "Try to win back her trust by telling her a secret.":
                        Shichi "If it makes you feel any better, I can tell you a secret I have never told anyone else."
                        "Naibu stares curiously at me."
                        Shichi "In exchange for not trusting you with that one before."
                        #show Naibu serious
                        Naibu "Well... go ahead"
                        menu:
                            "Tell her you're gay.":
                                Shichi "I'm gay."
                                #show Naibu surprised
                                "Naiby looks at me shocked, not expecting that to be my secret."
                                Naibu "A-are you for real?"
                                Naibu "You're gay?"
                                Shichi "Yes."
                                "She suddenly oubursts hyperactiveness."
                                #show Naibu excited
                                Naibu "{b}Yaoi~!{/b}"
                                Shichi "..."
                                extend "What?"
                                Naibu "So-"
                                "Oh"
                                Naibu "Soooooo-"
                                "Oh no"
                                Naibu "{i}Sugoiiiiii~!{/i}"
                                $ Naibu_Affection += 3
                                $ ToldNaibuYouWereGay = True
                                "My sister is an otaku"
                                Naibu "What's the name of your crush? Are you the seme or the uke? are you-"
                                Shichi "Whoa whoa there."
                                Shichi "I sure wasn't expecting you to be so excited about it."
                                Shichi "I thought you would be... worried?"
                                #show Naibu surprised
                                Naibu "Why would I be?"
                                Shichi "It's just that... you know... as the next clan leader..."
                                Naibu "...Oh... yeah"
                                Naibu "You need heirs."
                                Shichi "It's already bad enough that I'm adopted."
                                Naibu "Well, how would the bloodline thing work out now?"
                                Shichi "Mom told me I would need to later make one of my kids marry someone in the family."
                                #show Naibu serious
                                Naibu "Oh..."
                                "Naibu looks lost in thought."
                                Naibu "We will think of something later."
                                Shichi "Mhmm"
                                #show Naibu smiling
                                Naibu "Thank you for telling me onii-san."
                                #show Naibu happy
                                Naibu "I'm glad you trust me so much."
                                #show Naibu smiling
                                Naibu "Sorry for what I said earlier."
                                Shichi "It's fine, Naibu. What matters is that everything is fixed now."
                                "Naibu nods happily."
                                Naibu "I should go to bed now, if you don't mind."
                                Shichi "Oh, no. Not at all."
                                Naibu "If you need help with that whole thing..."
                                Naibu "You know you can trust me. I won't tell a soul."
                                Shichi "Thank you onee-chan."
                                "I stand up and stop by the door."
                                Shichi "Good night."
                                #show Naibu happy
                                Naibu "Good night!"
                                scene bg Black
                                hide Naibu
                                with fadein
                                "I close the door behind me and go to my room."
                                "I change my clothes, get in the bed and fall asleep shortly after."
                                jump .scene6

                            "Tell her a creepy childhood memory.":
                                Shichi "So... I have this childhood memory."
                                play music tense
                                Shichi "I don't know if it really happened to be honest,"
                                Shichi "I just kind of remember it."
                                Shichi "I was around... six years old."
                                Shichi "This was before they found me in the forest."
                                #show Naibu serious
                                Naibu "..."
                                Shichi "It was late at night looking for food."
                                Shichi "I would usually avoid doing that in fear of predators, but I failed to secure something during the day and I was hungry."
                                Shichi "I went to a local farm and saw there was a cow dangerously close to the fence near the forest."
                                Shichi "I carried my wooden spear and walked towards it."
                                Shichi "Then, it turned around in my direction and stood up."
                                Shichi "Its eyes were glowing in the dark, its body had more fur than usual."
                                Shichi "But what made me run away was the height."
                                Shichi "This was twice as tall as any of the other cows, and most of the height was in its {i}legs.{/i}"
                                Shichi "They were long and thin in a very abnormal way."
                                Shichi "I don't think it followed me to the cave, and if it did I lost it."
                                Naibu "..."
                                "I shrug carelessly and look at Naibu."
                                Shichi "I don't know if it was a nightmare, but I remember it too well."
                                Shichi "Well, you wanted a secret. I'm sure it's not what you wanted but I don't have more to hide."
                                $ Naibu_Affection += 2
                                Naibu "T-That's an interesting story..."
                                "Naibu's voice is shaky."
                                Naibu "Thanks for telling me..."
                                Naibu "...in the night..."
                                Naibu "...when I'm going to be alone in my room."
                                Shichi "..."
                                Naibu "..."
                                Shichi "..."
                                Naibu "..."
                                Shichi "Boo"
                                #Naibu show surprised
                                Naibu "AAHH-"
                                "Naibu falls to the floor from the \"scare\"."
                                "I laugh uncontrollaby, she blushes from the shame."
                                #show Naibu b_angry
                                Naibu "H-hey that's cruel!"
                                Shichi "Sorry, sorry. I had to do it."
                                Shichi "It's a true story though. I wasn't making it up."
                                Naibu "..."
                                Shichi "You are right about one thing. It's late, we should sleep."
                                #show Naibu b_surprised
                                Naibu "W-wait..."
                                Shichi "Yeah?"
                                Naibu "C-can you stay with me until I sleep?"
                                Shichi "That scared huh"
                                #show Naibu b_angry
                                Naibu "S-shut up it's your fault."
                                menu:
                                    "\"Sure, I can do that.\"":
                                        Naibu "G-good"
                                        scene bg Black
                                        hide Naibu
                                        with fadeout
                                        "I turn off the lights and leave her nightstand light open before sitting on the chair next to the bed."
                                        "I accompany Naibu until I'm sure she's asleep, then I leave the room without making noise."
                                        $ Naibu_Affection += 1
                                        jump .scene6

                                    "\"Nah\"":
                                        Naibu "..."
                                        scene bg Black
                                        hide Naibu
                                        with fadeout
                                        "I quickly spring out of her room and get in mine."
                                        jump .scene6

                            "Tell her you like someone you shoudln't.":
                                Shichi "I... like someone I shouldn't."
                                #show Naibu surprised
                                Naibu "Oh really?"
                                #show Naibu smiling
                                Naibu "May I know who's the fortunate lady?"
                                menu:
                                    "Tojaiwa.":
                                        "WIP"
                                    "Someone.":
                                        "WIP"
                                    "Refuse to tell her.":
                                        "WIP"
            "\"I am still your brother, Naibu\"":
                label .C5b22:

                    "WIP"

                    return
            "\"Don't act like a kid. Behave yourself\"":
                "WIP"


        return

    label .scene6:
        return




    ## This ends the game.

    return
