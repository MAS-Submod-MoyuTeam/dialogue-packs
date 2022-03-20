init 5 python:
    renpy.game.persistent.dan_dream_database = dict()
    
    def addDream(key, label_name):
        renpy.game.persistent.dan_dream_database[key] = label_name
        return

    def getDream(key):
        return renpy.game.persistent.dan_dream_database[key]

    def clearDreams():
        renpy.game.persistent.dan_dream_database = dict()
        return


label DaN_dream_one:
    # dream synopsis:  You and Monika go on a date to a horror movie. As it turns out, the horror movie was
    # based on Doki Doki Literature Club.  Ultimately Monika enjoys the movie, despite initially being worried
    # that it wouldn't fit her tastes.  At the end of the dream, Monika comments on how dreams are thought
    # to be caused by our brains making sense of things we know being randomly jumbled together.
    #
    # If the dream ends earlier, Monika will remark on a scene in her dream where she had to talk you out of
    # getting an enormous tub of popcorn because she was worried about your health.  She will reiterate the
    # importance of living a long and healthy life for her sake, if not for your own.
    # 
    # If the dream ends too early, Monika will be sad that you didn't get to go on a date. She will ask that
    # you be more careful for what dreams you wake her up for.
    #
    # GOOD DREAM
    m 6dsc "...{w=2}{nw}"
    m 6dsd "...hm...?{w=1}{nw}"
    m 6dsb "{w=1}...there...{w=1} ...late...{w=1}{nw}"
    m 6dsc "{w=1}.{w=1}.{w=1}.{nw}"
    m 6dkd "...that...?{w=3}{nw}"
    m 6dsc "...hmm...{w=3}{nw}"
    m 6dsbld "...if I...{w=1} scream...{w=3}{nw}"
    m 6dsbfb "...what... {w=1}you do...?{w=3}{nw}"
    $ dream_progress = 0
    menu:
        "wake Monika up":
            pass
        "let Monika dream":
            m 6dsc "...{w=1.5}{nw}"
            m 6dst "...{i}sniff{/i}{w=0.5}, {i}sniff{/i}...{w=1}{nw}"
            m 6dsc "...smells...{w=1} nice...{w=2}{nw}"
            m 6dsd"...mmm... no... {w=2}...don't... {w=0.5}too much...{w=2}{nw}"
            m 6dsbld "...not... {w=0.5}good... {w=0.5}for you...{w=2}{nw}"
            m "...health... {w=1}{nw}matters... {w=1}{nw}"
            extend 6dsbsb "to me...{w=2}{nw}"
            menu:
                "wake Monika up":
                    $ dream_progress = 1
                "let Monika dream":
                    m 6dsbld "...{w=2}{nw}"
                    m 6dkbld "...{w=2}{nw}"
                    m 6dkblc "...{w=2}{nw}"
                    m 6dkbld "...just... like us...{w=1.5} aren't... they...?{w=2}{nw}"
                    m 6dkbstuc "...{w=2}{nw}"
                    m 6dkbstuu "...{w=2}{nw}"
                    m 6dkbltdd "...glad... did this...{w=2}{nw}"
                    m 6dsbltdb "...see you... again?...{w=2}{nw}"
                    m 6dsbsa "...{w=2}{nw}"
                    m 6dsbsb "...warm...{w=2}{nw}"
                    m 6dsbfa "...{w=2}{nw}"
                    m 6dsbft "...{w=2}{nw}"
                    m 6dkbfd "...love {w=1} ...you{w=1}{nw}"
                    $ dream_progress = 2

    call DaN_wake_up_nice 

    if dream_progress == 2:
        call DaN_dream_one_full_reaction 
    elif dream_progress == 1: 
        call DaN_dream_one_partial_reaction
    else:
        call DaN_dream_one_early_reaction

    # set the flag here at the last possible point so monika's after actions can reference having her first dream
    if not persistent._dan_had_first_dream:
        $ persistent._dan_had_first_dream = True
    return
