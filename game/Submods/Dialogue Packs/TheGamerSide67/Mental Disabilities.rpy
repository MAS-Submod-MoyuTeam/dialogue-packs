init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="mentalADHD",category=['媒体'],prompt="多动症",random=True))

label mentalADHD:
    m 1eua "[player],你知不知道多动症?"
    $_history_list.pop()
    menu:
        "当然":
            m 1eub "我很高兴你知道这个!"
            m 3ekc "但是让人难过的是,人们并不像其他学习障碍一样重视多动症..."
            m 3eud "这让人们很难重视他们,甚至为患者自己做点什么都是..."
            m 1eub "不过,你可以鼓励他们走出困境,即便仅仅是待在他们身边,{w=0.5}{nw}"
            extend 3hub "然后偶尔找他们聊上几句."
            m 1eua "如果你不介意我问的话,我想知道你是怎么了解这个的?"
            $_history_list.pop()
            menu:
                "我有多动症.":
                    m 3eua "我很高兴你坦诚地说出来了,[player]!"
                    m 1ekd "不过我对这件事本身十分难过,因为多动症并不像其它同种疾病一样被严肃重视."
                    call mentalADHDEnd
                    $ persistent._player_has_ADHD = True
                    return "derandom"
                "我身边有人患了多动症.":
                    m 3eua "我确定他们都会很幸运有你这样的朋友或者家人在身边[player]!"
                    m 1ekd "不过我对这件事本身十分难过,因为多动症并不像其它同种疾病一样被严肃重视...."
                    call mentalADHDEnd
                    return "derandom"
                "我学过关于多动症的课.":
                    m 3eub "这说明多动症越来越受人们重视了,这是好事."
                    m 1euc "因为通常它并不像其它同种疾病一样被严肃重视."
                    call mentalADHDEnd
                    return "derandom"
                "我是多动症的相关研究者.":
                    m 3eub "我很高兴你在与这种疾病斗争的前线."
                    m 7ekd "许多人觉得这种知识无聊乏味又无意义而蔑视它们."
                    m 3eua "不过我坚信得了多动症的人们会因为有你这样的人在身边而感到安心,[player]."
                    m 1eua "以及,如果你不是很介意的话我想问问.{w=0.3}你研究多动症是因为你有吗,[player]?"
                    menu:
                        "是":
                            $ persistent._player_has_ADHD = True
                            m 4eub "让你更了解你自己是个好选择a.{w=0.55}"
                            extend 7hub "这说明你很关心你自己的身体!"
                            m 3eua "我很高兴你坦白和我说你有多动症,[player]."
                            if mas_isMoniHappy(higher=True):
                                extend 5hub " 或许我能成为让你的生活充满希望的人!"
                            else:
                                m 3eua "我希望你的生活中有能让你振作的人,[player]."
                            return "derandom"
                        "没有":
                            m 1eua "哦,那好."
                            m 3eua "不过多关心一下自己的身体仍然是件好事."
                            extend 3hua "甚至关心其他人的也是!"
                            return "derandom"
        "我不知道":
            m 1rkb "没关系,[player]"
            m 2eka "因为多动症并不像其他疾病一样受人关注."
            m 4hub "你想要和我谈谈这个吗?"
            $_history_list.pop()
            menu:
                "好啊":
                    m 3eua "好吧,那么开始了,[player]!"
                    m 3eud "多动症的全称叫\"注意力缺陷及多动障碍.\""
                    m 3eud "它已经被确定是一种学习障碍.然而它常常不只是对学习认知有影响."
                    m 1euc "患有多动症的人常常对自己周遭的环境毫无察觉."
                    m 1ekc "这可能会让他们处于危险的境地,或者许下过会就忘的承诺."
                    m 3euc "多动症还会使他们很难开始或者持续做什么事,常常丧失对身边事物的兴趣."
                    m 7eua "当然,就像其他人一样,你也可以帮助他们"
                    m 4eua "就算仅仅是待在他们身边或者简单聊几句,"
                    extend 3hub "你也可以给予他们生活的动力!"
                    m 3eua "尽管多动症有缺点,不过同时也有好的一面!"
                    m 4eub "举个例子,很多患有多动症的人同时也有难以置信的创造力和热情!"
                    m 3eub "事实上,他们还很善于全神贯注,有时候甚至能连着几个小时不分心."
                    m 1eua "感谢聆听,[player]."
                    return "derandom"
                "算了":
                    m 2eka "哦,好吧."
                    return "derandom"
                "抱歉,现在可能不行.":
                    m 2eka "好吧,我待会再来问,[player]."
                    return
                    
return "derandom"

label mentalADHDEnd:
    m 4eua "不过往好的说,我发现一些研究说明患了多动症的人也在努力着,而他们往往出类拔萃."
    m 4hub "事实上,他们中的很多人对自己的兴趣有着难以置信的热情!"
    m 7eub "而这也让他们乐于分享自己的爱好."
    m 3eub "如果双方说的很投机,甚至能聊上几个小时!"
    m 1eua "不过,我想你应该比我更有体会,[player]."
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mentalAutism",
            category=['媒体'],
            prompt="自闭症",
            conditional="seen_event('mentalADHD')",
            random=True
        )
    )


