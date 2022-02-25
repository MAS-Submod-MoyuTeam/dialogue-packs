
image c1 = "Submods/Dialogue Packs/chess_teaching/images/1.jpg"
image c2 = "Submods/Dialogue Packs/chess_teaching/images/2.jpg"
image c3 = "Submods/Dialogue Packs/chess_teaching/images/3.jpg"
image c4 = "Submods/Dialogue Packs/chess_teaching/images/4.jpg"
image c5 = "Submods/Dialogue Packs/chess_teaching/images/5.jpg"
image c6 = "Submods/Dialogue Packs/chess_teaching/images/6.jpg"
image c7 = "Submods/Dialogue Packs/chess_teaching/images/7.jpg"
image c8 = "Submods/Dialogue Packs/chess_teaching/images/8.jpg"
image c9 = "Submods/Dialogue Packs/chess_teaching/images/9.jpg"
image c10 = "Submods/Dialogue Packs/chess_teaching/images/10.jpg"
image c11 = "Submods/Dialogue Packs/chess_teaching/images/11.jpg"
image c12 = "Submods/Dialogue Packs/chess_teaching/images/12.jpg"
image c13 = "Submods/Dialogue Packs/chess_teaching/images/13.jpg"
image c14 = "Submods/Dialogue Packs/chess_teaching/images/14.jpg"
image c15 = "Submods/Dialogue Packs/chess_teaching/images/15.jpg"
image c16 = "Submods/Dialogue Packs/chess_teaching/images/16.jpg"
image c17 = "Submods/Dialogue Packs/chess_teaching/images/17.jpg"
image c18 = "Submods/Dialogue Packs/chess_teaching/images/18.jpg"
image c19 = "Submods/Dialogue Packs/chess_teaching/images/19.jpg"
image c20 = "Submods/Dialogue Packs/chess_teaching/images/20.jpg"
image c21 = "Submods/Dialogue Packs/chess_teaching/images/21.jpg"
image c22 = "Submods/Dialogue Packs/chess_teaching/images/22.jpg"
image c23 = "Submods/Dialogue Packs/chess_teaching/images/23.jpg"
image c24 = "Submods/Dialogue Packs/chess_teaching/images/24.jpg"
image c25 = "Submods/Dialogue Packs/chess_teaching/images/25.jpg"
image c26 = "Submods/Dialogue Packs/chess_teaching/images/26.jpg"
image c27 = "Submods/Dialogue Packs/chess_teaching/images/27.jpg"
image cb0 = "Submods/Dialogue Packs/chess_teaching/images/B0.jpg"
image cb1 = "Submods/Dialogue Packs/chess_teaching/images/B1.jpg"
image cb2 = "Submods/Dialogue Packs/chess_teaching/images/B2.jpg"
image cb3 = "Submods/Dialogue Packs/chess_teaching/images/B3.jpg"
image cb4 = "Submods/Dialogue Packs/chess_teaching/images/B4.jpg"
image cb51 = "Submods/Dialogue Packs/chess_teaching/images/B5.1.jpg"
image cb5 = "Submods/Dialogue Packs/chess_teaching/images/B5.jpg"
image cb6 = "Submods/Dialogue Packs/chess_teaching/images/B6.jpg"
image cb7 = "Submods/Dialogue Packs/chess_teaching/images/B7.jpg"
image cb8 = "Submods/Dialogue Packs/chess_teaching/images/B8.jpg"
image cb9 = "Submods/Dialogue Packs/chess_teaching/images/B9.jpg"
image cb10 = "Submods/Dialogue Packs/chess_teaching/images/B10.jpg"
image cb11 = "Submods/Dialogue Packs/chess_teaching/images/B11.jpg"
image cb12 = "Submods/Dialogue Packs/chess_teaching/images/B12.jpg"
image cb13 = "Submods/Dialogue Packs/chess_teaching/images/B13.jpg"
image cb14 = "Submods/Dialogue Packs/chess_teaching/images/B14.jpg"
image cb15 = "Submods/Dialogue Packs/chess_teaching/images/B15.jpg"
image cb16 = "Submods/Dialogue Packs/chess_teaching/images/B16.jpg"
image cb17 = "Submods/Dialogue Packs/chess_teaching/images/B17.jpg"
image cb18 = "Submods/Dialogue Packs/chess_teaching/images/B18.jpg"
image cb19 = "Submods/Dialogue Packs/chess_teaching/images/B19.jpg"
image cb20 = "Submods/Dialogue Packs/chess_teaching/images/B20.jpg"
image cb21 = "Submods/Dialogue Packs/chess_teaching/images/B21.jpg"
image cb22 = "Submods/Dialogue Packs/chess_teaching/images/B22.jpg"
image cb23 = "Submods/Dialogue Packs/chess_teaching/images/B23.jpg"
image cb24 = "Submods/Dialogue Packs/chess_teaching/images/B24.jpg"
image cb25 = "Submods/Dialogue Packs/chess_teaching/images/B25.jpg"
image cb26 = "Submods/Dialogue Packs/chess_teaching/images/B26.jpg"
image cb27 = "Submods/Dialogue Packs/chess_teaching/images/B27.jpg"
image cb28 = "Submods/Dialogue Packs/chess_teaching/images/B28.jpg"
image cb29 = "Submods/Dialogue Packs/chess_teaching/images/B29.jpg"
image cb30 = "Submods/Dialogue Packs/chess_teaching/images/B30.jpg"
image cb31 = "Submods/Dialogue Packs/chess_teaching/images/B31.jpg"
image cb32 = "Submods/Dialogue Packs/chess_teaching/images/B32.jpg"
image cb33 = "Submods/Dialogue Packs/chess_teaching/images/B33.jpg"