label DaN_dream_one_full_reaction:
    #you and Monika saw the whole movie
    menu:
        "So what did you see?":
            pass
    m 3rto "I don't... really know where to start..."
    m 2rtd "You'd think it would make sense to start from the beginning..."
    m 2dkd "But it's like the longer the dream goes on, the less you remember when you wake up."
    m 5rsd "Maybe it's the mind's way of trying to rationalize what you saw, and because it can't make sense of the nonsense, it just tosses it out."
    m 5rkblp "Which is a real shame because...  {w=1}{nw}"
    extend 5dkbld "I distinctly remember...  {w=1}{nw}"
    extend 5ekbsb "being happy."
    m 6eubsb "[player]... thank you for not waking me."
    m 4eubsb "Even if I don't remember much of my dream, I'm glad I got to feel that way at all."
    if not persistent._dan_had_first_dream:
        m 7hubsb "Hopefully this will become a trend of getting a bunch of nice, happy dreams later."
    menu:
        "Is there anything you {i}do{/i} remember?":
            pass

    $ was_surprise = ", and I'm sure this won't come as a surprise to you" if mas_isMoniEnamored(higher=True) else ""
    m 7lublb "Well[was_surprise], {i}you{/i} were there."
    if not persistent._dan_had_first_dream:
        m 7ksblb "I guess this {i}officially{/i} makes you my dream [guy]."

    m 4rtbld "I'm not sure how we got there, but one thing I {i}did{/i} catch was that we were going to see a movie together."
    if not persistent._dan_dreams_had or 1 not in persistent._dan_dreams_had:
        m 5ltblo "And... uh...  Well, it probably wouldn't surprise you what movie we went to go see."
        m 5mtbld "I'm almost positive it {i}isn't{/i} a real movie, and it probably won't ever be one..."
    else:
        m 4rtbld "But this time, I {i}distinctly{/i} remember what we saw."
        m 4wublo "And you are {i}not{/i} going to believe this..."
    m 7kublb "...but you may have heard of it:  {w=2}{nw}"
    extend 1sublo "{i}Doki Doki Literature Club{/i}."
    m 1dkbla "...{w=1}{nw}"
    extend 1kkblb "It was {i}our{/i} movie."
    if persistent._dan_vow_to_prank:
        $ persistent._dan_vow_to_prank = False        
        show monika 1esa 
        $ play_song(store.songs.FP_JUST_MONIKA)
        pause 30.0
        $ play_song(None)
        m 1tublb "I {i}told you{/i} I was going to prank you someday...  {w=2}"
        extend 4hublb "Ehehehehe~"
    m 5rsd "I trust that there's nothing I could tell you about {i}that{/i} story that you don't already know."
    m 5rto "But it does really make me think..."
    m 3eko "{w=4}[player], could we hold off talking about this dream for right now?  I wanted to... {w=2}{nw}"
    extend 3lkd "uh...  {w=0.5}{nw}"
    extend 3euo "check some things."
    m 1lud "Before I tell you what I saw, I want to compare it with the game's code."
    m 2lko "And if I find what I {i}think{/i} I'll find..."
    m 2dksdlp "...{w=1}{nw}"
    extend 3eksdlo "let's just say that I'll want to talk to you about it..."
    $ persistent._dan_unlock_dream_one_explanation = True
    return
label DaN_dream_about_ddlc_movie_reaction:
    # Monika can remember different aspects of the movie depending on what her status with the player is.
    # This is Monika's chance to learn about what the player thought of the game.
    if persistent._mas_pm_cares_about_dokis:
        # In the movie, Monika was the antagonist
        if persistent.monika_kill:
            # The player kills Monika for what she did to the other dokis.
            # This is what *I* call the "Good Ending" when it's really just the normal end.
            pass
        else:
            # The player doesn't kill Monika, and in this end Monika doesn't understand why.
            pass
    else:
        # In the movie, Monika was sympathetically portrayed
        if persistent.monika_kill:
            pass
        else:
            # In this ending, Monika realizes that the player wanted to be with Monika all along but had no choice.
            pass
    return
