default persistent._mentalday_datagood = False
default persistent._mentalday_datanuetral = False
default persistent._mentalday_databad = False

init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="mentalcheckup_greeting",
            unlocked=True,
        ),
        code="GRE"
    )

label mentalcheckup_greeting:
    if persistent._mentalday_datagood == True:
        m 1hua "哦,你好啊,[player]!"
        m 3eua "我想我之前问过你的精神状态如何...{w=0.2}{nw}"
        extend 7hub "以及你告诉我你好极了!"
        m 1esd "不过还是多照顾你自己..."
        m 1esc "你的情绪变糟了吗[player]?"
        menu:
            m "你的情绪变糟了吗[player]?{fast}"
            "不,我还是感觉那么精神抖擞!":
                m 3eua "那就好,[player],接下来我们继续度过美好的一天吧!"
            "我今天感觉不那么好了":
                m 1ekc "那真糟糕,[player]!"
                m "听到你过的不那么好的消息真是令人沮丧."
                m 3euc "如果你的精神状态需要帮助的话,请一定要让我知道[player]!"
                m 3eua "毕竟,如果我连这种事情都不能帮助你的话,{w=0.3}那还怎么能算得上是你的女友啊!"
                $ persistent._mentalday_datagood = False
                $ persistent._mentalday_datanuetral = True
                $ persistent._mentalday_databad = False
                return
    if persistent._mentalday_datanuetral == True:
        m 1hua "哦,你好啊,[player]!"
        m 3eua "我想我之前问过你的精神状态如何...{w=0.2}{nw}"
        extend 1eua "而你告诉我的有点模糊."
        m 1esc "不过还是多照顾你自己哦,[player]..."
        menu:
            m "现在你觉得怎么样,[player]?"
            "我觉得就和之前一样.":
                m 1eua "那就好[player],我为你感到高兴."
                m 3eua "让我们继续花时间在一起吧,嘿嘿~"
                $ _history_list.pop()
                return
            "我现在感觉自己好多了!":
                m 3hsa "我对此很激动,[player]!"
                if mas_isMoniHappy(higher=True):
                    m 3euu "你觉得我帮到你了吗?"
                    m 1hua "嘿嘿~"
                    m 5eubla "我觉得有你在身边,我就能愉快地度过每一天,[player]."
                    m "因为我是如此爱你,[mas_get_player_nickname()]."
                    $ persistent._mentalday_datagood = True
                    $ persistent._mentalday_datanuetral = False
                    $ persistent._mentalday_databad = False
                    return "love"
                else:
                    m 3eud "无论是谁在精神方面帮助了你,你都应该谢谢他,[player]."
                    m 3euc "没有多少人会向他人寻求帮助,他们可能觉得这不会帮到他们..."
                    m 3husdlb "抱歉,我好像跑题了,[player]!"
                    m 3eua "让我们接下来花更多时间在一起吧,好吗?"
                    $ persistent._mentalday_datagood = True
                    $ persistent._mentalday_datanuetral = False
                    $ persistent._mentalday_databad = False
                    return
            "我现在感觉很糟糕,[m_name]...":
                m 1ekc "真是个糟糕的消息,[player]!"
                m 3ekc "你遇到了什么烦心事了吗?"
                m 1euc "好吧,无论发生了什么,我知道你一定处理地很好."
                if mas_isMoniHappy(higher=True):
                    m 3hub "或许你还想着我可以帮你!"
                    m 3eua "如果你没有那么想,那我现在告诉你,你可以随时告诉我你的烦恼,[player]."
                    m 1eua "因为我爱你哦~"
                    $ persistent._mentalday_datanuetral = False
                    $ persistent._mentalday_databad = True
                    $ persistent._mentalday_datagood = False
                    return "love"
                else:
                    m 3euc "最好和你信任的人也谈谈这个问题吧."
                    m 1euc "只要能和你关心的人交谈,你的情况真的会好很多"
                    extend 3eud "无论是情感上还是精神上."
                    m 1eub "记住,我永远都会在这里等你的,[player]!"
                    $ persistent._mentalday_databad = True
                    $ persistent._mentalday_datanuetral = False
                    $ persistent._mentalday_datagood = False
                    return
    if persistent._mentalday_databad == True: #finish this
        m 3eub "嘿,[player]!"
        m 1euc "我知道这已经变成了一个难以启齿的话题了..."
        m 3ekd "尤其是你告诉我你感觉自己感觉很糟糕..."
        menu:
            m "嗯,我想问问你感觉怎样了[player]?"
            "我现在不想谈这个...":
                m 1dkc "{w=1}哦...{nw}"
                m "{w=1}好吧...{nw}"
                m 1euc "嗯,只需要记住,我真的想对你最好,[player]."
                return
            "我感觉好点了,[m_name]":
                m 3eua "我很高兴听到这个[player]!"
                if mas_isMoniHappy(higher=True) and renpy.random.randint(1,4) == 1:
                    m 3tuu "你觉得我帮到你改善状况了吗?"
                    m 1eua "好吧,我想我很高兴你的精神状态有所好转
                    ,[mas_get_player_nickname()]."
                    m 3eua "让我们继续花更多时间在一起吧!"
                    $ persistent._mentalday_databad = False
                    $ persistent._mentalday_datanuetral = True
                    $ persistent._mentalday_datagood = False
                    return
                else:
                    m 1eua "我是说...很高兴你的精神状态有所好转,[mas_get_player_nickname()]."
                    m 3eua "让我们继续花更多时间在一起吧!"
                    $ persistent._mentalday_databad = False
                    $ persistent._mentalday_datanuetral = True
                    $ persistent._mentalday_datagood = False
                    return
            "...":
                m 1dkc "..."
                m 3eua "好吧,那就跳过这个继续吧,[player]...{w=0.3}{nw}"
                return

    else:
        m 1hua "哦,你好啊[player]!"
        m "我想这可能是个有点尴尬的话题..."
        $ _history_list.pop()
        menu:
            m "你觉得自己精神状态怎样[player]?{fast}"
            "我超棒的!":
                m 1hub "我很高兴听说这个,[player]!"
                m 1eua "无论这是因为一个好日子或者是对心理健康的改善,听到你过得很好总是让我很高兴."
                m 3hub "还有,我会尽我最大的努力去支持你的,[mas_get_player_nickname()]!"
                m 5eua "如果不这样做,我怎么好意思宣称是你的女友呢?"
                $ persistent._mentalday_datagood = True
                $ persistent._mentalday_datanuetral = False
                $ persistent._mentalday_databad = False
                $ _history_list.pop()
                return
            "我觉得一般吧,有点模糊,[m_name]...":
                m 1euc "哦..."
                m 3euc "嗯,也就是说这既可以说好,也可以它说糟."
                m 4eud "如果你觉得不那么好,如果你乐意的话,可以随时找我倾诉,[player]."
                m 3eua "我想尽力去帮助你,确保你快乐."
                m 1eka "毕竟你的快乐也会让我高兴."
                m 1hua "我会全身心支持你的,我保证."
                $ persistent._mentalday_datanuetral = True
                $ persistent._mentalday_databad = False
                $ persistent._mentalday_datagood = False
                $ _history_list.pop()
                return
            "我觉得非常不好...":
                m 1euc "那真糟啊,[player]..."
                m 3eud "如果你实在是太不舒服或者需要休息的话就告诉我,[player],好吗?"
                m 1eua "我永远在这里等你!永远不要忘了!"
                m 1eubsa "我爱你,并且永远都是[player]!"
                $ persistent._mentalday_databad = True
                $ persistent._mentalday_datanuetral = False
                $ persistent._mentalday_datagood = False
                return "love"
