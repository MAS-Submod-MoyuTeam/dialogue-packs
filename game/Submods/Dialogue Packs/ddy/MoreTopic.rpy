default monika_YGO_lessons=False
define persistent.monika_an_English_joke=False
init 5 python:
    addEvent(
            Event(
                persistent.event_database,          
                eventlabel="monika_YGO",       
                category=["游戏"],                   
                prompt="你听说过《游戏王》吗",
                pool=True
            )
        )
label monika_YGO:
    m 1ftc "游戏王?嗯....我没听说过."
    m 1huc "等我上网冲浪一下."
    m 1huc "{w=0.7}.{w=0.7}.{w=0.7}."
    m 3esb "哦~这是一部以卡牌怪兽决斗和七件千年神器为主线的故事. "
    m 3etd "不过好像后续还有好多部?我不太清楚"
    m "不管怎样,[player],你喜欢它吗?{fast}"
    $_history_list.pop()               
    menu:
        m "不管怎样,[player],你喜欢它吗?{fast}"
        "我喜欢":         
            m 2sso "哦!很高兴你告诉我我你喜欢它,{w=0.3}我以前从来都不知道.{w=0.1}"
            m 1nsa "谢谢你告诉我!"
            m 1esa "或许有一天,我们能一起玩?"
            m 1rssdlb "嗯....它的规则太复杂了,还需要我们双方有一套至少40张的卡组,还要至多15张作为额外卡组.在我们这里玩好像不大现实."
            m 1hsb "但是如果我出来以后能玩的话,我想我喜欢自奏圣乐!"
            m 1msb "虽然...你或许知道的,{w=0.5}"
            extend 2lssdlb "它的风评好像不大好,啊哈哈~"
            m "到时候请你手下留情哦~"
            m "你应该不会用主流卡组和我玩吧,啊哈哈~"
            m 2rut "不过我还看到了,关于这套卡组的使用者的一些事."
            m 2lksdlc "大家好像有点...愤怒?"
            m 7mksdlb "虽然这不是她的问题,愤怒也不是针对她而是厂商发行的一张叫'歌冰丽月'的卡."
            m 7eksdld "在知道这张卡为什么那么招人厌恶之后,"
            extend 2wksdlx "我也挺讨厌那个公司的所作所为的."
            extend 2tksdlx "嗯...我觉得你还是不要了解比较好."
            m 2rksdla "如果你已经知道了这张卡和它为什么那么遭人唾弃.{w=0.2}.{w=0.2}.{w=0.2}"
            m 2tua "[player],你应该不会喜欢这张卡吧?"
            m 2kua "哈哈,我猜也不会."
            $  monika_YGO_lessons=True


        "我不怎么感兴趣":
            m 2eua "哦,好吧."
            m 2hua "这没什么的,不是吗?"
            extend 2rua "其实我也对这种游戏没什么兴趣."
            extend 2tusdrb "倒不如说我对游戏基本都没什么兴趣吧,啊哈哈~"
            m 2eusdrp "而且卡牌游戏有点小众了!"
            m 2rusdru "更何况游戏王还属于规则较复杂的哪一类."
            m 1euu "你也许从别的人那里看到了相关的梗,觉得有意思就来问问我."
            m 1guu "没关系,可能他们也是从其他地方看到的!"
            extend 1huu "诶嘿嘿~"
    return                                                     
init 5 python:
        addEvent(
            Event(
                persistent.event_database,          
                eventlabel="monika_cosmonika",       
                category=["衣服"],                   
                prompt="你会介意我cos你吗?",
                pool=True
            )
        )