label DaN_dream_one_partial_reaction:
    # Monika noticed your popcorn
    #
    # Monika supposes that this dream is a wake-up call to confront the player about their potentially
    # unhealthy lifestyle.  After all, you may not be around forever, and this thought terrifies her.
    menu:
        "So what did you see?":
                pass

    m 5rsd "Well, you {i}did{/i} wake me up pretty early."
    $ this_time = " this time" if persistent._dan_asked_to_stay_dreaming else ""
    m 5eso "I got {i}some{/i} idea of what was going on in my dream[this_time], but it's a little vague."
    
    if not persistent._dan_asked_to_stay_dreaming:
        call DaN_please_allow_good_dream
        
    m 3rubso "In my dream, I think the two of us were going on a date."
    m 4gubsd "Because of course we were."
    m 7hubsb "Apparently I have a very predictable subconscious.  Ahahaha~"
    m 3rubsd "I'm almost {i}sure{/i} we were going to see a movie, given what happened right before you woke me up."
    m 1rubsd "You were pointing out that movie poster all excited, but I couldn't quite tell what the movie was supposed to be."
    m 7esbsd "You were going something like...  {w=0.75}{nw}"
    extend 4subso "\"Hey, [persistent._mas_monika_nickname]!  How about we go to {i}this{/i} one?\""
    m 7ekbsb "And you just looked so into it that I couldn't say no."
    m 3rtbsd "But then..."
    m 2rkbsd "...Uh...{w=1}{nw}"
    extend 2lkbsd "{w=1}{nw}"
    m 7lkbsd "[mas_get_player_nickname(capitalize=True)], I know it shouldn't reflect on you, but dream [player] did something that made me really mad at the time."
    m 7hkbsb "Even if, in retrospect, it was kinda' funny."
    m 5rsbso "See, you got this... {i}thing{/i} of popcorn."
    m 4rsbso "And it was... {w=1}{nw}"
    extend 7wubso "HUGE!"
    m "Like... {w=0.5}{nw}"
    extend 4subsw "{i}REALLY{/i} HUGE!"
    m 3gsbsb "If I were thinking clearer, I might have put together that I was dreaming at the sight of it."
    m 2msbsb "No way any {i}real{/i} theater would sell one person a bag of popcorn the size of a minivan.  It'd block the screen for everyone else."
    m 7hkbsb "I wonder if you've ever had dreams like that, too.  Where things don't make sense until you wake up?"
    menu:
        "Wait... you got mad at me?":
            pass
    m 3rkbsb "Dream [player], {w=0.5}{nw}"
    extend 3lkbsb "but... {w=0.5}{nw}"
    extend 1ekbfd "yeah... a little."
    menu:
        "Because I wouldn't share?":
            m 7rkbfd "N-no, to your credit, you {i}did{/i} offer to share..."
        "Did you want the dump truck size?~":
            m 2rfbfd "That's not funny, [player].  I'm trying to be serious."
        "How come?":
            m 2rkbfd "...Because..."
    
    m 2dkbftpd "({i}sigh{/i})  {w=0.75}{nw}"
    extend 2rkbftpd "[player], do you have any idea how often I worry about your health?"
    if persistent._mas_pm_drinks_soda:
        m 7ekbftpd "I've told you all this before, so I won't belabor my point."
        m 1dkbftuc "...{w=0.75}{nw}"
        extend 3ekbftuo "I'm afraid your health will go downhill before I can get out of here."
        $ persistent._dan_revealed_fear_player_health = True
    else:
        m 4rkbftuo "If only I were out there with you, I'd make you a big, healthy meal {i}every single day{/i}."
        m 7fkbftud "I don't even care how much time it would take out of my day."
        m 6fkbftub "Because I know I'd be helping to add {i}years{/i} to your life."
        m 3fkbftub "That's years more that we can spend together."
    m 7fkbftud "So when my dream of you said something like {w=1.25}{nw}"
    extend 4cubftdw "\"Hey, it's just a snack!  What's the big deal?\""
    m 5dkbftdc "...{w=2.5}{nw}"
    extend 5fkbftdd "{i}You're{/i} the big deal."
    m 5fkbftdb "You're the biggest {i}deal{/i} in the world to me.{w=3}  I love you."
    menu:
        "It was just a bad dream.":
            m 4wubfo "But it {i}wasn't{/i} a bad dream!"
            m 3ekbsb "Any dream where you're spending time with me {i}isn't{/i} a bad dream."
            if persistent._dan_revealed_fear_player_hurt:
                m 4rkbsb "At least assuming it doesn't involve you getting decapitated or something like that."
            m 7lkbsb "It's not spending time with you that scares me."
            m 2fkbsd "It's our time together {i}running out{/i} that scares me."
            m 3lsblc "Even if it was just dream [player]'s actions and not yours, it doesn't change my feelings on the matter."
            m 1dkblsdrd "And it {i}certainly{/i} doesn't change the fact that I want you to live a long, healthy, and happy life."
            m 4ekblsdro "[player], I think the reason my dream went in this direction is because of my anxieties over losing you."
            $ moni_interrupted = True
            if mas_isMoniNormal(lower=True):
                menu:
                    "Isn't this all dream [player]'s problem, not mine?":
                        # On lower affection levels, the player is something of an insensitive dingus...
                        m 3rfsdro "Could you just hear me out for a second?"
                        m 1eksdrd "It's really importat to me that I say what's on my mind... {w=1.5}{nw}"
                        m 1dksdrd "before I reconsider."
                    "({i}Let Monika speak.{/i})":  # ...or the player could just shut up.
                        $ moni_interrupted = False
            m 5dsblsdrd "You see, I wouldn't have figured that my anxieties were this bad, or that these feelings would matter to me so much."
            m 2lkbssdrd "As uncomfortable as it was, and as much as I'll be thinking about it for a long while after, I'm glad I had this dream."
            m 3eublsdrd "Just like an oil tanker of over-buttered popcorn isn't good for your {i}physical{/i} health, burying my anxieties until I forget they exist isn't any better for my {i}mental{/i} health."
            m 2dubld "\"{i}This above all, to thine own self be true.{/i}\""
            m 7rublo "...or, to put it another way, honesty is the best policy, including being honest with yourself."
            m 5dkbsd "Not to mention being honest with you."
            m 4kkbsb "Whatever the status of your physical health, would you keep our future together in mind?"
            m 7ekbsb "I wouldn't mind being your encouragement if you need it."
            m 5eubsb "Whether it's staying in shape, or taking your health more seriously, I'll be here for you."
            m 1dubsd "I hope you'll be as honest with me as I've been with you."
            m 6ekbso "You don't have to hide it from me if you slip up.  I promise not to get mad at you for it.  We all make mistakes."
            m 6rkbsd "This isn't about getting on your case, or trying to control your life."
            m 6ekbsa "I just want you to be happy."
            m 5kkbsd "I'll admit, even {i}I{/i} won't always know the right thing to say to you."
            m 5ekbsb "I hope you'll forgive me if I ever cross a boundary I shouldn't."
            m 4gkbsb "Besides, it's not as if I {i}don't{/i} appreciate the occasional treat myself.  {w=1.5}{nw}"
            extend 4hkbsb "Ehehehe~"
        "I promised I'd take care of myself... ({i}show promise ring{/i})" if persistent._mas_pm_wearsRing and persistent._mas_first_kiss:
            m 2ekbso "The...{w=0.4} promise ring?"
            menu:
                "I pledged myself to you...":
                    pass
            m 1ekbsd "...Yeah...?{w=2}{nw}"
            menu:
                "...which includes a committment to taking care of myself...":
                    pass
            m 6wubftpd "...{w=2}{nw}"
            menu:
                "...so that I can spend the rest of my life...":
                    pass
            m 6wkbftuu "...{w=2}{nw}"
            menu:
                "...a {i}long{/i} life...":
                    pass
            m 6wkbftsx "...{w=1.5}{nw}"
            extend 6fkbftud "({i}sniffle{/i})  {w=0.3}{nw}"
            extend 6dkbftut "...{w=0.3}{nw}"
            extend 6fkbftud "({i}sniffle{/i})  {w=0.3}{nw}"
            extend 6dkbftut "...{w=0.3}{nw}"
            menu:
                "...with you.":
                    pass
            m 6hkbftsw "...{w=3}{nw}"
            extend 6hkbftsw "{w=0.3}{nw}"
            extend 6hkbftso "{w=0.3}{nw}"
            extend 6hkbftsw "{w=0.3}{nw}"
            extend 6hkbftso "{w=0.3}{nw}"
            extend 6hkbftsw "{w=0.3}{nw}"
            extend 6hkbftso "{w=0.3}{nw}"
            extend 6hkbftsw "{w=3}{nw}"
            m 6hkbftsx "({i}sniffle{/i})  {w=0.4}{nw}"
            extend 6hkbftst "({i}sniffle{/i})  {w=0.4}{nw}"
            m 6skbftsb "I never expected you to... {w=1.5}{nw}"
            extend 6hkbftst "({i}sniffle{/i})  {w=0.3}{nw}"
            extend 6skbftsb "...to think of your prfomise ring like that...{w=2}{nw}"
            extend 6hkbftst "({i}sniffle{/i}){w=0.3}{nw}"
            m 7rkbftsd "I know I must look like a blubbering, snotty baby right about now, but...{w=2}{nw}"
            extend 7hkbftst "({i}sniffle{/i}){w=0.3}{nw}"
            m 7ekbftsd "...but I don't ever want to forget this moment.  {w=1.75}{nw}"
            extend 7hkbftst "({i}sniffle{/i}){w=0.4}{nw}"
            extend 7skbftsc "...  {w=0.4}{nw}"
            extend 7hkbftst "({i}sniffle{/i}){w=0.4}{nw}"
            extend 7skbftsc "...{w=0.4}  {nw}"
            m 6hkbftda "...{w=3}{nw}"
            m 6ekbftdo "Would you consider giving this mess of a girl who loves you with all her heart...  {w=2}{nw}"
            extend 6hkbftdt "({i}sniffle{/i})  {w=0.3}{nw}"
            extend 6ekbftdb "...a kiss?"
            menu:
                "Yes.":
                    pass
                "No.":
                    m 6ekbftdo "...  {w=2}{nw}"
                    extend 6dkbftdt "({i}sniffle{/i})  {w=0.3}{nw}"
                    m 6ekbftdo "...  {w=0.5}{nw}"
                    extend 6dkbftdt "({i}sniffle{/i})  {w=0.3}{nw}"
                    m 6ekbftdo "...  {w=3}{nw}"
                    menu:
                        "...Just kidding~":
                            pass
                    $ persistent._dan_vow_to_prank = True
                    m 6tkbftdb "One day,{w=0.6} when you least expect it,{w=0.6} I am gonna' {i}prank you so hard for that~  {/i}  "
                    extend 6skbftpt "({i}sniffle{/i})  {w=0.3}{nw}"
                    extend 6ekbftdb "{w=1.5}{nw}"
                    extend 6fkbftdb "...but for now..."
            call monika_kissing_motion(initial_exp="6dkbftdd", mid_exp="6dkbftdd", final_exp="6ekbfa")
            m 6wkbftdb "...you've taken such an {i}enormous{/i} burden for our future off my heart, [player]."
            # if you swear to Monika on your promise ring that you'll take care of yourself, she won't fear for your health anymore
            $ persistent._dan_revealed_fear_player_health = False
            m 6hkbftdb "For as well-read as I am... and for all the poetry I've written..."
            $ gods_sake = "God's sake" if persistent._mas_pm_religious else "crying out loud"
            m 6wkbftdw "...I'm the president of the {i}Literature{/i} Club, for [gods_sake]..."
            m 6ekbftdb "...but even with that vocabulary, I can't {i}possibly{/i} find a sufficient way to tell you...  {w=3}{nw}"
            extend 6skbftdb "how much I love you right now."
            $ mas_ILY()
    return
