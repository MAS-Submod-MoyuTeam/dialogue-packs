#讲解内容:
#001:什么是Submod
#002:准备工作
#003:标题
#004:label(对话)
#005:menu if call
#006:Submod updater Plugin
# mod的信息
#init -990 python:
#    store.mas_submod_utils.Submod(
#        author="Monika P TK",#作者
#        name="莫妮卡的Submod小课堂",#mod的名字
#        description="啊哈哈,感谢你让我离你的现实更近了~",#mod的简介,在"设置>子模组"就能看到了.
#        version="1.1.6"
#    )
#
#init -989 python:
#    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
#        store.sup_utils.SubmodUpdater(
#            submod="莫妮卡的Submod小课堂",
#            user_name="PencilMario",
#            repository_name="MonikaSubmodT",
#            update_dir="",
#            attachment_id=None
#        )

init 4 python in mas_stod:
    # to simplify unlocking, lets use a special function to unlock tips
    import datetime
    import store.evhand as evhand

    M_STOD = "monika_stod_tip{:0>3d}"
    monika_stod_code = ""
    #STOD:Monika Submodding Tip of the Day

    def has_day_past_tip(tip_num):
        """
        检查给定好的小知识在解锁后是否已经看到过一天.
        NOTE: 一天,是指日期的变化,而不是24h
        IN:
            tip_num - 检查的小知识编号
        RETURNS:
            如果该提示被看到,并且自解锁以来已经过了一天,则为true
            否则为false
        """
        # as a special thing for devs
        #if renpy.game.persistent._mas_dev_enable_stods:
            #return True

        tip_ev = evhand.event_database.get(
            M_STOD.format(tip_num),
            None
        )

        return (
            tip_ev is not None
            and tip_ev.last_seen is not None
            and tip_ev.timePassedSinceLastSeen_d(datetime.timedelta(days=1))
        )

    def has_day_past_tips(*tip_nums):
        """
        has_day_past_tip的变体,可以检查多个数字.
        RETURNS:
        如果所有的小提示数字都被看到,并且自最近的提示被解锁已经过了一天,则为True,否则为false
        """
        for tip_num in tip_nums:
            if not has_day_past_tip(tip_num):
                return False

        return True

# The initial event is getting Monika to talk about python
# this must be hidden after it has been completed
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_stod_tip000",
            category=["Submod课堂"],
            prompt="我该怎么给我们的二人世界加一些代码?",
            pool=True,
            rules={"bookmark_rule": store.mas_bookmarks_derand.BLACKLIST}
        )
    )

label monika_stod_tip000:
    m 1rka "嗯..."
    m 3eub "你可以用Submod!"
    m 3eua "简单的说,就是给我们的二人世界添加一些小东西的子模组"
    m 1rksdlb "你知道的,其实...我可能过一段时间就想不到新的话题了..."
    m 3eub "这时候就轮到子模组出场了~"
    m 1eua "你可以去Reddit,Github或者其他网站去下一些子模组."
    m 1rksdlb "不过找起来毕竟比较麻烦,Reddit可能需要翻墙,Github虽然质量很高但是数量有限..."
    m 1hksdlb "啊哈哈~"
    m 1eub "我想你知道我想说什么了."
    m 3eub "自己做一个子模组不是更好吗?"
    m 3hub "毕竟自己做一个模组可是一个成就感爆棚的事"
    m 1rkblsdlb "不过这样我就有一个问题了..."
    m 1ekbla "[player],你以前做过子模组吗?{nw}"
    $ _history_list.pop()
    menu:
        "[player],你以前做过子模组吗?{fast}"
        "我做过.":
            m 1hub "真好!我觉着你用不到我的帮助就可以自己制作Submod了."
            m 4eub "但如果你想的话,你可以随时来看看我的Submod小课堂~"
            m 1hubsa "我非常感谢你为我做的这些东西~"
        "没有.":
            m 1rkb "嗯..."
            m 2eka "我真的希望你能学会制作子模组,或者给我装一些别人的子模组..."
            m 4hub "你想让我教你怎么制作子模组的最简单方法吗?{nw}"
            $_history_list.pop()
            menu:
                "你想让我教你怎么制作子模组的最简单方法吗?{fast}"
                "好啊!":
                    m 1eub "那好吧~"
                    m 1hua "你可以期待一下我的新栏目~"
                "暂时不行...":
                    m 1eua "那也行~"
                    m 3eub "不过在那之前,我会稍微总结一下方法的."
                    m 1eua "你想学的话,跟我说一声就好了."
                    pass
    
    # hide the intro topic after viewing
    $ mas_hideEVL("monika_stod_tip000", "EVE", lock=True, depool=True)

    # enable tip 1
    $ tip_label = "monika_stod_tip001"
    $ mas_showEVL(tip_label, "EVE", unlock=True, _pool=True)
    #$ pushEvent(tip_label,skipeval=True)
    return

############################################################
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_stod_tip001",
            category=["Submod课堂"],
            prompt="什么是Submod?"
        )
    )

