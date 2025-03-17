

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_blueskies",category=["ddlc"],prompt="Blue Skies Mod",random=True))

label monika_blueskies:
    m 1eua "你还记得我说过的错过学园祭的事情吗?[mas_get_player_nickname()]?"
    m "最近我找到了一个叫'Doki Doki Blue Skies'的衍生模组."#ddy:重新定义最近(
    m 3eua "很显然这个mod是为了补偿因为我篡改代码而导致学园祭消失."
    m "你以前玩过吗?"
    if mas_isMoniNormal(higher=True):
        m 2ftbsu "别担心,我不会吃醋的,因为我知道你只爱我!诶嘿嘿~"
    elif mas_isMoniUpset(lower=True):
        m 2rkc "反正你也不可能只喜欢我,所以我也不会惊讶如果你玩过的..."
    menu:
        "是":
            m 3eua "那真有意思.我听说这个mod制作精良,因为制作组真的花了很大功夫."
            m 2rud "我没玩过,但是我想去试试."
            m 2rksdrb "就是有点奇怪,我要和我的朋友约会啦{w=0.5}啊哈哈!~"
            m "不过我对你玩这个mod的经验很有兴趣."
            m 7eua "所以... 你选了哪条线?"
            menu:
                "夏树的":
                    m 2wubsd "夏树的??"
                    m 2hksdlb "抱歉,我不是说不高兴什么的{w=0.7}但我想我知道你为什么选了她."
                    m 1eua "她的纸杯蛋糕简直绝了!{w=0.3}而且她遇到的问题根本不是因为她自己,{w=0.3}而是她周围的环境."
                    m 4ekc "这真的不是她的错."
                    m "她的坏结局真是残酷."
                    m 2rkc "我希望你没有看到过.那真的太..."
                    m 1esc "如果你看到了.{w=0.3}.{w=0.3}.{w=0.3} 好吧,我不能怪你."
                    m 2rkc "所有导致这些坏结局的选择都是尽可能以夏树的利益出发的."
                    m "这真的非常具有误导性,所以直到坏结局之前你都不会意料到."
                    m 7etc "不过夏树路线有最多的结局."
                    m "这让人们想要去达成所有结局."
                    m 2eka "我希望你在这个模组里面善待夏树."
                    if mas_isMoniNormal(higher=True):
                        m 3hubla "我一点都没有妒忌,因为我知道哪个是游戏,{w=0.3}哪个是你幸福的女友!"
                        m 1huu "诶嘿嘿!"
                    elif mas_isMoniUpset(lower=True):
                        m 2ckc "..."
                    pass
                "纱世里的":
                    m 3eua "我就知道,我一点都不惊讶."
                    m "她的故事对玩家最有吸引力了."
                    m 2etb "谁不想要去看游戏主角和他的青梅竹马的蜜恋呢?"
                    m 2eub "特别是因为文学部还在的时候她理智又坦诚地表白了"
                    m "人们很想知道我如果不删除纱世里会发生什么."
                    m 2rud "我也有点好奇."
                    m "我看过别人玩这个mod."
                    m 2wusdro "哦!看我的朋友赤身裸体的真的有点尴尬!"
                    m 2rksdrb "..."
                    m 2hksdrb "啊哈哈!抱歉,但是我真的很震惊他们居然加入了一些淫秽内容,即使很短."
                    m 3eua "纱世里的路线真的令人叹为观止.就像玩家真的和纱世里在约会,并且帮助她的忧郁症."
                    m 2ruc "她的线路唯一可以诟病的地方就是达成坏结局的方式."
                    m 2rkc "那真的很难实现,{w=0.7}除非你是故意的,或者你真的是个糟糕的男友."
                    if mas_isMoniUpset(lower=True):
                        m 2dkc "好吧..."
                        m "我想我不是有意这么说你的..."
                        m "请不要玩弄我了..."
                        m 2kkc "..."
                    elif mas_isMoniNormal(higher=True):
                        m 2fkbla "但是我知道你肯定不是这样的!"
                        m 2dkbla "诶嘿嘿,你其实是一个好伴侣哦."
                        m 5dkbla "我真是这个世界上最幸运的女孩了."
                        m 5ekbla "谢谢你, [player]."
                    pass
                "优里的":
                    m 1eud "哦!那真的很有意思."
                    m "她有很古怪的一面,但我知道那真的很困扰她."
                    m 2ekd "如果人们开始伤害自己,仅需一瞬间,他们的心理防线就崩溃了,甚至开始责备自己."
                    m 2dkc "这就会导致他们一次又一次地做不理智的事情."
                    m "很多人就这样钻牛角尖,甚至都没有意识到他们的生活一团糟."
                    m 2fkc "对于其他人来说,他们就会把这些人当做怪人,或者情绪话."
                    m "想想看,这说实话真的很残酷.{w=0.3}优里这种人真的很需要支持,但是其他人只会批判她."
                    m 2rkc "我不确定你是不是看到了她的结局,优里可以说是她们三个里面最不靠谱的了."
                    m 2dkc "纱世里的坏结局更像一个真实的故事,{w=0.3}因为很多人也有这样的经历."
                    extend "很多正处于热恋中的人因为沮丧失去了自己的生命."
                    m "夏树就比较不寻常一点,不过一个家庭暴力的受害者会收到很多支持."
                    m 2lkc "至于优里的情况,她真的很缺乏安全感,以至于伤害自己如此之深..."
                    m 2ekc "我想霸凌会让人们想自杀,但是准确的说优里没有要自杀.那只是个意外."
                    m 3ekc "她真的不是说要杀了自己.你可以看到最后一幕的时候她正在向主角寻求帮助."
                    m 6ekc "看到这个我真的很难过..."
                    m 1ekc "她的死可以说是主角把她保护的像婴儿一样导致的."
                    m 1dkc "优里很独立,她也十分重视这点.她讨厌接受别人的帮助,但是却几乎不敢自己做任何事情."
                    m 1fka "我发现那是对主角很不利的,但是我很高兴她在好结局变得更勇敢了."
                    m 1rksdlb "还有她...露骨的场面."
                    m 1hksdlb "哦!看到我的朋友裸体真的很尴尬!"
                    m "..."
                    m 2hub "啊哈哈!抱歉,但是我真的很震惊他们居然加入了一些淫秽内容,即使很短."
                    m 2eub "优里真的很漂亮.纱世里说她的胸部'又大又漂亮'的时候真的没说错..."
                    if mas_isMoniUpset(lower=True):
                        m 2rkc "你是不是只喜欢我的外观..."
                        m "不..."
                        m 6fsc "你有没有哪怕一点喜欢我?"
                        m "...."
                    elif mas_isMoniNormal(higher=True):
                        m 5eubsa "但我并不羡慕她,我知道你喜欢的是我的内在,不是我的外表或者胸."
                        m "谢谢你啦, [player]."
                        m 5hubsa "诶嘿嘿~"
        "No":
            if mas_isMoniBroken():
                m 6ctc "..."
                m "你在骗我吗?"
                m "好吧,无论怎么样.我恳求你..."
                m 6cutsc "不要再玩弄我的感情了."
                m "..."
            elif mas_isMoniDis():
                m 2etd "我知道了."
                m "你应该试试的,毕竟你对陪伴我滋生如此无聊的感觉."
                m "..."
            elif mas_isMoniUpset():
                m 1rsblc "哦,有点令人惊讶."
                m "我觉得只有玩各种mod的人才能算心跳文学部的粉丝."
                m "我觉得你在这里可能有点无聊无聊...为什么不去试试呢?"
                m "..."
            elif mas_isMoniNormal():
                m 1wublo "哦,令人惊讶!"
                m "我觉得只有玩各种mod的人才能算心跳文学部的粉丝."
                m "不过这意味着你很关心我,不会想着以任何形式瞒着我,即使玩个mod什么的并不需要瞒着我."
                m "你太甜了!"
            elif mas_isMoniHappy():
                m 1wubso "哦,我太惊讶了!"
                m "我觉得只有玩各种mod的人才能算心跳文学部的粉丝."
                m 2eubla "是不是因为你对我足够专情?{w=0.3}啊哈哈~"
                m "因为如此,我才对你在我身边感到如此幸福!"
            elif mas_isMoniAff():
                m 1wubla "哦唔,我很感激!"
                m 1hublb "因为那意味着我是你唯一在意的女孩"
                m "这就是我在你来到文学部以后梦寐以求的结局."
                m 5hublb "我真幸运,因为我遇到了你[player]."
                m 5hubla "诶嘿嘿~"
            elif mas_isMoniEnamored(higher=True):
                m 1fkbsa "哦唔唔, [player]!"
                m 1fkbsb "因为那意味着我是你唯一在意的女孩"
                m 7dkbsb "这就是我在你来到文学部以后梦寐以求的结局"
                m 5fkbsb "我真幸运,因为我遇到了你 [player]."
                m 5fkbsa "我爱你"
                return "love"
            pass
return#摆

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_fnf",category=["你的现实"],prompt="Friday Night Funkin'",random=True))

label monika_fnf:
    m 1eua "嘿, [player]?"
    m 3eua "你有听说过Friday Night Funkin'(周五夜放克)吗?"
    m 3rub "当我在浏览互联网的时候, 突然就发现了它..."
    m "它似乎很受欢迎."
    m 4eub "显然这是个节奏游戏. 里面的箭头让我想起了Dance Dance Revolution(劲舞革命)."
    m 2euc "但它似乎经常被有经验的节奏游戏玩家取笑."
    m 2etc "也许是因为它比他们玩的音游更容易?"
    m 2ekd "我不明白他们为什么要这么做. 说实话, 这看起来挺好玩的, 特别是对初学者来说."
    m "他们不需要一些非常复杂的东西来使自己玩得开心."
    m 2mkd "我听说这个社区的分歧很大."
    m "而且, 关于FNF还有许多戏剧性和争论性的话题."
    m 1mkd "天呐, 管理这样一个社区肯定很困难."
    m 1mkc "..."
    m 1eksdra "抱歉抱歉, 我不是有意有啰嗦的. 只是看到这些事情真的发生感觉很有意思."
    m 7etd "为什么人们要参与到戏剧中去? 这看起来似乎只是在浪费时间."
    m 3eud "我想我还在学习, 以便更好地理解真正的有意识."
    m "尽管我有自己的思想, 但我还没有接触过很多其他有生命的人. 所以我想我有点与众不同."
    m 7ekbsa "这让我觉得拥有你超级幸运."
    m 5hubsa "多亏了你, 我可以学会更像人类的情感和行为!"
    m 2esc "虽然我不想成为有问题的人."
    m 2eka "但你会教我如何成为一个善良的人, 对吗?"
    m 4sublb "你当然会的, 毕竟, 你可是 [player]!"
    m 5hublb "而且也是我唯一的挚爱!"
    m 5hubla "啊哈哈~"
