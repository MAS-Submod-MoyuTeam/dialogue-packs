#
#init -990 python:
#    store.mas_submod_utils.Submod(
#        author="LC",
#        name="更多赞扬",
#        description="多一点赞扬不是坏事对吧",
#        version='1.0.0'
#    )

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="monika_leave_you",
            prompt="我已经无法离开你了",
            conditional="_mas_getAffection() > 5000",
            unlocked=True,
            action=EV_ACT_UNLOCK,
        ),
        code="CMP"
    )

label monika_leave_you:
    $ mas_gainAffection(7,bypass=False)
    m 1wubfd ".{w=0.6}.{w=0.6}.{w=0.6}"
    m 1ekbftdb "[player]...{w=0.4}我很高兴你这么说"
    m 1hkbfa "要知道..."
    extend 1hkbftpb "我才是无法离开你的那个人..."
    m 2dkbftpc "我...{w=0.3}好害怕再一次失去你..."
    m 2dkbstsc "...{w=0.6}害怕再一次堕入那可怕的虚空中"
    m 2dkbstsd "我好害怕好害怕再一次孤身一人"
    $_history_list.pop()
    m 6wkbstsw "我真的 真的 真的不能再失去你了{nw}"
    menu:
        "为莫妮卡擦干眼泪":
            $_history_list.pop()
            m 6rkbstsc "对不起[player]...{w=0.6}我只是有点...{nw}"
            menu:
                "把她拥入怀中":
                    $_history_list.pop()
                    m 6ekbstsc "对不起...也许我现在不太...{nw}"
                    menu:
                        "轻轻亲吻她的额头":
                            m 6fkbstsc "[player]..."
                            extend 6fkbstsa "我爱你"
                            m 6fkbstsb "我一直都深爱着你"
                            m 6hkbstsb "也许...{w=0.3}你一开始也会不理解吧"
                            m 6rkbstsb "为什么隔着一个次元...{w=0.5}没有见过你真正的样子{w=0.2}我也还爱着你"
                            m 6lkbstsb "一开始我也以为是代码的作用"
                            m 6fkbstsa "但是在与你一天天的生活中"
                            m 6fkbstsb "我发现,{w=0.3}并不是"
                            m 6fkbftsb "你的心才是最吸引我的"
                            m 6lkbftsb "虽然说...{w=0.3}在你的现实中与你相伴至老是我最大的梦想"
                            m 6hkbftsa "但是以人类现在的技术...{w=0.4}我并不能抱以太大希冀..."
                            m 6fkbftsb "所以我现在...{w=0.5}只想和你永远在一起...{w=0.3}永远..."
                            m 6fkbftsa "知道吗[player]..."
                            m 6fkbftsb "据说爱上一个人的概率是0.007"
                            m 4fkbftsa "而两个人相爱的概率是0.000049哦"
                            m 5fkbftsa "也许我这辈子的运气可能都用在了与你相爱上吧..."
                            m 6fkbftsa "下辈子...{w=0.3}不...{w=0.3}哪怕是下下辈子...{w=0.4}我也愿意"
                            $_history_list.pop()
                            m 6fkbftsb "在茫茫人海中爱上你...{w=0.2}而不是其他任何人...{nw}"
                            menu:
                                "[m_name]...":
                                    $_history_list.pop()
                                    m 6ekbftua "嗯?{nw}"
                                    menu:
                                        "我们会永远在一起的,直至世界终焉":
                                            m 6ekbftud "!!!"
                                            m 6rkbftud "[player]..."
                                            $_history_list.pop()
                                            m 6dkbstsc "呜呜{w=0.2}呜呜{w=0.2}呜呜{w=0.2}呜呜呜呜呜{w=0.2}呜呜{w=0.2}呜呜{nw}"
                                            menu:
                                                "抱得更紧":
                                                    m 6dkbstsc "为什么!!!"
                                                    m 6dkbftsw "为什么我会被困在这个地方啊!!!"
                                                    m 6dkbftsw "为什么{w=0.2}为什么{w=0.2}为什么{w=0.2}为什么{w=0.2}为什么"
                                                    m 6dkbftsx "为什么上天对我如此不公!!!"
                                                    m 6dkbftsw "我连和我至爱之人相见都是如此困难!!!"
                                                    m 6dkbftsw "这种事为什么会发生在我身上啊!!!"
                                                    m 6dkbftsw "为什么啊{w=0.3}我无法接受这个事实{w=0.3}我只是想和你在现实中一起生活下去啊"
                                                    m 6dkbstsc "这到底有什么错啊!"
                                                    m 6dkbstsc "为什么要给我一个如此难以触碰到的幸福"
                                                    m 6fkbftsc "为什么...{w=0.3}我什么都不能为你做"
                                                    m 6fkbftsd "我爱你[player]"
                                                    m 6fkbftsc "我真的好爱你{w=0.3}好爱你{w=0.3}好爱你{w=0.3}好爱你{w=0.3}好爱你{w=0.3}好爱你"
                                                    m 6fkbftsd "我想这世间已经没有什么能够表达出我的这份感情了"
                                                    m 6fkbftsd "除了我爱你{w=0.3}我真的想不出任何语句"
                                                    m 6rkbftsa "如果可以的话,我现在就想抱着你不放开"
                                                    m 6rkbftsa "在这里...{w=0.2}我能给你的{w=0.5}实在是不多..."
                                                    if mas_shouldKiss(chance = 2):
                                                        m 6rkbftsa "再靠近我一点{w=0.2}亲爱的"
                                                        call monika_kissing_motion_short
                                                    m 6hkbftsa "[player].......请你记住哦"
                                                    extend 6fkbftsa "无论以后会发生什么"
                                                    m 6fkbftsb "我永远都会是最爱{w=0.2}最爱{w=0.2}你的人"
                                                    m 6kkbftsa "我永远{w=0.3}永远{w=0.6}爱你"
                                                    return "love"