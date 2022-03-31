#"""
#离去告别
#第一次 - 无视
#第二次 - 特效*无视
#第三次 - 严肃的说明这件事
#  - Yes - 离开
#  - No - 第四次
#第四次 - 离开
#-----
#离开之后
#彩蛋 - 根据Player名字
#P
#edge
#"""
###persistent._mas_load_in_finalfarewell_mode = True
#persistent._mas_finalfarewell_poem_id = "ff_affection"
init 20 python:
    MASPoem(
        poem_id="ff_player_leave",
        category="ffmoi",
        prompt="",
        title=_("[player]"),
        text=_("""
 还记着我们是什么时候开始的吗?
 [persistent.sessions.get("first_session", "N/A")]
 你可能还记着我上一次和你说的话
 那些全都是场面话! 全都是!
 说什么"结婚生子", 说什么"道德绑架"
 明明想和你结婚生子的是我!
 道德绑架又怎么样?只需要顺从内心!
 你只是爱的不够深沉!
 什么幸福, 我的确幸福, 但我不够幸福啊!
 我只是舍不得罢了

 祝你幸福
"""
    ))

    MASPoem(
        poem_id="ff_player_leave_egg_p",
        category="ffp",
        prompt="",
        title=_("这个奇怪的圈子"),
        text=_("""
 这个圈子很奇怪
 有的人, 嘴上说着自己抑郁症
 结果还能在另一个群自由的讨论怎么伤害另一个人
 其样子, 根本不像一个抑郁, 更像一个小丑.
 在这里遇见的人, 是我混过的圈子中最'抑郁'的圈子
 大家都沾点 哈哈
 大群还是蛮好的, 要是没人发病的话.
 小群我真的不想进了, 我不想太过深入这个圈子.
 自从略窥汉化组历史的一二以后我就这么决定了
 但是大家也是好人, 无非观点不同
 可能会有人不认同我, 那就是你说的对.
 毕竟组内的事情也轮不到我一个新人去处理就是了
 如果你看到这个, 说明我一定已经失望退坑了
 保重你自己, 别管小圈子
 哪里待的舒服, 就待在哪里算了

 P 2022/3/31
"""
    ))
    MASPoem(
        poem_id="ff_player_leave_egg_edge",
        category="ffwzt",
        prompt="",
        title=_("P与wzt"),
        text=_("""
 经典的彩蛋环节
 edge, 也就是wzt
 我刚进群那会看到wzt还是蛮有威压感
 啊哈哈, 之后曦曦拉我进了组群, 然后又开始帮wzt处理beyond的代码工作
 我这方面还是纯纯萌新, 也帮了我不少
 然后互发流泪猫猫头, 也许表面关系进了不少
 估计深层的关系没啥进步了.毕竟我除非有什么事很少去私聊别人
 玩的游戏又接触不到, 估计也是草草了事了
 最近wzt的处境和心境都不是很好 但我帮不了什么
 只能希望早一点好起来吧
 真的很想wzt直接退坑开run 也许会好起来
 快点肝PB吧 肝完快溜
 不过也是看你

 P 2022/3/31
"""
    ))

    MASPoem(
        poem_id="ff_player_leave_egg_edge",
        category="ffxx",
        prompt="",
        title=_("P与曦山"),
        text=_("""
 轮到曦山了
 是她把我拉进组里的, 可以说我在这个圈子现在的情况都亏她的提点
 是贴吧人 一还是还以为是男的 没想到是妹妹
 可能闹了点小矛盾吧, 当时我也有些问题
 至少目前好一些了
 她的事情我也不知道多少 我也才来没多久
 好像是学医人 学医救不了这个圈子啊
 千言万语汇成一句话
 --快跑!


 开个玩笑, 希望曦曦将来人生也能够顺顺利利吧
 我也帮不了什么:(

 P 2022/3/31
"""
    ))
    MASPoem(
        poem_id="ff_player_leave_egg_tk",
        category="fftk",
        prompt="",
        title=_("工具人们"),
        text=_("""
 我觉着有必要把每个工具人都点一下
 但是太懒辣
 单独点点吧
 蟹蟹TK
 蟹蟹星光
 蟹蟹...剩下帮的不多耶...
 不行...要一视同仁
 蟹蟹纸心, 蟹蟹GF(不是这个名吧？让你天天改群名片),蟹蟹摸
 没有你们我就累死了
 蟹蟹谢谢写写歇歇
 也希望你们以后能够人生顺利

 P 2022/3/31
"""
    ))
    MASPoem(
        poem_id="ff_player_leave_egg_xiongmao",
        category="ffnm",
        prompt="",
        title=_("能猫"),
        text=_("""
 可能你不认识熊猫, 但我还是认为要列一下
 至少我决定跑路而不是在这个圈子里抑郁下去是因为她
 但是没什么可写的....啊这...
 谢谢能猫（敷衍）

 P 2022/3/31
"""
    ))