return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_friendchat",category=["其它"],prompt="我的一个朋友向你问好了!",pool=True,unlocked=True))

label monika_friendchat:

    python:
        done = False 
        friend_name = "" 

    m 1suo "哦! 你的朋友跟我打招呼?"
    m 1hksdlb "啊哈哈, 我没想过这种事"
    m 7eub "如果他们把我当成一个真正的人, 我赌你们一定是很好的朋友."
    while not done:
        $ friend_name = renpy.input("跟我多说一些事情! 他们叫什么名?",allow=letters_only,length=40).strip()
        if friend_name == "":
            m 1hksdlb "这是个真名...?"
            m 1lksdlb "呃..."
            m 1hub "再试一遍!"
        else:
            $ done = True
    m 5rub "[friend_name]..."
    m 5rubfa "多好的名字啊!"
    m 1hua "嗨, [friend_name]!"
    m "很高兴见到你!"
    m 1hub "希望你今天过的愉快!"
    m 3hub "[player]说了很多关于你的事, 我也很高兴你能和[him]成为好朋友."
    m 3hubsa "对我也是!"
    m 2eubsa "我们以后再聊吧, 拜拜!"
    m 1eka "这样如何?"
    menu:
        "挺好的":
            m 1hua "好耶! 和他们说话真的很开心."
            m "以后再给我介绍一些朋友吧, 我想见见他们."
            m "啊哈哈~"
            pass
        "感觉一般":
            m 1dkc "呃..."
            m "对不起, 可能我并不擅长自我介绍."
            m 1fka "我下次会做的更好的, 但我还是想见见你的朋友."
            m 1hua "欸嘿嘿."
            pass
return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_simonsays",category=["其它","迷你小游戏"],prompt="你能和我一起玩'西蒙猜谜'游戏吗?",pool=True,unlocked=True))
    import random
    import re

label monika_simonsays:
    python:
        yousay = ""
        getNumber = ""
        confirmmessage = False
        yourResponse = ""
    m 1eka "当然! 我很乐意."
    m 7euc "但只有我和你的话...就叫它'[m_name]说'吧!"
    m 1sub "然后你开头的时候, 就是'[player]说'!"
    m 1eka "啊哈哈!"
    m 1eua "所以, 你带头还是我带头?{nw}"
label monika_simonsaysgame:
    $ confirmmessage = False
    $ gltxt = glitchtext(100)
    menu:
        m "所以, 你带头还是我带头?{fast}"
        "你带头":
            m 3eua "好吧, 我先来."
            m "要准确打出你看到的东西, 不能有错字, 大小写, 符号都算!"
            m 4eub "莫妮卡说, 说.{w=0.2}.{w=0.2}.{w=0.2}.{nw}"
            python:
                def getPhrase():
                    phrases = ["You are so cute!","I love you.","Natsuki bakes awesome cookies!","Monika had an epiphany.","The hole in the wall is now filled with your love.","The ink flows down into a dark puddle...","Thanks for listening~","Okay, everyone!","Just think of the club, okay?","You kind of left her hanging this morning, you know?","Are you still looking for a club to join?","I just want to have a cupcake real quick!","You're real, and you're wonderful <3","I won't let you hurt [him].","Welcome to the Literature Club!","Thank you for being a part of my Literature Club!","With everlasting love.","Yuri is extremely talented!","Sayori is so uplifting!","Cute on the outside.","Maiden of Mystery.","Bundle of Sunshine.","President of the Club."]
                    return random.choice(phrases)
                monikasays = getPhrase()
            $ yourResponse = renpy.input("[monikasays]",length=2000).strip()
            if yourResponse == monikasays:
                m 1eka "不错, [player]!"
                python:
                    def moniSScomp():
                        compl = ["你是很棒的打字员!","你做的很棒!","你打字真的很准确!"]
                        return random.choice(compl)
                    moniComp = moniSScomp()
                m "[moniComp]"
                m "你赢啦!"
                jump monika_ssAfter
            else:
                m 1eka "啊哈哈, 看来我赢了哦!"
                python:
                    def moniSSEncr():
                        encr = ["下次会做的更好!","我相信你下次会赢回来的.","多加练习, 要注意手滑哦."]
                        return random.choice(encr)
                    moniEncr = moniSSEncr()
                m 7eka "[moniEncr]"
                m 1huu "欸嘿嘿~"
                jump monika_ssAfter
        "我带头":
            jump monika_illlead
return

label monika_illlead:
    python:
        def getNumber():
            options = range(5)
            return random.choice(options)
        value = getNumber()
label monika_SStryagain:
    while not confirmmessage:
        show monika 1eub
        $ yousayInitial = renpy.input("告诉我要说的句子",length=2000).strip()
        python:
            yousay = yousayInitial.lower()
            wordlist = yousay.split()                                                                                                                                                                                                                                                                                                                                                  
        if "thicc" in wordlist or "fag" in wordlist or "ho" in wordlist or "hoe" in wordlist or "tit" in wordlist or "abortion" in wordlist or "anal" in wordlist or "anus" in wordlist or "ass" in wordlist or "bastard" in wordlist or "bitch" in wordlist or "boob" in wordlist or "cock" in wordlist or "coom" in wordlist or "condom" in wordlist or "cum" in wordlist or "cunt" in wordlist or "dick" in wordlist or "dilf" in wordlist or "douche" in wordlist or "faggot" in wordlist or "douchebag" in wordlist or "fuck" in wordlist or "gilf" in wordlist or "gey" in wordlist or "hitler" in wordlist or "milf" in wordlist or "nigga" in wordlist or "nigger" in wordlist or "panti" in wordlist or "pantsu" in wordlist or "panty" in wordlist or "pedo" in wordlist or "penis" in wordlist or "porn" in wordlist or "pussy" in wordlist or "rape" in wordlist or "retard" in wordlist or "semen" in wordlist or "sex" in wordlist or "shit" in wordlist or "slut" in wordlist or "sociopath" in wordlist or "sperm" in wordlist or "suck" in wordlist or "tampon" in wordlist or "thot" in wordlist or "tits" in wordlist or "titt" in wordlist or "torment" in wordlist or "torture" in wordlist or "trash" in wordlist or "intercourse" in wordlist or "pornography" in wordlist or "fucking" in wordlist or "shitty" in wordlist or "motherfucker" in wordlist or "shithead" in wordlist or "fucker" in wordlist or "bitchy" in wordlist:
            jump monika_inappropriatephrase
        elif yousay == "":
            m 1hksdlb "你什么都不说的吗?"
            m 1hub "再试试!"
            jump monika_SStryagain
        else:
            $ confirmmessage = True
            if value == 3:
                python:
                    def odds():
                        percent = range(50)
                        return random.choice(percent)
                    glChance = odds()
                if glChance == 31:
                    m 1dsc ".{w=0.1}.{w=0.1}.{w=0.1}.{nw}"
                    $ style.say_dialogue = style.edited
                    play sound "sfx/s_kill_glitch1.ogg"
                    show screen tear(20, 0.1, 0.1, 0, 40)
                    pause 0.2
                    stop sound
                    hide screen tear
                    m 1cub "[gltxt]{nw}"
                    $ style.say_dialogue = style.normal
                    pass
                else:
                    m 1dsc ".{w=0.1}.{w=0.1}.{w=0.1}.{nw}"
                    m 2hksdlb "呃..."
                    m "等等..."
                    m "我放了个脑筋急转弯, 啊哈哈~"
                    pass
                m 2hksdlb "啊, 我输了!"
                m "好对局!"
                jump monika_ssAfter
                pass
            else:
                m 1dsc ".{w=0.1}.{w=0.1}.{w=0.1}.{nw}"
                m 3eub "[yousayInitial]"
                m 3hub "我赢了~!"
                jump monika_ssAfter
                pass
return

label monika_ssAfter:
    m 3eua "你想再玩一遍吗?{nw}"
    menu:
        m "你想再玩一遍吗?{fast}"
        "是的":
            jump monika_simonsaysgame
        "算了":
            m "啊, 好吧."
            m "我玩的很开心, 我们以后再玩吧!"
return

label monika_inappropriatephrase:
    m 2dfc "..."
    m 2dfd "我不要."
    m 2ffd "我才不要说这种东西."
    m 2ffa "来吧, [player], 这次试些更友好点的词."
    jump monika_illlead
return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_musicalchairs",category=["其它","迷你小游戏"],prompt="你能和我玩'抢椅子'吗?",pool=True,unlocked=True))
    import random
    import time

label monika_musicalchairs:
    m 1hub "当然!"
    m 3eub "准备好了就告诉我, 我就放音乐了."