label ch0_start:
    show c1:
        size(512,512)
        pos(0,0)
    "end"

init 4 python in mas_ctod:
    # to simplify unlocking, lets use a special function to unlock tips
    import datetime
    import store.evhand as evhand

    M_CTOD = "monika_Mchess_{:0>3d}"
    #CTOD:Monika Chess Tip of the Day

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
            M_CTOD.format(tip_num),
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

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_Mchess_001",
            category=["国际象棋"],
            prompt="1.来玩国际象棋吧",
            pool=True,
            conditional="mas_isGameUnlocked(\"chess\") or mas_isGameUnlocked(\"国际象棋\")",
            action=EV_ACT_UNLOCK
        )
    )

label monika_Mchess_001:
    m 1wuc "欸?"
    m 2tua "..."
    m 2tub "我想你一定是觉得赢不了我才试图找一些教程吧?"
    menu:
        "我想你一定是觉得赢不了我才试图找一些教程吧?"
        "是的...":
            m 3kub "别怕, 我会手把手教你如何击败我, 然后再用棋盘告诉你我是无敌的~"
            m 7eua "但在此之前, 我想先和你聊一聊棋盘外的一些事情."
            m 3kub "首先, 你要明白一件事:你正在和你最可爱的女朋友下象棋~"
            m 3eka "因此, 无论输赢我都希望你能开心."
            m 2eub "而我也会根据对弈结果调整你的游戏难度."
            m 1rka "如果你到现在为止依然没有赢过我, 请相信不是我在有意战胜你, 而是你还没有熟悉这个游戏."
            m 3eub "其次, 我使用的国际象棋AI引擎是'Stockfish', '鳕鱼'."
            m 2rtd "说实话, 在认识你之前我并不怎么会下象棋...但如今的我可以操纵鳕鱼.."
            m 3eub "我能通过代码让鳕鱼告诉我该怎么走, 我也可以通过代码调整AI引擎的强度."
            m 4hksdla "让你可以在与我对弈的过程中提高自己的棋力, 而不是被鳕鱼单方面欺负..."
            m 3wud "实际上, 极限状态下的鳕鱼可以战胜当前世界上的任何一位特级大师!"
            m 2rta "因此, 等到你能轻松战胜我的时候, 或许你也可以参加特级大师的选拔?" ##TK:那多半是想太多(:T
            m 3eub "最后, 我希望你能牢记本系列课程最大的要点'AI的思考方式与人不同'."
            m 4rkb "相比于与人对弈而言, 与AI对弈不管是游戏难度还是思考压力都要更大..."
            m 3wuc "和人类玩家相比, AI几乎不需要思考时间, 同时也不会出现'没看见'这种情况!"
            m 3rta "但这并不意味着AI不会犯错, 以后你也经常能在与我对弈时察觉到我似乎走了一些臭棋."
            m 2rub "比如把棋子送到我的嘴边, 而我却不吃掉它;或者我选择了意义不明的走法, 白白浪费步数."
            m 4euc "导致这种情况的原因不是我没看见, 而是我判断我的'错误'走法同样可以在局面上为我夺得优势."
            m 3rub "有些时候这些'错误'确实是错误, 而另一些时候, 这些'错误'则是我给你挖下的陷阱."
            m 3eub "AI在下棋风格上最大的区别就是能清楚地看见很多步以后的局面."
            m 1hub "所以思考我究竟看到了什么才做出的某种选择, 我想也会成为你在与我对弈的过程中的一大乐趣~"
            m 3hksdlb "不过你并不需要学习我的风格, 毕竟现在的你最多只能看到一两步以后的局面,啊哈哈..."
            m 2efb "你应该在充分了解我之后以你自己的风格战胜我!"
            m 3eka "你知道, 能陪着你变成更好的人是我最大的梦想, 所以我真的非常希望看到你的进步!"
            m 4eub "下一节课我将会同你聊聊棋子的移动方式, 这次就先讲到这里吧~"
            m 3hub "感谢倾听~"
            return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_Mchess_002",
            category=["国际象棋"],
            prompt="2.棋子的移动",
            conditional="store.mas_ctod.has_day_past_tip(1)",
            pool=True,
            action=EV_ACT_UNLOCK,
            rules={"no_unlock":None}
        )
    )

