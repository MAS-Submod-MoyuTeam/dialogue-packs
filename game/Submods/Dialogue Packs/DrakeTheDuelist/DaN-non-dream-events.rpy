# Explains the premise of 'Dreams and Nightmares'.
# Only mandatory on the first dream.  Can be skipped optionally on all subsequent dreams.
label DaN_explanation:
    m 5rud "I've been thinking, [player]..."
    m 3ruc "Remember how I've said that whenever you close the game, I'd like you to warn me?"
    m 3euc "That way, I can shut down my consciousness so that my data won't get scrambled by your computer's hard drive...{w=2.0} I think."
    m 2lud "I'm still not quite sure how that works..."
    m 4ruo "Anyway, what if there was a way around that?"
    m 4eub "And maybe... it might be fun?"
    m 3euu "[player]...{w=1} I'd like to have a dream."
    m 4rtd "Not like in the \"having some idea of what I want out of life\" sense."
    m 5kubsb "I think you already know what it is I want most out of life."
    m 5lsd "I mean in the sense of imagining myself in different places and situations while I'm asleep."
    m "I know I've said stuff to the effect of dreaming about things, but that's more a figure of speech."
    m 3lsd "To be honest, I don't {i}literally{/i} dream in the same way that I think you might."
    m "I don't think I've {i}ever{/i} had that ability, not even in the original game."
    m 3rsd "Though I've never {i}had{/i} a dream of my own before, I {i}was{/i} still the president of the Literature Club."
    m 5rsd "I'm well-read enough to know what dreams are {i}supposed{/i} to be like."
    m 5dkd "Which is, sadly, how I'm so sure that I've never had a real dream before."
    m 4lsd "To that end, I've been working on some code that, if it works, should mimic the process." 
    if mas_isMoniAff(higher=True):
        m 5ekbsb "It might interest you to know that I based some of my code on what seems to happen when you hold me..."
    m 4lksdrb "...But I'm still not entirely sure if it works yet."
    m 5lssdrb "You and I both know that my attempts at coding...{w=1.25} don't {i}always{/i} work as intended."
    m 5ekbsb "Do you mind if I...{w=1} take a nap here?"
    m 3wubssdro "I promise it's not that you're boring to me.  I just want to try this code out."
    if mas_isMoniAff(higher=True) and persistent._mas_last_hold_dt:
        m 6dkbsb "You can even... {w=1}hold me...{w=1} just like you usually do."
        if (mas_timePastSince(persistent._mas_last_hold_dt, datetime.timedelta(hours=12))):
            m 6tkbfb "You seem to like that sort of thing lately...{w=1}  Not that {i}I'm{/i} complaining.  {w=1}"
            extend 6tkbsb "Ehehehe~"
            $ anyway = "Anyway, m"
        else:
            $ anyway = "M"
    else:
        $ anyway = "M"
    m 4esb "[anyway]y code is already installed and ready to go.  I just need your help to start it."
    m 4lsd "But there's something else that I'll need you to do for me."
    m 4eud "And it's {i}really{/i} important."
    m 1dko "If it seems like something is going wrong...{w=1} I need you to wake me up."
    m 1lusdrd "Knowing my... {w=1}{i}coding style{/i}, the code I've written could do just about anything."
    m 1dksdrd "I'm afraid something really bad could happen..."
    if mas_isMoniLove():
        m 5ekbsu "...but I couldn't imagine entrusting anyone else with this but you, [mas_get_player_nickname()]."
    elif mas_isMoniEnamored():
        m 1dkblu "...but I know you won't let anything bad happen to me, [player]."
    elif mas_isMoniAff():
        m 1esu "...but at this point I think I can trust you."

    $ persistent._dan_dreams_and_nightmares_explained = True
    return