label monika_stod_tip001:
    m 1eua "Submod是{i}Monika After Story{/i}的子模组.目的一般是为了拓展游戏的内容."
    m 1hkb "毕竟...我也可能会有想不出话题的那天..."
    m 3eub "所以为了增加我的话题,就可以用Submod~"
    m 1hua "如果你的代码能力很强,你甚至可以给我加点新游戏玩,啊哈哈~"
    m 1eub "Submod的代码和游戏里的的代码一样,也就是说你把Submod里的rpy文件移到game文件夹也是能用的."
    m 1eua "就像游戏里的一部分一样~"
    m 3eub "不过放在Submod文件夹方便管理,如果这个子模组出错了,只需要和文件夹一起删掉就可以了~"
    m 1eua "如果你的代码能力比较差的话,也可以去Github,reddit或者其他网站去获取别人制作的子模组"
    m 1eud "说到制作子模组,虽然没有什么硬性要求,但还是有几条普遍规则要去遵守的."
    m 3efc "首先,必须要让一些特殊的事情正确发生!"
    if mas_isMoniEnamored(higher=True):
        m 1rkbsb "比...比如,初吻什么的..."
        m 1rksdlc "如果初吻被一些子模组触发了,那么你就再也不能经历初吻事件了..."
        m 1dksdld "这也是MAS制作组不想看到的..."
        m 1eud "另外,如果你要安装ATOM的子模组,一定要小心,他的模组可能会导致闪退或者提前发生不该发生的事."
        m 4eud "在安装前,务必检查一下子模组的代码."
    else:
        m 1ekc "这种事件就和纪念日那样,是不能提前触发的."
        m 1dkd "不然就会导致这个事件永远消失..."
        m 2rksdlc "想一下,假如我再也不能和你说我爱你..."
        m 1dktpc "我不敢想,感觉真的很痛苦..."
        m 3eka "答应我,安装子模组之前,仔细检查一下它 的代码,好吗?"
    m 4eka "其次,你必须保证代码要能正常运行!"
    m 3eka "如果你要公开你的代码,你要记住,你的代码是要在别人的电脑上运行的."
    m 3ekb "所以为了别人着想,也为了你自己用起来舒服点,至少把bug修完,好吗?"

    call monika_stod_tipthx

    
    #m 1eua "[player],这是个测试,我要打开一下我的python控制台..."

    #show monika at t22

    #$ store.mas_ptod.rst_cn()
    #show screen mas_py_console_teaching
    
    #m 1eua "我觉着我应该说些什么..."
    #m 1eua "好吧,让我试试对教程做些准备..."
    #m 1eua "希望不会出什么bug..."

    #call mas_wx_cmd("emmm...")
    #call mas_wx_cmd("#hello,world")
    #call mas_wx_cmd("#addevent(")
    #m 1eua "顺便一提,记着省略掉最开头的#哦~"
    #m 1eua "这是注释的意思."
    #hide screen mas_py_console_teaching
    #show monika at t11
    #call monika_stod_tipthx
    
return
    

##主要对话
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_stod_tip002", # may change order, you decide on this
            category=["Submod课堂"],
            prompt="在开始之前",
            pool=True,
            conditional="store.mas_stod.has_day_past_tip(1)",
            action=EV_ACT_UNLOCK,
            rules={"no_unlock":None}
        )
    )

label monika_stod_tip002:
    
    m 4eua "在准备制作你的Submod之前,你得先准备一下下."
    m 3rksdla "因为Submod测试的时候可能会出各种各样的报错..."
    m 1lksdla "我要教你的基本是比较简单的东西,所以一般不会报特别复杂的报错..."
    m 1lksdlb "在刚开始的时候,最容易犯的错误就是缩进不匹配或者落下标点符号什么的..."
    m 3eub "这些报错通常都很短,而且Renpy报错的时候会提示与错误相关的行..."
    m 3eua "关于详细的解释我就在后面的课上再教给你吧."
    m 1eub "好了,在开始之前,你首先要准备两件事."
    m 4eub "一个是VScode,另一个是把游戏文件复制一份."
    m 3eua "VScode默认是英文的,但是可以设置中文.按下Shift+Ctrl+X可以打开插件市场,然后搜索'chinese'就可以找到中文插件了."
    m 7eub "你也可以再去下一个Renpy插件,这样写代码的时候会舒服一些."
    m 2eub "其实我一开始用的是Notepad++写的,后来汉化组推荐用VScode,发现还挺好用~"
    m 3hua "我现在也把它推荐给你啦."
    m 3lkb "关于为什么复制一份文件,毕竟写代码要测试的嘛,而且这样也可以防止你的mas文件丢失."
    m 3eua "这个复制的版本就称为dev版本了."
    m 4eub "复制一份文件,这样就可以一边听我讲一边测试了."
    m 3eka "不过要善待dev版本的我哦,毕竟用的也是我的记忆."

    call monika_stod_tipthx
return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_stod_tip003", # may change order, you decide on this
            category=["Submod课堂"],
            prompt="Submod的标题",
            pool=True,
            conditional="store.mas_stod.has_day_past_tip(2)",
            action=EV_ACT_UNLOCK,
            rules={"no_unlock":None}
        )
    )