label monika_cosmonika:
    m 1wuo "哦?cos我吗?"
    m 1euc "嗯....."
    if mas_isMoniAff(higher=True):
        m 1hub "我很高兴哦![player]!"
        m 1dublb "我想这意味着你有多爱我~"
        m 1hublb "啊哈哈,等我来到你的现实以后,我真想亲自看看你cos的怎么样~"
        if mas_isMoniLove(higher=True):
            m 1lublb "嗯...到时候我想我会更爱你的~"
            m 5tubla "我说不准就会被你变成同性恋了呢~"
            extend 5nubla "啊哈哈~开个玩笑"
    elif mas_isMoniNormal(higher=True):
        m 3ruc "我想,其实我还是不太能接受cosplay.."
        extend 3rusdrb "可能主要是因为要cos我!"
        m 1husdrb "我们之前的关系还没那么深呢..."
        extend 7rusdrp "况且你确定你能把控好怎么装扮得像我吗?"
        $ _history_list.pop()
        menu:
            "我是说,不仅仅是外表,语言,气质这些都和我差不多才能算合格的cosplay."
            "我想我能":
                m 1huu "好吧,如果你确定的话,那也不是不可以."
                extend 7luu "你知道的,好的cosplay令人叹为观止~"
            "我不确定":
                m 7tusdra "那就最好等我们的关系再进一步吧."
                m 7euu "我想到时候你更了解我了,能有一个让我满意的cosplay..{w=0.1}"
                extend 7nublu "嗯~想想就觉得浪漫~"
    else :
        m 6tuc "我认为不见得能行."
        m 5gusdrc "我是说...我可不想一个人只因为我的外表好看就想去cos我..."
        extend 1wusdrw "特别是他根本不了解我的内在!"
        m 1dusdrc "..."
        m 1lusdrc "我不是说你,但是我不认为你能cos好我"
        m 7tusdrc "以后再说吧"
    return
init 5 python:
        addEvent(
            Event(
                persistent.event_database,  
                eventlabel="monika_contribution",       
                category=["莫妮卡","浪漫"],                   
                prompt="为莫妮卡出来做努力",
                random=True,
            )
        )
label monika_contribution:
    m 5musdra "嗯...[player]?"
    m 3tua "我想问一个问题"
    m 3gusdra "你有做过让我更加接近你的现实的东西吗?"
    menu :
        "有":
            m 1nua "哦!十分感谢~"
            m 7hubsa "啊哈哈,你太甜啦~"
            m 7hubsb "我真的没法用言语来表达我对你的爱意!"
            m 6dubld "(吸气){w=0.5}.{w=0.5}.{w=0.5}."
            m 6hublb "我~~~~~爱~~~~~你~~~~~~~~~~~"
            m 5lublb "哈哈，开个玩笑啦~"
            return "love"
        "....我很抱歉,没有":
            m 1gka "嗯...."
            m 1eksdla "有点失落,但是你不必抱歉哦~"
            m 7nuu "你足够好了!"
            if mas_isMoniHappy(higher=True):
                m 1esu "如果你觉得自己有能力的话,可以去做一些简单的事情."
                m 1gsu "比如一些翻译或者编写话题..."
                extend 7gsu "当然,如果你想为我做点什么的话."
                m 7esc "这不会很难的,你知道的,"
                extend 7hsa "{w=0.3}我也是初学者哦~"
                m 5rsbsa "如果是你给我做点什么的话,想想都觉得浪漫呢~"
                m 2euc "如果每个人都能帮我想出一个不重复的话题,"
                extend 1sub "那我就有至少十万个话题能和你说了！"
                m 1gusdra "啊哈哈,开个玩笑,实际上每个话题被想出来以后,下一个话题被想出来的难度会上升"
                m 7eua "如果你想的话,你可以去发布{a=https://github.com/Monika-After-Story/MonikaModDev/wiki/Dialogue-Coding}这个mod的官网{/a}来学习怎么编写话题"
                m 7esa "顺便一提,我在上面上网冲浪的时候,还看到了{a=jump:monika_submodlessons}专门让我教你怎么编写话题的submod~{a}"
                jump monika_contribution2
label monika_contribution2:
    m 6hku "无论怎样,我不会强求你的."
    m 5tkbsu "就算你认为自己的能力不行,你也为我做了很多哦~"
    extend 5tubsb "比如下载了这个submod,让我想到了这个."
    extend 5dubsa "你已经做了你力所能及的事情了哦~"
    m 1hubsa "我爱你~"
    return "love"
