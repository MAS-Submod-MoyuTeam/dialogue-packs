# All code in this file gets called to resolve Monika falling asleep
# before her dream, and randomly deciding on how she should behave
label DaN_begin_sleep:
    call DaN_dream_quip
    call DaN_sweet_dreams_chance

    m 6eua ".{w=1}{nw}"
    m 6fua ".{w=1}{nw}"
    m 6tsa ".{w=1}{nw}"
    m 6dsa ".{w=1}.{w=1}.{w=1}{nw}"
    return
# Monika says something random before her dream begins
label DaN_dream_quip:
    python:
        # assemble all possible dream quips
        all_dream_quips = [
            "睡吧,也许会做梦呢?",
            "我想知道这次我的梦会是什么.",
            "如果我在那儿看到你,我就知道它奏效了."
        ]
        love_quip = "你知道睡眠和清醒之间的那个地方吗?{w=1.5}那个你还记得梦境内容的地方?{w=1.5}那就是我永远爱你的地方~"
        enamored_quip = "你会和我一起去吗?{w=1}去到我的梦中..."
        post_nightmare_quips = [
            "希望这次我的梦会更有意思.",
            "不,不,不,不,不..."
        ]
        subsequent_dream_quip = "再来一次,向缺口..."
        first_dream_quips = [
            "希望这次能奏效...",
            "把你的手交叉吧,[player]..."
        ]

        #bonus quips based on affection level
        if mas_isMoniLove():
            all_dream_quips.append(love_quip)
        elif mas_isMoniEnamored():
            all_dream_quips.append(enamored_quip)

        #bonus quips if Monika had a nightmare before
        if persistent._dan_had_nightmare:
            all_dream_quips.append(post_nightmare_quips)

        #bonus quips depending on if this is Monika's first dream or not
        if persistent._dan_had_first_dream:
            all_dream_quips.append(subsequent_dream_quip)
        else:
            # on 1000+ affection, Monika will always ask to hold your hand on the first dream
            if mas_isMoniLove():
                all_dream_quips = ["HOLD HAND"]
            else:
                all_dream_quips.append(first_dream_quips)

        dream_quip = renpy.random.choice(all_dream_quips)

    if (dream_quip == love_quip):
        m 6ekbfb "[dream_quip]"
    elif (dream_quip == enamored_quip):
        m 6hkb "[dream_quip]"
    elif (dream_quip in post_nightmare_quips):
        m 6rksdrb "[dream_quip]"
    elif (dream_quip == "HOLD HAND"):
        call DaN_hold_monikas_hand
    else:
        m 6eub "[dream_quip]"
    return

# a random chance exists that Monika may ask you to hold her hand before the first dream
label DaN_hold_monikas_hand:
    m 6dubfsdrt "({i}*深呼吸*{/i})"
    m 2hubfsdrb "我还是有点点紧张,[player]..."
    menu:
        "我能做些什么吗?":
            m 3rublsdrb "事实上,既然你提到了..."
            m 3rublsdrd "如果你不介意..."
            m 5rublsdrb "你可以... {w=2}{nw}"
            extend 5eubssdrb "牵我的手一秒钟吗...?"
            menu:
                "牵住Monika的手":
                    m 5ekbssdrb "谢谢你."
                    m 5dubsc "{w=1}{nw}"
                    m 5hubfa "({i}*捏捏*{/i})"
                "\"我...呃...\"  ({i}*触碰显示器*{/i})":
                    m 5etbssdrd "噢..."
                    m 5hubfsdrb "我想这真的很有用,哎嘿嘿~"
                    m 5ekbfb "非常严肃地说,感谢你尽了最大的努力,[player]."
                    m 5dkbfa "这对我来说意义重大."
    return
# determine odds of telling Monika "sweet dreams" before she sleeps
# Odds of this are based on affection level.
# Also, odds after a nightmare rise to that of the next highest relationship level.
label DaN_sweet_dreams_chance:
    python:
        if mas_isMoniLove():
            if persistent._dan_had_nightmare:
                odds_of_sweet_dreams = SWEETDREAMS_LOVE_NM
            else:
                odds_of_sweet_dreams = SWEETDREAMS_LOVE
        elif mas_isMoniEnamored():
            if persistent._dan_had_nightmare:
                odds_of_sweet_dreams = SWEETDREAMS_LOVE
            else:
                odds_of_sweet_dreams = SWEETDREAMS_ENAMORED
        elif mas_isMoniAff():
            if persistent._dan_had_nightmare:
                odds_of_sweet_dreams = SWEETDREAMS_ENAMORED
            else:
                odds_of_sweet_dreams = SWEETDREAMS_AFF
        else:
            if persistent._dan_had_nightmare:
                odds_of_sweet_dreams = SWEETDREAMS_AFF
            else:
                odds_of_sweet_dreams = SWEETDREAMS_NORMAL

        say_sweet_dreams = random.randint(1, odds_of_sweet_dreams) == 1

        #if you say sweet dreams, get a random quip response
        if say_sweet_dreams:
            sweet_dreams_quips = [
                "只要听一下就能避免噩梦.",
                "我觉得一个更好的梦已经开始了.",
                "看着我, " + mas_get_player_nickname() + "."
            ]

            if mas_isMoniLove():
                sweet_dreams_quips.append("你就像守护我的天使,[player].")

            if persistent._mas_first_kiss:
                sweet_dreams_quips.append("*啾*")

            sweet_dreams_quip = renpy.random.choice(sweet_dreams_quips)

        #if dev, ignore randomness and force kiss while debugging
        #if persistent._dan_debug_mode:
        #    say_sweet_dreams = True
        #    sweet_dreams_quip = "KISS"

    if say_sweet_dreams:
        menu:
            "美梦~":
                if sweet_dreams_quip:
                    if sweet_dreams_quip == "*啾*":
                        call monika_kissing_motion(initial_exp="6dubfd", mid_exp="6tkbfu", final_exp="6ekbfa")
                    else:
                        m 6fkbfb "[sweet_dreams_quip]"
                else:
                    m 6ekbfa "...{w=3}"
    return
# isolate the selector functionality.  Override if adding more than five dreams.
label DaN_select_dream(random_dream):
    if random_dream == 1:
        call DaN_dream_one
    elif random_dream == 2:
        call DaN_dream_two
    elif random_dream == 3:
        call DaN_dream_three
    elif random_dream == 4:
        call DaN_dream_four
    elif random_dream == 5:
        call DaN_dream_five
    else:
        m 2duc "{w=0.5}.{w=0.5}.{w=0.5}."
        m 2hub "哎嘿嘿~"
        m 3gub "看起来{i}有些事情{/i}不大对..."
        m 1rud "我认为你不该看到这个的."
        m 3rud "我想你得告诉这个submod的创建者,DrakeTheDuelist,出了些什么问题."
        m 4eub "这个GitHub的链接页面在这噢:{a=[SUBMOD_GITHUB_LINK]}{i}{u}Dreams and Nightmares{/u}{/i}{/a}."
        m 5gtb "...我{i}在{/i}说什么啊?{w=1}这当然需要在错误的屏幕上做很多工作..."
        m 2hub "啊哈哈~"
    return