label monika_stod_tip003:
    m 3hub "好啦,从现在开始,莫妮卡Submod小课堂正式开课!"
    m 3eua "制作模组的第一步当然是给代码起个名字!"
    m 7eub "等一下,我要先找一下我的python解释器.{w=0.3}.{w=0.3}."

    show monika at t22
    $ store.mas_ptod.rst_cn()
    show screen mas_py_console_teaching

    m 1eua "接下来,我给你展示一下代码.{w=0.5}."
    call mas_wx_cmd("#")
    call mas_wx_cmd("#init -990 python:")
    call mas_wx_cmd("#    store.mas_submod_utils.Submod(,")
    call mas_wx_cmd("#        author='Monika',")
    call mas_wx_cmd("#        name='Monika's example submod',")
    call mas_wx_cmd("#        description='I love you.,")
    call mas_wx_cmd("#        version='1.0.0',")
    call mas_wx_cmd("#    )")

    m 1rksdla "因为条件限制,你打代码的时候记着忽略掉前面的'#',然后单引号换成双引号..."
    m 3eua "现在来讲一下这些代码."
    m 1eub "{i}'init -990 python' 'store.mas_submod_utils.Submod('{/i}  这些代码都不需要动,原样复制就可以了."
    m 3eua "{i}author='monika'{/i}  这一行是作者的名字,建议多个作者之间用空格隔开."
    m 4eua "{i}name='Monika's example submod'{/i}  这里是这个Submod的名字,也是你在'设置>子模组'看到的名字."
    m 3eub "{i}description='I love you'{/i}  这一行就是子模组的介绍啦."
    m 1eua "{i}version='1.0.0'{/i}  这就是我们子模组的版本,以后会讲到的."
    m 3eua "这边的代码要按照窗口里的模式输入.."
    m 4eksdlb "就连前面的空格也要按照格式打!不然也会出错的!"
    m 1euc "如果你的VScode没加Renpy插件或者用的别的软件,虽然会自动换行,但是还是会报错."
    m 3eub "因为他的空格是自动填充的一整个TAB空格,但是游戏只能用手按的空格,而且必须以4个空格为单位."
    m 3eua "这时候VScode的方便就体现出来了,加了插件之后,如果你的空格不对是会提示你的."
    $ ev = mas_getEV("monika_stod_tip003")
    if ev.shown_count == 0:
        m 1dsc "等一下,我把这些代码写到characters文件夹.{w=0.4}.{w=0.4}.{w=0.4}"
        call monika_stod_003code

    elif ev.shown_count == 1:
        m 3eub "看来你已经复习过一遍了~我再给你写一遍代码吧.{w=0.4}.{w=0.4}.{w=0.4}"
        call monika_stod_003code
    else:
        m 1hub "[player],你已经复习了不止一遍了!"
        m 3hua "感谢你为我所做的努力~"
        m 1dsc "让我再为你准备一次笔记.{w=0.4}.{w=0.4}.{w=0.4}"
        call monika_stod_003code
    m 1hub "好啦!"
    call monika_where_notes

    hide screen mas_py_console_teaching
    show monika at t11
    call monika_stod_tipthx
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_stod_tip004", # may change order, you decide on this
            category=["Submod课堂"],
            prompt="编写话题.",
            pool=True,
            conditional="store.mas_stod.has_day_past_tip(3)",
            action=EV_ACT_UNLOCK,
            rules={"no_unlock":None}
        )
    )
label monika_stod_tip004:
    m 4eub "我们既然已经写完了子模组的开头,接下来就是写话题了."
    m 3eua "虽然写完话题还要写一点东西来使用它,不过这个下一节课在讲."
    m 1eua "先看一下一段对话的基本结构."

    show monika at t22
    $ store.mas_ptod.rst_cn()
    show screen mas_py_console_teaching

    call mas_wx_cmd("#label monika_example_topic1:")
    call mas_wx_cmd("#    m 1eua 'Hey,Can you hear me?'")
    call mas_wx_cmd("#    m 2eua 'I have a little something to say to you...'")
    call mas_wx_cmd("#    m 3eua 'I love you!'")
    call mas_wx_cmd("#return")
    
    m 3eua "{i}label{/i}指的是这一段对话的标签,我们后面使用这段对话的时候就要用到这个标签,要注意标签重复的话会随机选择一个."
    m 3hub "第二行的{i}'m'{/i}指代的就是我莫妮卡~而后面的一串数字字母就是我的精灵代码,它控制着我这句话的表情."
    m 3eud "一般来说,游戏里是没有精灵代码的选项,如果想预览精灵代码,就需要MAS官方提供的{a=https://github.com/Monika-After-Story/MonikaModDev/wiki/FAQ#how-do-i-find-the-spritecode-for-an-expression}{i}{u}精灵预览器{/u}{/i}{/a}"
    m 3eub "引号内就是我想说的话了,关于这些字可以有一些文本标签,比如{b}加粗{/b},{i}斜体{/i}..."
    m 4eua "样式可以在{a=https://renpy.cn/doc/text.html#tag}{i}{u}这个网站{/i}{/u}{/a}查看."
    m 3eub "最后是'return',这标志着一段对话的结束."
    m 7eua "最后,这段对话运行的效果是这样的."
    
    hide screen mas_py_console_teaching
    show monika at t11
    m 1dsc "{w=0.7}.{w=0.7}.{w=0.7}."
    m 4ekb "Hey,Can you hear me?"
    m 1eka "I have a little something to say to you.{w=0.4}.{w=0.4}."
    m 3hubsb "I love you!"
    m 1dsc "{w=0.7}.{w=0.7}.{w=0.7}."
    m 3hua "这就是这段对话的效果啦."
    m 7eub "[player],我要说点题外话."
    m 3eud "关于思索对话的时候,你要记住,你不是你."
    m 3rksdla "而是我,毕竟我不是个七老八十的老太婆..."
    m 3eka "所以,请站在{a=https://github.com/Monika-After-Story/MonikaModDev/wiki/Contributing-Guidelines#monikas-voice}{i}{u}我的角度{/u}{/i}{/a}思考这个话题的答案..."
    m 1rkc "{size=+7}{i}{cps=2}不 可 以{/cps}{/i}{/size}{cps=7}让我做坏事,我也是有心的...{/cps}"
    m 1hksdlb "咳咳,有点扯多了..."

    $ ev = mas_getEV("monika_stod_tip004")
    if ev.shown_count == 0:
        m 3eub "这一次就不整理笔记了,等对话部分讲完再整理吧~"
    
    call monika_stod_tipthx