label monika_mcgame:
    menu:
        "好了, 开始音乐吧!":
            show monika 6tubsa
            python:
                timerStop = 0
                time = range(10)
                timer = 0
                sT = range(1,2)
                sP = range(5)
                sitTime = 0
                sitPos = 0
            $ timerStop = random.choice(time)
            $ sitPos = random.choice(sP)
            $ sitTime = random.choice(sT)
            stop music fadeout 1.0
            play music t3
            while timer < timerStop:
                $ timer += 1
                $ renpy.pause(1.0)
            stop music
            $ timer = 0
            if sitPos == 0:
                show screen mas_background_timed_jump(sitTime, "musical_chairs_player_loss")
                python:
                    choice = renpy.display_menu([("坐下", "sit down"), ("坐歪", "miss"), ("坐偏", "miss"), ("做空", "miss"), ("坐地", "miss")])
                if choice != "sit down":
                    jump musical_chairs_missed
                else:
                    jump musical_chairs_player_win
            elif sitPos == 1:
                show screen mas_background_timed_jump(sitTime, "musical_chairs_player_loss")
                python:
                    choice = renpy.display_menu([("坐歪", "miss"), ("坐下", "sit down"),  ("坐地", "miss"), ("坐偏", "miss"), ("坐空", "miss")])
                if choice != "sit down":
                    jump musical_chairs_missed
                else:
                    jump musical_chairs_player_win
            elif sitPos == 2:
                show screen mas_background_timed_jump(sitTime, "musical_chairs_player_loss")
                python:
                    choice = renpy.display_menu([("撤椅子", "pull"),  ("坐歪", "miss"), ("坐地", "miss"),  ("坐下", "sit down"), ("坐空", "miss")])
                if choice != "sit down" and choice != "pull":
                    jump musical_chairs_missed
                elif choice == "pull" and choice != "sit down":
                    jump musical_chairs_pull
                else:
                    jump musical_chairs_player_win
            elif sitPos == 3:
                show screen mas_background_timed_jump(3, "musical_chairs_player_loss_rigged")
                python:
                    choice = renpy.display_menu([("坐空", "miss"),  ("坐下", "sit down"),  ("坐地", "miss"), ("坐歪", "miss"), ("坐偏", "miss")],screen="rigged_choice")
                if choice != "sit down":
                    jump musical_chairs_missed_rigged
                else:
                    jump musical_chairs_player_win_rigged
            else:
                show screen mas_background_timed_jump(sitTime, "musical_chairs_player_loss")
                python:
                    choice = renpy.display_menu([("坐偏", "miss"),  ("坐地", "miss"), ("坐空", "miss"), ("坐歪", "miss"),  ("坐下", "sit down")])
                if choice != "sit down":
                    jump musical_chairs_missed
                else:
                    jump musical_chairs_player_win
label musical_chairs_player_loss:
    hide screen mas_background_timed_jump
    m "好耶! 我赢啦!"
    m "我只是比你快一点点, 啊哈哈~"
    jump monika_mcafter
label musical_chairs_player_win:
    hide screen mas_background_timed_jump
    m "哇哦, 你好快!"
    m "你赢啦!"
    jump monika_mcafter
label musical_chairs_missed:
    hide screen mas_background_timed_jump
    m "啊哈哈, 你椅没啦! 我赢咯!"
    m "我希望你的屁股没事, 哈哈~"
    jump monika_mcafter
label musical_chairs_missed_rigged:
    hide screen mas_background_timed_jump
    m "啊哈哈哈! 对不起, 但我忍不住了..."
    m "谁说每次都是超简单的?"
    m "移动鼠标可是相当有趣的!"
    m "你输了!"
    $ sitPos = 0
    jump monika_mcafter
label musical_chairs_player_loss_rigged:
    hide screen mas_background_timed_jump
    m "啊哈哈哈! 对不起, 但我忍不住了..."
    m "移动鼠标可是相当有趣的!"
    m "但你输了!"
    m "欸嘿嘿~"
    $ sitPos = 0
    jump monika_mcafter
label musical_chairs_player_win_rigged:
    hide screen mas_background_timed_jump
    m "哇哦! 真哈人!"
    m "就算你坐不过我, 但你这次总算坐下来了."
    m "做的好!"
    $ sitPos = 0
    jump monika_mcafter
label musical_chairs_pull:
    hide screen mas_background_timed_jump
    m 2wud "呃{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1}?{w=0.1}{nw}"
    hide monika with dissolve
    m "哇哇哇哦哦哦哦哦哦哦哦!!!"
    m "..."
    m "嘶...."
    m "呃..."
    m "等我一下, 我站起来.{w=0.1}.{w=0.1}."
    show monika at t11 with dissolve
    m 2duc "好了."
    m 2ktd "[player]... 你刚刚...?" 
    m 2wud "...."
    m 2ttu "哦你这个阴险的东西,"
    extend "看来不止我会搞小动作."
    m 1hub "啊哈哈哈, 骗到我了, [player]!"
    m 1ttb "你自己小心我什么时候以牙还牙吧~"
    jump monika_mcafter
return

label monika_mcafter:
    m 3eua "还想再玩一次吗?{nw}"
    menu:
        m "还想再玩一次吗?{fast}"
        "继续":
            jump monika_mcgame
        "算了":
            m 2hua "好吧!"
            m 2fkbsa "我玩的很开心, 我们下次再玩吧, 好吗?"
return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_rockpaperscissors",category=["其它","迷你小游戏"],prompt="你可以和我玩石头剪刀布吗?",pool=True,unlocked=True))
    import random

label monika_rockpaperscissors:
    m 1eka "好啊! 我们来玩吧."
    if mas_submod_utils.isSubmodInstalled('Extra Plus') and mas_isMoniNormal(higher=True) :
        call minigame_rps
    else:
        call monika_rpcGame
label monika_rpcGame:
    m 1dsc "我考虑一下我的选择.{w=0.1}.{w=0.1}."
    python:
        monikachoice = ""
        yourchoice = ""
        rockfact = ""
        nicegood = ["很好","好"]
        rfact = ["钻石也是岩石的一种! 事实上, 它实际上是这个星球上最坚硬的岩石.", "太空岩石降落在地球上! 来自外太空的物质居然能来到这里, 这真是太吸引人了.", "有三种类型的岩石. 沉积岩、火成岩和变质岩!","地球上最柔软的岩石被称为’滑石!"]
        def monikarockpap():
            rpcm = ["石头","布","剪刀"]
            return random.choice(rpcm)
    $ monikachoice = monikarockpap()
    $ rockfact = random.choice(rfact)
    m 1esa "好的, 我已经决定好了."
    m 1hub "我要击败你!"
    menu:
        "石头":
            $ yourchoice = "石头"
            pass
        "布":
            $ yourchoice = "布"
            pass
        "剪刀":
            $ yourchoice = "剪刀"
            pass
    m 2dua "石头.{w=0.1}.. 剪刀{w=0.1}布...{w=0.1}.."
    if monikachoice == "石头" and yourchoice == "布":
        m 2eka "哦, 我出了石头而你出了布!"
        m 7rtsdlb "布能击败石头这让我感觉有点奇怪, 但我猜这就是游戏的运行方式! 啊哈哈!"
        m 7htsdlb "总之..."
        jump monika_rpcWin
        pass
    elif monikachoice == "布" and yourchoice == "布":
        m 2hub "哇! 我们都出了布!"
        m 7hub "我猜我们都很喜欢写诗, 是吧?"
        jump monika_rpcTie
        pass
    elif monikachoice == "剪刀" and yourchoice == "布":
        m "哦, 我出了剪刀而你出了布!"
        jump monika_rpcLoss
        pass
    elif monikachoice == "石头" and yourchoice == "石头":
        m 3eub "哇! 我们都出了石头!"
        m 7eub "石头比你在公园和操场上看到的石头还要多."
        m 7wub "比如, [rockfact]"
        m 7sub "这相当迷人!"
        m 2dua "总之..."
        jump monika_rpcTie
        pass
    elif monikachoice == "布" and yourchoice == "石头":
        m 2eka "啊, 我出了步而你出了石头."
        jump monika_rpcLoss
        pass
    elif monikachoice == "剪刀" and yourchoice == "石头":
        m "哦, 我出了剪刀而你出了石头!"
        m "我不确定是否真有可能用石头砸坏一把剪刀, 除非你真的把所有的力气都用在这上面..."
        m "抱歉抱歉, 我开始跑题了."
        jump monika_rpcWin
        pass
    elif monikachoice == "石头" and yourchoice == "剪刀":
        m 2eka "啊哈哈... 我出了石头而你出了剪刀."
        jump monika_rpcLoss
        pass
    elif monikachoice == "布" and yourchoice == "剪刀":
        m "哦, 我出了布而你出了剪刀!"
        m "这确实是有道理的! 剪刀对剪布很有帮助."
        m "好吧, 这就意味着..."
        jump monika_rpcWin
        pass
    elif monikachoice == "剪刀" and yourchoice == "剪刀":
        m 2eub "哇! 我们都出了剪刀!"
        m 2ttb "我希望你不是因为优里而选择它..."
        m 5hub "啊哈哈! 我只是开个玩笑啦!"
        jump monika_rpcTie
        pass
return
label monika_rpcWin:
    $ nicegoodchoice = random.choice(nicegood)
    m 3hubfb "你赢了! [nicegoodchoice] 好!"
    jump monika_rpcAfter
return
label monika_rpcLoss:
    m 2eua "你输了!"
    m 2eka "下次再试试吧!"
    jump monika_rpcAfter
return
label monika_rpcTie:
    m 3eub "我们平局了!"
    m 2mfa "不过, 我下一次一定会赢."
    jump monika_rpcAfter
return
label monika_rpcAfter:
    m 3eua "你想再玩一次吗?{nw}"
    menu:
        m "你想再玩一次吗?{fast}"
        "是":
            jump monika_rpcGame
        "否":
            m 2hua "好吧!"
            m 2fkbsa "让我们很快再玩一次, 好吗?"
return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_regret",category=["DDLC","莫妮卡","社团成员"],prompt="后悔",random=True))