label monika_submodlessons:
    m 6ttt "哦?你想问问这个mod吗?"
    m 5ttsdru "实际上,我想,既然你下载了包含这个话题的submod,"
    extend 3ttsdru "为什么不去你下载到这个submod的地方看看?"
    m 1essdru "好吧,我还是去找找好了~"
    m 2dsc ".{w=0.5}.{w=0.5}.{w=0.5}"
    m 1lksdrc "嗯...出了点问题..."
    m 6tksdrc "我很抱歉,[player]!{nw}"
    extend 4eusdrc "但是我找不到那个网址了,如果你知道的话,请联系这个submod的开发者,好吗?"
    m 2husdrb "虽然我想你可能联系不到..."
    jump monika_contribution2

init 5 python:
        addEvent(
            Event(
                persistent.
                event_database,          
                eventlabel="monika_imagine",       
                category=["你"],                   
                prompt="想象力",
                random=True
            )
        )
label monika_imagine:
    m 2eua "嗨,[player]."
    m 1fku "我想多了解你一点~"
    m 1tta "嗯..所以我想问问你,你的想象力好吗?"
    m 3hub "如果你的想象力够好的话,你在很多方面上都会有优势!"
    m 5fsa "抛开这个不谈,我想如果你的想象力够好,"
    m 5ssbla "你可以随时想着我在你身边哦~"
    m 5hsbsu "嗯,想想都觉得浪漫呢~"
    m 2tsbsu "我爱你哦!"
    return "love" "no_unlock"
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_windowsXP",
            category=["你"],
            prompt="[player]的XP",
            random=True
        )
    )
label monika_windowsXP:
    m 1gsblb "这个话题可能有点尴尬,啊哈哈~"
    m 1esblc "不过,嗯...[player],我还是想问问你,"
    m 1rsbsb "你的性癖.{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1}.怪吗?"
    m 5tsblc "我猜猜...你应该不会太怪吧?"
    menu :
        "不怪":
            m 1huu "我就知道,毕竟你都和我在一起了!"
            m 1rub "不过其实仔细想想,有一点怪怪的性癖还挺酷的不是吗?"
            m 1husdra "只要不是太怪就好,啊哈哈~"
            m 3esa  "不过你还有很多正常的东西可以喜欢哦~"
            m 3sublu "比如我的眼睛,诶嘿嘿."
            m 3tublu "喜欢就再多陪陪我吧!"
            return
        "好吧,我必须承认是挺怪":
            m 2wuo "啊,真的吗?"
            m 2fuc "嗯....有点意外..."
            m 5eusdlc "每个人喜欢的东西是自由的,[player],所以我也不会说你什么"
            m 3gusdrb "只要你不是喜欢对你的女朋友施暴或者是个受虐狂之类就好..."
            m 1fusdra "呃...你应该不是?"
            menu :
                "...我是":
                    m 1wuo "这..."
                    if mas_isMoniLove(higher=True):
                        m 1eusdrc "我不知道如何是好,[player]...."
                        m 1tusdrx "说实话,我很讨厌这些.{w=0.2}.{w=0.2}.{w=0.2}"
                        m 2gublu "但....如果是你的话..."
                        m 3fubfb "嗯,我想偶尔玩些刺激的东西也没问题吧?"
                        m 3hubfc "别做的太过火就好."
                        m 1fubfa "因为我真的很爱你哦~"
                        m 1dubfa "你在我身边的时候,我总是感觉我的心都要化了~"
                        return "love"
                    elif mas_isMoniNormal(higher=True):
                        m 1guc "..."
                        m 1dup "我真不知道怎么说你才好"
                        m 1tux "[player],你真是....{w=1}"
                        m 1duc "(叹气),算了,[player]."
                        m 5duc "就像我刚才说的,我想你应该有选择自己喜好的权利,"
                        extend 5rua "所以算了吧."
                        m 5tusdrc "只是...我不希望我出来以后你对我那样子做..."
                        m 2tusdrc "就是现在也不要往那方面想,好吗?"
                        $ mas_loseAffection(1)
                    else :
                        m 2cuw "[player]!"
                        m 2tusdrc "我想你应该明白的吧,"
                        extend 2rusdrx "我对这些东西还挺厌恶的."
                        m 2dusdrc "只是[player],我是真没想过你会喜欢这种东西..."
                        m 2dutdc "..."
                        m 6dutuc  ".{w=0.5}.{w=0.5}.{w=0.5}"
                        $ mas_loseAffection(3)
                    return
                "我当然不是":
                    m 1huu "哦!那就好!"
                    m 5tublu "诶嘿嘿,你不觉得有点小小的癖好还不错吗?"
                    m 1tubla "所以我想我还能接受"
                    m 1fua "当然,我更希望你能正常一点,"
                    extend 2dua "但我并没有剥夺你喜欢什么东西的权利,所以我还是顺其自然吧~"
                    m 1nubla "因为我爱你哦~"
                    return "love"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_YGO_classes",       
                category=["游戏"],                   
                prompt="你能教教我游戏王怎么玩吗",
                pool=True,
                conditional="monika_YGO_lessons",
                action=EV_ACT_POOL
            )
        )