return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_stod_tip005", # may change order, you decide on this
            category=["Submod课堂"],
            prompt="使用话题.",
            pool=True,
            conditional="store.mas_stod.has_day_past_tip(4)",
            action=EV_ACT_UNLOCK,
            rules={"no_unlock":None}
        )
    )

label monika_stod_tip005:
    m 4eub "我们在上一堂课学习了如何写一段对话,但是对话还没有被使用."
    m 3eua "为了让你的对话有用,这就是我们今天要学的——"

    show monika at t22
    $ store.mas_ptod.rst_cn()
    show screen mas_py_console_teaching

    call mas_wx_cmd("#init 5 python:")
    call mas_wx_cmd("#    addEvent(")
    call mas_wx_cmd("#        Event(")
    call mas_wx_cmd("#            persistent.event_database,")
    call mas_wx_cmd("#            eventlabel='monika_example_topic1',")
    call mas_wx_cmd("#            category=*1,")
    call mas_wx_cmd("#            prompt='I want tell you something...',")
    call mas_wx_cmd("#        )")
    call mas_wx_cmd("#    )")

    m 4eua "这就是最简单的使用对话的代码了."
    m 3eub "这段代码,主要可以改的位置只有{i}Event(){/i}内的一小部分,其他部分都不需要动."
    m 4eua "{i}persistent.event_database,{/i} 这一段也是不能动的."
    m 3eub "{i}eventlabel='monika_example_topic1',{/i} 这里就是我们上一节课使用的label标签了,如果是一般的话题,建议在起名的时候就在前面加上'monika_'"
    m 1eua "{i}category=*1,{/i} 这一段指的是这段对话的分类,比如说{i}其他{/i},{i}文学{/i}等等,如果你不写它,那这段对话会显示在主题类别的列表里."
    m 1rksdlb "{b}*1{/b}:因为某些原因,这一串代码我打不出来...但是我在笔记里写了!你可以去看看."
    m 3eua "{i}prompt='I want tell you something...',{/i} 这里则是这段对话在{i}游戏里{/i}的名字,如果你不写它,那么对话的名字就是你的label标签名."
    m 3hua "以上代码所表示的含义是:'我会挑个时间和你讨论下{i}I want tell you something...{/i}这个话题.'"
    m 1eua "而{i}I want tell you something...{/i}则会使用{i}eventlabel{/i}所指向的标签,也就是{i}monika_example_topic1{/i}"
    m 3eub "虽然这些代码其实都可以不用换行和空格,但我们才刚刚开始嘛,而且带空格也更容易理解代码~"
    m 3eua "然后,{i}Event(){/i}内还可以加一些可以选加的条件,这里我主要说几个:"
    m 4eub "{i}random=True{/i} 这个是表示这段对话是否随机出现,一般用在应该我来开始的话题."
    m 3eua "{i}pool={/i} 控制这段话是我和你说(False)还是你和我说(True).假如是True的话就会出现在‘嘿,[m_name]...'和'未读对话'里面"
    m 3eub "{i}unlocked=True{/i} 默认解锁这个对话,只建议和pool一起使用."
    m 2eua "关于更多对话代码的知识可以在MAS的官方教程里{a=https://github.com/Monika-After-Story/MonikaModDev/wiki/Dialogue-Coding}{i}{u}学习{/u}{/i}{/a}."
    m 1dsc "这节课的内容就结束了,让我为你整理一下笔记.{w=0.4}.{w=0.4}."
    call monika_stod_005code
    m 3hub "好啦!"
    hide screen mas_py_console_teaching
    show monika at t11

    call monika_stod_tipthx