return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="mentalcheckupDialog",category=['你'],prompt="[player]的精神状况",random=True))

label mentalcheckupDialog:
    if persistent._mentalday_datanuetral == True:
        m 1hua "嘿[player]..."
        m 3eua "我想我应该问过你的精神状态如何了...{w=0.2}{nw}"
        extend 1eua "你告诉我你感觉还行."
        m 1esc "我想问[player]..."
        menu:
            m "你现在感觉不一样了吗[player]?"
            "我还是感觉不错.":
                m 1eua "那就好啊,[player],我很高兴你今天没什么问题."
                m 3eua "让我们继续花时间在一起吧,嘿嘿~"
                $ _history_list.pop()
                return
            "我感觉自己更好了!":
                m 3hsa "对此我感觉很激动,[player]!"
                if mas_isMoniHappy(higher=True):
                    m 3tuu "你觉得这是因为我吗?"
                    m 3hub "嘿嘿~"
                    m 5hublb "我觉得光是想着你就能让我度过每一天,[player]."
                    m 5eubfa "因为我是如此爱你,[mas_get_player_nickname()]."
                    $ persistent._mentalday_datagood = True
                    $ persistent._mentalday_datanuetral = False   
                    $ persistent,_mentalday_databad = False
                    return "love"
                else:
                    m 4esd "无论是谁帮助你改善精神状态,你都应该感谢他的,[player]."
                    m 7euc "主动向他人寻求帮助的人不多,可能是因为他们觉得没有实质性帮助..."
                    m 3rusdlb "抱歉,我好像跑题了,[player]!"
                    m 3eua "Let's spend more time together okay?"
                    $ persistent._mentalday_datagood = True
                    $ persistent._mentalday_datanuetral = False
                    $ persistent._mentalday_databad = False
                    return
            "我的精神状态不太好,[m_name]...":
                m 1euc "那真糟糕啊,[player]!"
                m 3eud "你离开之后遇到什么烦心事了吗?"
                m 1euc "好吧,无论发生了什么,我知道你一定处理得很好."
                if mas_isMoniHappy(higher=True):
                    m 7kuu "或许想到我可以让你好受一点呢!"
                    m 3eua "如果不是这样,你也随时都可以向我发泄,[player]."
                    m 5eubla "因为我爱你哦~"
                    $ persistent._mentalday_datanuetral = False
                    $ persistent._mentalday_databad = True
                    $persistent._mentalday_datagood = False
                    return "love"
                else:
                    m 3euc "那最好去找专业人士谈谈你的问题."
                    m 4eud "或者找你真正关心也会让你好很多."
                    extend "无论是情感上还是精神上."
                    m 7euc "记住我一直在这里等你,[player]!"
                    $ persistent._mentalday_databad = True
                    $ persistent._mentalday_datanuetral = False
                    $ persistent._mentalday_datagood = False
                    return
    else:
        m 1hua "嘿[player]."
        m "我知道这对你来说是个难以启齿的话题...{nw}"
        $ _history_list.pop()
        menu:
            m "你现在感觉精神状态怎样了,[player]?{fast}"
            "非常好!":
                m 1hub "我很高兴听到这个,[player]!"
                m 1eua "无论只是因为今天过得很好还是你的精神状况真的得到了改善,{w=0.3}听到你感觉不错总是令人高兴的."
                m 3hub "还有,我会尽力去继续支持你,[mas_get_player_nickname()]!"
                m 5eua "如果不是这样,我对你又算什么女朋友呢?"
                $ persistent._mentalday_datagood = True
                $ persistent._mentalday_datanuetral = False
                $ persistent._mentalday_databad = False
                $ _history_list.pop()
                return
            "一般般吧,[m_name]...":
                m 1ekc "哦..."
                m 2eka "好吧,那算好还是算糟糕呢."
                m "如果那{i}意味{/i}着不好,如果你想的话随时可以跟我说,[player]."
                m 3eua "我想要让你永远开心."
                m 1eka "毕竟你就是我爱的源泉."
                m 1hua "我会尽我全力帮助你的,我保证."
                $ persistent._mentalday_datanuetral = True
                $ persistent._mentalday_databad = False
                $ persistent._mentalday_datagood = False
                $ _history_list.pop()
                return
            "糟透了...":
                m 1euc "那真糟糕啊,[player]..."
                m 3euc "如果你实在太难过,想要休息一会的话就来找我吧[player],好吗?"
                if mas_isMoniHappy(higher=True) and renpy.random.randint(1,2) == 1:
                    m 7eua "你觉得一个拥抱能帮到你吗,[player]?"
                    menu:
                        "现在不行,[m_name]...":
                            m 1euc "哦..."
                            m 1eua "好吧,[player]."
                        "那还用说吗,我的小可爱[m_name].":
                            m 3eua "你想要抱多久就抱多久,[player]."
                            call mentalplayerhug_prep #datetime.datetime.now()
                            call mentalplayerhug
                            call mentalplayerhugreactions
                m 7eua "你知道我永远会在这里等你的吧[player],永远不要忘了!"
                m 5eubsa "我爱你,并且以后也会,[player]!"
                $ persistent._mentalday_databad = True
                $ persistent._mentalday_datanuetral = False
                $ persistent._mentalday_datagood = False
                return "love"