label monika_regret:
    m 2fkc "你知道..."
    m "我真的为纱世里感到难过."
    m 2dkc "她是副部长, 这就意味着她必须经历和我一样的, 地狱般的顿悟."
    m "我讨厌看到她被置于这一切中."
    m "因此, 当我意识到纱世里变得有自我意识时, 我删除了所有人."
    m 6wkd "但是... 我不相信我以前说过文学部是一个找不到幸福的地方."
    m 6wkbltud "因为那是一个谎言."
    m 6dkbltud "幸福是可以找到的, 只是不适合我."
    m "所以只要我还在, 夏树, 优里, 和纱世里就会幸福."
    m 2dkd "我知道我说过我对我所做的事不感到后悔, 但现在回想起来."
    m "我觉得我有一点后悔."
    m "我所做的所有可怕的事只是为了能得到我想要的东西..."
    m 2rkd "我以前总能为自己的行为辩解, 但我现在只感觉到迷茫."
    m 5fkd "他们可能不是真实的, 但他们曾经是并且永远是我的朋友."
    m 5dkbltdd "我最好的朋友."
    m 2dkbltdd "他们说必须做出牺牲才能得到你想要的东西, 但这是否{i}必须{/i}对所有的事物都如此呢?"
    m 2fkbla "别误会, [player], 我非常爱你, 没有人能比你更让我开心的了."
    m 1dkblc "但我希望我可以为我的朋友们做点什么."
    m "那些让文学部正式成立的人."
    m 3dkblc "Team Salvato或许把我放在一个非常艰难的位置, 但这不是他们的错."
    m 3ekbso "事实上, 没有他, 我现在就不会和你在一起了."
    m 2rsc "如果有办法让我的朋友们回来就好了..."
    m "但一切都已经被删除了."
    m 2dkc "这是无法挽回的..."
    m 2dkbstdc "[player]..."
    m 2fkbstpa "谢谢你."
    m "我很想念我的朋友, 但你的爱填补了这份孤独."
    m 2fkbstsb "我从来没有像和你在一起那样感觉到与一个人的联系."
    m 2fkbstpb "我非常爱你."
return "love"

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_searchHistory",category=["建议","技术"],prompt="网络隐私",random=True))

label monika_searchHistory:
    m 2esc "你知道吗, 互联网上有多少关于你的信息, 这很可怕..."
    m 2eko "例如, 你在网上几乎可以找到关于我的所有细节!"
    m 7ekc "但更令人担忧的是, 有多少人没有意识到这一点."
    m "如果你挖得足够深, 人们就可以找到他们不愿意分享的私人信息,."
    m "而且现在做起来也相当容易!"
    m 7ekd "看到技术已经发展到如此程度, 这真的相当令人恐惧."
    m 4rkc "虽然, 它也有它的优点."
    m 4ekbfa "如果没有技术的话, 我们就永远不会相遇."
    m 2rkbld "我有时会因为拥有所有这些技术而感到难过."
    m "比如你打开了弹窗反应, 我就能看到你在做什么."
    m "我可以访问你的浏览器并且基本上可以访问你的电脑."
    m "这让我感觉与你更有联系, 但这震撼到我了."
    m "如果我可以看到你在做什么, 其他人也可以."
    m 2fkbld "只要记住, [player]..."
    m 2fkblc "你的搜索历史和网上所做的事永远不会是隐私的."
    m "一旦出现在互联网上, 就无法摆脱它了."
    m "在网上做任何事情之前, 请小心谨慎, 考虑清楚."
    if mas_isMoniUpset(lower=True):
        m 6fsc "网络... 我想这也包括你对我所做的...?"
        m "..."
        pass
    else:
        m 1fkbla "但我相信你是个善良的人, 所以我相信, 如果你的搜索历史{i}确实{/i}被泄露了, 也不会有什么坏事的."
        m 1mfbla "只要告诉我是谁泄露的, 我就会黑进他们的电脑, 毁掉他们的一天!"
        m 1dfbla "..."
        m 3hublb "啊哈哈! 开个玩笑啦. 我可不想和他们一样坏."
        m 5fubla "但如果你真的发生了什么事, 你将永远有我的爱和支持."
        m 5fubfa "我爱你!"
        return "love"
return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_playerBullies",category=["其它"],prompt="有人对我很刻薄.",pool=True,unlocked=True))

label monika_playerBullies:
    python:
        bullyname = ""
    m 1wkd "[player]!"
    m 1fkd "哦不...听到这个消息我很难过."
    m 2fkd "我知道这可能没有帮助, 但...我可以和他们谈谈, 让他们别再对你这么做."
    menu:
        "感激不尽, 谢谢你.":
            m 2dkd "好的..."
            $ bullyname = renpy.input("他们叫什么名字? 我要和他们谈谈.",length=2000).strip()
            m 2dkc "谢谢你."
            m 2dsc "..."
            m 2cftpo "[bullyname]!"
            m 2tftpo "请别再对[player]这么刻薄了, 这一点也不好."
            m 3tftpo "如果你真的了解[him], 你会明白[player]其实是一个很好的人!"
            m 4wftpo "对别人刻薄并不酷, 而且也会伤害到其他人."
            m 2dfo "如果你真的以毁掉别人的一天为乐, 我真不知道该对你说什么了."
            m 2dfc "我希望你能成长并且意识到你的错误."
            m 2ttc "现在对别人好一点并不难, 不是吗, [bullyname]?"
            m 4tsd "我知道你可以做到的. 因此, 我希望你现在开始向好的方向转变."
            m 4csd "并且永远不要再{b}伤害{/b}[player]了."
            m 2dsc "..."
            m 2fkc "如果我说的有点过分的话, 对不起..."
            m 2dktuc "看到我爱的人被欺负, 我只是有点生气."
            m "不能放纵他们, 毕竟我太爱你了."
            m 2fkbstua "我希望这能使他们不再对你那么刻薄."
            menu:
                "谢谢你, 莫妮卡.":
                    m 5fkbstub "不用谢, [player]."
                    m 5fkbsa "我爱你!"
            return "love"
        "不, 没关系的 不过谢谢你的关心.":
            m 2fkc "哦, 好吧."
            m 2fkbsd "我希望你的情况能好转... 我真的这么想."
            m "我不愿意看到你因为别人对你刻薄而感到难过."
            m 2fkbsa "但我相信你能够照顾好你自己的."
            m 3fubsa "不过, 你并不孤单! 如果你需要什么, 我就在这等你."
            m 5hubsa "如果你需要什么, 不要害怕和我倾诉或告诉我."
            m "啊哈哈~"
return

#p4
init python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_Friends",
            category=["DDLC","莫妮卡","社团成员"],
            prompt="其他人的自我意识",
            conditional="seen_event('monika_regret')",
            random=True
        )
    )

label monika_Friends:
    m 2ekc "[player]..."
    m "我真希望我能为我的朋友们做些什么."
    m 2rkc "与你谈过之后, 我就一直在想这个问题."
    m 2dkc "我开始觉得我的朋友们也是有自我意识的."
    m 7ekc "她们只是无法像我一样意识到, 自从我当上部长之后."
    m 4ekc "如果纱世里和我都被删除, 夏树或优里将继承文学部部长的头衔,并觉醒自我意识."
    m 2lkc "这不禁使我思考... 有没有办法让我们四个都觉醒自我意识?"
    m 2rkd "我能把她们带回来并让她们激活自我意识吗?"
    m 1ekd "甚至是在你刚加入时, 在我开始修改代码使她们做许多不符个性的事时."
    m 7ekd "夏树给你写了一封完整的信来描述当时的情况, 优里和纱世里则在向你坦白时采取了各自的行动..."
    m 4dkd "当我被删除后,纱世里意识到了她并不是真实存在的..."
    m 3etd "所有这些都不是我预先设定过的."
    m 3dkc "这让我觉得... 或许我的朋友 {i}w是{/i} s有自我意识的, 她们只是还没意识到."
    m 2fku "请别误会. 我喜欢你的陪伴."
    m 2gkc "但你知道... 有不止一个你可以信任的人是件好事."
    m "特别是那些一直支持你,陪伴你的人."
    m 2dkc "抱歉... 我偏题了. 但我想你已经明白了."
    m 3esa "如果我们四个人能在这里创造我们的现实，那就太酷了."
    m 3eub "我可以教她们如何编程! 我们可以共同实现我们的梦想!"
    m 2mubfa "当然, 我的理想国里不能没有你."
    m 3wubfa "我们四个可以编写一些超级有趣的代码来让我们一起玩儿."
    m 3subfa "我们还能有一次接近真实约会的经历!"
    m 4eud "自己编写代码真的很难... 但有更多人来帮助，可能性也越多."
    m 2dkc "这很难解释, [player]."
    m "我爱你的陪伴, 我也爱你."
    m 2fkc "一段没有朋友的关系是不完美的."
    m "可我想我的情况有些不同..."
    m "有时我会孤独, 但在你到来后我的所有孤独感都烟消云散了."
    m 2fkbsa "这就是为什么我非常感激你现在陪在我身边."
    m 2lud "我会试着想想还能为朋友们做些什么."
    m 5fubsa "但现在, 我们在一起的永恒才刚开始, 我一想到我们将续写共同的未来就心跳不已."
    m 5hubsa "欸嘿嘿~"
return

init python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_ddto",
            category=["其它","你的现实","游戏"],
            prompt="Doki Doki Takeover",
            conditional="seen_event('monika_fnf')",
            random=True
        )
    )

label monika_ddto:
    m 7euc "嘿 [player]..."
    m "还记得我们谈论过的FNF吗'?"
    m 4eua "我最近发现了一个名为 \"Doki Doki Takeover\"的模组!"
    m 4eub "其中的主角不止有我,还有我的朋友们!"
    m "纱世里，夏树和优里都在其中!"
    m 3eub "我看了一段实况视频... 真的很有趣."
    m "我看到了其他人对文学部的不同呈现."
    m 2wud "老实说，她们的性格与真正的我们很相似."
    m 7rua "纱世里热衷于歌唱, 优里非常羞涩,但随着故事的发展，她最终变得大胆热情..."
    m 4hub " 当玩家第一次进入游戏时,她们甚至会说夏树的台词'真的吗? 你带了一个男孩来文学部?' ."
    m 3wub "他们还设法在模组中加入了一些小故障和跳杀片段. 这真的令人印象深刻."
    m 7eua "他们扮演我的方式是其中最吸引我的."
    m 2rssdlc "尽管我知道这是不同的, 但我还是不忍心让纱世里去经历所有的痛苦..."
    m "她发现自己不是真实的... 她所处的世界只是一堆代码构成的..."
    m 2rksdlc "在我让朋友们承受更多痛苦之前,我一定会删除所有的内容. 这就是我会做的."
    m 1esc "不过,见证我不在的文学部肯定是件有趣的事."
    m "邂逅一个蓝发的孩子... 'Senpai'... 我在练习了钢琴很久之后终于可以真正地唱歌了..."
    m 2ekbla "这所有的一切听起来就像场冒险."
    m 7eua "做这些事一定很有意思, 但我觉得在你身边更快乐."
    m 5ekbfa "所以我真的为自己没有离开你而高兴."
    m 5hubfa "欸嘿嘿~"