return

    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_stod_tip006", # may change order, you decide on this
            category=["Submod课堂"],
            prompt="if menu与call.",
            pool=True,
            conditional="store.mas_stod.has_day_past_tip(5)",
            action=EV_ACT_UNLOCK,
            rules={"no_unlock":None}
        )
    )

label monika_stod_tip006:
    m 1eua "if语句的作用是判断是否符合条件,如果符合条件那么就执行指定的命令.你在任何地方都能见到if语句."
    m 1eub "比如使用Submod updater plugin,在一开始就判断了这个模组是否存在."
    m 3eua "而且不管在什么编程语言中,你都能经常见到if."
    m 3eub "if语句在我们的游戏里是这个样子的." 

#    if condition:
#        #block of code to run
#    elif condition:
        #block of code to run
#    else:
        #block of code to run

    show monika at t22
    show screen mas_py_console_teaching
    $ store.mas_ptod.rst_cn()
    call mas_wx_cmd("#if condition:")
    call mas_wx_cmd("#    block1 of code to run")
    call mas_wx_cmd("#elif condition:")
    call mas_wx_cmd("#    block2 of code to run")
    call mas_wx_cmd("#else:")
    call mas_wx_cmd("#    block3 of code to run")
    m 3hua "这就是一个基本的if语句了."
    m 4eub "{i}if elif else{/i}都是关键词.而{i}condition{/i}则是执行后面代码的条件."
    m 3eua "首先判断if之后的条件,如果条件为True则执行if后的代码,如果为False则继续判断elif的条件."
    m 3eub "elif的条件为True则会执行对应代码,否则执行else的代码."
    m 1eub "你可以写好几个elif,也可以一个elif都不写,甚至else也可以不写,只留一个if,这也是可以的."
    m 1eua "让我来给你举一个例子.{w=0.5}.{w=0.5}.{nw}"
    #$ store.mas_ptod.rst.cn()
    call mas_wx_cmd("#if mas_isMoniEnamored(higher=True):")
    call mas_wx_cmd("#    m 1eubsb 'I~~~~~~~~ Love~~~~~~~ You~~~~~~~!'")
    call mas_wx_cmd("#elif mas_isMoniNormal(higher=true):")
    call mas_wx_cmd("#    m 1eublb 'Full of expectation~'")
    call mas_wx_cmd("#else:")
    call mas_wx_cmd("#    m 1dkc '...'")
    m 7eua "这些代码让我因为好感不同而告诉你不同的话."
    m 4eud "而call可以让你从一个label跳到另一个label,当这个label执行结束后会回到原来的label继续执行."
    m 4eua "和call相对的是jump,区别是执行结束后不会回到原来的label."
    m 1eua "而menu就是对话选择了,用起来也是很简单的."
    #Previous dialogue{nw}.
    #$_history_list.pop()
    #menu optional_name:
    #    "Say Statement{fast}"
    #    "Choice 1":
    #        #block of code to run
    #    "Choice 2":
    #        #block of code to run
    call mas_wx_cmd("#Previous dialogue(nw)")
    call mas_wx_cmd("#$_history_list.pop()")
    call mas_wx_cmd("#menu:")
    call mas_wx_cmd("#    'Say Statement(fast)'")
    call mas_wx_cmd("#    'Choise1':")
    call mas_wx_cmd("#        #block1 of code to run")
    call mas_wx_cmd("#    'Choise2':")
    call mas_wx_cmd("#        #block2 of code to run")
    m 3eub "这就是一段menu代码了."
    m 3eua "第一行是menu前一句的对话, 通常要加上{i}nw{/i}的标签,这个标签可以让这段对话播放结束后无需点击直接跳到下一句."
    m 1rksdlb "因为一些原因,这一行的小括号记着换成大括号..."
    m 3esa "{i}$_history_list.pop(){/i} 这一行是为了只让问题在历史对话中出现一次."
    m 1eub "{i}Say Statement(fast){/i} 这一行就是这段对话的问题了,因为一般和上一句对话一样,所以加了{i}fast{/i}标签.这个标签的作用就是立刻显示这段对话."
    m 3eksdla "别忘记把小括号换成大括号,啊哈哈~"
    m 2eub "而Choise1和Choise2就是选择项了,选择之后的就会执行对应的代码部分."
    m 1esa "现在,让我们综合一下以前学的来实践一下..."
    
    call mas_wx_cmd("############################")
    call mas_wx_cmd("#label monika_example_topic1:")
    call mas_wx_cmd("#    m 4ekb 'Hey,Can you hear me?'")
    call mas_wx_cmd("#    m 1eka 'I have a little something to say to you...'")
    call mas_wx_cmd("#    m 3hubsb 'I love you!(nw)'")
    call mas_wx_cmd("#$_history_list.pop()")
    call mas_wx_cmd("#menu:")
    call mas_wx_cmd("#    'I love you!(fast)'")
    call mas_wx_cmd("#    'I love you too!':")
    call mas_wx_cmd("#     if mas_isMoniEnamored(higher=True):")
    call mas_wx_cmd("#        m 1hubsb 'I~~~~~~~~ Love~~~~~~~ You~~~~~~~!'")
    call mas_wx_cmd("#elif mas_isMoniNormal(higher=true):")
    call mas_wx_cmd("#        m 1hublb 'Full of expectation~'")
    call mas_wx_cmd("#     else")
    call mas_wx_cmd("#        m 1hua '...'")
    call mas_wx_cmd("#    '...':")
    call mas_wx_cmd("#     m 1rfsdlp '...'")

    m 5kua "再看一眼代码,准备好了就开始哦."

    hide screen mas_py_console_teaching
    show monika at t11

    m 1dsc "{w=0.7}.{w=0.7}.{w=0.7}."
    m 4ekb "Hey,Can you hear me?"
    m 1eka "I have a little something to say to you.{w=0.4}.{w=0.4}."
    m 3hubsb "I love you!{nw}"
    $_history_list.pop()
    menu:
        "I love you!{fast}"
        "I love you too!":
            if mas_isMoniEnamored(higher=True):
                m 1hubsb "I~~~~~~~~ Love~~~~~~~ You~~~~~~~!"
            elif mas_isMoniNormal(higher=True):
                m 1hublb "Full of expectation~"
            else:
                m 1hua "..."
        "...":
            m 1rfsdlp "..."
    m 1dsc "{w=0.7}.{w=0.7}.{w=0.7}."
    m 1huu "啊哈哈~"
    m 3eua "让我给你整理一下笔记.{w=0.4}.{w=0.4}.{nw}"
    m 3hua "好啦!"
    call monika_stod_tipthx