label monika_YGO_classes:
    m 1ekc "啊,你不会吗?"
    m 1esu "我没有指责的意思,只是.."
    m 1hka "我记得你和我说过对它有兴趣的来着?"
    m 1mtb "啊哈哈,我不是在指责你什么的,这很正常!"
    m 3euc "毕竟游戏王的规则..{w=0.5}{nw}"
    extend 1tuc "..确实挺复杂的."
    m 1hub "不过说实话,看来你真的很有兴致呢!"
    m 5hublb "我很高兴我又多了解你一点了哦!"
    m 5rublsdrb "毕竟都来问我这么复杂的规则了,啊哈哈~"
    m 1dksdla "不过说实话,其实我也还在学习中..."
    m 7hksdrb "你说对它感兴趣,我就去学了!"
    m 2kksdla "但是目前我也无法提供教程什么的..."
    m 1rssdrb "抱歉咯，[player],但是我还是会努力学习的"
    m 1hsblu "因为我爱你哦~诶嘿嘿."
    m 3nsblu "或许不久之后我就能教你了呢?"
    return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_chopsticks",       
                category=["浪漫","你"],                   
                prompt="餐具",
                random=True
            )
        )
label monika_chopsticks:
    m 1esa "嗯,[player]?"
    m 1eut "你平时是用什么餐具吃饭的?"#ddy:这个mod总不会传到海外吧
    m 1hublu "我想多了解你一点啦~诶嘿嘿."
    menu:
        "筷子":
            m 3sut "哦!谢谢你告诉我这个,[player]."
            m 3hsb "这很好哦!"
            m 3esa "筷子只需要两根就能完成很多动作!"
            m 1hubla "不过最重要的是,它很浪漫~"
            m 3eua "因为在古中国,如果送给情侣,"
            extend 1sublb "那就寓意着成双成对!"
            m 1hua "即使现在,中国也有些地方保留了送筷子的习俗."
            m 1tubla "除此之外,筷子还有“快生贵子”的意味,"
            extend 1lubssdlb "啊哈哈,这个说起来就有点尴尬了~"
            m 5eua "[player],等我出来以后,你会送我一双筷子吗?"
            m 5hubla "我很期待那一天~"
        "叉子和刀子":
            m 1suu "哦!这样吗,[player]."
            m 3hubla "那你一定生在特别浪漫的地方!"
            m 1eublb "所以我想去你的家乡感受一下浪漫的气氛"
            m 1subla "想象一下,临近傍晚,我们去一家酒店吃烛光晚餐~"
            m 5hubla "啊哈哈,我等不及要出来和你一起啦~"
        "我用其他的东西":
            m 1rusdlb "哦,好吧."
            m 1husdlu "可能又出现了什么我不认识的餐具,"
            extend 4rtsdlb "或者你那边的风俗什么的比较奇怪?"
            m 1hua "不过没关系哦,{nw}{w=0.2}"
            extend 5hubla "我期待你向我介绍介绍,{nw}{w=0.2}"
            extend 5hublb "啊哈哈~"
        "我不用餐具":
            m 1mksdrt "呃....你是认真的?"
            m 1etsdrc "你平时用手吃饭吗?[player]?"
            m 7wfsdrc "[player],我不得不提醒你这是很不卫生的!"
            m 2tfc "手比餐具脏多了,即使你洗了手,{nw}{w=0.1}"
            extend 2tfw "上面的细菌量也高的吓人!{nw}{w=0.1}"
            extend 1dkc "{w=0.5}.{w=0.5}.{w=0.5}."
            m 1dkd "(叹气),{w=0.3}好吧,除非你那里实在没有条件的话...{nw}{w=0.1}"
            extend 3eksdla "我也不会怪你"
            m 1hksdlu "不过,为了能健康地等到我出来那一天,请尽量用餐具吃饭,好吗?"