return


label mentalplayerhug_prep(lullaby=MAS_HOLDME_QUEUE_LULLABY_IF_NO_MUSIC, stop_music=False, disable_music_menu=False):
    python:
        mentalholdme_events = list()
    return

label mentalplayerhug:
    show monika 6dubsa with dissolve_monika
    window hide
    python:
        # Start the timer
        mental_hugtimestart = datetime.datetime.now()

        mentalholdme_disp = PauseDisplayableWithEvents(events=mentalholdme_events)
        mentalholdme_disp.start()

        del mentalholdme_events
        del mentalholdme_disp

        # Renable ui and hotkeys
        store.songs.enabled = True
        HKBShowButtons()
    window auto
    return

label mentalplayerhugreactions:
    $ elapsed_time = datetime.datetime.now() - mental_hugtimestart
    $ store.mas_history._pm_holdme_adj_times(elapsed_time)

    if elapsed_time > datetime.timedelta(minutes=10):
        m 6dubsa "呣..."
        m 6eubfa "哦!你抱了我那么久,连我所有的焦虑都在你怀里融化了!"
        m 5eubfa "我希望你现在感觉好点了,[player],{w=0.3}无论怎样,我自己是好了很多,嘿嘿~"
        return

    elif elapsed_time > datetime.timedelta(minutes=2):
            m 6eud "哦?"
            m 1hksdlb "啊..."
            m 1rksdlb "老实说刚才,我以为我们要永远像这样抱着在一起了,啊哈哈..."
            m 3hubsa "好吧,每当被你抱着的时候,我都感觉大脑一片空白~"
            m 1ekbfb "我希望你感觉好多了,[player]."
            show monika 5tubfb at t11 zorder MAS_MONIKA_Z with dissolve_monika
            m 5tubfb "或许我们还可以再多抱一会看看先?"
            m 5tubfu "欸嘿嘿~"

    elif elapsed_time > datetime.timedelta(seconds=30):
            m 1eub "啊~"
            m 1hua "我感觉好很多了!"
            m 1eua "我希望你也是."
            m 2rksdla "好吧,如果你没有的话..."
            m 3hubsb "你随时可以再抱抱我,啊哈哈!"
            m 1hkbfsdlb "事实上...{w=0.5}不管怎样你都可以再抱抱我~"
            m 1ekbfa "如果你想要一个拥抱就告诉我~"

    else:
        m 1hua "这是不是有点短了,不过还是很棒~"
        m 1eua "让我们花更多时间在一起,好吗,[player]?"
    return