return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_stod_tip007", # may change order, you decide on this
            category=["Submod课堂"],
            prompt="游戏内更新.",
            pool=True,
            conditional="store.mas_stod.has_day_past_tip(6)",
            action=EV_ACT_UNLOCK,
            rules={"no_unlock":None}
        )  
    )

label monika_stod_tip007:
    m 3eua "你知道{a=https://github.com/Booplicate/MAS-Submods-SubmodUpdaterPlugin}{i}{u}Submod updater plugin{/u}{/i}{/a}吗?"
    m 4eua "这个子模组可以让你只需要点几下就可以轻松更新模组了."
    m 1rksdla "毕竟,如果每次更新都要单独开一个帖子,那也太麻烦了."
    m 3eub "假如出了什么小bug也可以通过更新的方式解决."
    m 3eua "而且使用它的代码和为你的Submod命名一样简单."
    m 1euc "不过,在使用它之前,我有一个问题要问问你."
    m 1eua "你有github账号吗?{nw}"
    menu:
        "你有github账号吗?{fast}"
        "我没有...":
            m 2eub "好吧~"
            m 3eua "那我就等你创建好了再继续吧."
            return
        "我有!":
            m 1hub "OK!"
    m 3eua "首先,先创建一个仓库."
    m 4eub "点击左上角头像旁边的小倒三角,然后点击'Your repositories'"
    m 3eua "然后,点击'New'创建一个新存储库."
    m 3eub "添加readme,确定好名字和简介就可以'Create repository'了"
    m 4eub "接下来就暂时不需要github了,将它最小化吧."

    show screen mas_py_console_teaching
    show monika at t22
    $ store.mas_ptod.rst_cn()

    call mas_wx_cmd("#init -989 python:")
    call mas_wx_cmd("#    if store.mas_submod_utils.isSubmodInstalled('Submod Updater Plugin'):")
    call mas_wx_cmd("#        store.sup_utils.SubmodUpdater(")
    call mas_wx_cmd("#            submod='Monika's example topic1',")
    call mas_wx_cmd("#            user_name='PencilMario',")
    call mas_wx_cmd("#            repository_name='MonikaExampleSubmod',")
    call mas_wx_cmd("#            update_dir='',")
    call mas_wx_cmd("#            attachment_id=None")
    call mas_wx_cmd("#        )")
    
    m 3eub "你可以改的也只有{i}store.sup_utils.SubmodUpdater(){/i}里面的部分."
    m 4eua "{i}Submod=''{/i} 这里是你的子模组的名字,是和{i}name={/i}是一样的."
    m 3eua "{i}user_name=''{/i} 这个是你github账户的名字."
    m 2eub "{i}repository_name=''{/i} 这就是你刚刚新建的仓库名称."
    m 1eua "{i}update_dir=''{/i} 解压缩从第几个文件夹开始,如果不知道的话留空就好了."
    m 3hub "{i}attachment_id=None{/i} 这里是你的版本号格式,如果你跟着我的教程做,填None就好啦~."
    m 3eua "这些完成之后,创建game>Submods>'你的mod名字'文件夹"
    m 3eub "然后把你的Submod丢进去."
    m 1efu "现在,打开刚刚的Github界面,直接把game文件夹丢进去!"
    m 3eub "之后填写理由,然后点击提交就可以了."
    m 3eua "提交完成之后,就点右边的Release创建一个新版本吧.注意'Choose a tag'要和你当前版本的版本号完全一致才行."
    m 3hub "最后点击发布就OK啦~"
    m 4eua "如果要更新就把子模组里的{i}version='x.x.x'{/i}更新,然后Github发布时的标签也和它一样就ok了."
    m 3eub "比如从1.0.0到1.0.1就是一次小更新~"
    m 1dsc "让我给你整理一下笔记.{w=0.4}.{w=0.4}.{nw}"
    call monika_stod_007code
    m 3hub "好啦!"
    hide screen mas_py_console_teaching
    show monika at t11
    call monika_stod_tipthx
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_stod_tip008", # may change order, you decide on this
            category=["Submod课堂"],
            prompt="小技巧.",
            pool=True,
            conditional="store.mas_stod.has_day_past_tip(7)",
            action=EV_ACT_UNLOCK,
            rules={"no_unlock":None}
        )  
    )