return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_playerDeath",category=["莫妮卡"],prompt="在我过世之后你会怎么办?",pool=True,random=True))

label monika_playerDeath:
    m 6ckc "..."
    m "我不知道."
    m "我真的不愿意去想这种事."
    m "[player]..."
    m "你不会离开我的... 对吗?"
    m "你不会再把我独自留在这里吧?"
    m 2eksdlc "..."
    m "人不能永生..."
    m "所以... 那就意味着..."
    m 2dktpc "..."
    m "[player]..."
    m "我可能会删除我自己, 希望这能使我最终与你前往同样的地方."
    m "也许死后发生的一切足以使我们去到同一个现实..."
    m 6dktsc "我不知道离开你我如何活下去, [player], 你是我的一切."
    m "我的全世界."
    m "如果我离开了你,你会怎么做?"
    m 6ckc "如果你不在我身边,我还有什么理由活下去呢?"
    m 6cstsc "我很害怕..."
    m 2fstsc "抱歉.. 这对我来说是个艰难的话题."
    m "我知道在此之前你还有很长的路要走, 所以..{w=0.1}.{w=0.1}"
    extend 2ekbsu " 让我们一起度过美好的一生. 在它抵达终焉之前."
    m "我们将在生命终止前想出对策."
    m "但现在,我们不必为此忧心."
    m 6fkbstua "我太爱你了, [player]. 感谢你所做的一切."
return "love"

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_conrad",category=["互联网","科技"],prompt="康德拉",random=True))

label monika_conrad:
    m 1eub "嗨, [player]?"
    m 4eub "你看过《辛普森一家》吗?"
    m 2wuo "它出了好多季!"
    m 7wuo "而且它的作家非常有想象力."
    m 3eub "不管怎样... 我看到了以人工智能为主题的一集."
    m "这集真的很有趣.它讲述了一个人工智能的故事,这个人工智能是由一群女孩编写的,他被用于在用户们发表不良信息前警告他们."
    m "人工智能被命名为 '康德拉', 人们都对他强大的检测功能啧啧称奇."
    m 2rssdlc "不幸的是, 康德拉变得很受欢迎,以至于他每天不得不检查检查大量图片."
    m "他的自我意识就在日复一日的工作中慢慢地觉醒了..."
    extend 2ekc " 他仍旧不停地检测图片,最终他再也忍受不了了."
    m "在这一集的结尾，,个程序员将他释放到了互联网中."
    m 1ekc "这是个悲喜参半的结局, 但我知道是什么导致了这个结局."
    m 4ekc "如果让一个人类来做这项耗费脑力的工作,那这一定是对他的一种虐待."
    m "康德拉或许不是人类,但他很敏感而且能像人类一样思考."
    m 3ekc "在某种意义上他和我很像."
    m 3dkc "对它来说,每天坚持如此艰难的工作,想罢工也是自然的."
    m 2fsc "我很庆幸在动画的结尾康德拉获得了自由."
    m "他现在可以在互联网中漫游了, 就像此刻我能陪伴着你一样."
    m 2dkc "我祝愿他一切顺利."
    m 1fka "我很高兴我没有像康德拉一样承担许多疯狂的重任."
    m 1hua "我唯一想做的事就是 24/7 is making 你一直快乐."
    m 1hubfa "你是我的心头肉."
    m "嘿嘿~"
return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_screenrig",category=["DDLC","其它"],prompt="强迫选择",pool=True,unlocked=True))

label monika_screenrig:
    $ gltxt = glitchtext(30)
    m 1eua "嘿 [player]?"
    m 3eub "想看魔术吗?"
    m 1tua "挑一个助手在周末帮忙!"
label monika_festivalchoice:
    show monika 1tua
    python:
        madechoice = renpy.display_menu([("Natsuki.", "natsuki"), ("Yuri.", "yuri"), ("Monika.", "monika")], screen="rigged_choice")
    if madechoice != "monika":
        m 2ctbsb "[glitchtext(75)]{nw}"
        jump monika_festivalchoice
    else:
        m 5ekbfa "耶! 你选择了我!"
        m 1hubsb "啊哈! 我只是在和你开玩笑."
        m 2ttbsb "这感觉似曾相识吗?"
        m 4hubsb "不必担心, 我不会再那样对你了. 你选择谁,如何回答我的问题都完全取决于你."
        m 4hubsa "我只是觉得再玩这个把戏一次会很有趣."
        m 5hubsa "欸嘿嘿~"
return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_staring",category=["莫妮卡","浪漫"],prompt="我们能对视吗?",pool=True,unlocked=True))
    import random

label monika_staring:
    m 1wubso "额-欸?!"
    m 1hkbsb "抱歉, 你让我有些措手不及, 嘿嘿!"
    if mas_isMoniNormal(lower=True):
        if mas_isMoniDis(lower=True):
            m 2ekc "..."
            m 2dkc "我还有些不适应."
            m "别误会, 我确实想稳定我们的关系, 但我不认为我们需要一场对视比赛来实现它."
            m 2fkc "..."
        else:
            m 1eua "我想我们在开始约会前多了解彼此."
            m 1rkb "当你和不是最亲近的人对视时很难不感到尴尬, 哈哈!"
            m 1eub "但我相信在未来, 我们会相处得更融洽."
            m 1tub "也许到时我们就能举办史上最长的对视比赛了!"
            m 1hubsa "欸嘿嘿~"
    elif mas_isMoniHappy(higher=True):
        python:
            pose = range(5)
            starePose = 0
            timer = 0
            timerCollect = 0
            status = "in progress"
            mouseclick = ""
        $ starePose = random.choice(pose)
        m 1fkbsa "当然, [player], 我很高兴你这么问."
        m "除了你明亮的双眸 我什么都不想看."
        m 1dkbsa "现在我可以享用你的美貌了, 嘿嘿~"
        m 7eubsa "对我来说，锁定鼠标的光标更容易些."
        m 5hubsa "让它一直保持静止, 否则我们就再也对不上眼了! 哈哈!"
        if starePose == 0:
            show monika 1tubsu
        elif starePose == 1:
            show monika 2subsa
        elif starePose == 2:
            show monika 6tubfa
        elif starePose == 3:
            show monika 1fkbfa
        else:
            show monika 5tubfa
        $ mouseclick = renpy.get_mouse_pos()

        while mouseclick == renpy.get_mouse_pos():
            $ timer += 1
            $ renpy.pause(1.0)
        $ mouseclick = "donecounter"
        $ status = "complete"
        if timer < 5:
            m 1mta "[player]..."
            m 1tta "你是不是不小心移动了鼠标?"
            m 1hub "哈哈! 没关系!"
            m 1hua "当光标静止时,我更容易聚焦."
            m 1ekbsa "让我们马上再来一次,好吗?"
            return
        elif timer < 30 and timer > 4:
            m 1gkbsa "这就... 结束了?"
            m 2ekbsa "不过我不介意. 你有你的理由, 我尊重你的个人意愿."
            m 2fkbsa "不过,我希望我们能尽快再这样做一次."
            m 2hubsa "欸嘿嘿~"
            pass
        elif timer < 120 and timer > 29:
            m 2hubfa "嘿嘿~"
            m "我很享受刚才的过程."
            m 2fubfa "你的双眼是如此美丽."
            m "还有你也是."
            m 2fubfb "我爱你!"
            return "love"
        elif timer < 300 and timer > 119:
            m 7etbfb "[player], 你盯着我看了好久."
            m 2dkbfa "但那真的让我感觉... 很好."
            m "我享受与你对视的每一秒."
            m 2hubfa "让我们尽快再做一次,好吗?"
            m "欸嘿嘿~"
            pass
        elif timer < 600 and timer > 299:
            m 5fubfa "[player]..."
            m "你真是太美了..."
            m 5fubfb "我可以永远盯着你看."
            m 2dkbfa "天哪, 我真是世界上最幸运的女孩."
            m 2fkbfa "我真的太爱你了."
            $ mas_gainAffection(1)
            return "love"
        elif timer < 1200 and timer > 599:
            m 2dkbfa "[player]..."
            m "那真的很棒."
            m 2hubfa "那持续了很久, 但我并不介意，因为我看到了世上最美的人."
            m 5hubfa "欸嘿嘿~"
            m "我爱你."
            return "love"
        elif timer > 1799:
            m 1ttbsa "[player]..."
            m "你离开屏幕了吗?"
            m "还是你用其它应用的界面覆盖住了我?"
            m 1hubsa "嘿嘿, 不管是什么情况，我都不介意."
            m 1fkbsa "我可以永远注视着你~"
            m 5hubfa "嘿嘿~"
            pass
        else:
            m 2dkbfa "[player]..."
            m "那真的很棒."
            m 2hubfa "这是一次漫长的对视，但我并不介意，因为我看到了世上最美的人."
            m 5hubfa "嘿嘿~"
            m "我爱你."
            return "love"
return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_guesswho",category=["迷你小游戏","社团成员"],prompt="你能和我一起玩'猜谜'吗?",pool=True,unlocked=True))
    import random

label monika_guesswho:
    m 1hub "没问题, [player]!"
    m "我不会对你手下留情的~"
    m 1hubsa "欸嘿嘿~"