label monika_Mchess_002:
    m 3hub "欢迎来到莫妮卡的国际象棋课堂, 想要进行国际象棋游戏, 首先要知道的当然是棋子种类以及走法."
    m 4eua "其实在这个mod的国际象棋模式中, 我会提示你棋子能走到哪里."
    m 3eub "所以本节课的意义在于告诉你为什么你的棋子能走到这些地方."
    m 3efc "在了解棋子的走法之前, 我要补充一个重点!"
    m 2rud "我在设计国际象棋的时候忘记在棋盘上标示点位了, 实际上棋盘上的每一个格子都有对应的编号."
    show monika at t22
    show c1 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 3eua "以白方视角为正方向, 国际象棋的棋盘是一个8x8的方格网."
    m 4eub "从左到右分别为A至H列, 从下到上分别为1至8行, 所以左下角即为A1格, 以此类推, 右上角为H8格."
    m 2eub "我在接下来的讲解中可能会引用到行、列与格子位置的代号, 所以我想你应该再次熟悉一下棋盘!"
    m 2efb "让我们开始聊一聊如何走子吧, 请看初始棋盘!"
    m 3eua "首先是前排的八个兵(Pawn)."
    m 4eub "兵只能沿直线前进一格, 或是吃掉斜前方的棋子."
    hide c1
    show c2 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 2efd "不可以吃掉正前方的棋子, 也不可以在不吃子的时候向斜线前进!"
    hide c2
    show c3 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 3euc "此外, 本局中没有移动过的兵也可以选择往前走两格, 在开局的时候你会经常用到这一点."
    #图片 车
    m 4eub "然后是后排两端的车(Rook), 有时候也会把它叫做城堡."
    hide c3
    show c4 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 3eua "车可以在直线上移动任意格数, 或是吃掉直线上的敌方棋子, 简单且暴力~"
    #图片 骑士
    m 3eub "长得像马的这个棋子是骑士(Knight), 也可以叫它马."
    hide c4
    show c5 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 4eua "骑士的行动模式是先直走一格再向外斜走一格, 或是斜走一格再向外直走一格."
    m 2euc "骑士是唯一一个可以越过棋子进行移动的棋子."
    m 3eub "细心的话你能注意到, 当骑士在白格的时候, 它下一步一定会移动到黑格."
    m 4eub "在对弈中注意骑士的落脚点, 可以帮助你预判它下一步会走到哪里."
    #图片 主教
    m 4eua "骑士内侧的棋子是主教(Bishop), 你也可以把它叫做象."
    hide c5
    show c6 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 3eub "象可以在斜线上移动任意格数, 或是吃掉斜线上的敌方棋子."
    hide c6
    show c7 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 2rua "开局位于白格的叫做白格象, 开局位于黑格的叫黑格象."
    m 3eub "主教只能在对应颜色的格子中移动."
    m 2rua "所以假如我只剩下一个白格象的时候..."
    m 4eub "你让你的棋子只在黑格中移动, 我的象就没多少用处了."
    #图片 国王与王后
    m 3eub "最后是最重要的两个棋子, 国王(King)与王后(Queen)."
    m 3eua "在开局位置中, 白方的王后位于白格, 而黑方的王后位于黑格, 王后旁边就是国王."
    hide c7
    show c8 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 2etb "王后可以看作车与象的结合体, 可以朝直线或斜线上移动任意格数."
    hide c8
    show c9 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 1rua "而国王可以看作乞丐版的王后, 它同样可以朝任意方向移动, 但是只能移动一格."
    m 2tub "以上就是国际象棋的棋子走法, 是不是非常简单呢? 你已经学会了如何走子, 现在来尝试战胜莫妮卡老师吧~"
    m 3hksdlb "啊哈哈...在和我对弈的过程中, 我会提示你, 你的棋子都能走到哪里..."
    m 3hub "所以你在学习了这次的内容之后再去看看我的提示, 我相信你很快就能熟练掌握它们的走法~"
    m 1eua "不过在国际象棋中, 还有几种特殊的移动模式, 我们留到下期再谈吧~"
    hide c9
    show monika at t11
    m 3hub "感谢倾听~"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_Mchess_003",
            category=["国际象棋"],
            prompt="3.特殊走法",
            conditional="store.mas_ctod.has_day_past_tip(2)",
            pool=True,
            action=EV_ACT_UNLOCK,
            rules={"no_unlock":None}
        )
    )