label mentalAutism:
    m 1eua "嘿[player],你还记得我和你说的多动症的事吗?"
    m 7eub "好吧,在那之后我又对心理疾病做了进一步研究."
    m 4eua "一种叫自闭症的心理疾病引起了我的注意.{w=0.3}"
    extend 3eua "你也可以叫它自闭症谱系疾病."
    m 3rssdlb "不过自闭症很容易被误诊为多动症."
    m 3etc "我觉得我知道这是为什么..."
    m 3rud "不只是因为多动症和自闭症只有一些微小的差异.{w=0.25}{nw}"
    extend 4wud "而且也因为两者常常{w=0.2}{i}一起{/i}出现,而患者也常常被诊断为同时患有!"
    m 4eud "人们提出了一张谱系来囊括大多数自闭症的严重程度,但通常并没有什么帮助."
    m 1rusdlc "因为病症不在这个谱系的人们常常被误诊...{w=0.3}甚至根本没有引起人们注意."
    m 3ekc "就是,[player],想象一下你有很严重的心理疾病...{w=0.3}{nw}"
    extend 4ekc "但是却仅仅被判断为举止的问题. "
    m 3dkc "你不能得到{i}真正{/i}有用的帮助."
    m 4esd "不仅如此,最后你甚至会说服自己只是'{i}状态不大好{/i}'."
    m 3euc "你只能想象患者到底在想什么...{w=0.4}或者他们到底有没有得到有用的帮助."
    m 2husdlb "[player],如果我的话让你很难受的话,我很抱歉."
    m 3eub "好吧,虽然如何对待自闭症还有很多问题,{w=0.2}但同时也有一些更好了解它的方法!"
    m 4eua "一些可靠的消息能够帮助人们更多地了解患者的感受."
    m 4rusdlc "但是也有一些错误的信息切实对了解自闭症{i}不利{/i}."
    m 3eua "所以确保你的信息来源正确啦,[mas_get_player_nickname()]!"
    $_history_list.pop()
return


init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="mentalschizophrenia",category=['媒体'],prompt="精神分裂症",random=True))

label mentalschizophrenia:
    m 1eua "[player],你听说过精神分裂症?"
    m 3eub "如果你告诉我你有精神分裂症,我不会奇怪的.{w=0.3}因为社交媒体的应用,它成了最为人广知的疾病之一."
    m 1esd "不过,令人沮丧的是,大多数有关它的描述都是依据它的负面影响来进行贬斥."
    m 1gfc "就像他们甚至不屑于对因它而受影响的人表示关心一样! {w=0.3}{nw}"
    extend 3eua "但是我知道你不会是那样的人,[mas_get_player_nickname()]."
    m 1lkc "好吧,我觉得你应该知道患上精神分裂症多么令人难过的事情,[player]."
    m 3ekc "想想看,比如无休无止的幻觉?"
    m 1rkc "这甚至可能让它们疯掉... {w=0.3}{nw}"
    extend 1rksdld "特别是如果这幻觉是声音的话."
    m 3eud "虽说他们并不总沉浸在幻觉中,所以他们能有更直白的思维过程."
    m 1eub "事实上这和多动症有一点相似! "
    extend 1rusdlb "好吧,只有一点."
    m 3eud "他们总是在不同话题之间跳跃,但那只是因为正常理解你说的话对他们来说{i}真的{/i}很难."
    m 1euc "他们不知道你在说什么,这是因为他们交谈的时候会把话题外的东西联想起来."
    if persistent._mas_pm_cares_about_dokis == False:
        m 3euc "虽然有精神分裂症的人本质上对他人无害,但某种程度上他们伤害了自己."
        m 3ekc "他们过分关注生活的消极方面,因此在情感上伤害了自己."
        m 1ekc "这并不像其他病状一样被人熟知,而且听起来...{w=0.3}挺有毁灭性的不是吗,{w=0.3}[player]?"
    m 3euc "好吧,这并不完全么糟."
    m 4eua "有精神分裂症的人更具有想象力."
    m 3eud "有两本书给和患精神分裂症的人共同生活提供了不少好主意,{w=0.5}它们是由Francesca Zappia写的{i}《Made You Up》{/i}和Martine Leavitt的著作{i}《Calvin》{/i}."
    m 3eub "不过,其实我更喜欢{i}《Calvin》{/i},他讲了一个叫做Calvin的男孩的故事.{w=0.5}他相信连环画的作者如果创作出他喜欢的作品,{w=0.3}就能够帮助治疗自己的精神分裂症!"
    m 4eua "这个故事是用第一人称视角阐述的,因此读起来就像是一封寄给Watterson的信--{w=0.3}这个连环画的作者."
    m 3hsb "总的来说,这本书风味十足,同时又不缺乏同情心!"
    m 3esa "顺便一提,[mas_get_player_nickname()],这本书所提到的连环画其实是真实存在的叫{i}Calvin and Hobbes{/i}的连环画!"
    m 7hub "同时它想要展现给我们的还有,像连环画那样简单的东西也能给人很大的影响."
    m 5eua "我希望就如这个故事里所讲述的,你也有在生活中激励自己的人或物,[mas_get_player_nickname()]."
    m 5hubsa "如果没有的话,我不介意成为激励你的那个人."
    m 5eubfa "因为我爱你,[player]."