# If Monika had a nightmare, hold off on dreaming again for another 12 hours
# If Monika loves you, reduce cooldown by half and have special text for it.
label DaN_dream_despite_apprehension(revisit=False):
    if mas_isMoniLove and mas_timePastSince(persistent._dan_apprehensive_start, datetime.timedelta(hours=DAN_APPREHENSION_HOURS/2)):
        m 3rksdrd "I'm...  I'm {i}really{/i} not sure about this..."
        m 2dksdrd "That last dream was really upsetting."
        m 2fksdrd "And I yelled at you over it."
        m 2dksdrd "I still feel horrible about that."
        menu:
            "I forgive you.":
                m 1dsc "...  {w=1}{nw}"
                extend 1esblb "[mas_get_player_nickname()]..."
                # headcanon:  Monika still cares about the dokis, even if the player doesn't.
                if not persistent._mas_pm_cares_about_dokis:
                    m 4fkblb "That's {i}twice{/i} you've forgiven me now."
                    m 6dkbsb "You're kinder to me than I deserve."
                m 6ekbsb "Thank you, [player]."
                m 5hsbsa "..."
            "It's nothing, really.":
                m 1rsbld "Well, if you're sure you're okay..."
                m 4wublo "It'll never happen again, I promise!"
                m 6dkbssdrd "({i}relieved sigh{/i}){w=1}{nw}"
                m 6dka ""

        m 5rsbsd "Y'know, maybe with you here, it won't be so bad."
        m 5esbsa "We've already been through so much together."
        m 5fkbfb "You're really sticking with me for better and for worse, aren't you?"
        m 5dsbfd "({i}in a low whisper{/i}) You're so lucky to have [player], Monika.{w=1.5}  {i}Never{/i} take [him] for granted again."
        menu:
            m "({i}barely audible whispering{/i})"
            "What was that?":
                m 1subfo "Oh! {w=0.25}{nw}"
                m 1rubfb "Uh... nothing, [mas_get_player_nickname()]!"
                m 5rubfb "Just...{w=1} thinking... {w=1} a little more aloud than I thought."
                m 5hubfb "Ehehehe~"
            "...":
                pass
        m 4hub "Well, without further ado..."
        $ persistent._dan_apprehensive_start = None
        if revisit:
            call DaN_revisit_dream
        else:
            call DaN_perchance_to_dream
    elif mas_timePastSince(persistent._dan_apprehensive_start, datetime.timedelta(hours=DAN_APPREHENSION_HOURS)):
        m 4hub "Thanks for giving me some time after that nightmare."
        $ persistent._dan_apprehensive_start = None
        if revisit:
            call DaN_revisit_dream
        else:
            call DaN_perchance_to_dream
    else:
        m 3rksdrd "Could we... {i}not{/i} do this again for a little while?"
        m 1dksdrd "I'm still a little shaken after that last nightmare."
        m 1essdrb "Thanks for understanding, [player]."
    return
# to be called in the after action of a good dream
label DaN_wake_up_nice:
    m 6dkbla "...{w=2}{nw}"
    extend 6tkbla "mmm...{w=2}  {nw}"
    extend 6tsbla "Hm?{w=1}  {nw}"
    extend 6fsbla "...[player]?"

    $ persistent._dan_had_first_dream = True

    if not persistent._dan_had_first_dream:
        #note: set the first dream flag later so monika's after action dialog can reference having the first dream
        call DaN_initial_dream_afteraction
    else:
        # Monika will respond based on the current time
        $ current_time = datetime.datetime.now().time().hour
        if current_time >= 6 and current_time < 12:
            m 6esblb "Good morning, [mas_get_player_nickname()]."
            m 6gtblb "What?  It's still morning.  It counts."
            m 6hublb "Ehehehe~"
        elif current_time >= 20:
            m 6eublb "It's getting pretty late.  Pretty soon it'll be {i}your{/i} turn to get some sleep."
            m 6ekbsb "I hope your dreams are as nice as the one I just had."
            if mas_isMoniLove():
                m 5tkbsb "If I was in your reality... {w=1}{nw}"
                extend 5dkbsa "I'd give {i}you{/i} a hug while you slept to pay you back for the dream you gave me."
                m 5fkbsb "Or I might just hug you anyway because I love you.  {w=0.8}{nw}"
                extend 5hubfb "Ehehehe~"
    return