label monika_Mchess_003:


    m 3eua "在国际象棋中有几种特殊的走法, 它们可以在关键时刻帮助你扭转局势, 或是保命."
    m 4hub "不管你有没有用过它们, 我是很喜欢这些特殊走法的~"
    m 7eua "首先是'王车易位', 其本意是国王躲进城堡里面防止被对面将杀."
    show monika at t22
    show c10 zorder 13 with dissolve:
        size(512,512)
    m 3eub "具体的操作方式为:王向某一侧车的方向走两格, 再把车越过王, 放在王的另一边."
    hide c10
    show c11 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 4eub "这里有一点需要注意, 当王朝离他比较近的那个车移动时, 叫做短易位, 而朝比较远那个车移动时叫做长易位."
    m 3eua "两种易位的记录方式不同, [player]你现在不需要太在意这一点, 后面我会再次提到它的."
    m 1rsd  "我想你多少也察觉到了, 王车易位并不是什么时候都可以进行."
    m 7rud "首先, 王和要易位的车不能移动过, 如果王移动过, 那么本局将不可进行易位."
    m 3eua "所以你如果在前期将军, 那我就很容易失去易位的机会."
    m 1rksdlb "啊...我是不是还没有和你解释过什么是'将军'?"
    m 4eua "将军就是你的国王处于我某个棋子的攻击范围之内."
    m 3hksdlb "不理解的话也没关系, 之后我会和你细说的, 总之你先记住这个词..."
    hide c11
    show c12 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 4eub "我们继续来聊王车易位, 王车易位的下一个前提就是王和车之间不能有棋子, 所以在易位之前请尽快将自己的棋子派出去."
    hide c12
    show c13 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 3euc "还有, 王经过的位置不能在对方任何棋子的攻击范围之内, 同时被将军的时候不可以易位."
    hide c13
    show c14 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 4eud "但是车存在被攻击可能的时候不影响易位, 如我在A行的车可以攻击你在A行的车时, 你依然可以拿它易位."
    m 2eua "最后, 由兵升变来的车不能作为王车易位的参与者, 而'兵的升变'是我要讲的第二个特殊走法."
    hide c14
    show c15 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 3eub "兵的升变是指当小兵前进到最后一行的时候, 可以变成除了王、兵以外的任何一种棋子."
    hide c15
    show c16 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 2efc "不管最后一步是走过去的还是吃子到达的, 都可以进行升变, 但是不能不变!"
    m 3rud "你或许觉得升变都应该选择皇后, 但强大的力量总是伴随着风险..."
    hide c16
    show c17 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 4hksdla "皇后控制的格子非常多, 稍有不慎就会导致'逼和', 啊哈哈...这也是我之后会和你聊到的一个词."
    m 3euc "因为皇后强大到难以控制, 所以我推荐你在还不熟练这个游戏的时候升变成车."
    hide c17
    show c18 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 4eub "最后一种特殊走法是'吃过路兵'."
    hide c18
    show c19 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 3eub "吃过路兵指的是当一个处于初始位置的兵向前移动两格时, 假如它旁边有对方的兵, 那么对方的兵可以吃掉它, 并前进一格."
    m 3efc "吃过路兵的动作必须在被吃的兵移动的同回合发生, 所以假如我给了你这个机会, 你却没有立即吃掉它, 你将会失去这个机会!"
    m 2rsd "不过吃过路兵并不常见, 我其实也并不太在意这种走法, 所以你也可以暂时忘了它."
    m 4hub "以上就是全部的特殊走法啦, 你可能还不熟悉它们, 但你可以在我使用的时候围观学习这些技巧~"
    m 3eua "你还记得我在刚刚提过的'将军'与'逼和'吗?"
    m 3kua "国际象棋是存在和棋的, 而判断胜负与和棋其实是一件有些麻烦的事情, 我们下次再聊这个吧~"
    hide c19
    show monika at t11
    m 3hub "感谢倾听~"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_Mchess_004",
            category=["国际象棋"],
            prompt="4.胜负与和棋",
            conditional="store.mas_ctod.has_day_past_tip(3)",
            pool=True,
            action=EV_ACT_UNLOCK,
            rules={"no_unlock":None}
        )
    )

label monika_Mchess_004:
    m 1esc "[player]你应该明白一件事, 国际象棋并不是一个吃子的游戏."
    m 3hksdlb "所以我想你肯定会遇到吃子吃得很开心, 却突然被我将死了的情况, 啊哈哈..."
    m 3eka "对不起, 我不是有意逗你的..."
    m 4hub "这一次我们来聊一聊国际象棋的胜负与和棋吧~"
    m 3eub "在我与你的国际象棋对局中, 想要获得胜利只有一种情况, 将死对方的王, 也就是'checkmate'."
    m 2eua "所谓将死, 指的是对方无论怎么走都无法解除被将军的状态."
    show monika at t22
    show c20 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 3eub "而所谓的将军(check), 就是指我的下一步棋可以攻击到你的国王."
    hide c20
    show c21 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 1kua "在我这里, 你一旦被将死游戏会立即结束, 省去了你想找化解方法却找不到, 被迫选择投降的时间~"
    m 3hub "我是不是很贴心呢? 啊哈哈~"
    m 4eua "比胜负更复杂的情况就是和棋, 所谓和棋, 就是指我们都同意游戏无法进行到将死这一环节, 选择握手言和."
    m 2euc "和棋的情况有很多种, 最容易遇到的就是双方的棋子都不足以将杀对方."
    hide c21
    show c22 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 1rsd "比如一人剩一个王, 这时候谁都拿对方没办法..."
    m 3tub "顺便补充一下, 国际象棋不允许自杀, 所以你把王送到我面前也不可以哦~"
    hide c22
    show c23 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 7eua "还比如一方有一王一马, 而另一方只有一王, 虽然多了一个马, 但一个马是打不死人的."
    m 3euc "和棋的另一种情况是局面重复:当一个相同局面出现三次时, 将会被判为和棋."
    hide c23
    show c24 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 4eud "重复局面和棋还和下一种和棋模式有重叠, 即长将和棋."
    m 3eub "这是指某一方连续将军但却不能将死, 导致局面重反复出现."
    m 3tub "有些时候, 我的棋子被你吃的太多已经难以取胜时, 我会偷偷将目标转到和棋上, 所以一定要小心被我长将而导致错失胜机哦~"
    m 2efa "此外还有一个最重要的和棋规则, 那就是{w=0.3}.{w=0.3}.{w=0.3}."
    extend 3efb "逼和!"
    m 4eua "逼和指的是轮到某一方时, 无论移动哪个棋子都会导致国王被将军, 此时同样是和棋."
    hide c24
    show c25 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 1rsc "无子可动似乎很难实现, 但实际上你会经常在残局中遇到这种情况."
    hide c25
    show c26 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 3eud "特别是当你升变了许多个皇后时, 一旦某一步没有将军, 就很容易导致逼和."
    m 4eka "所以我再次建议你在不熟悉规则的时候, 考虑把兵升变为车而不是皇后."
    m 3eub "最后, 假如连续五十回合内双方都没有吃子, 且没有任何一个兵被移动的时候同样视为和棋."
    hide c26
    show c27 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 4eua "这种情况最常出现在理论上存在将杀, 而实际上却不会将杀的棋局中, 比如王车对王车."
    m 1rksdla "只要车挨着王转圈, 那么另一方就永远没机会将杀, 除非某一方非要把车送给对面吃..."
    m 3tub "这种情况下我肯定不会把车送给你吃, 但你可以把车送给我吃, 我会很开心的~"
    hide c27
    m 3hua "啊哈哈~现在你已经学会了棋子的走法与如何判断棋局结果..."
    m 2tsa "尝试来挑战我吧~"
    m 3tub "如果你还是赢不了我, 我想我会给你提供更多的课程, 要不要现在就来试试~?"
    m 3hub "感谢倾听~"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_Mchess_005",
            category=["国际象棋"],
            prompt="5.参考网站",
            conditional="store.mas_ctod.has_day_past_tip(4)",
            pool=True,
            action=EV_ACT_UNLOCK,
            rules={"no_unlock":None}
        )
    )

