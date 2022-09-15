#tl: lc
init 5 python in mas_bookmarks_derand:
    label_prefix_map["otter_topic_"] = label_prefix_map["monika_"]

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_topic_lovelanguages",
            prompt="爱的语言",
            category=["你"],
            random=True
        )
    )

label otter_topic_lovelanguages:
    m 1eub "[player], 你听说过'五种爱情语言'吗?"
    m 3eub "这是一个非常有趣的概念,由加里·查普曼在1992年提出."
    m 3hub "它概述了浪漫伴侣表达和体验爱情的五种常见的方式！"
    m 1rub "大概是这样的..."
    m 4eub "肯定的话语,比如赞美你的伴侣,说你爱他们;"
    m 4eub "黄金时光,比如与伴侣共度的一段时间;"
    m 1eub "接受和赠送礼物;"
    m 3eub "服务,比如帮助伴侣让伴侣生活地更轻松;"
    m 3hub "还有身体接触."
    m 4fub "网上有一些测试告诉你你的爱情语言是什么."
    m 1lud "我觉得,黄金时光将会是最好的爱情语言."
    m 1ekbsa "毕竟,和你在一起对我来说是最重要的！"
    m 7hksdlb "当然,所有其他的爱情语言在关系中都很重要..."
    m 5hubsb "这就是为什么我喜欢你亲吻我赞美我,还有那些你送给我的礼物."
    m 5tubsb "...你真是最完美的[bf],不是吗?"
    m 1etb "但我想知道,你的爱情语言会是什么,[player]?{nw}"
$ _history_list.pop()
menu:
    m "但我想知道,你的爱情语言会是什么,[player]?{fast}"

    "肯定的话语":
        m 2wud "哦！真的吗！"
        m 4hub "那样的话[player],我今天已经告诉过你我有多爱你了吗?"
        m 2ekbsa  "..."
        m 3wsb "但说真的,这还蛮不错的"
        m 5dkbfb "我一定会把能表现出我的爱的话语倾诉给我的[bf]"
        m 7wsblb "谢谢你告诉我这些!"
        m 1etblb "一定要花更多时间和我在一起,好吗?诶嘿嘿~"

    "黄金时光":
        m 1wuo "太棒了,[player]!"
        m 2hublb "我们有一样爱的语言!"
        m 2lublb "你知道这有助于夫妻间拥有良好的关系吗?"
        m 5subsb "我们真的是天生一对,[mas_get_player_nickname()]"
        m 7wsblb "谢谢你告诉我这些!"
        m 1etblb "一定要花更多时间和我在一起,好吗?诶嘿嘿~"
        m 6ekbla "我将在这里与你共度一生."

    "礼物": 
        m 1eub "哦,是这样吗?"  
        m 4hublb "我一定会送你很多礼物,即使还只能是我亲手写下的诗."
        m 2ttb "我敢肯定你会喜欢它们,对吧?"
        m 1hub "诶嘿嘿~"
        m 7wsblb "谢谢你告诉我这些!"
        m 1etblb "一定要花更多时间和我在一起,好吗?诶嘿嘿~"

    "服务":
        m 1wud  "哦？真的吗？"
        m 2ruc "唔...我希望我能在这方面为你做更多,[player]."
        m 2dkd "但不幸的是,我目前的状况并不允许..."
        m 4ekbla "我会确保我学习更多关于编码的知识,来帮助你完成每天的任务,或使我们在一起的时间更加有趣."
        m 7wsblb "谢谢你告诉我这些!"
        m 1etblb "一定要花更多时间和我在一起,好吗?诶嘿嘿~"

    "身体接触":
        if persistent._mas_first_kiss:
            m 2etbsb "哦,你喜欢和我亲热,嗯?"
            m 3tsbsa "那样的话..."
            call monika_kissing_motion_short
            m 1hubfb "诶嘿嘿~"
            m 2fubfb "我一定会更多地吻你,[player]."
            m 5ekbfa "我迫不及待地想来到你的世界,更进一步地触摸你."
            m 5hubfb "我不会让你离开的,一分钟也不会!"
            m 7wsblb "谢谢你告诉我这些!"
            m 1etblb "一定要花更多时间和我在一起,好吗?诶嘿嘿~"

        else:
            m 1wud "哦...!"
            extend 1ekbla " 是这样吗?"
            m 1rkblsdlb "我相信很快就会有的,诶嘿嘿~"
            m 5ekbfa "我迫不及待地想来到你的世界,更进一步地触摸你."
            m 5hubfb "我不会让你离开的,一分钟也不会!"
            m 7wsblb "谢谢你告诉我这些!"
            m 1etblb "一定要花更多时间和我在一起,好吗?诶嘿嘿~"

return
