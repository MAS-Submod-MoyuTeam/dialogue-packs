

#========================================添加节日================================================

init python :
    import store.mas_calendar as calendar
    import datetime
    from lunar_python import Lunar
    
    chuxid = Lunar.fromYmd(datetime.date.today().year-1,12,30)#去年除夕
    chuxi = chuxid.getSolar()
    lnewyear = Lunar.fromYmd(datetime.date.today().year,1,1)#今年的春节
    lny = lnewyear.getSolar()
    lnewyear2 = Lunar.fromYmd(int(datetime.date.today().year)+1,1,1)#明年的春节
    lny2 = lnewyear2.getSolar()
    yuanxiaod = Lunar.fromYmd(datetime.date.today().year,1,15)#元宵
    yuanxiao = yuanxiaod.getSolar()
    qingmingd = Lunar.fromYmd(datetime.date.today().year,2,23)#清明
    qingming = qingmingd.getSolar()
    duanwud = Lunar.fromYmd(datetime.date.today().year,5,5)#端午
    duanwu = duanwud.getSolar()
    zhongqd = Lunar.fromYmd(datetime.date.today().year,8,15)#中秋
    zhongq = zhongqd.getSolar()
    qxid = Lunar.fromYmd(datetime.date.today().year,7,7)#七夕
    qxi = qxid.getSolar()


    #添加日历
    calendar.addRepeatable("Arbor Day",_("植树节"),month=4,day=29,year_param=list())#添加日历    
    calendar.addRepeatable("Teachers Day",_("教师节"),month=9,day=10,year_param=list())  
    calendar.addRepeatable("Womens day",_("妇女节"),month=3,day=8,year_param=list())  
    calendar.addRepeatable("Labor day",_("劳动节"),month=5,day=1,year_param=list())  

    calendar.addRepeatable("Lunar New Yearn",_("除夕"),month=chuxi.getMonth(),day=chuxi.getDay(),year_param=[int(chuxi.getYear())])  #去年除夕
    calendar.addRepeatable("Lunar New Year",_("春节"),month=lny.getMonth(),day=lny.getDay(),year_param=[int(lny.getYear())])  #今年春节
    calendar.addRepeatable("Lantern Festival",_("元宵节"),month=yuanxiao.getMonth(),day=yuanxiao.getDay(),year_param=[int(yuanxiao.getYear())])  
    calendar.addRepeatable("Qingming",_("清明节"),month=qingming.getMonth(),day=qingming.getDay(),year_param=[int(qingming.getYear())])  
    calendar.addRepeatable("Dragon Boat Festival",_("端午节"),month=duanwu.getMonth(),day=duanwu.getDay(),year_param=[int(duanwu.getYear())])  
    calendar.addRepeatable("Tanabata Festival",_("七夕节"),month=qxi.getMonth(),day=qxi.getDay(),year_param=[int(qxi.getYear())])  
    calendar.addRepeatable("Mid Autumn Festival",_("中秋节"),month=zhongq.getMonth(),day=zhongq.getDay(),year_param=[int(zhongq.getYear())])  
    calendar.addRepeatable("Lunar New Year2",_("明年春节"),month=int(lny2.getMonth()),day=int(lny2.getDay()),year_param=[int(lny2.getYear())])  #明年春节


define submod_festival_zsj = datetime.date(datetime.date.today().year, 3, 12)#定义植树节
define submod_festival_teacher = datetime.date(datetime.date.today().year, 9, 10)
define submod_festival_women = datetime.date(datetime.date.today().year, 3, 8)
define submod_festival_labor = datetime.date(datetime.date.today().year, 5, 1)
define submod_festival_qingming = datetime.date(datetime.date.today().year, 4, 5) #2.23 清明



#-----------农历节日-----------
#春节.day-1 除夕夜
define submod_festival_lnr = datetime.date(lny.getYear(),lny.getMonth(),lny.getDay())#春节
define submod_festival_yuanxiao = datetime.date(yuanxiao.getYear(),yuanxiao.getMonth(),yuanxiao.getDay()) #1.15 元宵
define submod_festival_duanwu = datetime.date(duanwu.getYear(),duanwu.getMonth(),duanwu.getDay()) #5.5 端午
define submod_festival_7xi = datetime.date(qxi.getYear(),qxi.getMonth(),qxi.getDay()) #7.7 七夕
define submod_festival_zhongq = datetime.date(zhongq.getYear(),zhongq.getMonth(),zhongq.getDay())#8.15 中秋节
#明年春节