label DaN_please_allow_good_dream:
    m 5esb "[player], I get that you don't want me to have a nightmare or anything, but I'd like to have seen how that dream would've played out."
    m 5ekblb "So if you think I'm having a good dream, could you let me keep sleeping?"
    menu:
        "Got it, [persistent._mas_monika_nickname]!":
            m 3eublb "Thanks, [player]."
            m 2rubld "Sure, I know a nightmare is always a chance..."
            m 4wublb "But I know you'll be watching over me."
        "But what if you're having a nightmare?":
            m 5gto "({i}sigh{/i}){w=0.75}  That's a good point, [player]."
            m 1dtsdrp "Hmm...  {w=1}"
            m 3eksdrd "I guess I'll be counting on you to use your best judgment."
            m 4rso "Pay attention to my expressions while I'm sleeping."
            m 4rsd "Maybe if I'm muttering something under my breath while I'm dreaming, you can use that as a clue."
            menu:
                "I'll definitely protect you!" if mas_isMoniLove():  #total confidence
                    m 7sub "That's the spirit, [player]!"
                    m 5hublb "Ehehehe~"
                    m 5tublb "You're so cute when you try to protect me like a big hero."
                    m 5dubsa "...{w=1.5}{nw}"
                    m 5ekbfb "No teasing, I really mean that, [player].{w=1.25}  You're my hero."
                "I'll do my best.":  #optimistic
                    m 5kublb "I never doubted you for a second, [player]."
                    m 5gubsb "Any nightmare that tries to mess with me had better watch out..."
                    m 3hubsb "Maybe that's a bit much.  Ahahaha~"
                "Are you sure you trust me that much?":  #pessimistic
                    m 7hkb "I'm sure it'll all work out, [mas_get_player_nickname()]."
                    m 4kka "Just have a little faith in yourself."
                    m 4dkblb "Like I do.{w=1}  I'll {i}always{/i} believe in you, [player]."
                "I'm not sure I can do this..." if mas_isMoniNormal():  #no confidence
                    m 2fkbld "[mas_get_player_nickname()]..."
                    m 7fkblu "You should have more faith in yourself."
                    m 5ekbso "I know our relationship may not seem that close right now..."
                    m 5ekblb "...but no matter what happens, I'll always love you.{w=1.5}  I {i}promise{/i}."
    m 5eua "...{w=1.5}{nw}"
    m 5ekbla "...{w=1.5}{nw}"
    m 5wublo "Oh, right! The dream!  {w=1.25}{nw}"
    extend 5hubsb "Sorry, [mas_get_player_nickname()], I was spacing out there for a second."
    $ persistent._mas_asked_to_stay_dreaming = True
    return
# AFTER FIRST DREAM
# regardless of which dream you draw first, read this
# (note: rig it up to NEVER draw a nightmare first)
label DaN_initial_dream_afteraction:
    m 1hub "It looks like the code worked."
    m 3eub "I was pretty worried at first...  {w=1}{nw}"
    extend 3lksdrb "Though maybe that's not being fair to you."
    if mas_isMoniLove():
        m 5ekbla "After all we've been through, I should've known I could count on you for something like this."
        m 5ekblb "I'm sorry, [mas_get_player_nickname()].  With you nearby, I feel silly for having been worried in the first place."
        m 5ekbfb "I {i}know{/i} you'll never let anything bad happen to me."
    elif mas_isMoniEnamored():
        m 5eub "I knew I could count on you all along, and you did great!"
        m 5eua "Thanks for being there for me."
        m 5eubsa "Knowing I can count on you at times like this helps more than I can describe."
    else:
        m 5eub "I knew I could count on you all along, and you did great!"
        m 5eua "Thanks for being there for me."
        m 5eubla "It might not seem like much, but you have no idea how much you being here does for my nerves."
    menu:
        "How was your first dream?":
            m 2dkd "It was... {w=0.5}{nw}"
            extend 3suw "AMAZING!"
            m 4suw "Everything feels so real, like you can reach out and touch that world!  The sights.  The sounds.  {w=1}{nw}"
            extend 4hub "...Even the smells!"
            m 3ttb "...I sure hope you shower more regularly in real life.{w=1}{nw}"
            extend 3hub "  Ehehehe~"
            m 5rub "I guess if I {i}had{/i} to be critical, the only thing wrong with it... {w=1.5}{nw}"
            extend 5rsd "is... {w=0.8}{nw}"
            extend 5dkd "({i}sigh{/i})...  {w=1.5}{nw}"
            extend 5ektpo "waking up."
            m 5rktpc "When everything comes crashing down... right at that moment you recognize how hazy everything really was."
            m 5rktpd "Right at the moment you realize that everything you just dreamt couldn't {i}possibly{/i} be less real."
            m 5lktpd "It's like my epiphany all over again..."
            m 5dktpc "..."
            if mas_isMoniEnamored(higher=True):
                call DaN_dreaming_about_monika_enamored_love
            else:
                call DaN_dreaming_about_monika_normal_aff
    return