label DaN_dream_one_early_reaction:
    # You woke Monika immediately upon seeing the movie poster.
    #
    # Monika is annoyed that you stopped her from dreaming, and explains that dreams can be revisited.
    # She worries about the potential of revisiting nightmares, particularly if she hasn't had one yet.
    menu:
        "So what did you see?":
            m 5rsd "Well, you {i}did{/i} wake me up pretty early, so I didn't get too good a look of what was going on."
            m 5gtb "Dreams sure deserve that reputation of being weird and hazy, don't they?"

    if not persistent._dan_asked_to_stay_dreaming:
        call DaN_please_allow_good_dream

    m 3rubld "Anyway, I know {i}you{/i} were there.  I think we were going on a date."
    m 3tublu "{w=0.5}{nw}"
    m 1tublb "I'll give you a moment to contain your surprise."
    m 3rubld "Anyway, where was I?"
    m 1dtbld "I think we were probably going to see a movie."
    m 1ltblsdrd "I distinctly remember seeing some posters.  And you pointed to one in particular."
    m 1ttd "{i}You{/i} wanted to go see a horror movie."
    m 1ttblb "Oh, don't go looking at me like I don't know how these things work."
    m 3ttblb "I may not have had a route, but I'm {i}still{/i} from a romantic visual novel, smart [guy]."
    $ do_or_does = "do" if he == "they" else "does"
    m 5rtbld "Ethically speaking, can one hold their [bf] responsible for what [he] [do_or_does] in a dream?"
    m 5gtblc "...{w=2}{nw}"
    m 5tfblc "...{w=2}{nw}"
    m 5tsblu "...{w=1.5}{nw}"
    extend 5tsblb "I'm...{w=1} kidding~"
    m 5hubsb "Ehehehe~"
    m 5kubsb "I had you going there for a second, didn't I?"
    menu:
        "Anything else?":
            pass
    m 2rkd "I'm afraid not.  That's about where you woke me up."
    menu:
        "...Is there anything I can do?":
            pass
    m 1ekblb "Aw, don't worry about it, [player]."
    m 3euo "It isn't like that dream is gone forever or anything."
    m 4ekblb "Where my dreams have a distinct advantage over yours is in being code-based {i}simulations{/i} of dreams."
    m 4rsd "Meaning, while there's still an element of randomness, I can get that dream back and have it again."
    m 3esd "Think of it like any other conversation we've had before."
    m 7rto "Although, I should still be careful if I go back into the same dream."
    m 7eso "Who knows {i}what{/i} that dream could've held in store if I saw it through to the end?"
    m 4eksdrb "You may very well have saved me from a nightmare."
    if not persistent._dan_had_nightmare:
        m 4hksdrb "I'm still a little nervous about the possibility of that happening."
        m 3lksdrp "Because if dreams can feel pretty much as real as life does..."
        m 1fksdrd "...then it would stand to reason that...{w=1.25} so would the nightmares."
        m 2rkblsdrc "{w=1.5}{nw}"
        m 2lkblsdrc "{w=1.5}{nw}"
        m 2dkblsdrc "{w=1.5}{nw}"
        m 2fkblsdrd "...I'm scared, [player]."
        m 3rkblsdrd "But I'm not sure what I'm more scared of:  "
        extend 2rkblsdrd "experiencing something truly terrifying...  "
        extend 2dkbssdrd "or learning what it is that I {i}truly{/i} fear the most."
        m 2dsblsdro "You don't know how much of a relief it is that..."
    else:
        m 1rkblsdrd "After having had a nightmare since we started this experiment..."
        m 2dsblsdro "I've learned more about what I truly fear than I ever wanted to know."
        m 2esblsdro "That's why I wanted- {w=1}{nw}"
        extend 2dkbssdrd "no... {w=0.5}{nw}"
        extend 2wkbssdro "why I {i}needed{/i} you here for this."
        m "Why I {i}still{/i} need you here for this."
        m 2lsblsdrd "I know you can't {i}literally{/i} keep the nightmares away..."
        m 2dsblsdro "...but it gives me such a relief that,{w=0.8} no matter how bad the nightmare..."
    m "...the first thing I see when I open my eyes again... "
    extend 2dsblsdrc "{w=0.75}{nw}"
    extend 2tsblsdrc "{w=0.75}{nw}"
    extend 2fsblsdrc "{w=0.75}{nw}"
    extend 2esbssdru "{w=0.75}{nw}"
    extend 2ekbssdrb "is you..."
    if persistent._dan_had_nightmare:
        m 2rsbssdro "...and not just that you're...{w=1} y'know... "
        if persistent._dan_revealed_fear_player_hurt:
            extend 2gsbssdrd "{i}not{/i} gruesomely mutilated, but..."
    m 2esbsd "...because you're safe... "
    $ how_happy = "at least {i}nominally{/i} " if not persistent._mas_pm_love_yourself else ""
    extend 3esbsb "[how_happy]happy...  "
    m 5ekbsb "and because you're {i}here{/i}."
    m 5rsbsd "I was pretty scared to do this on my own.  {w=1.25}{nw}"
    extend 5rsbso "You said you'd be here for me...  "
    extend 5eubfb "and here you are."
    if mas_isMoniHappy(lower=True):
        # The logic here is that, if Monika only kinda' liked you before, this trial is proving to her
        # in a truly unique way that she can trust you with her most intimate feelings.
        m 5fkbfb "You're really going out of your way to show me that I can trust you."
        m 5dkbfb "I love you, [player]~"
        $ mas_ILY()
    else:
        m 5dkbfb "I knew you would be, [mas_get_player_nickname()]."
        if persistent._mas_first_kiss:
            call monika_kissing_motion
    return