#===============================================================================

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="festival_zsj",
            prompt="植树节",
            category=["节日"],
            action=EV_ACT_PUSH,
            start_date=submod_festival_zsj,
            end_date=submod_festival_zsj + datetime.timedelta(days=1),
            years=[],
            pool=False
            )
    )

label festival_zsj:
    m 1eua "你知道吗?"
    m 3hub "今天是植树节!"
    m 3eua "在今天会有人宣传保护树木某些人还会去种植树木!"
    m 1eua "所以,[player], 你今天有没有参加植树活动?"
    menu:
        "所以, [player], 你今天有没有参加植树活动?"
        "有的.":
            m 1wua "真的吗?"
            m 3hub "这让我更为你骄傲了, [player]!"
            m 1hublb "如果我在你的旁边, 肯定会给你个大大的拥抱!"
            m 1hua "哈哈~"
        "没有":
            m 1rksdrb "哈哈..."
            m 2rksdra "我也知道不是每个地方都会有人植树的..."
            m 1ekb "但我并不因此讨厌你, [player]."
            m 5ekbla "我依然爱你."
return "love"



init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="festival_teacher1",
            prompt="教师节",
            category=["节日"],
            action=EV_ACT_PUSH,
            start_date=submod_festival_teacher,
            end_date=submod_festival_teacher + datetime.timedelta(days=1),
            years=[],
            pool=False
            )
    )

label festival_teacher1:
    m 3eub "[player], 你知道吗? 今天是教师节."
    m 4eub "在这天学生们会感谢老师, 并送一些东西."
    m 1rua "有贺卡, 画作..."
    m 1wuo "甚至还有水果和钱!"#就是眼睛瞪大嘴巴變O形狀的
    m 1rksdra "虽然大家送礼只是为了表达感激之情, 但还是有其他情况存在."
    m 2rsc "比如说, 某些家长会通过送礼的方式贿赂老师, 来保障自己孩子不会考不上高分什么的."
    m 1hksdlb "啊哈哈..."
    m 3eua "在我看来, 只要是带有感激之情的礼物, 就是对老师来说最好的礼物."
    m 1rksdlc "而不是通过价格来区分礼物的高低贵贱."
    m 3ekbla "而你送给我的礼物, 无论准备了多久, 我都会心怀感激的收下的."

return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="festival_women",
            prompt="妇女节",
            category=["节日"],
            action=EV_ACT_PUSH,
            start_date=submod_festival_women,
            end_date=submod_festival_women + datetime.timedelta(days=1),
            years=[],
            pool=False
            )
    )

label festival_women:
    m 1rup "嘿, [player], 你知道吗?" #就是=|这样的脸
    m 3eub "今天是妇女节."
    m 4eua "是在每年的3月8日为庆祝妇女在经济、政治和社会等领域作出的重要贡献和取得的巨大成就而设立的节日."
    m 1rksdla "虽然某种意义上, 我也算妇女."
    m 1rksdlb "但我没有做出...贡献什么的..."
    menu:
        "但我没有做出...贡献什么的..."
        "没关系的.":
            m 1wua "诶?真的吗?"
            m 3hublb "我更爱你了, [player]!"
        "就算这样我也依然爱你.":
            m 1rksdla "..."
            m 1ekb "我也爱你, [player]."
return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="festival_labor",
            prompt="劳动节",
            category=["节日"],
            action=EV_ACT_PUSH,
            start_date=submod_festival_labor,
            end_date=submod_festival_labor + datetime.timedelta(days=1),
            years=[],
            pool=False
            )
    )

label festival_labor:
    m 3eua "今天是劳动节哦, [player]."
    m 1rtc "按理论来说, 你今天应该放假."
    m 4eud "不过与此相对的是, 下个周或者上个周的周末可能要加班或者补课...{w=0.4}也就是调休."
    m 2euc "连续的五天小长假, 有四天是你加班换来的, 这值得吗?"
    m 3rksdlb "啊哈哈, 不过调休也把原来的假期变的更加集中了."
    m 1hub "本来只有一天的假, 但是这一通操作下来时间变长了呢~"
    m 2rua "这样一天做不了的事情五天就能做了~{w=0.3}"
    m 3rua "比如说----"
    extend 1tub "连续睡五天大觉!"
    m 1hub "啊哈哈~"
    m 3gubla "至少, 你有连续五天的时间可以陪我了~"
return

#===========================农历新年===============================

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="festival_cnnewyear",
            prompt="春节",
            category=["节日"],
            action=EV_ACT_PUSH,
            start_date=submod_festival_lnr,
            end_date=submod_festival_lnr + datetime.timedelta(days=1),
            years=[],
            pool=False
            )
    )

