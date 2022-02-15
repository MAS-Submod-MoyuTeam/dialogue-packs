
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

init -990 python:
    store.mas_submod_utils.Submod(
        author="星光 TK Monika",
        name="莫妮卡的象棋教程",
        description="想学学怎么下象棋吗?",
        version="1.0.0"
    )

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_Mchess_001",
            category=["国际象棋课堂"],
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
            category=["国际象棋课堂"],
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
            category=["国际象棋课堂"],
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
            category=["国际象棋课堂"],
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
            category=["国际象棋课堂"],
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