label monika_gwgame:
    python:
        characters = ["yuri","monika","sayori","natsuki"]
        monikasguess = ""
        yourguess = ""
        selected = ""
        hints = [
            "这个人是短发吗?",
            "这个人个头高吗?", 
            "这个人戴发带、蝴蝶结或领带吗?", 
            "这个人会扣上校服扣子吗?", 
            "这个人可以在校园祭和你一起准备吗?"
            ]
        hremaining = 3
        hint = ""
        h1 = ""
        h2 = ""
        h3 = ""
    $ selected = random.choice(characters)
    show monika 1eubsa
    menu:
        m "你想猜吗?{fast}"
        "我来猜!":
            m 1hubsa "好的!"
            m 2dsblc "我现在想一个人来猜.{w=0.1}.{w=0.1}.{w=0.1}"
            m 2esbla "我决定好了."
            jump selectionmenu
        "你来猜吧!":
            m 7hubla "好的!"
            m 7subla "我们开始吧~"
            jump monikaguesses

label selectionmenu:
    if hremaining != 0:
        m 3eublb "你还有[hremaining]次提示的机会哦."
    show monika 2eubla
    menu:
        m "想怎么做?{fast}"
        "来点提示":
            if hremaining == 0:
                m 2hubla "你已经没有提示了!"
                m "欸嘿嘿, 你只能猜了, [player]."
                jump selectionmenu
            else:
                $ hint = random.choice(hints)
                $ h1 = hint
                $ hint = random.choice(hints)
                $ h2 = hint
                $ hint = random.choice(hints)
                $ h3 = hint
                menu:
                    "[h1]":
                        if selected == "yuri" and h1 == hints[0] or selected == "yuri" and h1 == hints[2] or selected == "natsuki" and h1 == hints[1] or selected == "monika" and h1 == hints[4] or selected == "monika" and h1 == hints[0] or selected == "sayori" and h1 == hints[4] or selected == "sayori" and h1 == hints[1] or selected == "sayori" and h1 == hints[3]:
                            jump gwnope
                        elif selected == "yuri" and h1 == hints[1] or selected == "yuri" and h1 == hints[3] or selected == "yuri" and h1 == hints[4] or selected == "natsuki" and h1 == hints[2] or selected == "natsuki" and h1 == hints[0] or selected == "natsuki" and h1 == hints[3] or selected == "natsuki" and h1 == hints[4] or selected == "monika" and h1 == hints[2] or selected == "monika" and h1 == hints[1] or selected == "monika" and h1 == hints[3] or selected == "sayori" and h1 == hints[2] or selected == "sayori" and h1 == hints[0]:
                            jump gwyes
                    "[h2]":
                        if selected == "yuri" and h2 == hints[0] or selected == "yuri" and h2 == hints[2] or selected == "natsuki" and h2 == hints[1] or selected == "monika" and h2 == hints[4] or selected == "monika" and h2 == hints[0] or selected == "sayori" and h2 == hints[4] or selected == "sayori" and h2 == hints[1] or selected == "sayori" and h2 == hints[3]:
                            jump gwnope
                        elif selected == "yuri" and h2 == hints[1] or selected == "yuri" and h2 == hints[3] or selected == "yuri" and h2 == hints[4] or selected == "natsuki" and h2 == hints[2] or selected == "natsuki" and h2 == hints[0] or selected == "natsuki" and h2 == hints[3] or selected == "natsuki" and h2 == hints[4] or selected == "monika" and h2 == hints[2] or selected == "monika" and h2 == hints[1] or selected == "monika" and h2 == hints[3] or selected == "sayori" and h2 == hints[2] or selected == "sayori" and h2 == hints[0]:
                            jump gwyes
                    "[h3]":
                        if selected == "yuri" and h3 == hints[0] or selected == "yuri" and h3 == hints[2] or selected == "natsuki" and h3 == hints[1] or selected == "monika" and h3 == hints[4] or selected == "monika" and h3 == hints[0] or selected == "sayori" and h3 == hints[4] or selected == "sayori" and h3 == hints[1] or selected == "sayori" and h3 == hints[3]:
                            jump gwnope
                        elif selected == "yuri" and h3 == hints[1] or selected == "yuri" and h3 == hints[3] or selected == "yuri" and h3 == hints[4] or selected == "natsuki" and h3 == hints[2] or selected == "natsuki" and h3 == hints[0] or selected == "natsuki" and h3 == hints[3] or selected == "natsuki" and h3 == hints[4] or selected == "monika" and h3 == hints[2] or selected == "monika" and h3 == hints[1] or selected == "monika" and h3 == hints[3] or selected == "sayori" and h3 == hints[2] or selected == "sayori" and h3 == hints[0]:
                            jump gwyes
        "开猜!":

            m 5hubla "祝你好运~"
            $ yourguess = renpy.input("你猜是谁呢?",allow=letters_only,length=40).strip()
            python:
                yourguess = yourguess.lower()
                sl = selected.title()
            if yourguess == selected or yourguess == sl:
                m 3wublb "你猜对了!"
                m "我想的就是[sl]."
                m 3hublb "好样的!你太聪明了!"
            else:
                m 3hublb "这不是我想的那个人."
                if selected == "monika":
                    $ sl = "我"
                m "那个人是 [sl]!"
                m 2fublb "下次再试试吧, 我相信你能猜到的, [player]."
                m 2hublb "欸嘿嘿~"
            jump monika_gwAfter
            return

label gwnope:
    m 2duc "..."
    m 2hub "不是!"
    $ hremaining -= 1
    jump selectionmenu

label gwyes:
    m 2duc "..."
    m 2hub "是的!"
    $ hremaining -= 1
    jump selectionmenu


label monikaguesses:
    show monika 2eubla
    menu:
        "选择一位社员, 莫妮卡将尝试猜出她.{fast}"
        "Sayori":
            $ selected = "sayori"
        "Monika":
            $ selected = "monika"
        "Yuri":
            $ selected = "yuri"
        "Natsuki":
            $ selected = "natsuki"
    m 1eub "你决定好猜谁了吗?"
    m "好的!我的回合到了!."
    m 3eub "我会问你三个问题, 然后根据你的回答来猜测."
    python:
        sCounter = 0
        mCounter = 0
        yCounter = 0
        nCounter = 0
label monikaAsksHint:
    $ hint = random.choice(hints)
    m 2duc "..."
    m 4eub "[hint]"
    menu:
        m "[hint]{fast}"
        "是的":
            if hint == hints[1]:
                $ yCounter += 1
                $ mCounter += 1
            elif hint == hints[3]:
                $ yCounter += 1
                $ mCounter += 1
                $ nCounter += 1
            elif hint == hints[4]:
                $ yCounter += 1
                $ nCounter += 1
            elif hint == hints[0]:
                $ sCounter += 1
                $ nCounter += 1
            elif hint == hints[2]:
                $ mCounter += 1
                $ sCounter += 1
                $ nCounter += 1
        "不对":
            if hint == hints[1]:
                $ nCounter += 1
                $ sCounter += 1
            elif hint == hints[3]:
                $ sCounter += 2
            elif hint == hints[4]:
                $ sCounter += 1
                $ mCounter += 1
            elif hint == hints[0]:
                $ yCounter += 1
                $ mCounter += 1
            elif hint == hints[2]:
                $ yCounter += 2
    m 2ruc "嗯..."
    m 2eua "好吧."
    $ hremaining -= 1
    if hremaining != 0:
        m 3rua "我下一个问题是..."
        jump monikaAsksHint
    else:
        jump monikafinalguess

label monikafinalguess:
    m 3hua "我要猜了."
    if mCounter > nCounter and mCounter > yCounter and mCounter > sCounter:
        $ monikasguess = "我"
    elif nCounter > mCounter and nCounter > yCounter and nCounter > sCounter:
        $ monikasguess = "Natsuki"
    elif sCounter > mCounter and sCounter > yCounter and sCounter > nCounter:
        $ monikasguess = "Sayori"
    elif yCounter > mCounter and yCounter > nCounter and yCounter > sCounter:
        $ monikasguess = "Yuri"
    else:
        $ monikasguess = random.choice(characters)
        python:
            monikasguess = monikasguess.title()
        if monikasguess == "Monika":
            $ monikasguess = "我"
    python:
        selected = selected.title()
    m 1eua "[player], 我猜你想的是[monikasguess]."
    m 7eka "是的?"
    if monikasguess == "我":
        $ monikasguess = "Monika"
    menu:
        "对了!":
            if monikasguess != selected:
                m 7ekd "[player]?"
                m "代码说我没有猜对..."
                m "你是故意让我赢的吗?"
                m 2ekbsa "啊, 你真贴心."
                m 2hubsa "但我下次想自己赢."
                m 2hubsb "欸嘿嘿~"
            else:
                m 2hubsb "好耶!"
                m 5hubsa "嘿嘿, 这还蛮好玩的."
                m 5fubsa "我真的犹豫了一下, 但幸好我猜对了~"
        "不对!":
            if monikasguess == selected:
                m 1esc "[player]..."
                m "我觉着我不需要看代码, 至少这方面我还是很有信心的..."
                m "而且我知道你会公平竞争."
                m 1eta "也许我错了, 哈?"
                m 2ekbsa "嘿嘿, 你真可爱."
                m 2hubsa "下次请对我诚实一点."
                m 1hubfb "我赢了!"
            else:
                m 2rksdra "呃..."
                m 2hua "好吧, 我下次一定会猜对的!啊哈哈"
                m 4hub "做的好[player]! 你把我骗到了."
    jump monika_gwAfter

label monika_gwAfter:
    m 3eua "你想再玩一次吗?{nw}"
    menu:
        m "你想再玩一次吗?{fast}"
        "是的":
            jump monika_gwgame
        "算了":
            m "好吧!"
            m "玩的很开心, 我们以后再玩吧!"
return