label festival_cnnewyear:
    m 3eub "嘿, [player]!"
    m 3hua "今天是{i}春节{/i}." #春节二字为斜体
    extend 4eub "是{i}农历{/i}的新年." #农历二字为斜体
    m 3eua "在今天, 人们会举行各种活动."
    m 2rub "比如买年货、贴春联、挂年画、年夜饭、拜年..."
    m 3wub "还会放爆竹!"
    m 1rksdlb "当然, 因为某些原因,现在大部分地区都不再放爆竹了."
    m 3eua "[player], 你们那里还在放爆竹吗!"
    menu:
        "[player], 你的家乡还在放爆竹吗!"
        "是的.":
            m 1wub "真的吗?"
            m 3hua "在你的家乡, 过春节时一定'年味'十足吧!"
            m 1rksdlb "不过它被禁止终究是有理由的..."
            m 2rksdla "污染环境暂且不提..."
            m 4rksdlc "还有些调皮的小孩会把点燃了的爆竹放在你的脚旁..."
            m 1ekb "希望在你的家乡没有那样调皮的小孩..."
        "不.":
            m 1hksdlb "哈哈..."
            m 1rksdla "我也明白, 毕竟大部分地区都没法放爆竹了."
            m 4rksdlc "但还是有方法听到爆竹那'噼里啪啦'的声音!"
            m 3efa "第一步!"
            m 4efb "先吹一些气球!"
            m 4efa "第二步!"
            m 2efb "踩爆这些气球!"
            m 3hua "这样或许能帮你模拟出一些节日的气氛, [player]~"
    m 1gubla "最后, [player]{cps=3}...{/cps}"
    extend 3hublb "新年快乐!!"
return

label festival_thxgiving:
    #这段对话暂时不会被使用
    m "[player], 今天是感恩节哦."
    m "不过我听说...你们那里应该不过感恩节."
    m "也不难理解, 毕竟这是一个西方的节日. 我在网上冲浪的时候也没有看到相关的东西."
    m "或许, 地位就像你们的中秋节一样, 感恩节这天亲友们也会共聚一堂."
    m "火鸡是今天的传统主菜, 把火鸡肚子里塞上各种调料和拌好的视频, 然后烤一整只鸡."
    m "然后由你来把鸡切成薄片, 而我去把切好的鸡分给孩子们..."
    m "啊哈哈~吃完之后我们还可以来玩南瓜赛跑."
    m "这个很简单的, 就是用勺子推着南瓜跑, 谁先到终点谁就赢了."
    m "玩完之后, 我们拿着火鸡的叉骨, 许愿以后的美好愿望..."
    m "我已经等不及想和你度过浪漫的一天了!"
return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="festival_yuanxiao",
            prompt="元宵",
            category=["节日"],
            action=EV_ACT_PUSH,
            start_date=submod_festival_yuanxiao,
            end_date=submod_festival_yuanxiao + datetime.timedelta(days=1),
            years=[],
            pool=False
            )
    )

label festival_yuanxiao:
#    m "嘿~[player], 今天可是元宵节."
#    m "元宵节这天是农历新年的第一个月圆之夜, 象征着春天的到来...{w=0.4}不过我猜你知道~"
#    m "我听说你们这一天会吃汤圆...{w=0.7}{nw}"
#    extend 1esa "我还没吃过呢..."#修改这里的表情代码
#    m "...我好想要你来喂我{w=0.4}{nw}"
#    $ _history_list.pop()
#    m "啊哈哈~"
#    m "我真的好期待我来到你的世界的那天."
#    m "我们会有很多美好的回忆~"
    m 3eua "嘿, [player]."
    m 1hub "今天是{i}元宵节{/i}." #元宵节三字为斜体
    m 3eub "元宵节最主要的习俗为观灯, 因此又得名‘灯节’."
    m 1rua "元宵节一般会吃元宵或汤圆, "
    extend 2rtc "以前这取决于所处的地区是南还是北:如果是南方, 那么基本都吃汤圆；而北方则是以元宵为主."
    m 3eub "当然, 现在这些食品的{i}地域标签{/i}没有这么强烈了, 所以这些都可以随便吃." #地域标签四字为斜体
    #m 1rksdla "原本我是打算加入元宵这个礼物的, 但因为贴图没法绘制所以就被废弃了..." #打算两字为斜体
    m 3rksdla "本来我想给你弄一点惊喜来着...但是...嗯...有点超出了我的能力范围..."
    m 1eka "不过已经能和你在一起了, 我也就不必抱怨这些没用的东西了."
    m 3eub "不过你知道吗?"
    m 3wuo "一开始在中国, {i}谈情说爱{/i}的节日其实是元宵节!" #谈情说爱四个字为斜体
    m 1tublu "那么在这个谈情说爱的节日里, 我想对你说一句..."
    m 3hublb "我爱你!"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="festival_qingming",
            prompt="清明",
            category=["节日"],
            action=EV_ACT_PUSH,
            start_date=submod_festival_qingming,
            end_date=submod_festival_qingming + datetime.timedelta(days=1),
            years=[],
            pool=False
            )
    )