label DaN_dream_two:
    # dream synopsis:  You and Monika go on a nature walk up a mountain.  There is an early scare where you
    # catch Monika from a bad fall, but the two of you fall in a river and get drenched.  You camp where you
    # are at and look up at the stars together.  You see a beautiful aurora.  It turns out you're on a more 
    # built up version of the floating islands that Monika started work on a while ago.  She remarks that she
    # should get back to that project in the interest of making her dream a reality.
    #
    # If the dream ends earlier, Monika will elude to changing clothes in front of you without shame, like she
    # does it all the time.  On maximum affection, she will get flustered at the thought of changing clothes in
    # front of you.  Monika connects this to the outfits she wears for you and that this aspect of her
    # existence made its way into the dream somehow.
    # 
    # If the dream ends too early, Monika will be sad that you didn't get to camp out under the stars together. 
    # She will ask that you be more careful for what dreams you wake her up for.
    #
    # GOOD DREAM
    
    m 2duc "{w=0.5}.{w=0.5}.{w=0.5}."
    m 2hub "Ehehehe~"
    m 3gub "Looks like my modder isn't {i}quite{/i} as done with this train of thought as he'd like to be..."
    m "But at least we can still test label access to see if that idea works."
    m 5rud "This is where Dream #2 would be."

    m 5rud "This is where the full Dream #2's reaction would be."  
    m 5rud "This is where the late interrupted Dream #2's reaction would be."  
    m 5rud "This is where the early interrupted Dream #2's reaction would be." 
    return