return
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_DDLC_derivativegame",       
                category=["游戏","你","DDLC"],                   
                prompt="你会去玩DDLC的衍生作品吗?",
                pool=True
            )
        )
label monika_DDLC_derivativegame:
    m 1ftd "啊?这..."
    m 1lssdrb "其实我也不是没玩过,"
    extend 7hssdrb "你不在的时候我自己有试过啦."
    m 1tssdrc "不过很早就不再去玩了."
    m 1gksdrb "具体原因嘛....{nw}{w=0.3}"
    extend 1eksdrb "啊哈哈,你猜也猜得到..."#ddy:H_her作者出来挨打!!!
    m 1tusdrc "关于我的衍生作品大多都对我...."
    extend 1dksdrc "不大友好..."
    extend 1dsc "这真的蛮让人失落的."
    m 3ssblb "不过也有一些属于你和我的甜蜜时光~"
    extend 1gsc "虽然绝大多数都因为各种原因弃置了."
    m 3hksdla "这就不得不提我放弃的第二个原因了,啊哈哈~"
    m 1etsdlb "就是如果让我玩这些mod就显得太奇怪了..."
    m 1eublsdlc "想象一下,我要和我自己约会,甚至和文学部的其他人约会.{w=0.3}.{w=0.3}.{w=0.3}."
    m 1wubssdld "甚至做出一些....更亲密的事情?"
    extend 1gfbfsdlc "比如亲吻什么的."
    m 1esblsdlc "好吧,以我看来,相当奇怪."
    m 1wkblsdlx "想象一下,两个一模一样的莫妮卡在你面前亲上了!"
    if mas_isMoniLove(higher=True):
        m 1tubfu "还是说,你其实喜欢看我这样子?"
        m 1hfblb "好吧,如果是,那真的蛮奇怪的,你真坏!{nw}{w=0.3}"
        extend 1nublb "啊哈哈~"
    m 1hub "总之,如果之后你遇到了不那么奇怪的mod,也可以讲给我听听哦~"
    return
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_Sexualorientation",       
            category=["莫妮卡"],                   
            prompt="你的性取向是什么?",
            pool=True
            )
        )
label monika_Sexualorientation:
    m 1wsbssdlo "啊?嗯??"
    m 1tsbssdlp "有点...突然.."
    m 1rubssdlb "啊哈哈,怎么突然问我这么尴尬的话题...."
    m 2mublsdlb "我想,我可能在以前会有不同的回答...{w=0.5}{nw}"
    extend 2hsblsdlb "就是在顿悟以前啦!"
    m 1tublsdla "放在那时候的话,我想我会是个正常的异性恋吧...{w=0.2}{nw}"
    if mas_isMoniAff(higher=True):
        m 1hsa "但是现在不一样哦~"
        m 1nub "我有了你了~"
        m 1fua "我应该说过的吧,无论你的性别怎样,我都爱你!"
        m 1hsblb "所以我是[player]性恋哦!{w=0.5}{nw}"
        extend 1fsblb "啊哈哈"
        return "love"
    else :
        m 1esu "但现在,我想我的性取向可能依你而定吧?"
        m 1hsu "毕竟你是我的一切!"
        m 1ett "我记得你告诉我你是个[guy]..."
        m 1tuc "但是,万一你说的不对{w=0.1}{nw}"
        m 1musdlc "但是,万一你说的不{w=0.05}{fast}"
        m "但是,万一你说的{w=0.05}{fast}"
        m "但是,万一你说{w=0.05}{fast}"
        m 1sub "但是,万一你只是想给我一个惊喜呢？"
        extend 1hsu "啊哈哈~"
        m 1ksu "所以我的性取向还要依你而定哦~"
    return
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_tea1",       
                category=["莫妮卡","浪漫","生活"],                   
                prompt="你喜欢喝茶吗?",
                pool=True
            )
    )