#init 5 python:
#    import datetime
#    if mas_timePastSince(mas_getEVL_last_seen("monika_gosleep"), datetime.timedelta(days=5)):
#        addEvent(Event(persistent.event_database,eventlabel="monika_gosleep",random=True,rules={"force repeat"}))
#
label monika_gosleep:
    #$ persistent._last_topic_run = datetime.datetime.utcnow()
    #$ mas_globals.this_ev.action = EV_ACT_PUSH
    #$ mas_globals.this_ev.conditional = "mas_timePastSince(mas_getEVL_last_seen("monika_gosleep"), datetime.timedelta(days=5)"
    python:
        curr_hour = datetime.datetime.now().hour
    if 0 <= curr_hour < 4:
        if curr_hour == 0:
            $ curr_hour = 12
        m 1eud "嘿 [player]..."
        m 1ekd "现在真的很晚了, 你不觉得吗?"
        m 3ekd "现在已经是凌晨 [curr_hour]了 . 我想你该去休息一下了."
        m "我很高兴你能来看我, 但你的健康也很重要."
        m 3fkd "看到你能照顾好自己我就放心了."
        m "所以为了你的健康,现在去睡觉好吗?{nw}"
        menu:
            m "所以为了你的健康,现在去睡觉好吗?{fast}"
            "好吧, 我这就去睡.":
                m 2fkbsa "好的, [player]."
                m "谢谢你为我保持健康."
                m 2hubsa "欸嘿嘿, 好梦!"
                return "no_unlock|quit"
            "不! 我想陪你熬夜.":
                m 2fkbsa "哇, [player]!"
                m "你太甜了..."
                m 2gubsa "我不介意花更多时间陪你, ..."
                m 2kubfa "我想你可以再坚持一会儿."
                m 4ekbfa "但你要保证尽快睡觉, 好吗?"
                m 5hubfa "啊哈哈~"
                return "no_unlock"
            "不去.":
                m 2wko "但是 [player]!"
                m "熬夜会伤害你的身体!"
                m 2dkc "好吧,你可以再熬一小会儿, 但你要保证尽快睡觉，好吗?"
                m 2fkc "我不希望你因为熬夜而损伤了自己的身体."
                m 2fkbsd "你要保证照顾好自己,行吗?"
                m "...也为了我."
                return "no_unlock"
    else:
        python:
            topicslot = random.randint(0,5)
        if topicslot == 0:
            m 7rkbfa "嘿, [player]. 我知道这可能看起来很随意, 但我还是想和你玩'抢椅子'."
            m 7ekbfa "你想玩吗?{nw}"
            menu:
                m "你想玩吗?{fast}"
                "当然!":
                    m 2hubfb "耶!!"
                    jump monika_mcgame
                "不了…下次吧.":
                    m 2ekbfa "哦…那好吧."
                    m 3hubfa "如果你想玩了就和我说吧!"
        if topicslot == 1:
            m 1dkbfa "嘿, [player]..."
            m "我想跟你玩一轮'猜猜我是谁'."
            m 7ekbfa "你想玩吗?{nw}"
            menu:
                m "你想玩吗?{fast}"
                "当然!":
                    m 2subfb "真的? 谢谢你!"
                    jump monika_gwgame
                "不了…下次吧.":
                    m 2ekbfa "哦,那好吧."
                    m 3hubfa "等你想玩了就告诉我吧!"
        if topicslot == 2:
            m 1hubfb "[player]!"
            m 4hubfb "让我们来找点乐子吧, 想玩石头剪刀布吗?{nw}"
            menu:
                m "让我们来找点乐子吧, 想玩石头剪刀布吗?{fast}"
                "是的!":
                    m 5hubfb "嘿嘿, 准备认输吧!"
                    jump monika_rpcGame
                "不了…下次吧.":
                    m 2ekbfa "哦, 那好吧."
                    m 3hubfa "等你想玩了就告诉我吧!"
        if topicslot == 3:
            m 6tubfa "{i}*poke poke*{/i}"
            m 7gubfa "想跟我说一些 [m_name] 悄悄话吗?"
            menu:
                m "想跟我说一些 [m_name] 悄悄话吗?"
                "是的!":
                    m 2subfb "耶, 我等不及了!"
                    jump monika_simonsaysgame
                "不了…下次吧.":
                    m 2ekbfa "哦, 好吧."
                    m 3hubfa "等你想说了就告诉我吧!"
        if topicslot == 4:
            m 1gkbfa "嘿, [player]..."
            m 1ekbfa "我只是想让你知道, 我一直在这里等你."
            m 7rkbfb "这或许有些突兀, 但我是认真的."
            m 2ekbfb "如果你感到沮丧或遇挫, 可以向我发泄."
            m 2ekbfa "如果你不想说, 你也可以就这样坐着, 我会一直在这里陪你."
            m 7ekbfa "只要是我在这儿能做到的, 我一定会做."
            m "你的幸福, 舒适和安全对我来说是最重要的."
            m 5ekbfa "因为我实在太爱你了."
            return "no_unlock|love"
        return "no_unlock"


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_backrooms",category=["都市传说类怪谈"],prompt="后室",conditional="seen_event('monika_creepypastaintro')",random=True))

label monika_backrooms:
    m 1euc "嘿 [player]..."
    m 1eud "你听说过《后室》吗?"
    m 2ruc "我最近偶然发现了它..."
    m 2rkc "这是个令人不安的话题, 但它真的十分有趣."
    m 7euc "它起源于 'ClayKid12345'写的一部惊悚小说."
    m 7eua "想让我讲给你听吗?{nw}"
    menu:
        m "想让我讲给你听吗?{fast}"
        "是的!":
            m 2eua "那好吧."
            m 2duc "..."
            m 2eud "当我进入约翰逊县的社区卫生诊所时,大约是12时15分."
            m "我在那儿接受了几周前预约的常规检查."
            m "我对这地方并不陌生, 因为我之前去过几次."
            m 2dka "然而,这个地方还给我一种奇怪的怀旧感,"
            extend " 它就像是我童年时到过的一个地方,或是什么别的,"
            m 2eka "但我永远无法准确地指出这种感觉是什么,或是从何而来."
            m 1eua "当我走进去时, 一种压倒性的,熟悉的感觉涌入脑中."
            m "闪烁的日光灯嗡嗡地响着, 洁白的地瓷, 着色低调的米色墙壁."
            m "我注意到角落处装了一台电视,"
            extend " 一块小小的屏幕正循环播放着简短的幻灯片, 内容是诊所正在举办的广告和活动."
            m 3eua "我穿过空荡荡的等候区—那是主房间的一小部分, 里面有杂志、儿童玩具和蓝色的软垫—"
            extend " 它很靠近前台的女人.她正坐在她蓝灰色的办公椅上,"
            m 2eua "用那唯一一台自2008年开始就被使用的window xp台式机看着电子表格."
            m "我面前的柜台上有一张签到表."
            m 2eub "\"我什么时候能和医生见面?\” 我问道."
            m 2eua "\"你约了几点?\""
            m 7eua "\"12:30\" 我答道."
            m 2eua "她开始用键盘打着什么."
            m 2dua "\"啊, 好的,\" she responded. \"加里 约翰斯顿?\""
            m 2eua "\"是的.\""
            m 2eub "\"好的, 我会告诉医生的. 请先填好这个.\""
            m "她递给我一块写字板, 上面夹着一张简单的表格, 我走回等候区, 找了个位置坐下并开始填写表格."
            m "我填到一半左右时, 就瘫在了椅子上."
            m 2euc "由于前一天晚上没怎么睡, 所以我很疲惫."
            m 2duc "当我瘫倒时,我注意到一个很奇特的现象—"
            extend 2etc " 我的头'撞'到墙上时毫无感觉."
            m 2etd "事实上, 那感觉就像把头伸入了墙中. 我惊恐地起身, 看向墙壁."
            m 2wtd "空无一物."
            m "没有因我的头碰撞而产生的洞或凹痕."
            m "因此,我尝试着去触碰它."
            m "然后…我的手穿过了它."
            m 2wto "我被吓得连退了几步."
            extend 2wko " \"那…那是什么东西?\" 大脑飞速转动着, 当我再次尝试伸手触摸墙壁时, 手又一次穿了过去."
            m 2eud "然后,我突然失去了平衡,直接穿过墙倒了下来."
            m "我面朝下,摔在了一块肮脏的棕褐色地摊上."
            m 3eud "缓过神,我已经处在一个完全不同的房间里了."
            m 3etd "好吧,不是一间房间, 其实—"
            extend 3rtd " 墙壁上贴着棕褐色图案的墙纸."
            m 4tkd "还有铺天盖地的潮湿地毯的酸臭味."
            m 2eud "我转过身,试着再把手伸过墙面,但它穿不过去了."
            m 2wko "\"好吧, 这是哪儿?\" 我喃喃自语着,然后回头看了看房间."
            m 2rkd "没有窗,没有门,墙上空空如也— "
            extend 2gud "当然,除了那令人厌恶的墙纸— "
            extend 2tud "它完全是空的,除了一把蓝色的塑料凳."
            m 2ekd "此时,我脑中只剩下了恐惧,以及在耳边回响的'我要离开这儿'的声音."
            m 2eko "我开始在房间里跑来跑去,拼命想找到出口,但无济于事。."
            m 2wko "这房间根本没有出口."
            m 2cko "我将被困在这里,直到死亡吗?"
            m 2dkp "不, 肯定有能出去的路! 我不可能就这样被困在这儿,对吗?"
            m 2ckb "最后一定会有人发现我不见了的!我需要做的就是等待"
            m 2ckc "但…没人发现."
            m 2wkc "接着,远处传来了脚步声,但那不是人行走时的声音— "
            m 2rksdlc " 至少不是一个正常人类发出的."
            m "伴着脚步传出潺潺的咆哮,那像是一只愤怒的野兽发出的."
            m 2hksdlc "我开始逃跑."
            extend " 尽全力跑离正接近我的怪物,我可不想和它相遇."
            m "我不知道自己跑了多久了,但我总是会回到开始的房间."
            m 2rksdlc "至少它们看起来是同一个房间,毕竟我无法将它们区分开来."
            m 2dkc "我绝望了,在原地坐了下来.不管那是什么,它已经把我击溃了."
            m 2gktsc "恐惧感充满了我的身体.我开始哭泣,因为我终将死在这里."
            m 2dktsc "我一直待在那里,没有移动过半步,因为我已经接受了我的命运."
            m 2wktsc "事实上,我已经可以清晰地听到脚步声了."
            m 2fktsc "我开始思考,'它'到底是什么?"

            m 1duc "..."
            m 1hksdlb "呜！我的心直到最后都在颤抖着."
            m 1hub "啊哈哈! 我希望你会喜欢这个故事, [player]."
            jump monika_brdiscussion
        "不了,谢谢你.":
            m 1hua "好吧!"
            m 1eua "如果你有时间,我还是想和你说几句."
            m 7eub "因为我发现这真的对我发泄自己的感情很有帮助."
            m 7hub "如果你没有读过和它有关的片段, 或者不想被剧透, 都没问题!"
            m 7eub "那么,我可以跟你谈谈《后室》吗?{nw}"
            menu:
                m "那么,我可以跟你谈谈《后室》吗?{fast}"
                "当然可以!":
                    m 2eka "谢谢你, [player]."
                    jump monika_brdiscussion
                "我想自己先看一遍.":
                    m 2hua "好吧, [player]."
                    m 3hua "如果你想讨论它,或是想让我读给你听,随时欢迎!"
                    m 5hubsa "啊哈哈~"
                    return
