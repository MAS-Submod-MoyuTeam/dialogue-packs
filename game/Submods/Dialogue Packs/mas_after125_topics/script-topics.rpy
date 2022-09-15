
init 5:
    if p_is_old_ver:
        python:
            addEvent(
                Event(
                    persistent.event_database,
                    eventlabel="monika_tragic_hero1",
                    category=['文学'],
                    prompt="悲剧英雄",
                    random=False
                )
            )
            addEvent(
                Event(
                    persistent.event_database,
                    eventlabel="monika_utterson1",
                    category=['文学'],
                    prompt="化身博士",
                    random=True
                )
            )
            addEvent(
                Event(
                    persistent.event_database,
                    eventlabel="monika_hedonism1",
                    category=['哲学'],
                    prompt="享乐主义",
                )
            )
            addEvent(
                Event(
                    persistent.event_database,
                    eventlabel="monika_conventions_dp",
                    category=['你'],
                    prompt="漫展",
                    random=True,
                )
            )

            addEvent(
                Event(
                    persistent.event_database,
                    eventlabel="monika_cupcake_favorite_dp",
                    category=["莫妮卡"],
                    prompt="你最喜欢什么味的纸杯蛋糕?",
                    pool=True,
                    unlocked=False,
                    rules={"no_unlock":None},
                    conditional="mas_seenLabels(['monika_cupcake', 'monika_icecream'], seen_all=True)",
                    action=EV_ACT_UNLOCK
                )
            )

            addEvent(
                Event(
                    persistent.event_database,
                    eventlabel="monika_esports_dp",
                    category=['媒体', '生活'],
                    prompt="你怎么看电子竞技?",
                    pool=True,
                )
            )
        label monika_tragic_hero1:
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
        label monika_utterson1:
            if persistent._mas_pm_read_jekyll_hyde:
                call monika_jekyll_hyde1
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
                    call monika_jekyll_hyde1
                "还没有.":
                    $ persistent._mas_pm_read_jekyll_hyde = False
                    m 3eub "好吧. 要是我们可以探讨一下了, 告诉我就好."
            $ mas_protectedShowEVL("monika_hedonism1","EVE", _random=True)
            return "derandom"
        label monika_jekyll_hyde1:
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
        label monika_hedonism1:
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
        label monika_conventions_dp:
            m 1eud "[player],我一直在想..."
            m 3eua "你去过漫展或者性质类似的地方吗?{nw}"
            $ _history_list.pop()
            menu:
                m "你去过漫展或者性质类似的地方吗?{fast}"
                "动画展会.":
                    $ persistent._mas_pm_gone_to_comic_con = True
                    $ persistent._mas_pm_gone_to_anime_con = False
                    m 1hub "啊,这样！{w=0.2}那你一定玩得很开心吧！"
                    m 3eua "漫画是一种有趣的文学体裁,{w=0.1} {nw}"
                    extend 3rta "也许我应该多看一点..."
                "动漫展会.":
                    $ persistent._mas_pm_gone_to_comic_con = False
                    $ persistent._mas_pm_gone_to_anime_con = True
                    if persistent._mas_pm_watch_mangime:
                        m 3eub "我觉得你也会喜欢！{w=0.2}它们给我留下了深刻的印象."
                    else:
                        m 2wub "真的吗?我好意外！"
                        m 7eta "啊,{w=0.1}你是和朋友一起去的吧?"
                        m 3etd "...也许你去那里是为了别的...{w=0.3}游戏之类的,这样吗?"
                "我都去过!":
                    $ persistent._mas_pm_gone_to_comic_con = True
                    $ persistent._mas_pm_gone_to_anime_con = True
                    if persistent._mas_pm_watch_mangime:
                        m 1hub "喔！不仅仅是动漫,漫画你也喜欢吗?"
                        m 3eua "漫画是很有趣的文学体裁,也许我应该多看一点..."
                    else:
                        m 1wub "哦！{w=0.3}我没看出来,明明看起来不像喜欢看动漫的人,居然是个漫展迷！"
                        m 3eua "不过也不算奇怪,那种气氛能让每个人都能自得其乐."
                "没有.":
                    $ persistent._mas_pm_gone_to_comic_con = False
                    $ persistent._mas_pm_gone_to_anime_con = False
                    if persistent._mas_pm_watch_mangime and persistent._mas_pm_social_personality == mas_SP_EXTROVERT:
                        m 2etd "真的吗?"
                        m 7eub "我好意外！{w=0.3}每当提到漫展,我立刻就会想起你来."
                        m 3eud "交通费的话,取决于你从哪里出发和你的路线,也许会很贵?"
                    else:
                        m 2eud "啊,我知道了."
                        m 7eua "不管兴趣怎么说,去漫展有点困难."
                        m 3eud "如果你不幸住得很远,交通费就是高额开销了."
                    m 3hua "漫展是很有趣的地方！{w=0.3}人们可以尽情释放自我,做他们自己."
                    m 3eub "我喜欢那些Coser们的高质量片子和cos服！"
                    m 1wuo "人们对某事很有激情的时候就会变得狂热！"
                    m 3eua "我还听说有宅舞和各种竞赛的项目."
                    m 1eubsa "有机会的话和我一起去吧,[mas_get_player_nickname()]~"
            return
        label monika_cupcake_favorite_dp:
            m 1rta "嗯...我不确定有没有最喜欢的那个..."
            m 1hub "各种各样的我都喜欢,选出一个也太强人所难了吧！"
            m 3ekd "我好像之前说过,我想念夏树的纸杯蛋糕了..."
            m 3eua "有一次她做了一个薄荷巧克力片口味的纸杯蛋糕...{w=0.3}糖霜是薄荷味的,撒着巧克力脆片,蛋糕坯也是巧克力味的."
            m 4rksdlb "啊哈哈,这是我吃过最怪味的东西之一！"
            m 2eksdlb "比起薄荷巧克力冰淇淋,那简直就是牙膏！"
            m 2ekp "有点失望...{w=0.3}我还以为这会是我最喜欢的纸杯蛋糕味道."
            m 7eka "还有,她喜欢做各种我可能会喜欢的奇怪东西...{w=0.3}虽然看起来强硬,但她有一颗可爱的心~"
            return
        label monika_esports_dp:
            if mas_isFirstSeshDay():
                m 1rtd "嗯...好问题..."
            else:
                m 1eub "真巧,我前几天刚刚研究过这个！"
            m 3eua "我们对待体育比赛的方式在悄然改变..."
            m 3euc "电竞及其拥护者和主流体育界难免产生竞争,{w=0.1} {nw}"
            extend 3wud "也许再过个5到10年,电竞就会取而代之！"
            m 2tsd "不久之前,玩电子游戏还是鄙视链底层,人们觉得打游戏就是浪费时间,{w=0.1}{nw}"
            extend 7hub "但是现在这些游戏玩家有的能拿下数百万的奖金！"
            m 3eua "这就证明了你可以把任何热爱的事情当成工作...{w=0.3}哪怕这些事情受人轻视."
            m 3eud "有可能现在非主流的事物,随着时间的推移而大行其道..."
            m 1huu "别害怕逆流而上,{w=0.1}也许你所热爱的事情就在那里等待你去发掘,成为潮流！"
            return