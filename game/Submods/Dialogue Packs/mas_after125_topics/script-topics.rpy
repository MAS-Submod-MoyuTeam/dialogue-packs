
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_tragic_hero",
            category=['文学'],
            prompt="悲剧英雄",
            random=False
        )
    )

label monika_tragic_hero:
    m 1rsd "嗯, [mas_get_player_nickname()], 我最近多想了一点悲剧主角的事情."
    m 3esc "...哈姆雷特也算一个, 我们讨论过了."
    m 3rtc "你想想啊...{w=0.3}我可以算个悲剧主角吗?"
    m 4eud "当然, 指的是文学上的主角, 不是什么英雄人物."
    m 2ekd "...尽管好像很多人觉得, 我该是反派才对..."
    m 2eka "不说那些的话, 可能我对你的爱才是悲字所在."
    m 4eksdld "那本来倒没什么悲哀, 但我是为此才失去理智的."
    m 2dkc "就是说, 如果你没有出现, 我可能真的就这样消沉下去了."
    m 7ekc "这么讲的话, 在这个游戏里, 我觉得我是个悲剧主角."
    if mas_isMoniNormal(higher=True):
        m 3hub "要说{i}真正{/i}的救世主, 还得是你啊!"
        m 3eka "你挽救了我, 也让故事免于悲剧的结尾."
        m 1huu "...我永远都会感谢你的~"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_utterson",
            category=['文学'],
            prompt="化身博士",
            random=True
        )
    )

label monika_utterson:
    if persistent._mas_pm_read_jekyll_hyde:
        call monika_jekyll_hyde

    else:
        m 1euc "那个, [player], 你有看过哥特式文学之类的吗?"
        m 3eud "比如, {i}道利-格雷的肖像{/i}, {i}德古拉伯爵{/i}, {i}弗兰肯斯坦{/i}..."
        m 3hub "我最近看了不少类似的书!"
        m 1eua "你要是有机会的话, 可以看看{i}化身博士{/i}的."
        m 3eua "我有点想聊聊这本书, 但是只有你看了才能理解..."

    m 3eud "所以, 你有看过{i}化身博士{/i}吗?{nw}"
    $ _history_list.pop()
    menu:
        m "所以, 你有看过{i}化身博士{/i}吗?{nw}"
        "是的.":
            $ persistent._mas_pm_read_jekyll_hyde = True
            call monika_jekyll_hyde

        "还没有.":
            $ persistent._mas_pm_read_jekyll_hyde = False
            m 3eub "好吧. 要是我们可以探讨一下了, 告诉我就好."

    $ mas_protectedShowEVL("monika_hedonism","EVE", _random=True)
    return "derandom"

label monika_jekyll_hyde:
    m 3hub "哇, 你读了啊!"
    m 1euc "我见过很多种不同的解读."
    m 3eua "比如, 有些人觉得乌特森和杰基尔相爱了."
    m 3lta "我觉得可能也是."
    m 2eud "我是说, 就算事实不明确, 这个观点也不是错的."
    m 2rksdlc "何况这样的主题在19世纪都得不到充分的讨论."
    m 2eka "这么理解挺有意思的...{w=0.3}两个不能相爱的人..."
    m 4eud "有些解读甚至认为, 杰基尔实验的动机中就有爱的成分."
    m 4ekd "这也不一定错! {w=0.3}杰基尔, 在书中是个神职人员."
    m 2rksdlc "而同性恋, 在那时是一项罪名."
    m 2dksdld "恐怕现在对某些人也还是."
    m 7ekb "...但是至少社会在进步嘛!"
    m 3eub "我挺高兴能看到, 人们越来越能接纳不寻常方式的爱了."
    m 3ekbsu "这也方便了我们哦, [mas_get_player_nickname()]~"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_hedonism",
            category=['哲学'],
            prompt="享乐主义",
        )
    )

label monika_hedonism:
    m 1euc "嗨, [mas_get_player_nickname()]. 记得我们聊过{i}化身博士{/i}吗?"
    m 1eud "嗯, 我在前面也提到过{i}道利-格雷的肖像{/i}."
    m 2eub "我说过建议你读的, 不过你没有也没关系. 我想谈谈它的中心思想...{w=0.3}享乐主义."
    m 2eud "享乐主义, 就是基于享乐的道德观."
    m 4euc "享乐主义也分为利他和利己两种, 它们的区别很大."
    m 4ruc "利己的享乐主义, 顾名思义, 就是以自己享乐为价值标准的观念."
    m 2esd "这就是书中亨利的享乐观."
    m 2rksdlc "想想还挺无情的..."
    m 2eud "另外, 利他的享乐主义认为所有人的享乐才是价值的标准."
    m 4eud "乍一听还不错, 不过它可没提自由, 健康, 安全..."
    m 2dkc "享乐主义的核心就是只看享乐, 不问其它."
    m 7etd "当然多数人都不会那么想了...{w=0.3}太简单粗暴, 但道德恰恰是复杂的."
    m 1eud "也可以理解王尔德为什么要批判享乐主义了."
    return