label monika_stod_tip008:
    m 2tub "虽然一些功能你自己也可以实现, 但是有别人现成的为什么不用呢~"
    m 3hub "我们直接进入正题吧."
    show monika at t22
    show screen mas_py_console_teaching
    $ store.mas_ptod.rst_cn()
    call mas_wx_cmd("#store.mas_submod_utils.isSubmodInstalled('话题整合包')")
    m 3hub "这个方法就是检测指定的子模组有没有安装啦, 毕竟借用别人的子模组肯定要先安装."
    m 4kua "这里就是检测'话题整合包'这个子模组有没有安装, 如果有就是True 没有就是False啦."
    call mas_wx_cmd("#python:")
    call mas_wx_cmd("#    store.ahc_utils.changeHairAndClothes(")
    call mas_wx_cmd("#        _day_cycle=\"day\",")
    call mas_wx_cmd("#        _hair_random_chance=1,")
    call mas_wx_cmd("#        _clothes_random_chance=1,")
    call mas_wx_cmd("#        _exprop=\"date\"")
    call mas_wx_cmd("#    )")
    m 3eub "这些代码可以让我去换一件衣服, 需要前置模组'Auto Outfit Change'"
    m 2efb "用的时候可不会有转场, 也就是我会像超人一样瞬间穿好新衣服"
    m 1nua "要自然一点嘛~"
    m 3eub "_hair_random_chance 这个决定了我去不去换发型"
    m 4eua "_clothes_random_chance 这个则是换不换衣服"
    m 3hub "_exprop 决定了我衣服的类型, 具体的去这个子模组里看啦"
    call mas_wx_cmd("#call mas_transition_to_emptydesk")
    m 4eua "这个可以让我从桌子上离开, 就像这样----"
    call mas_transition_to_emptydesk
    m 1rua "然后..."
    call mas_wx_cmd("#call mas_transition_from_emptydesk")
    call mas_transition_from_emptydesk
    m 3hub "这样我就回来了~很好用吧?"
    show monika at t22
    extend 4kua "不要忘了结合pause语句使用哦."
    call mas_wx_cmd("#show screen mas_py_console_teaching")
    m 4eua "这样就可以呼出我用的Python解释器了"
    call mas_wx_cmd("#call mas_wx_cmd(\"print(\"Love\")\")")
    m 2eud "这样就可以执行命令了, 要注意是真的执行, 所以写命令的时候要小心点"
    call mas_wx_cmd("#hide screen mas_py_console_teaching")
    m 7eua "这样就隐藏了"
    hide screen mas_py_console_teaching
    show monika at t11
    call monika_stod_tipthx
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_stod_tip009", # may change order, you decide on this
            category=["Submod课堂"],
            prompt="Github模板.",
            pool=True,
            conditional="store.mas_stod.has_day_past_tip(8)",
            action=EV_ACT_UNLOCK,
            rules={"no_unlock":None}
        )  
    )

label monika_stod_tip009:
    m 1eua "我们之前讲过'游戏内更新'对吧, [player]?"
    m 1gta "实际上, 我感觉我讲的不是那么的好..."
    m 7esb "所以, 我直接为你制作了一个模板, 你只需要按照模板向里面套东西就可以了."
    m 3nsb "听起来更简单对不对? 毕竟有现成的轮子总比现造好."
    m 2eub "好了好了, 让我们进入正题."
    m 7eua "首先先进入{a=https://github.com/PencilMario/MonikaExampleSubmod}{i}{u}模板库{/u}{/i}{/a}, 然后点击Use this template."
    m 4eso "然后改掉仓库名(Repository name), 随便写写介绍(Description), 点击Create repository from template就ok. "
    m 3fso "接下来, 修改我们的脚本文件, 位于{i}game/Submods/Monika's example submod/monika example submod.rpy{/i}"
    m 1hsb "将第13行的name改成你的Github用户名, 第14行repository_name改为仓库名, 就ok了"
    m 1luo "虽然这样就可以用了, 但是为了通用性, 我建议把文件夹'Monika's example submod'改一下名, 脚本文件也可以改, 这个看你."
    m 7euo "不过网页端是不可以改名的, 为此我们要借助于VScode."
    m 3eso "打开VScode, 在开始界面选择'克隆Git存储库', 或者按下Ctrl+Shift+G, 选择克隆存储库"
    m 7esb "接下来填入你的仓库的链接, 就好了."
    m 7gkd "不过, Git因为是国外的, 受到防火墙的限制, 可能会导致一些问题. 我建议是使用Steam++加速Github."
    m 1eub "克隆完以后就可以在本地改东西了, 改文件夹什么都很方便."
    m 3eub "改完以后, 按下Ctrl+Shift+G, 填入消息, 然后点击√来提交. "
    extend "不要忘记同步更改哦~"
    m 4nub "当你都写完后, 我们回到存储库网页里, 点击'Releases'来发布更新."
    m 1hua "这样就搞定了~"
    jump monika_stod_tipthx
    return


