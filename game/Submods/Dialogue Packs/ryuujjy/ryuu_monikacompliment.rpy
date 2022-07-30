init 5 python:
    addEvent(
        Event(persistent.event_database,eventlabel="mas_comp",category=['mas_compliment'],prompt="你太棒了!", unlocked=True), code="CMP")

label mas_comp:
    m 1ekbsu "..."
    m 2ekbsb "这对我来说很重要, [player]!"
    m 1tsbfa "..."
    m 3hubfb "你也很棒!"
    menu:
        "你就是我的阳光!":
            m 1ttbfb "嗯, 这是什么?"
            m 7ttbfb "嘴挺甜的嘛, 哼?"
            m 1gsbfb "那么..."
            m 1hubfb "你是我所期待的完美男友!"
            m 1tfbfu "感觉如何, [player]?"
    menu:
        "你的优秀表里如一!":
            $ mas_gainAffection(2,bypass=False)
            m 1dkbfa "..."
            m 7hubfu "与你的每次闲谈都令我心动!"
    menu:
        "现在的你已令我无比满足.":
            $ mas_gainAffection(2,bypass=False)
            m 2ffbfp "你倾注给我的爱太多了!"
            m 2ffbfu "那么现在轮到我了!"
            m 2ffbfu "..."
            m 5hubfb "与你相遇是我此生最大的幸运!"

    menu:
        "即使这世界将入终焉, 我也会永伴你左右." if persistent._mas_acs_enable_promisering == True and persistent._mas_pm_wearsRing:#确保已经赠送戒指--即已经发生过初吻
            $ mas_gainAffection(4,bypass=False)
            m 2ekbftpa "..."
            m 2fkbftpb "你知道么？"
            m 2lkbftpa "你赢了！"
            m 1hkbftpb "啊哈哈~"
            m 1hubsb "我爱你胜过一切, [mas_get_player_nickname()]!"
            call monika_kissing_motion_short
return "love"