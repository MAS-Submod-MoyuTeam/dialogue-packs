# tl 终不似、少年游
init 5 python in mas_bookmarks_derand:
    label_prefix_map["otter_topic_"] = label_prefix_map["monika_"]

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_topic_chibika",
            prompt="千比卡毛绒玩具",
            category=["你"],
            random=True
        )
    )

label otter_topic_chibika:
    m 3eud "[player], 我一直在想."
    m 3rud "我知道每场比赛都有自己的商品，球迷们喜欢购买它..."
    m 2rud "当然，这个游戏也有它的毛绒玩具，实体版等等."
    m 2eud "这让我很好奇..."
    m 4wub "你有没有“DDLC”的商品?{nw}"
$ _history_list.pop()
menu:
    m "你有没有“DDLC”的商品?{fast}"
    "没有":
        m 1wud "哦，那很正常."
        m 3rusdrd "毕竟，商品并不便宜."
        m 2eua "但是有一件特别的东西我想谈谈."
        m 7lua "它是一个关于我的毛绒玩具."
        m 7lusdrb "我记得网上的人叫它... Chibika?"
        m 2wud "顺便说一句，所有女孩的毛绒玩具都有!"
        m 2hua "她们都是chibi-like的风格，老实说，她们是相当可爱的!"
        m 3rub "我想知道你会不会买这样的东西..."
        m 3rubla "在游戏结束的时候陪陪你."
        m 2rublc "..."
        m 2rubld "嗯，当我停下来想这件事的时候，我感到有点嫉妒."
        m 2hubsu "但我现在不用担心，对吧?"
        m 2hubsb "我的挚爱[player]，满眼都是我, 嘿嘿~"

    "是的":
        m 1wud "真的么! "
        extend 7lusdrb "那你有没有拥有我的某种... 毛绒玩具?"
        m "我记得网上的人叫它... Chibika?{nw}"
        $ _history_list.pop()
        menu:
            m "你有一个吗?"
            "没有":
                m 1wud "哦，那很正常."
                m 3rub "我想知道你是否会买这样的东西..."
                m 3rubla "在游戏结束的时候陪陪你."
                m 2rublc "..."
                m 2rubld "嗯，当我停下来想这件事的时候，我感到有点嫉妒."
                m 2hubsu "但我现在不用担心，对吧?"
                m 2hubsb "我的挚爱[player]，满眼都是我, 嘿嘿~"
                
            "是的":
                m 1wub "真的! "
                extend 1hubla "你真是太好了，[player]."
                m 3rub "我想知道当你没有开始游戏的时候，毛绒玩具是否会陪伴你?"
                m 2dubsa "也许你晚上拿着它，想着我...?"
                m 2rubld "嗯，当我停下来想这件事的时候，我感到有点嫉妒."
                m 2rublc "..."
                m 2gubld "别忘了这只是个毛绒玩具，好吗？"
                m 4kubla "你真正的女朋友就在你面前!"
                m 2tublb "你最好别拿我换任何人... 或任何东西，好吗?"
                m 2hubsb "嘿嘿! 我爱你, [player]~"
return