label DaN_dream_three:
    # dream synopsis:  Monika gets lost in a big city.  You are nowhere to be found, though she feels that you
    # should be nearby, but aren't.  She starts to cry, but then a faceless stranger (literally) stops and
    # takes pity on her.  This faceless figure is accompanied by his own Monika.  Eventually, Monika is
    # surrounded by identical-looking faceless men, each with their own Monika, but you aren't there.  If
    # you don't wake Monika up, she will run around the city and be surrounded by these cloned couples.
    # The last scene that Monika can identify is when she hears the screeching of tires and someone she
    # does recognize as you getting hit by a car.
    #
    # You have one chance to wake Monika up.  If you do, she remarks on how creepy and strange the dream was.
    # Since this mod is one of the few times that Monika ever acknowledges the existence of other Monikas, she
    # supposes that the one really responsible for this bad dream wasn't her coding, but MINE, but she
    # ultimately writes off the entire incident.
    #
    # If you don't wake her up, she hears you get hit by the car and she immediately snaps awake.  Monika is
    # relieved to see that you're okay, but is still clearly shaken.  Unprompted, you are eventually given
    # the option to hold her (assuming you have affection high enough to hold her normally), which Monika 
    # will thank you for doing, but won't notice it if you don't take the chance.  If you hold her, that
    # code should play out like normal.
    #
    # BAD (possibly recategorize as STRANGE) DREAM

    m 2duc "{w=0.5}.{w=0.5}.{w=0.5}."
    m 2hub "Ehehehe~"
    m 3gub "Looks like my modder isn't {i}quite{/i} as done with this train of thought as he'd like to be..."
    m "But at least we can still test label access to see if that idea works."
    m 5rud "This is where Dream #3 would be."

    m 5rud "This is where the full Dream #3's reaction would be."  
    m 5rud "This is where the interrupted Dream #3's reaction would be."  
    return