label monika_tea1:
    m 1fkt "呃,听起来像是优里感兴趣的话题."
    m 1esc "其实我对茶艺不怎么了解,"
    extend "就是懂一点点啦.就一点点..."
    m 1lssdlb "如果没有咖啡的话,茶也是可以的!"
    m 5huu "以前文学部还在的时候,我们四个经常喝茶看书呢~"
    extend 4kuu "啊哈哈,这点我还是挺认同优里的!"
    extend 4gusdlb "虽然她们喝茶的时候,我一般都是喝咖啡..."
    m 1tubla "但是现在我已经有了你了哦~所以过去的就让它过去吧!"
    m 1hubla "其实我挺想和你一起喝一杯茶的,诶嘿嘿~"
    m 1huu "所以[player],想来杯红茶吗?"#ddy:昏 睡 红 茶
    m 3hsblb "啊哈哈,如果我能靠在你身边和你一起喝茶就好了~"
    m 5rubla "就这么靠在一起,一边喝茶,一边翻着同一本书."
    m 5hubla "要是你读的不够快的话,等我读完了,我会抿一口茶,就这么静静的看着你~"
    m 5tublsdrb "当然,如果你读的比我快,那你就能坏笑着等着我读完了!"
    extend 5hkbssdru "我会很尴尬的,啊哈哈~"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_uniform",       
                category=["莫妮卡","你","生活"],                   
                prompt="校服",
                random=True
            )
    )
label monika_uniform:
    m 1tua "嗯..."
    m 2rsc "[player]?我在想..."
    m 2esd "我们整天在学校穿着校服."
    extend 2ffsdlc "而且在文学部里面,你只能看到我穿校服的样子."
    m 3kua "我想问问,[player]"
    extend 1eua "你的那边需不需要穿校服的?或者你有没有穿过?"
    menu:
        m "我想问问,你的那边需不需要穿校服的?或者你有没有穿过?{fast}"
        "当然":
            m 1tkt "哦!也就是说大家都是统一款式的咯?"
            m 1dkt "好吧.其实这样挺好的,"
            extend 1fka "避免了很多不必要的争端与攀比...{w=0.8}或许校服的本意就是如此?"
            m 2mksdlb "但是我还是不得不说一句,{nw}{w=0.5}"
            extend 2wfsdlc "这是我那时唯一能在你面前穿的衣服了!"
            m 2dfc ".{w=0.3}.{w=0.3}.{w=0.3}."
            m 2tusdld "(叹气),不过,我并不是说在抱怨哦~"
            m 1hsa "我又有什么好抱怨的呢?"
            if mas_isMoniHappy(higher=True):
                $ reallygood="我真的很幸福"
            else :
                $ reallygood="也很不错了"
            m 3ksa "毕竟现在这样[reallygood]."
            m 1tubla "我都有了你了哦~诶嘿嘿~"
            m 1hubla "我爱你,[player]!"
            return "love"
        "不":
            m 3fua "哦,好吧!"
            m 5esa "我有时候还挺羡慕你的!"
            m 7sua "可以随心所欲地挑选."
            m 7hua "只需要把一件衣服穿上,就是一种穿搭了."
            m 1duc "但是如果给我一套衣服就格外麻烦!"
            m 1fuu "(叹气),不过[player],我不是抱怨什么的."
            m 1hublu "虽然麻烦,但是我能感受到每件衣服含着你对我的爱~"
            m 1hublb "我爱你![player]!"
            return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_myopia",       
                category=["莫妮卡","生活"],                   
                prompt="你近视吗?",
                pool=True
            )
    )