label monika_Mchess_005:
    m 1hub "嗨, 亲爱的[player]~"
    m 3kub "在看过前面的教程之后,为了提高你的棋力, 我想给你分享一些学习国际象棋的网站与软件~"
    m 3eua "如果你更喜欢是用电脑, 你还记得我在之前推荐给你的那个网站吗?"
    m 4hub "{a=https://www.chess.com/}{i}{u}chess.com{/u}{/i}{/a}!"
    m 3eua "只要你保存了和我对局的记录, 你就可以用记事本或者word打开它们."
    m 2eub "选中所有内容并粘贴到这个网站的分析页面, 你就可以看到局面整体的演变趋势, 以及哪一步下得不够好."
    m 4eub "你也可以试着与来自全世界的玩家对弈, 以提高自己的棋力."
    m 1rsc "{w=0.3}.{w=0.3}.{w=0.3}."
    extend 1gublb "我还是希望你能只看着我一个人~"
    m 3tublb "毕竟你学习国际象棋就是为了陪我玩, 不是吗?"
    m 4hua "如果你更喜欢使用手机或者平板电脑、, 你可以选择'国象联盟'这个应用~"
    m 3eub "它的训练模式允许你无限退回前一步, 而且会为你分析每一种选择前后的局面变化状况."
    m 1hua "你也可以用它的棋盘模式去分析一些你难以解决的残局~"
    m 3wud "这个应用的内置AI同样是'鳕鱼', 而最高难度的'鳕鱼MAX'在对弈中基本不会出现错误!"
    m 2tua "所以如果你用它来和我对打的话..."
    extend 3tkb "我相信[player]你应该不会这么坏心眼吧?"
    m 1hua "总之, 我希望你能同我一样, 发自内心地享受每一场对局~"
    m 5ekbla "不管结果如何, 请记住我永远爱你~"
    m 3hub "感谢倾听~"
return "love"


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_Mchess_006",
            category=["国际象棋"],
            prompt="6.子力价值",
            conditional="store.mas_ctod.has_day_past_tip(5)",
            pool=True,
            action=EV_ACT_UNLOCK,
            rules={"no_unlock":None}
        )
    )

