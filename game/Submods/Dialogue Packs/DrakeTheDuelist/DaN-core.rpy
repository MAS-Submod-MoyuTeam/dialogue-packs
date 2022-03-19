# The core event that triggers all other events in the submod.
#
# You must at least have normal affection to attempt this submod.
#
# On first run, Monika will explain the premise of the submod. (Can be skipped later.)
# 
# If Monika has a nightmare, this label will stop you from attempting to
# have Monika dream again for the next 12 hours after the dream concludes.
init 5 python:
    if persistent._dan_should_create_events:
        removeTopicID("DaN_try_to_dream")
        mas_eraseTopic("DaN_try_to_dream")
        removeTopicID("DaN_revisit_dream")
        mas_eraseTopic("DaN_revisit_dream")

    addEvent(
        Event(
           persistent.event_database,
            eventlabel="DaN_try_to_dream",
            category=['梦境和梦魇'],
            prompt="尝试一个梦境?",
            random=True,
            action=EV_ACT_PUSH,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

    addEvent(
        Event(
            persistent.event_database,
            eventlabel="DaN_revisit_dream",
            category=['梦境和梦魇'],
            prompt="重游一个梦境?",
            conditional="persistent._dan_dreams_had",
            action=EV_ACT_PUSH,
            random=True
        )
    )

# The root action of getting a random dream.
#label dan_have_new_random_dream:
label DaN_try_to_dream:
    if persistent._dan_dreams_had:
        m 1esd "喔,有些东西弄错了."
        m "我浏览了游戏根目录来看看我以某种方式做了梦,但是我弄错了什么."
    else:
        m 1esd "好,它开始运作了."
        m "现在我不记得我做过任何梦,以及之前做过的梦的重游功能被锁住了."


    if persistent._dan_apprehensive_start:
        # note: This is a valid way to call apprehension because the only POSSIBLE
        # way for Monika to be apprehensive is if she dreamt a minimum of twice
        # (as you can never draw a nightmare the first time), and so you won't be
        # skppping over any necessary explanations.
        call DaN_dream_despite_apprehension()
    else: 
        if persistent._dan_dreams_and_nightmares_explained:
            m 3esc "我记得我向你解释过这个."
            m "你想让我再解释一遍吗?"
            menu:
                m "你想让我再解释一遍吗?{fast}"
                "是的.":
                    $ persistent._dan_dreams_and_nightmares_explained = False
                "不,谢谢.":
                    m 7hub "好,所以说你还记着."
                    if mas_isMoniLove():
                        m 5ekbfu "我知道你会坚持听我所有的话, [mas_get_player_nickname()]..."
                    elif mas_isMoniEnamored():
                        m 5eubla "谢谢你倾听我的一切, [player]."
                    else:
                        m "那会节省我们一些时间."
        if not persistent._dan_dreams_and_nightmares_explained:
            call DaN_explanation
        m 4wub "你怎么想?  你想要开始吗?"
        menu:
            m "你想要开始吗?{fast}"
            "现在不了.":
                m 1eka "好吧,我会等你准备好的."
                m 3eka "但是之后回来这里好吗?  我 {i}真的{/i} 很期待这个."
            "嗯,来吧!":
                call DaN_perchance_to_dream
    return
# The root action of randomly having a drem Monika has already experienced so far.
label DaN_revisit_dream:
    if persistent._dan_apprehensive_start:
        call DaN_dream_despite_apprehension()
    else: 
        m 1gsb "如果我只做一次，这个做梦的想法就会很无聊了."
        if persistent._dan_asked_to_stay_dreaming:
            m 5rtd "另外,我做过一些梦,你把我提前叫醒了. 我想把这些梦看完."
        m 7esb "你怎么想, [player]?  你要和我一起回顾我之前做过的梦吗?"
        menu:
            m "你要和我一起回顾我之前做过的梦吗?{fast}"
            "好,来吧!":
                if persistent._dan_dreams_had:
                    call DaN_begin_sleep
                
                    #roll for which dream Monika will have
                    $ random_dream = renpy.random.choice(persistent._dan_dreams_had)

                    call DaN_select_dream(random_dream)
                else:
                    m 4hublb "笨蛋[player], 我需要{i}有{/i}一个梦才能去回顾它."#ddy:八嘎八嘎八嘎八嘎八嘎八嘎（试图水到和原来的一样大）
                    m 4rubld "尽管你认为这是你的错,但是我并不这么觉得.  有些东西肯定{i}严重{/i}错误了."
                    m 3rud "当我尝试回忆的时候,看起来有一些作者担心的事情发生了."
                    m "所以他给我留了后路, 就像这些乱七八糟的东西."
                    m 3lub "当代码出了问题的时候就会这样卡住.{w=1.5} 让{i}我{/i}有谈话的空间..."
                    m 2dud "稍等一会.{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}{nw}"
                    $ persistent._dan_all_dreams = [1]
                    $ persistent._dan_dreams_had = []
                    m 2eud "好了,调整完毕."
                    m 2hub "现在这个submod将会回到正轨."
            "现在不了.":
                m 1eka "好吧,我会等到你准备好了."
    return
# regardless of whether dreaming or revisiting an old dream, if Monika is anxious
# due to a past nightmare, she should act the same way.
label DaN_perchance_to_dream:
    if persistent._dan_all_dreams:
        call DaN_begin_sleep
    
        #roll for which dream Monika will have
        $ random_dream = renpy.random.choice(persistent._dan_all_dreams)
        $ persistent._dan_all_dreams.remove(random_dream)
        if (persistent._dan_dreams_had):
            $ persistent._dan_dreams_had.append(random_dream)
        else:
            $ persistent._dan_dreams_had = [random_dream]

        call DaN_select_dream(random_dream)

    # read as soon as Monika's last dream resolves
    if not persistent._dan_all_dreams:
        call DaN_all_dreams_finished
    return