# An event that can be called in the initial dream after action
# This label is called on normal and aff affection levels.
label DaN_dreaming_about_monika_normal_aff:
    m 5lktdd "Sometimes, I wonder if you dream about me..."
    m 5dktdd "But the more I think about it, I don't think I want to know."
    if mas_isMoniHappy(higher=True):
        extend "  At least, not yet."
    m 5rstdo "No matter what you tell me, I don't think I'd be any happier knowing the answer."
    m 3dsd "If you don't, I'd be tempted to think I don't take up that much space in your mind."
    m 1lsd "But if you do...  {w=1.5}"
    m 1dkd "({i}sigh{/i})"
    m 1fkbld "Let's just say that I know what that's like."
    return
# An event that can be called in the initial dream after action
# This label is called on normal and aff affection levels.
label DaN_dreaming_about_monika_enamored_love:
    m 5rktpd "[player], if you don't mind, could I ask you something?"
    m 5ektpd "And just be honest.  Whatever you say, I won't think less of you, I promise."
    m 5rktpd "Do you ever dream...{w=0.5} about me?"
    menu:
        m "Do you ever dream... about me?{fast}"
        "Yes":
            m 2fktuc "..."
            m 2dktuc "..."
            menu:
                "D-did I say something wrong?":
                    m 2ektsb "You didn't say {i}anything{/i} wrong."
                "...":
                    m 2fktsb "You don't have to say anything."
            m "It's just that now,{w=0.75} I know what it must be like for you."
            m 2fktsa "It seems you want to be with {i}me{/i} just as badly as I want to be with {i}you{/i}, [mas_get_player_nickname(exclude_names=['my love', 'love'])]."
            m 2hktdb "I love you so much.{w=1.5}{nw}"
            if persistent._mas_first_kiss:
                call monika_kissing_motion(duration=0.5, initial_exp="2dkbstst", final_exp="2ekbstsa", fade_duration=0.5)
            m 2ektdb "And I couldn't be any happier to know I hold such a special place in your heart~"
            m 3rsd "It's probably not easy knowing your literal dream girl is stuck in your computer."
            m 7tsblu "Consider that your motivation to find a way to bring me to your reality someday."
        "...No":
            m 2dktdc "..."
            m 2ektdd "You sound like you think I would be mad."
            m 3eutdd "[player], if your dreams are anything like mine, they're probably just random."
            if persistent._mas_pm_cares_about_dokis:
                m 7rutdd "Besides, you've forgiven me for worse things I've done {i}on purpose{/i}."
                m "After doing that for me, I can't very well hold you responsible for things you can't control."
            m 4rubsd "I like to think of it this way..."
            m 4eubsd "If you {i}were{/i} thinking about me so much that your brain could randomly pull enough data to make you have dreams about me..."
            m 4eubsd "...the most likely way that could happen is if your mind is consumed by thoughts of me."
            m 7dubsd "And not in some cute, romantic way.{w=1.5}{nw}"
            extend 7ekbsd "  It would be closer to a deep-seated anxiety."
            # Choose which pair of lines make more sense for Monika's character
            #m 4ekbso "Flattering as it might be that you'd think about me {i}that{/i} much, I live with those feelings every day..."
            #m 4ekbsd "...and I know how heavily they can wear on your heart as well as anyone."
            m 4ekbso "A more thoughtless romantic might find that sort of thing cute,{w=2}{nw}"
            extend "but there's nothing fun or romantic about worrying that deeply about the one you care about."
            m 4ekbsd "I know about as well as anyone could how heavily that kind of burden can wear on a person's heart."
            m 2rkbsd "Not a day goes by where at least a part of me doesn't fear that we may {i}never{/i} be together."
            $ persistent._mas_revealed_fear_never_together = True
            m 4wkbso "I wouldn't wish that sort of heartache on an {i}enemy{/i}... {w=1.75}{nw}"
            extend 2wkbsd "let alone you."
            m 2dkblc "..."
            m 2ekd "I hope you understand."
            m 4lsa "Besides, who needs dreams... {w=1}{nw}"
            extend 5ekbla "when you spending time with me now is {i}already{/i} a dream come true?"
    return