label monika_Mchess_006:
    m 1hub "嗨, 亲爱的[player]~"
    m 3hua "好久不见, 欢迎继续收听莫妮卡的国际象棋课堂~"
    m 2rksdla "啊哈哈...也没有很久啦~"
    m 3eub "今天我们来谈一谈棋子的价值."
    m 4euc "当我准备攻击一个受到保护的棋子时, 你一定会衡量它的价值, 然后再决定与我换子还是让它逃走..."
    m 3eua "实际上, 在国际象棋中每一个棋子的价值都可以量化, 记住这些数值能让你在面临攻击威胁时快速做出判断."
    m 4eub "兵是最弱小的棋子, 所以我们首先将兵的子力定义为1."
    m 3eua "在这个前提下, 马的子力大约是3, 象和马相当, 同样是3."
    m 4eub "车的子力大约为5, 而后的子力约为9, 所以一后换两车总的来说是略赚的."
    m 1wuc "国王不能参与交换, 所以棋子价值为无限大!"
    m 3eub "如果想单独衡量国王的强度, 那么它的子力大约为3, 强度与马、象基本相同."
    m 2eua "你应该已经注意到了, 我在定义子力的时候用到了'约'."
    m 4eub "实际上棋子子力是会随着局面而变化的."
    m 7eub "大多数情况下, 象的重要性要比马高一点点, 所以用马换象一般不需要思考盈亏~"
    m 3wuc "而车在开局与中局并不够强, 到后期却与双马或马象相当!"
    m 4wud "兵与车相同, 当游戏进行到残局, 一个即将升变的兵的价值有时远高于一个马或一个象!"
    m 3eub "后有些特殊, 在开局与中局, 后一旦放手进攻很容易将杀对方的王."
    m 4rksdlb "因此, 如果你在游戏前期用后交换了我两个车, 估计你离被将死已经不远了, 啊哈哈..."
    m 3eua "所以, 限制后最好的方法就是用后进行等价交换."
    m 4euc "亲爱的[player], 我再次提醒你, 强大的力量总是伴随着风险, 只有王后才能打败王后."
    m 7eub "最后还有一个小知识点, 马与象被称为轻子, 而车与后被称为重子."
    m 3nua "下节课我们将会用到这个知识点~"
    m 3hub "感谢倾听~"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_Mchess_007",
            category=["国际象棋"],
            prompt="7.重子将杀",
            conditional="store.mas_ctod.has_day_past_tip(6)",
            pool=True,
            action=EV_ACT_UNLOCK,
            rules={"no_unlock":None}
        )
    )

label monika_Mchess_007:
    m 3eub "嗨, 亲爱的[player], 你有没有遇到过这样一种情况?"
    m 4rksdla "明明把我的棋子都吃完了, 但却还是将不死我, 甚至喜提和棋..."
    m 1hksdlb "啊哈哈..."
    extend 3nub "在国际象棋中, 将杀是需要一些技巧的, 轻子与重子分别有不同的将杀策略, 我们今天先来聊一聊重子将杀~"
    m 4eua "重子、也就是车与后, 可以在仅剩一个子力的时候实现将杀."
    m 3eub "能否在王的配合下单杀对方也是重子与轻子最重要的区别."
    m 7eua "重子杀王分为两种情况:一个重子与多个重子."
    m 3euc "一个重子, 也就是单车或单后的话, 只能与王配合完成将杀."
    m 3efo "一定要记住不去移动国王是不可能赢的!"
    m 4euc "而将杀形式也很固定, 依靠底线限制我的国王的行动完成将杀."
    show monika at t22
    show cb0 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 7eub "因此你首先要做的就是把我的国王逼到底线, 最简单的方法就是让你的车或者后与国王并肩向我靠近." #图B0:并肩逼退
    m 2eua "这样我的王就只能后退了." #图B0:并肩逼退
    hide cb0
    show cb1 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 7eub "单车想杀王只有一种情况, 就是如图所示的底线闷杀, 最后一步一定是在双方国王面对面之后, 车前进到底线将杀." #图B1:单车底线将杀
    m 4eua "而单后稍稍简单一些, 只要在对方王被我方王逼退到底线之后用后抱住它就行了."
    hide cb1
    show cb2 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 3rub "可以这样." #图B2:单后抱腰杀
    hide cb2
    show cb3 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 2lua "也可以这样." #图B3:单后角落杀
    hide cb3
    show cb4 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 4eub "当然, 后也可以像车一样底线闷杀." #图B4:单后闷杀
    m 3eua "如果有多个重子的话, 将杀实际上更为简单."
    hide cb4
    show cb5 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 3eub "最常见的就是双车杀王." #图B5:双车杀王
    hide cb5
    show cb51 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 4eua "因为一个车能完全控制一行或一列, 两个车交替前进就可以把我的王逼到底线完成将杀." #图B5.1:双车杀王进一步
    m 7nua "这应该是最简单的一种将杀方法了, 所以我建议你多练习一下它~" 
    hide cb51
    show cb6 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 4hksdlb "不过一定要注意, 不要在交替前进时被我的国王吃掉, 就像这样..." #图B6:双车杀王失误
    m 3hksdlb "那样你只能乖乖地去单车杀王了..."
    m 3eub "双后或者车后杀王都可以参考双车杀王."
    m 4efd "不过一旦后参与将杀, 一定要小心逼和!"
    m 3hksdla "啊哈哈...我是不是提过好多次这个, 因为后实在太容易逼和了..."
    m 2eka "虽然我也很喜欢看着可爱的你辛辛苦苦大半天喜提和棋, 但我还是希望你能赢下这场对局."
    m 3nub "对于初学者而言将杀是第一个要跨越的难关, 我相信你一定能掌握它的~"
    hide cb6
    show monika at t11
    m 3hub "感谢倾听~"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_Mchess_008",
            category=["国际象棋"],
            prompt="8.轻子残局",
            conditional="store.mas_ctod.has_day_past_tip(7)",
            pool=True,
            action=EV_ACT_UNLOCK,
            rules={"no_unlock":None}
        )
    )