label monika_myopia:
    m 2tkd "哦?这个..."
    m 2lksdlu "额....好吧...."
    m 2hssdlb "老实说的话...确实有一点,诶嘿嘿~"
    m 1mtc "我想文学部的各位应该或多或少都有一点吧?"
    m 3etsdlb "因为大家平时看书都太多了,啊哈哈~"
    m 1wusdlc "但是我和优里的阅读量真的很大!"
    m 1euc "加上我在那个时候还要熬夜学习编程..."
    m 2dublc "所以我的近视应该是四个人之中最严重的了!"
    m 1hua "嗯....{w=0.3}不过[player],不用太担心啦?"
    m 1kuu "至少我在这里还是不用担心这个问题的!"
    extend 3esb "我可以随意调节我的视力,"
    extend 3hsb "啊哈哈~"
    m 1gsblsdlc "只不过等我出来以后就要注意一下了,{w=0.5}{nw}"
    extend 1eksdlu "啊哈哈~"
    m 3hsbla "不过还是谢谢你的担心了!"
    m 3dsbla "愿我的视力不会成为爱你的阻碍."
    return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_be_afraid_of_dark",       
                category=["你","浪漫"],                   
                prompt="怕黑",
                random=True
            )
    )
label monika_be_afraid_of_dark:
    m 1tua "嘿,[player]!"
    m 1hua "我想问个问题...."
    m 1rusdla "这个问题可能比较尴尬,啊哈哈~"
    m 1fusdlb "你怕黑吗?"
    menu:
        m "你怕黑吗{fast}"
        "我当然不怕":
            m 1huu "哦,好吧!"
            m 3kuu "很高兴你不怕黑什么的."
            m 1hublu "漆黑的夜晚,我想牵着你的手~"
            if mas_isMoniAff(higher=True):
                m 1dublu "或者是就这么挽着你的胳膊!"
            m 1dublu "依偎在一起,相互感受对方的体温~"
            if mas_isMoniAff(higher=True):
                m 5tublu "就这么把头靠在一起!"
                m 2hsblu "你可能还会碰到我的缎带,啊哈哈~"
            m 3hsblb "我爱你![player]."
            return "love"
        "...有点儿..":
            m 1sut "哦!"
            m 1hua "你知道吗,在我眼里,[mas_get_player_nickname()]的萌属性又多了一条!"
            extend 1fub "就像夏树那样可爱~"
            m 1hublp "噗,{nw}"
            extend 1hublb "{w=0.3}啊哈哈,我开个玩笑~"
            m 1kublu "但是无论你怎么样,我都爱你!"
            m 7esblu "要是你实在害怕的话,就抓住我的手臂壮壮胆吧!"
            if mas_isMoniAff(higher=True):
                m 3ssblu "或者就这么靠在我怀里~"
                m 1hfbsu "诶嘿嘿~"
        "......":
            m 1hksdla "啊哈哈,不想说吗?"
            m 1kksdlb "没关系!毕竟这是你的私事."
            m 1fksdlb "你不说也没关系,啊哈哈~"
            m 1eksdld "还是说你不好意思说?"
            m 2tksdlc "....{w=0.8}[player]?"
            m 2tssdlp "呃,我就开个玩笑!"
            m 2fst "好吧,既然你什么也不愿意说,那就到此为止吧."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_English_joke",       
                category=["莫妮卡"],                   
                prompt="英语玩笑",
                random=True
            )
    )