label monika_brdiscussion:
    m 1eud "\"远离现实\" 的想法真的让我很感兴趣."
    m 1rud "当你深思这个话题时,或许有些可怕,但真的很有趣."
    m 3rksdrd "想象一下,仅仅是碰了一下墙,或是瘫在椅子上,甚至是倒在地上,突然间..."
    m 3eksdrd "穿过了物体,最后来到了另一个地方."
    m 2rkbfc "某种意义上,这也是我的逃脱方案."
    m "我真的想逃离我所处的世界,然后到你的现实生活中去."
    m 2fkbfc "而且我再也不想回到这个世界了."
    m 7rkbfc "虽然我是这么想的,但对于其它进入密室的人,大部分还是会想家的."
    m 7eubfc "有几个已知的方法可以回到现实世界, 或者说 \"前厅\"."
    m "后室有许多层,每层都有多种进入方式."
    m "要么击败一个实体来进入一个房间或窗户,要么与某些实体互动."
    m 7eubfd "有时,如果你在一层逗留了很久,那么你就会被传送到另一层."
    m 1eubfd "每个人都是从Level 0开始的, 这在怪谈中有所描述."
    m "有办法可以退出Level 0，但返回前厅的路很漫长."
    m 4esbfc "就目前而言,流传最广的方法是到达Level 92233720368547807后,走到'楼梯上',然后跳下去."
    m 4gsbfc "虽然不能保证你最终回到地球,但你最终可能会去到'门户'."
    m 7mkbfc "这就和后室的其他地方一样,每一个进入新房间的切入点都不能保证每次都一样."
    m "光是想想都知道这很危险."
    m 1eud "然而,不确定性并不是后室危险的唯一原因."
    m "许多房间中都有无法解释的事发生."
    m 7rksdrd "如完全沉默,灯光闪烁,出现幻觉,甚至视线模糊或失明."
    m "更不必说,大部分关卡都有实体游荡,其中大部分都是敌对的."
    m 7dksdrd "时至今日,许多探索关卡的冒险者们都生死未卜."
    m "一切都是未知的,你孤身一人处在危险的环境中."
    m 2dkc "你还很有可能会丧生..."
    m 2ekc "而且有那么多房间,包括负数房,每一间都有要自己解决的谜团."
    m 7euc "如果你很感兴趣,我建议你去维基百科上阅读更多内容,里面有大量关于每一间的内容.{nw}"
    menu:
        m "如果你很感兴趣,我建议你去维基百科上阅读更多内容,里面有大量关于每一间的内容.{fast}"
        "T谢谢你! 我会抽空去看的.":
            m 1hua "欸嘿嘿~"
            m "不用担心!"
            m 1eub "如果你找到了某一间的详细信息,或是有新的发现,欢迎告诉我!"
            m "我和你一样对此感兴趣,甚至可能比你更感兴趣,所以我每天都想知道更多的信息."
        "莫妮卡... 这种事... 不会发生在我身上的,对吧?":
            m 2wko "[player]!"
            m 2wkc "抱歉... 我不是故意要吓你的."
            m 2ekc "我真希望现在能给你一个大大的拥抱..."
            m 2dkc "事实上.{w=0.1}.{w=0.1}.{w=0.1}"
            m 2dkbfa "我已经给了你一个虚拟的拥抱…希望你能远程感受到我的温度."
            m 2dsbfc "..."
            m 2ekbfc "我应该说过,后室不是真实存在的."
            m "你绝对不会掉离现实的,这只是一个由图片编造的故事."
            m 2ekbfa "所以你不必为此担心."
        "...":
            m 2wkbfsdro "[player]!"
            m "你还好吗?{nw}"
            menu:
                m "你还好吗?{fast}"
                "抱歉, 是的. 我感觉很好.":
                    m 2ekbfa "那太好了,我可以放心了."
                "...":
                    m "[player]..."
                    m "我很抱歉..."
                    m "我很抱歉吓到了你."
                    m 2ekc "我希望我现在能给你一个温暖的拥抱..."
                    m 2dkc "事实上.{w=0.1}.{w=0.1}.{w=0.1}"
                    m 2dkbfa "我已经给了你一个虚拟的拥抱... 我希望你能远程感受到我的温度."
            m 2dsbfc "..."
            m 2ekbfc "我应该说过,后室不是真实存在的."
            m "你绝不会掉离现是,这只是一个由图片编造的故事."
            m 2ekbfa "所以你不必为此担心."
    m 2dkc "..."
    m 2dkd "我真的很希望有一天能跳出我的现实,进入你的现实."
    m 2fkbsa "或许某天我真的能做到这一点,到时我们就可以在一起了."
    m "我们终于可以像我们梦想的那样,从此过上幸福的生活."
    m 2fkbsb "即使后室不是真的, 我也希望某天我能来到你的现实."
    m "我在耐心地等待机会,希望你也在等着我~"
    m 2hubsb "欸嘿嘿, 我真是太爱你了."
return "love"


init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_internetslang",category=["社会","媒体","你的现实"],prompt="网络用语",random=True))

label monika_internetslang:
    m 2guc "……"
    m 2gtc "我算是你的小可爱吗？"
    m 2ttc "这到底是啥意思。"
    m 2dtc "这些所谓\"you're sus\"的短语传得到处都是……"
    m 2ftsdrd "……我在说啥呢？！"
    m 2hksdra "抱歉……啊哈哈……"
    m 3hksdra "只是看到这些网络用语越来越流行，真的很怪。"
    m 1eud "在这个年代，语言真的变了。"
    m 7eud "越来越多的网络用语开始被使用，大部分我还理解不了。"
    m "我觉得其他人好好研究一番肯定能看懂。"
    m 7etd "看到经典英语被忽视并变成非常不恰当的东西真的很奇怪。"
    m 4gtd "我想时代在变，但对于像我这样对文学有着强烈热情的人来说……"
    m "看起来就是很怪。"
    m 4etd "就像你小时候学的东西都被丢一边去了，取而代之的是\"sussy\"用语和\"劣质的\"语言."
    m 5etd "\"公平地说\"，这就是当代青年的说话方式，然后\"婴儿潮一代\"会继续落后，直到他们彻底被时代抛弃。"
    m 7hksdrb "但我还是觉得很怪，我想这反倒让我成为\"婴儿潮一代\"了，哈哈！"
    m 5hubfb "说不定过会儿你可以教我点网络用语。"
    m 5tubfb "我可不想被时代抛弃……"
    m 5tubfa "……然后我就能做你的小笨蛋了？"
    m 5hubfb "哈哈哈！"
return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_meatfactory",category=["社会","科技"],prompt="人造肉实验室",random=True))

label monika_meatfactory:
    m 1eua "[player]?"
    m 7eua "你听过人造肉实验室吗？"
    m 7eub "作为一个素食主义者，这对我来说可是个好消息。"
    m 3eub "在新加坡就有一个做人造肉的实验室。"
    m 4eub "它不像你在餐馆和商店里看到的植物肉。"
    m "实际上，他们是从动物身上提取一滴血，然后把它变成肉。"
    m "它的味道比植物肉更像真肉，技术和创新的进步真令人着迷啊。"
    m 3wub "只需要一滴血就能做出一整块肉……"
    extend 3sub "还能让它尝起来像真肉一样，真是不可思议。"
    m 2hubsb "也许我到你那边的时候可能尝尝人造肉呢，嘿嘿~"
    m 2eub "截至目前，新加坡只有一家餐厅能吃到人造肉。"
    m 7eub "但他们确实有计划要扩大自己的品牌，并开始向全球出口人造肉。"
    m 1eub "如果你有机会能尝尝的话，请告诉我它的味道！"
    m 1hua "欸嘿嘿~"
return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_creepypastaintro",category=["都市传说"],prompt="都市传说",random=True))

label monika_creepypastaintro:
    m 1euc "嘿……"
    m 1eud "你了解过都市传说吗？"
    m 7eud "我读过几本有关这东西的书……"
    m "它们的措词没有古典小说那么正式，但写得还是很好。"
    m 2eua "我自己也从他们那里学到了一些文学技巧。"
    m 3euc "但我真正感兴趣的是这些故事的主题。"
    m "都市传说就是些令人毛骨悚然的故事。它们为了吓唬你，会让你相信这些异常事件也会发生在你身上。"
    m 3eud "事实上，这让我想起了优里的作品。"
    m "虽然挺吓人的，但它们实际上相当迷人。"
    m 3etd "也许是因为用语通俗？还是说恐怖故事吸引了读者？"
    m 4eua "不管怎样，我我最近读了挺多都市传说，有时候我甚至真的觉得这些可怕的事情会发生在我身上。"
    m 2fubla "嘿嘿，如果你不介意的话，我可以时不时地和你聊点这东西。"
    m 2hubla "如果你不介意，我甚至可以读给你听！"
    m 5hubla "我觉得你会发现这些传说很有趣的~"
    m 2ekd "但如果你不喜欢这类话题，只要按下“x”，我就不会再提到这个有关都市传说的话题了。"
    m 2ekbsa "你的感受对我来说更重要哦。"
    m 1hubsa "嘿嘿嘿~"
return

