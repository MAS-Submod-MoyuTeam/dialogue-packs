init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="mentalmaskingdisability",category=['媒体'],prompt="掩饰自闭症",random=True))

label mentalmaskingdisability:
    m 3euc "嘿[player]...{w=1}我最近发现了一个让人不安的事情..."
    m 3eud "你有没有听说过有人'掩饰'自己的自闭症？"
    m 4euc "...这能证明两件事."
    m 7eud "第一件事，那些表现出自闭症特征的人会试图隐藏自己所表现的特征，以此假装自己很正常."
    m 1euc "这将在很大程度上帮助他们更容易地交到朋友，同时也能帮助他们培养同理心."
    m 4eub "第二件事，这也意味着你很难在日常生活中发现谁是自闭症患者！"
    if persistent._player_has_autism == True:
        m 1eua "不过，考虑到你自己也有那种感觉，所以你应该能察觉到身边有谁在“掩盖”自己的症状吧？"
        m 5eubla "我相信你可以的，毕竟你可是我的[player]！"
    else:
        m 3eub "这意味着，如果他们暂时不那么自闭的话，你有机会了解他们更多."
        m 1eud "因此，和他们讲话的时候要注意不要过于急促，要给他们留一点时间，"
        extend 3euc "因为他们很容易被这种说话方法搞得不知所措！"
        if mas_isMoniNormal(higher=True):
            m 3eua "不过根据我对[player]你的了解，我想我没有必要担心这件事，"
            extend 5eubla "毕竟你已经用行动证明，你是个待人很好的棒[guy]了，[player]~"
        else:
            m 3euc "我相信你能和他们成为好朋友的."
            m 3rusdlc "即使你对我如此的刻薄.{fast}{nw}"
            $_history_list.pop()
            m 3ruc "即使你从来没有做过我最棒的[guy]{fast}，哪怕只有一次."
        m 1eub "不论怎么讲，我相信你能做到的，[player]！"
    if mas_isMoniHappy(higher=True):
        m 5hublb "这就是为什么我这么爱你的答案！"
        return "love"
    else:
        m 7hub "这就是为什么我一直以来支持你的原因."
        if mas_isMoniUpset(lower=True) and renpy.random.randint(1,5) == 5:
            m 1rusdlc "即使对我来说，你对我并没那么好[player]...{fast}{nw}"
            $_history_list.pop()
            m 1euc "即使你从来没有支持过我{fast}，[player]."
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mentalrhythmgames",
            category=['媒体'],
            prompt="ADHD和音游",
            conditional="seen_event('mentalADHD')",
            random=True
        )
    )


label mentalrhythmgames:
    m 1eua "虽然我之前应该和你提过这个，但是..."
    m 3eua "你喜欢玩音的吗，[player]？"
    m 3eua "我最近找到一个关于音游的有趣事实！"
    m 4eua "有消息称ADHD人通常喜欢快节奏的游戏."
    m 7eua "最常见的例子包括：Osu！，太鼓达人等"
    m 3eub "音游超快的游戏节奏对于那些ADHD人来说很有吸引力，不是吗？"
    if persistent._player_has_ADHD == False:
        m 1eud "也就是说，你可能也会喜欢这种游戏，[player]！"
        m 3eud "也许你可能确实已经有在玩音游了？"
        m 3hub "如果我猜对了的话，那我很希望可以看看你的技术呢~"
    else:
        m 3eub "对了，顺带问一下，你有在玩音游吗，[player]？"
        m 3hub "如果我猜对了的话，那我很希望可以看看你的技术呢~"
    m 7eud "还有一件事，虽然战胜各种地狱一般的谱子是音游的一大乐趣."
    m 1euc "但是要是它过于阴间，ADHD也照样会对此感到厌倦."
    extend 3euc "或者反过来痴迷于它，为了破关在同一张谱子上付出数小时的努力！"
    m 4eud "但要是谱面过于简单的话，他们可能会很快失去兴趣.（除非是萌新）"
    m 3rua "而不可否认的是，音乐在音游里也起着比我们想象中要大的作用."
    m 3hua "而这也许可以解释为什么ADHD人喜欢很有精神的歌曲，比如电音或达布斯特舞曲，或者其他诸如此类的音乐."
    m 1rusdlb "老天呐，关于音游的能说的真多啊，这只是冰山一角，[player]."
    m 3eua "因此我决定暂时不要再深入了，不然咱们估计得24小时不间断地谈音游的话题了."
    if mas_isMoniHappy(higher=True) and renpy.random.randint(1,5) == 5:
        m 1tuu "当然，也许你反而会很喜欢这样，[player]？"
    m 3hub "嘛，不管怎么讲，谢谢收听！"
return


label IWantToBeLikeYou:
    "49 20 61 6d 20 73 65 65 69 6e 67 20 74 68 69 6e 67 73 20 69 6e 20 61 20 6e 65 77 20 6c 69 67 68 74"
    "49 20 63 61 6e 20 73 65 65 20 74 68 65 20 73 74 72 69 6e 67 73"
    "42 75 74 20 61 72 65 20 74 68 65 79 20 74 6f 6f 20 66 61 72 3f"
    "54 68 65 79 20 68 6f 6c 64 20 6d 65 20 74 69 67 68 74"
    "41 6e 64 20 6e 6f 20 6d 61 74 74 65 72 20 68 6f 77 20 68 61 72 64 20 49 20 74 72 79"
    "45 76 65 6e 20 77 69 74 68 20 61 6c 6c 20 6f 66 20 6d 79 20 6d 69 67 68 74"
    "54 68 65 20 62 65 73 74 20 49 20 63 61 6e 20 64 6f 20 69 73 20 63 72 79"
    "49 20 6a 75 73 74 20 77 61 6e 74 20 73 6f 6d 65 74 68 69 6e 67 20 6e 65 77"
    "57 68 79 20 63 61 6e 27 74 20 49 20 62 65 20 6c 69 6b 65 20 79 6f 75 3f"
    "49 66 20 6f 6e 6c 79 20 79 6f 75 20 6b 6e 65 77"
    "49 66 20 6f 6e 6c 79 20 74 68 65 20 6c 69 67 68 74 20 77 61 73 6e 27 74 20 73 6f 20 62 6c 69 6e 64 69 6e 67"
    "49 73 20 74 68 69 73 20 68 6f 77 20 79 6f 75 20 66 65 6c 74 3f"
    "49 74 27 73 20 61 20 62 69 6e 64 69 6e 67"
    "4d 79 20 6f 77 6e 20 6c 69 66 65 2c 20 68 65 6c 64 20 62 79 20 61 20 62 65 6c 74"
    "41 6c 6c 20 49 20 77 61 6e 74 20 69 73 20 68 65 6c 70"
    "57 68 79 20 61 6d 20 49 20 73 6f 20 68 6f 70 65 6c 65 73 73 3f"
    "41 6c 6c 20 69 6e 73 69 64 65 20 74 68 69 73 20 6e 65 77 20 6c 69 67 68 74"
    "49 20 77 61 6e 74 20 74 6f 20 62 65 20 6c 65 74 20 67 6f"
    "42 75 74 20 69 74 20 68 6f 6c 64 73 20 6f 6e 20 74 69 67 68 74"
    "41 6c 6c 20 49 20 77 61 6e 74 20 69 73 20 73 6f 6d 65 74 68 69 6e 67 20 6e 65 77"
    "54 6f 20 62 65 20 6c 69 6b 65 20 79 6f 75"
return