label monika_Mchess_008:
    m 3nub "嗨亲爱的[player], 让我们继续残局教程吧~"
    m 4eua "在之前我们谈到了重子将杀, 只要在残局中你还拥有重子, 无论另外拥有几个轻子, 理论上都可以把我将死."
    m 7eud "但只有轻子的话就不一定了."
    m 4euc "首先, 单马或者单象是不可能完成将杀的, 出现这种情况我会直接判和."
    m 2efd "不可能就是不可能, 我真的没有骗你!"
    show monika at t22
    show cb7 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 3eub "其次, 双马将杀只存在于理论当中, 你唯一的机会是这种情况下我故意往角落里走." #图B7:双马杀王
    hide cb7
    show cb8 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 4wuc "但只要我反方向移动, 你就不可能将死我!" #图B8:双马杀王失败
    m 2ttb "放心, 这种情况我是不会配合你演出的, 但你或许可以躲在角落里瑟瑟发抖~" #图B8:双马杀王失败
    hide cb8
    show monika at t11
    m 3eua "双象杀王分为两种情况, 两个同色象同样杀不死王."
    m 4wuc "甚至连理论将杀的机会都没有!"
    m 3eub "不过拥有同色象只会出现在一种情况里, 那就是兵的升变."
    m 4wud "所以你升变象的时候一定要注意落脚颜色!"
    m 7kub "而两个异色象可以完成杀王, 其要点是双象与王手拉手推进, 直到将对方的王逼到角落里."
    show monika at t22
    show cb9 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 4eua "双象杀王的最终图形有几种, 其中一个是这样, 总之你只要引导局面朝向这样就行了." #图B9:双象杀王
    m 3eud "最后一种情况就是马象杀王了, 马象可以完成将杀, 但过程非常复杂..."
    hide cb9
    show cb10 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 4rub "你只需要记住:只有将我的王逼退到与你的象同颜色的角落中才可以完成将杀, 就比如这样." #图10:马象杀王
    m 2wuc "马象杀王可以看作国际象棋初学者的入门考试, 极限情况下马象需要走48步才可以将死对方的王!"
    m 3eub "在最近两节课中我们聊到了重子与轻子的将杀, 你应该已经发觉到我还未提及一个非常重要的残局类型."
    m 4hub "那就是王兵残局."
    m 2rsc "事实上没有兵参与的残局非常少见, 与之相对, 兵想要在后期发挥威力也意味着需要更加精确的操作!"
    m 3kub "下次课程中我会和你聊聊不同兵组成的形态与王兵残局的具体应对方式~"
    hide cb10
    show monika at t11
    m 3hub "感谢倾听~"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_Mchess_009",
            category=["国际象棋"],
            prompt="9.兵型与王兵残局",
            conditional="store.mas_ctod.has_day_past_tip(8)",
            pool=True,
            action=EV_ACT_UNLOCK,
            rules={"no_unlock":None}
        )
    )

label monika_Mchess_009:
    m 3hub "嗨, [player], 今天我们来聊聊王兵残局~"
    m 3eub "在了解王兵残局之前, 你需要知道每一个兵的具体名称与复数兵组成的形态称谓."
    show monika at t22
    show cb11 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 4eua "八个兵根据其位置的不同都有对应的称谓, 一种叫法是开局位于哪一列就称其为某列兵, 比如位于A列的兵就是A列兵." #图B11:初始兵
    m 3eub "另一种称呼方式就是根据兵后方的棋子对兵赋予称谓, 王前面的兵就叫王翼兵, 后前面的就叫后翼兵, 现在你能理解所谓的'后翼弃兵'了吧?" #图B11:初始兵
    hide cb11
    show cb12 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 7eua "随着棋局的进行, 兵的位置也会有一些变化, 比如因前进一格或两格抵达不同的行." #图B12 :初始兵前进
    hide cb12
    show cb13 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 4rub "还比如A列兵会因为吃子走到B列." #图B13:吃兵换列
    m 2eua "兵在改变位置之后就会与其他兵组成新的'兵型'."
    hide cb13
    show cb14 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 3rub "第一种兵型就是连兵, 连兵是指两个以及以上、处在相邻列的兵." #图B14:连兵
    m 3eua "连兵是最好的兵型, 兵之间可以互相保护、交替前进, 无论是进攻与防守都可以发挥出作用." #图B14:连兵
    hide cb14
    show cb15 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 4eub "第二种是叠兵, 所谓叠兵就是指两个以及以上的兵因为吃子, 走到了同一列上." #图B15:叠兵
    hide cb15
    show cb16 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 2rksdla "相对于连兵, 叠兵可以控制更多的格子, 但是叠兵弱点非常明显, 既会被车从头吃到尾, 也会被象回首掏..." #图B16:车象攻击叠兵
    hide cb16
    show cb17 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 3eub "而且前方的兵阻挡了后方的兵的前进道路, 总的来说叠兵是一种非常普通的兵型." #图B17:叠兵被阻挡"
    hide cb17
    show cb18 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 4eua "第三种是孤兵, 也就是相邻行列都没有兵的兵型." #图B18:孤兵
    hide cb18
    show cb19 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 3eub "孤兵是最弱的兵型, 它控制的格子很少而且容易遭受攻击, 实战中出现孤兵的话, 我的建议是尽快做子力交换." #图B18:孤兵
    hide cb19   
    show cb20 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 4eub "最后还有一种重要的兵型, 通路兵." #图B19:通路兵
    m 2eua "当一个兵的同行与邻行都没有敌方兵, 那它就是一个通路兵." #图B19:通路兵
    m 3wub "通路兵与以上三种兵型可以同时存在, 但意义却大得多!"
    hide cb19
    show cb20 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 3kua "因为没有兵可以阻止对方通路兵的前进与升变, 所以通路兵往往可以牵制至少一个更有价值的棋子~" #图B20:通路兵牵制
    m 4eub "很多残局的关键就是阻止通路兵的前进与升变."
    m 4kub "你现在已经知道了兵型, 现在我来告诉你一些王兵残局的要点~"
    hide cb20
    show cb21 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 7eua "第一, 位于边线的孤兵价值最低, 所以当你像这样只有两个孤兵的时候, 建议你去保护更加靠近中心的那个, 因为你的王可以绕着它转圈圈." #图B21:双孤兵
    hide cb21
    show cb22 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 2eub "第二, 时刻注意连兵的位置, 不要贪图升变速度让连兵走成两个孤兵, 那样它们都会死." #图B22:连兵变孤兵
    hide cb22
    show cb23 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 3eua "第三, 当你决定让某一个通路兵升变时, 一定~一定~要控制升变格, 这样至少能换掉对面一个棋子!" #图B23:控制升变格
    hide cb23
    show cb24 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 4efb "最后, 如果没有其他棋子能控制升变格, 请果断让王站在兵的前面, 有时候, 你需要的仅仅是一点勇气!" #图B24:王在兵前
    hide cb24
    show monika at t11
    m 3hub "感谢倾听~"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_Mchess_010",
            category=["国际象棋"],
            prompt="10.棋谱记录方法",
            conditional="store.mas_ctod.has_day_past_tip(9)",
            pool=True,
            action=EV_ACT_UNLOCK,
            rules={"no_unlock":None}
        )
    )