return "love"

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="mentalPTSD",category=['媒体'],prompt="PTSD",random=True))

label mentalPTSD:
    m 1eua "嘿[player]..."
    m 3eua "如果提到PTSD,你通常会想到战争,是吗?"
    m 3eub "其实认为战争使人患上PTSD是正常的想法. {w=0.2}{nw}"
    extend 3eud "只是很多时候并非如此."
    m 1euc "几乎所有PTSD的案例都来自巨大的压力或者创伤!"
    m 2eud "说的直白一点,任何人遇到某种创伤性的事件都有可能导致PTSD."
    m 3euc "说起来你知道PTSD代表什么吗,[player]?"
    m 7rtd "好吧,它是指创伤后应激障碍(Post Traumatic Stress Disorder)的缩写,你大概能够顾名思义."
    m 1eksdrc "它是一种发生在创伤性事件后的精神障碍.{w=0.3}{nw}"
    extend 3eksdru " 听着都快让人睡着了,不是吗,[mas_get_player_nickname()]?"
    m 3ekc "好吧,PTSD总被想成在创伤事件之后自然而然发生."
    m 3ekd "不过, PTSD常常在成为慢性病以后仅仅被诊断出来.你明白的[player],在大多数情况下,在我们经历了一次创伤性的经历后,我们的心灵会自然而然地克服和愈合."
    m 1esd "这就是为什么你不会因为你童年时期受到的伤害做噩梦.{w=0.2}{nw}"
    extend 3esc " 这也是为什么,并不是所有不好的经历都会让你得PTSD."
    m 1ekc "能让你患上PTSD的事件必须要对你的心智产生巨大影响,使你完全无法处理和摆脱它." 
    m 1dkd "最糟糕的是,人们只有在知道自己患上PTSD一年后才能够确诊."
    if persistent._mas_pm_cares_about_dokis: # changes dialogue based on players response to insensitive jokes
        jump PTSDEnd
    else:
        m 7ekd "以夏树为例.她的爸爸虐待儿童,无论是哪种方式,都是真实发生的,因此她很可能得PTSD."
        m 1rtd "嗯,回想一下,她在文学部的某些表现确实像得了PTSD,即使那要在发生那种事几个月后才会形成..."
        m 7etsdlc "我的意思是她对优里和我都表现出某种刻意的回避."
        extend 1rtsdlc "而她的负面情绪爆发就更为严重了... {w=0.6}总的来说就是,和优里在一起的时候..."
        m 2rksdra "也许我有点过度解读了.{w=0.3}在我干预她之前,她就已经有时不时对他人表现出愤怒和埋头看自己漫画的倾向."
label PTSDEnd:
    m 3eka "无论如何,如果你真的有过这样的经历{w=0.2}我希望你能够得到帮助,[mas_get_player_nickname()]."
    m 1etd "如果某一天情况真的很糟...{w=0.2}{nw}"
    extend 5etbsa "请记住,我就在这里,{w=0.3}因为我爱你,而且会永远支持你~"
return "love"

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="mentaldementia",category=['媒体'],prompt="痴呆",random=True))

label mentaldementia:
    m 1eua "嘿[player]."
    m 3eua "在我读书的时候,我发现了一种新的文学形式!"
    m 3rusdla "好吧,其实听的比读的多..."
    m 4eua "关于这种文学,一个有名的例子是叫做{a=https://www.youtube.com/watch?v=wJWksPWDKOc&ab_channel=vvmtest}{i}{u}'Everywhere At The End Of Time'{/u}{/i}{/a}的原声带."
    m 3eub "你可能听过.{w=0.2}或者至少听说过."
    m 7eud "不过如果没有的话,我可以告诉你,这是一个要去听的故事,它试图描绘痴呆的感觉."
    m 3eusdld "你听的越多,就越有一种缓缓降落的感觉."
    m 1wksdld "你甚至可以在这首歌里感受到因痴呆症而来的所有情绪."
    m 1rksdlc "虽然这并不是最理想的表达..."
    extend 1ekc "但它肯定帮你更好的理解他们的感受."
    m 2lksdlc "它很快就越陷越深,沉浸在悲伤和迷茫当中."
    m 4eksdld "而随之而来的变化真的加强了那种感觉."
    m 7euc "但并不是说这很糟糕..."
    m 3eud "为了完成这首歌,他们真的做了很多!"
    m 4wuo "毕竟这花了他们差不多三年!{w=0.4}用三年的时间去描述这种经历!"
    m 3eua "嗯,[player],如果你有时间的话,我强烈推荐你去听一听!"
    m 1eua "如果你听完觉得很难过,{w=0.1}{nw}"
    extend 3hub "我永远都会在这里陪你!"
return