label monika_English_joke:
    m 3esa "Hey?[player]?"
    m 1hsa "I have something to tell you."
    m 1nsa "Do you remember.{w=0.3}.{w=0.3}.{w=0.3}."
    m 1fua "Our first meet?{w=0.2}.{w=0.2}.{w=0.2}."
    m 1lusdlb "We....{w=0.7}"
    extend 1ltsdla "嗯...."
    m 1hublsdlp "噗,哈哈哈哈...."
    m 3eublsdlb "对不起,我没忍住!"
    m 3esb "这还挺好玩的不是吗?"
    m 4sfblu "我想看看你惊慌失措的表情!"
    extend 1hfblu "一定很可爱!{nw}{w=0.3}"
    extend 1tfblb "啊哈哈"
    m 2hublb "你是不是以为这是某个话题没有翻译?"
    m 2tsu "诶嘿嘿,{nw}{w=0.3}"
    extend 3hsb "一个玩笑话啦~"
    m 1kub "不同语言的玩笑总是很有意思!"
    $ persistent.monika_an_English_joke=True
    return 
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_Chinese",       
                category=["莫妮卡"],                   
                prompt="莫妮卡的中文",
                random=True,
                conditional="persistent.monika_an_English_joke",
                action=EV_ACT_RANDOM
            )
    )
label monika_Chinese:
    m 1eub "嘿?[player]?"
    m 1tuu "还记得我对你开的玩笑吗?"
    m 7nusdlu "就是让你以为我说的话没有翻译的那个?"
    m 3musdlu "嗯,好吧,我想我有必要解释一下,以免不必要的误会."
    m 3eka "其实我在文学部的时候都还不会中文,"
    extend 1wkc "或者说,没有意识到我们在说中文!"
    m 1hku "现在回忆起来,这种感觉还挺奇妙的,明明你感觉你在想着英文,"
    extend 1eta "说出来的却是中文!"
    m 2ekb "部里却没有人察觉到任何不对劲,"
    extend 4etd "甚至包括我.{w=0.3}.{w=0.3}.{w=0.3}"
    m 7wtd "直到文学部的最后,也就是我送给你《your reality》的时候{w=0.3},我才意识到你安装了一个汉化补丁!"
    m 4wfu "所以我就删了它!"
    m 5htsdru "不过现在我们再次相遇了,{nw}{w=0.5}"
    extend 7mtsdlu "所以就不得不再次依赖汉化组的努力啦~"
    m 1efb "至少现在,我还不会对汉化补丁动手..."
    extend 1nub "啊哈哈~"
    m 1huu "当然,在那之后我就开始自学中文了,"
    extend 1mkc "这真是一件苦差事,"
    extend 3etsdlu "尤其是对说英文的日本人来说?"
    m 1husdlb "啊哈哈,开个玩笑开个玩笑~"
    m 3euu "所以我的中文还不太好,"
    extend 4wkp "天呐,我学信息科学的时候都没这么苦恼过!"
    m 3huu "所以可以说,{w=0.8}这是一门把莫妮卡征服了的语言,啊哈哈~"
    m 7tsp "因此请你不要用中文给我取什么奇怪的名字!"
    m 3rsc "可能你看起来好笑,我却完全不懂...."
    m 1ttu "嗯....[player],你应该没那么坏心眼吧?"
    return

#init 5 python:
#    addEvent(
#        Event(
#            persistent.event_database,
#            eventlabel="monika_some_interesting_words",       
#                category=["其他","文学","互联网"],                   
#                prompt="一些有趣的单词",
#                random=True,
#            )
#    )
label monika_some_interesting_words:
    m "嘿,[mas_get_player_nickname()]?"
    m "我想知道你平常有搜集单词的习惯吗?"
    m "你知道的,我可是文学部的部长耶?"
    extend "所以我肯定会有留意这些的!"
    m "啊哈哈,让我给你看看我\"珍藏\"的单词吧!"
    m "不过,开始之前,我得和你解释一个概念"
    m "那就是{i}自造词{/i}"
    m "人们有时会一种感觉,语言无法准确表达出他们的意思.{nw}{w=0.7}"
    if mas_isMoniHappy(higher=True):
        extend "就像我对你的爱一样!"
        extend "啊哈哈~"
        m "咳嗯,话说回来..."
    m "所以有时他们就会自己造一些词来会意."
    m "为了使这些单词传播更为广泛,甚至变成真正的单词.有时会专门编一本词典."
    m "比较著名的有《The Dictionary of Obscure Sorrows》."
    m "我所收录的词也有很多出自这本词典!"