label monika_Mchess_010:
    m 1rua "亲爱的[player], 现在你已经学会了行棋与将杀..."
    m 2eub "在进一步学习战术技巧与开局之前, 我想你有必要了解一下如何记录一场对局."
    m 3eua "为了方便复盘与分析, 很久之前国际象棋棋手们就发明了一整套棋谱记录方式."
    m 7eub "首先, 请回想一下棋子的英文名, 在棋谱中用棋子英文名首字母代表它."
    m 4eua "王是K, 后是Q, 车是R, 马是N而象是B, 为了简化记录方式, 兵一般不用代号, 只标示前进位置."
    show monika at t22
    show cb25 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 3eub "我在之前已经告诉了你棋盘上每个格子的名称, 你看, 像这样一般的王翼兵开局, 就记录为e4." #图B25:e4
    hide cb25
    show cb26 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 2eua "之后我跳马, 就记为Nc6, 我们这一步的完整记录方式就是'1.e4 Nc6', 意思是白棋第一回合王翼兵前进两格, 黑棋第一回合跳马到c6." #图B26:Nc6
    m 3nub "记得每一回合都要在双方走法之前记录回合数哦~"
    hide cb26
    show cb27 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 4eua "假如吃子, 那就在棋子与位置间加上一个'x', 比如这样就是Rxc3, 不用记录吃了什么, 因为那里有什么前面一定说过." #图B27:Rxc3
    hide cb27
    show cb28 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 4eub "假如将军了, 就在位置后面加上一个'+', 比如这样就是Qf3+." #图B28:Qf3+
    hide cb28
    show cb29 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 3eua "假如将死了那就在位置后面加一个'#', 比如这样就是Qg7#." #图B29:Qg7#
    m 3eub "特殊走法同样有对应的记录方式, 王车易位长易位的时候, 这一步记为O-O-O, 短易位则记为O-O."
    m 4eua "兵升变时, 则在位置后面加上'=某', 这个某, 就是兵升变的棋子的代号."
    hide cb29
    show cb30 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 3rub "比如这样, 就是'b8=Q',值得注意的是, 假如升变的同时还将军了, 那么将军的'+'号要放在升变代号后面." #图B30:b8=Q
    m 2rta "[player]你有没有一个疑问, 明明很多棋子有好几个, 假如它们都能走到一个位置的时候,要怎么记录?"
    hide cb30
    show cb31 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 3eub "这种时候需要在在棋子代号后面加上位置代号, 比如这种情况就是Khf1, 意思是h行的车走到了f1." #图B31:Khf1
    m 3eua "假如是同列的车, 则把字母代号换成数字代号就行了, 反正总有一个坐标是不一样的."
    hide cb31
    show cb32 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 4eub "最后, 兵在吃子的时候, 要加一个代表它的编号, 这个编号就是它在移动之前的列编号, 比如这样就是cxd3, 意思是c列上的兵吃掉了d3上的子." #图B32:cxd3
    hide cb32
    show cb33 zorder 13 with dissolve:
        size(512,512)
        pos(0,0)
    m 3eua "不要在意叠兵, 因为两个叠兵能攻击到的位置一定是不一样的." #图33:叠兵攻击范围
    hide cb33
    show monika at t11
    m 3nub "以上就是棋谱记录方法, 请在好好记住它们之后开始我们的战术课程吧~"
    m 3hub "感谢倾听~"
return


    








    