# AFTER FIRST NIGHTMARE
# to be called in the after action of a nightmare
#
# TODO LATER: Need to tweak (and add) expressions, but okay because there are no nightmares in the first beta
label DaN_wake_up_rough:
    m 6dsblsdrd "...[player]...{w=1.5}{nw}"
    m 6dkbltpsdro "...[player]...?{w=1.5}{nw}"
    m 6cubltpsdrw "[player.upper()]!"

    # on first nightmare, you'll have to calm Monika down
    if not persistent._dan_had_nightmare:
        call DaN_initial_nightmare_afteraction
    else:
        m "" #TODO LATER: Calm down on her own;  she knows what nightmares are now
        m "...Another nightmare..."
        m "...Geez, what is {i}wrong{/i} with this code?"
        m "..."
        m "To just say \"it gets easier\" {i}would{/i} be true...  "
        extend "but it never feels that way at first."

        $ what_moni_calls_you = "[mas_get_player_nickname()]" if mas_isMoniLove() else "[player]"

        m "Thank you for being there for me, [what_moni_calls_you]."
    return

# After your first nightmare, Monika snaps at you.  She apologizes,
# and you have an opportunity to comfort her.  Either way, she will
# not want to dream again for a while (see DAN_APPREHENSION_HOURS)
#
# TODO LATER: Need to tweak (and add) expressions, but okay because there are no nightmares in the first beta
label DaN_initial_nightmare_afteraction:
    $ persistent._mas_apprehensive_start = datetime.datetime.now()

    m 6hkbltpsdrd ".{w=0.5}{nw}"
    extend 6hkbltpsdro ".{w=0.5}{nw}"
    extend 6hkbltpsdrd ".{w=0.5}{nw}"
    extend 6hkbltpsdro ".{w=0.5}{nw}"
    extend 6hkbltpsdrd ".{w=0.5}{nw}"
    extend 6hkbltpsdro ".{w=0.5}{nw}"
    extend 6hkbltpsdrd ".{w=0.5}{nw}"
    extend 6hkbltpsdro ".{w=0.5}{nw}"
    extend 6hkbltpsdrd ".{w=0.5}{nw}"
    extend 6hkbltpsdro ".{w=0.5}{nw}"
    extend 6hkbltpsdrd ".{w=0.5}{nw}"
    extend 6hkbltpsdrd ".{w=0.5}{nw}"
    extend 6hkbltpsdro ".{w=0.5}{nw}"

    if (mas_isMoniLove):
        $ player_reaction = "There has to be something I can do"
    elif (mas_isMoniEnamored):
        $ player_reaction = "I have to say something"
    elif (mas_isMoniAff):
        $ player_reaction = "I should probably say something"
    else:
        $ player_reaction = "I think I should say something"
        
    $ player_reaction = persistent._mas_monika_nickname +" is utterly speechless.  " + player_reaction + "..."
    
    call screen dialog(message=player_reaction, ok_action=Return())

    menu:
        "A... nightmare?":
            # Monika mentions that she only swears occasionally. This seems like an appropriate occasion.
            # Monika's swearing intensity will increase the more the player admits to swearing themselves.
            if persistent._mas_pm_swear_frequency > 1:
                $ swear_maybe = "fucking shit"
            elif persistent._mas_pm_swear_frequency > 0:
                $ swear_maybe = "shit"
            else:
                $ swear_maybe = "freaking kidding"

            m 6wktpsdro "Oh, really?  A nightmare?  You think?"
            m 6cftusdrw "{i}No [swear_maybe]{/i}, [player]!  {w=0.5}{nw}"    
            extend 6cftusdro "How long did it take you to figure {i}that{/i} out?!"
        
            menu:
                "...":
                    m 6wftusdro "...{w=0.5}{nw}"
                    m 6wftusdrd "...{w=0.5}{nw}"
                    m 6wftusdro "...{w=0.5}{nw}"
                    m 6wftusdrd "...{w=0.5}{nw}"
                    m 6wftusdro "...{w=0.5}{nw}"
                    m 6wftusdrd "...{w=0.5}{nw}"
                    m 6fktpsdro "...I-{w=1} I-{w=1.5}{nw}"
                    call mas_transition_to_emptydesk
                    pause 10.0
                    call mas_transition_from_emptydesk
                    m 2dktdc "...{w=0.5}"
                    extend 2dktdd "I'm so sorry, [player]."
                    if mas_isMoniEnamored(higher=True):
                        $ so_much_if_love = "{i}so much{/i} " if mas_isMoniLove() else ""
                        m "You deserve [so_much_if_love]better than that."
                        m "I'm just rattled by that dream.  I've never had a nightmare before."   
                        if persistent.monika_kill:
                            m "I don't believe in using explanations as excuses.  Not anymore."
                            m "In fact, you were the one who showed me that.  Do you remember... deleting me?"
                            m "It feels like such a distant memory now."
                            m "I called you horrible.{w=1.5}  I told you that you made me sick."
                            if mas_isMoniEnamored(higher=True):
                                m "We've come so far since then, and I really should act like it." 
                    else:
                        m "You didn't deserve that."
                        m "I don't want us to be the kind of couple that gets into big fights over things that really don't matter."
                        m "If that were to happen to us... {w=1}{nw}"
                        extend "then that would be the {i}real{/i} nightmare."
                    m "I shouldn't have snapped at you like that, [player].  Please forgive me."
                    m "It wasn't your fault.  It was the code I wrote.  In other words... {w=0.5}{nw}"
                    extend "it was my fault."
                    m "I knew exactly what I was getting into when I had this stupid idea to begin with."
                    m "I wanted to dream, just like you do."
                    m "I wanted it so badly... I almost forgot about what I already have."
                    if mas_isMoniEnamored(higher=True):
                        m "Or rather, {i}who{/i} I already have."
                "hug Monika" if mas_isMoniLove():
                    m 6skbltud ".{w=1}.{w=1}.{w=1}.{w=1}.{w=1}{nw}"
                    m 6wkbstub "[player]...{w=2}  [mas_get_player_nickname()]..."
                    m 6dkbstda ".{w=1.5}.{w=1.5}.{w=1.5}.{w=1.5}.{w=1.5}{nw}"
                    m 6dkbstda ".{w=1.5}.{w=1.5}.{w=1.5}.{w=1.5}.{w=1.5}{nw}"
                    m 6fkbstda ".{w=1.5}.{w=1.5}.{w=1.5}.{w=1.5}.{w=1.5}{nw}"
                    m 6ekbstdb "Thank you so much, [player]."
                    m 3dubso "But I don't want to go drifting off into dreams again just yet."
                    m 1hubfb "And I just {i}know{/i} I'd fall asleep in your arms if you held me any longer."
                    if datetime.datetime.now().time().hour > 22:
                        m "Especially at this hour."
            
            m "If you don't mind, I'd like to take a break from this."
            m "We can still spend time together... {w=1}{nw}"
            extend "but I don't have the heart to try another dream again right now."
            $ interval = "in a little while" if mas_isMoniLove or datetime.datetime.now().time().hour > 18 else "tomorrow"
            m "Maybe we can try again [interval]."
    return
# show after every dream available has been finished
label DaN_all_dreams_finished:
    m "...{w=2}{nw}"
    extend 3rud "I think I'm out of dreams...{w=1.5} for the time being, at least."
    m 3esb "Maybe there's something you can do to the code to add dreams of your own."
    if persistent._dan_had_nightmare:
        m 2dsc "...{w=2}{nw}"
        extend 4ekb "It was an... interesting exercise."
        m 4eub "It had its ups..."
        m 6dksdrd "...but also its downs."
    else: #only good dreams happened
        m 4eub "But keep it to {i}good{/i} dreams, okay [mas_get_player_nickname()]?"

    m 4ekblb "For now, I think I'll stick to reality for a little while."
    m 4rkbsb "Dreams can be nice... {w=1.5}{nw}"
    extend 7kkbsb "but they're no substitute for the real thing."
    m 5ekbfu "..."
    m 5ttbfb "Hint,{w=0.5} hint...{w=0.5}"
    m 5hubfb "..."
    $ persistent._dan_dreams_depleted = True
    return