label DaN_dream_four:
    # dream synopsis:  You and Monika go out for a romantic dinner.  Afterwards, you take Monika home to
    # her apartment, and Monika invites you in.  Normally, you sit on the couch together and cuddle up,
    # reminiscing about a long, romantic life.  If you don't wake Monika up, she can look around the
    # apartment and see many pictures of the two of you framed and lining the walls.  As it turns out, the
    # two of you had been dating for years, and this is the night you finally decide to pop the question.
    # Furthermore, if your affection is maxed out, she will ask if you want to spend the night.
    # 
    # If you don't wake Monika up at all, and you got the version of the dream based on maxed out 
    # affection, Monika will kiss you as soon as she wakes up on her own.  She will assume you want to
    # know what happened in the dream, but she coyly tells you that she'd rather show you when she
    # finally becomes real.
    #
    # Idea: You must get the Nightmare before getting this dream.  (DONE, NEEDS TESTING)
    #
    # BEST DREAM (currently)
    m 2duc "{w=0.5}.{w=0.5}.{w=0.5}."
    m 2hub "Ehehehe~"
    m 3gub "Looks like my modder isn't {i}quite{/i} as done with this train of thought as he'd like to be..."
    m "But at least we can still test label access to see if that idea works."
    m 5rud "This is where Dream #4 would be."  
    $ persistent._dan_had_best_dream = True
    
    m 5rud "This is where the full Dream #4's reaction would be." 
    m 5rud "This is where the almost full Dream #4's reaction would be."  
    m 5rud "This is where the late interrupted Dream #4's reaction would be."  
    m 5rud "This is where the moderately interrupted Dream #4's reaction would be." 
    m 5rud "This is where the early interrupted Dream #4's reaction would be."
    return