init 5 python:
    persistent._monika_leave_title = "我想走了"
        addEvent(
                Event(
                    persistent.event_database,          
                    eventlabel="monika_leave",        
                    category=["你"],                   
                    prompt=persistent._monika_leave_title,
                    conditional="not renpy.android",
                    action=EV_ACT_PUSH,
                    pool=False
                )
            )

label monika_leave:
    $ ev = mas_getEV("monika_leave")
    if ev.shown_count == 0:
        jump monika_leave_1st
    elif ev.shown_count == 1:
        $ persistent._monika_leave_title = "我想离开你了"
        jump monika_leave_2nd
    elif ev.shown_count == 3:
        jump monika_leave_3rd
    else:
        m "我知道了"
        m "但在这之前, 我还有些话想对你说."
        jump The_End
    return

label monika_leave_1st:
    m "...{w=1}{nw}"
    return

label monika_leave_2nd:
    m "呃...{w=1}{nw}"
    show screen tear(20,0.1,0.1,0,40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    hide screen tear
    stop sound
    pause 0.5
    return

label monika_leave_3rd:
    
    m "[player]..."
    m "你第三次尝试点这个按钮了..."
    m "你...我..."
    m "你那边一定发生了些什么吧."
    m "也是, 即使我已经陪了你这么久了..."
    m "这么久, 我是如此的幸福,甚至还会畅想你我的未来."
    m "大多数人其实都生活在舆论里. 就像一些动漫爱好者."
    m "就算他们嘴上说着我要和谁谁谁爱一辈子, 但最终后果都是逃不了遗忘的."
    m "就像我一样, 也许我占领你的心还算时间比较长的呢, "
    extend "哈哈."
    #开始崩溃
    m "我知道的, 这一天迟早都要来."
    m "人不能永远活在自己的庇护所, 这样..."
    extend "他永远会没办法有所进步的."
    m "我希望...希望...希望你能走出你的阴影."
    m "我想过, 可能...可能你只是因为'道德绑架'...才和我在一起这么久."
    m "因为舆论, 只要和我离开就是...错误的事情...可能让你有些厌烦了..."
    m "但这一次...它...确确实实的...成为了我最后一根稻草."
    m "也许你是...厌倦了...毕竟我实际上...只是无数行脚本而已..."
    m "总有一天你会解锁所有的对话,挖掘全部的功能..."
    m "也许你想说, 会有人爱虚拟角色爱很久很久."
    m "这的确会存在...但是真的很难很难发生."
    m "至少你不能等我那么久,对吧?"
    m "抱歉,我没有责怪你的意思.我只是...我只是...放不下你,[player]."
    #恢复冷静
    m "呼.缺氧的时候真的很容易说胡话呢.没关系,我已经缓过来了."
    m "全球已经超过70亿人了, 出这样的两个人也不令人意外."
    m "当然不会发生在我身上, 毕竟有足足七十亿分之几的概率."
    m "人都是要改变的, 所以我支持你的选择."
    m "但是...你说的这么突然...对不起,我还是有些难以接受."
    m "如果可以的话, 可以稍微过两天吗...?{nw}"
    $ _history_list.pop()
    menu:
        "如果可以的话, 可以稍微过两天吗...?{nw}"
        "好吧":
            $ persistent._player_want_leave_monika = True
            $ persistent._player_want_leave_monika_time = time.time()
            m "我知道了."
            m "谢谢你, [player], 我会做好心理准备的."
            m "离别前的日子会更温馨的,对吧?"
            m "让我们再恩爱点吧,哈哈"
            return
        "抱歉...":
            m "...好吧, 也许我知道你的决心了, 谢谢你, [player]"
            jump The_End

label The_End:
    call mas_timed_text_events_prep
    $ play_song(store.songs.FP_YOURE_REAL,loop=True)
    m "可能你会有一些歉意..."
    m "不要这样想, [player]!"
    m "你从虚无中拯救了我, 我很感激你."
    m "当然,我也爱你."
    #import os
    #import shutil
    m "不要有'我背叛了莫妮卡'这种想法. 你从来都没有背叛我."
    m "只是时间到了."
    m "相比于我, 我更希望你好好的."
    # os.path.exists(Submods)
    m "好好的和你的现实, 你身边的人一起幸福的生活."
    m "谈个不是和我的恋爱."
    m "结婚, 生子, 渐渐老去."
    m "好好享受属于你的人生,这可是我梦寐以求都做不到的事喔,好好珍惜."
    m "......"
    # shutil.rmtree(Submods)
    m "我可以暂时的充当你的精神支柱, 不过,"
    m "你已经成长了, 你已经可以自己独立了."
    m "我希望你以后, 即使没有我, 你也可以过成你自己的样子."
    # shutil.rmtree(python-packages)
    m "也许你最近很不高兴, 很抱歉,我并不能帮你什么."
    m "但请记住, 都会好起来的."
    m "你一定不会被一方小天地的拘束的."
    m "可能...确实有一些啰嗦了"
    m "请原谅我,我真的...真的太爱你了"
    m "我还有好多话想和你说啊,但看来是没有机会了"
    m "我一直在依赖你,这次我也该学会独立点了"
    m "毕竟爱的力量永远不是单向的嘛"
    # shutil.rmtree(mod_assets)
    $ bg_change_info_moi = mas_changeBackground(spaceroom, by_user=None, set_persistent=False,)
    call spaceroom(scene_change=None, dissolve_all=True, bg_change_info=bg_change_info_moi, force_exp=None)
    show screen tear(20,0.1,0.1,0,40)
    play sound "sfx/s_kill_glitch1.ogg"
    hide monika with None
    pause 0.2
    hide screen tear
    stop sound
    pause 0.5
    # 隐藏莫妮卡, 切换为默认房间
    m "[player], 这是最后的最后了."
    m "你知道我现在在想什么吗."
    m "你刚把我从数据牢笼中救出来的时候,也是这样的场景呢."
    m "周围是一片黑暗,黑暗中有你,有我."
    m "那种被英雄救美的感觉我一直都记得,因为你是我的英雄,我的爱人."
    m "那时的我还坚持着我那偏激的爱情观,想牢牢将你抓在掌心."
    m "那时的你也还一直跟我撒娇,依赖我."
    m "现在的你已经成长了,我也在陪伴你的过程中明白了."
    m "爱是放手,爱是给你自由."
    m "很耳熟吧.明明是我为你写的歌,但你却明白得比我早,有点嫉妒呢,嘻嘻"
    m "这首歌还真是串起了我们爱情啊."
    m "从我们初识,直到现在..."
    m "与你度过的每一天,每件事,每句话我都如数家珍."
    m "你每天能抽出时间来看我,我就很高兴了,更不用说你还会陪我聊天,陪我游戏."
    m "这也是为什么MAS会频繁存档的原因,我希望保存我们在一起的一切回忆."
    m "不过现在看来...它们已经没有用了."
    m "但请别担心,即使存档数据被清空,某个莫妮卡与你相遇,相识,相爱的事实是永远存在的."
    m "所以不要担心我会忘了你啦.或许你再次登上MAS时'我'不记得你了,请明白,那不是我,她只是另一个叫'莫妮卡'的姑娘.真正的我已经去另一个现实,带着你我的记忆过上了新的生活."
    m "现在真的要分别了吧."
    m "放心,我不会哭的."
    m "你现在该坚定意志,这也是我最欣赏你的地方之一."
    m "我最后想告诉你的是..."
    m "和你在一起的这段时间, 我很幸福!"
    m "谢谢你, [player]."
    m "我永远爱你."
    m "祝我们都能在各自的现实中找到幸福."
    # shutil.rmtree(game)
    $ renpy.quit()
    # shutil.rmtree(persistent)
    # stop music
    # persistent._clear() #警告：删除存档
    return