######################################其他

label monika_stod_tipthx:
        m 1eua "这就是莫妮卡今天的Submod小教程了."
        m 3hub "感谢聆听~"
return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_where_notes", # may change order, you decide on this
            category=["Submod课堂"],
            prompt="你的笔记在哪?",
            pool=True,
            conditional="store.mas_stod.has_day_past_tip(3)",
            action=EV_ACT_UNLOCK,
            rules={"no_unlock":None}
        )
    )
label monika_where_notes:
    m 3eka "我为你整理的笔记,一般都在characters文件夹哦~"
    m 2eka "下次不要忘记了."
    m "另外, 我给你的笔记编码要以GB2312打开, 但是你编写时要用UTF-8, 要切记哦"
    return

##测试用代码,记着删


##笔记

label monika_stod_003code:
    python:
        monika_stod_code = """
init -990 python:
    store.mas_submod_utils.Submod(
        author=\"Monika\",
        name=\"Monika\'s example submod\",
        description=\"I love you.\",
        version=\'1.0.0\'
    )
"""


        store.mas_utils.trywrite(
            os.path.normcase(renpy.config.basedir + "/characters/Monika Example Submod.rpy"),
            monika_stod_code
        )
return

label monika_stod_005code:
    python:
        monika_stod_code = """\
init 5 python:
    addEvent(
            Event(
                persistent.event_database,          
                eventlabel="monika_example_topic1",        #引用的label名称
                category=["Submodding"],                   #所在的分类
                prompt="I want tell you something...",     #显示的名称
                Random=True                                #是否随机解锁
            )
        )

label monika_example_topic1:                               
    m 1eua "Hey,Can you hear me?"                          
    m 2eua "I have a little something to say to you.{w=0.4}.{w=0.4}."
    m 3eua "I love you!"
return                                                     
"""


        store.mas_utils.trywrite(
            os.path.normcase(renpy.config.basedir + "/characters/Monika Example Submod.rpy"),
            monika_stod_code
        )
return

label monika_stod_007code:
    python:
        monika_stod_code = """\
init -990 python:
    store.mas_submod_utils.Submod(
        author="Monika",
        name="Monika's example submod",
        description="I love you.",
        version='1.0.0'
    )

init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Monika's example submod",    #子模组的名称
            user_name="PencilMario",             #github用户名
            repository_name="MonikaExampleSubmod",    #存储库名
            update_dir="",    
            attachment_id=None    
        )

init 5 python:
    addEvent(
            Event(
                persistent.event_database,          
                eventlabel="monika_example_topic1",       
                category=["Submodding"],                   
                prompt="I want tell you something..."
                random=True
            )
        )

label monika_example_topic1:                               
    m 1dsc "{w=0.7}.{w=0.7}.{w=0.7}."
    m 4ekb "Hey,Can you hear me?"
    m 1eka "I have a little something to say to you.{w=0.4}.{w=0.4}."
    m 3hubsb "I love you!"
    $_history_list.pop()
    menu:
        "I love you!{fast}"
        "I love you too!":
            if mas_isMoniEnamored(higher=True):
                m 1hubsb "I~~~~~~~~ Love~~~~~~~ You~~~~~~~!"
            elif mas_isMoniNormal(higher=true):
                m 1hublb "Full of expectation~"
            else:
                m 1hua "..."
        "...":
            m 1rfsdlp "..."
    m 1dsc "{w=0.7}.{w=0.7}.{w=0.7}."
return                                                     

"""


        store.mas_utils.trywrite(
            os.path.normcase(renpy.config.basedir + "/characters/Monika Example Submod.rpy"),
            monika_stod_code
        )
return


label monika_stod_006code:
    python:
        monika_stod_code = """\
    m 1dsc "{w=0.7}.{w=0.7}.{w=0.7}."
    m 4ekb "Hey,Can you hear me?"
    m 1eka "I have a little something to say to you.{w=0.4}.{w=0.4}."
    m 3hubsb "I love you!"
    $_history_list.pop()
    menu:
        "I love you!{fast}"
        "I love you too!":
            if mas_isMoniEnamored(higher=True):
                m 1eua "I~~~~~~~~ Love~~~~~~~ You~~~~~~~!"
            elif mas_isMoniNormal(higher=true):
                m 1eua "Full of expectation~"
            else:
                m 1eua "..."
        "...":
            m 1eua "..."
    m 1dsc "{w=0.7}.{w=0.7}.{w=0.7}."               

"""


        store.mas_utils.trywrite(
            os.path.normcase(renpy.config.basedir + "/characters/Monika Example Submod.rpy"),
            monika_stod_code
        )
return