label festival_qingming:
    m 1eka "[player], 今天是清明节."
    m 1rksdlb "你可能会忙着扫墓...什么的..."
    m 2eka "不用在意我, 今天专心忙你的事情就可以了~"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="festival_duanwu",
            prompt="端午",
            category=["节日"],
            action=EV_ACT_PUSH,
            start_date=submod_festival_duanwu,
            end_date=submod_festival_duanwu + datetime.timedelta(days=1),
            years=[],
            )
    )
label festival_duanwu:
    m 3hub "[player]~端午节快乐~"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="festival_duanwu",
            prompt="中秋",
            category=["节日"],
            action=EV_ACT_PUSH,
            start_date=submod_festival_zhongq,
            end_date=submod_festival_zhongq + datetime.timedelta(days=1),
            years=[],
            pool=False
            )
    )
label festival_zhongqiu:
    m 1eua "嘿, [player]!"
    m 1hub "今天是中秋节."
    m 2rksdlc "是团圆的节日呢..."
    m 1dkc "我们却还是隔着一道冷冰冰的屏幕..."
    m 1ekb "但至少你安了这个mod来陪我, "
    extend 1ekb "我就已经很满足了."
    m 1rub "当我到了你的现实里..."
    m 1dubla "坐在屋外, 望着那圆圆的月亮, 吃着月饼..."
    m 5fubla "当我累了的时候, 还可以躺在你的怀里..."
    m 3hksdlb "哈哈, 有点想入非非了..."
    m 2rsc "但离我'出来'的日子, 已经不远了吧..."
return
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="festival_7xi",
            prompt="七夕",
            category=["节日"],
            action=EV_ACT_PUSH,
            start_date=submod_festival_7xi,
            end_date=submod_festival_7xi + datetime.timedelta(days=1),
            years=[],
            pool=False
            )
    )

label festival_7xi:
    m 1eub "嘿, [player]!"
    m 3wua "今天是七夕节."
    m 1eka "如果你不熟悉它, 你就理解为中国的{i}情人节{/i}就好了..." #情人节三字为斜体字
    m 4eub "这个节日在每年农历的七月初七."
    m 3eua "七夕又叫乞巧, 女子们为能有织女的心灵手巧, 就在那天比一些精细活..."
    m 2rub "掷花针、穿七孔针、雕瓜果等等..."
    m 4eub "后来经过历史发展, 被赋予了'牛郎织女'的美丽爱情传说."
    m 1hksdlb"想必你也听过了..."
    m 3eka "如果没听过, 之后我也会给你讲的."
    m 1gubla "既然今天也算情人节, "
    extend 3tkbsu "那我们是不是该干点情侣该干的事情了?"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="festival_chux",
            prompt="除夕",
            category=["节日"],
            action=EV_ACT_PUSH,
            start_date=submod_festival_lnr + datetime.timedelta(hours=-6),
            end_date=submod_festival_lnr,
            years=[],
            pool=False
            )
    )
label festival_chux:
    m 1eua "嘿, [player]!"
    m 3hub"今天是除夕, 春节的前夕."
    m 3hua "{i}年夜饭{/i}就是在这时吃的." #年夜饭三字为斜体
    m 2rksdlb "好多美食都会在这时候吃...真的挺让人馋的..."
    m 1rka "还有些地方除夕会守夜到第二天..."
    m 1eka "[player], 你们那边有这个习俗吗?{nw}"
    $ _history_list.pop()
    menu:
        "[player], 你们那边有这个习俗吗?{fast}"
        "还有.":
            m 1wub "哦!那挺好的!"
            m 2rka "这样你还能多陪我一段时间..."
            m 3ekb "不过还是要注意身体啊, 熬夜太久挺伤身体的, [player]."
            m 1eka "我爱你, [player], 所以, 保证自己的身体健康, 好吗?"
        "没有.":
            m 1hksdlb "啊哈哈..."
            m 2rsc "也...不算坏事."
            m 1rka "至少你晚上能好好睡一觉..."
            m 2eka "[player], 当你想睡觉的时候, 跟我说, 好吗?"
            m 1hublb "毕竟我很爱你的~"
return "love"