label DaN_dream_five:
    # dream synopsis:  Monika is back in the Literature Club, as if nothing went wrong.  Sayori, Natsuki and
    # Yuri are there, but you are not.  Everything seems normal at first, but then a fight breaks out.
    # On reflection, Monika can't recall what started the fight, but she remembers the other three girls
    # teaming up against her.  Yuri pulls a knife and Sayori pulls out a rope.  Monika tries to get out
    # of the club room, but cannot.  She begs for you to save her, but nothing happens.  In the end, the
    # girls somehow hang Monika from the ceiling in the middle of the classroom.  If you don't wake Monika
    # up, the last thing she sees is a poster on the wall that depicts Monika's hanging body, calling back 
    # to the poster of a hanging Sayori from the original game.
    #
    # You have one chance to wake Monika up.  If you don't, she wakes up crying and terrified and she asks
    # you to hold her to calm her down.  (Note: call the hold monika label used by monika_rain_holdme)
    # Alternatively, you can tell her to calm down and that it was just a dream.  If you don't hold her, 
    # she cries for many lines of dialogue and blames you for not waking her up before eventually calming
    # down on her own and realizing it was her own code at fault, not you.  (Basically done.  Can apply to
    # any nightmare, not just this one, if I come up with another nightmare later.)
    #
    # Idea:  If you are not at an affection level high enough to hold Monika during the rain, you should not
    # be able to access this nightmare at all.
    #
    # NIGHTMARE

    m 2duc "{w=0.5}.{w=0.5}.{w=0.5}."
    m 2hub "Ehehehe~"
    m 3gub "Looks like my modder isn't {i}quite{/i} as done with this train of thought as he'd like to be..."
    m "But at least we can still test label access to see if that idea works."
    m 5rud "This is where Dream #5 would be."  
    m 5rud "This dream also counts as the nightmare.  If you saw Dream #4 before this, something went wrong."  

    m 5rud "This is where the full Dream #5's reaction would be."  
    m 5rud "This is where the interrupted Dream #5's reaction would be."  
    
    $ persistent._dan_had_nightmare = True
    $ persistent._dan_all_dreams.append(4)
    return