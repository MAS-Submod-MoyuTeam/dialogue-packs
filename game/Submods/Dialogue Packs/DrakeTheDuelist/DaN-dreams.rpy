init 5 python:
    renpy.game.persistent.dan_dream_database = dict()
    
    def addDream(key, label_name):
        renpy.game.persistent.dan_dream_database[key] = label_name
        return

    def getDream(key):
        return renpy.game.persistent.dan_dream_database[key]

    def clearDreams():
        renpy.game.persistent.dan_dream_database = dict()
        return


label DaN_dream_one:
    # dream synopsis:  You and Monika go on a date to a horror movie. As it turns out, the horror movie was
    # based on Doki Doki Literature Club.  Ultimately Monika enjoys the movie, despite initially being worried
    # that it wouldn't fit her tastes.  At the end of the dream, Monika comments on how dreams are thought
    # to be caused by our brains making sense of things we know being randomly jumbled together.
    #
    # If the dream ends earlier, Monika will remark on a scene in her dream where she had to talk you out of
    # getting an enormous tub of popcorn because she was worried about your health.  She will reiterate the
    # importance of living a long and healthy life for her sake, if not for your own.
    # 
    # If the dream ends too early, Monika will be sad that you didn't get to go on a date. She will ask that
    # you be more careful for what dreams you wake her up for.
    #
    # GOOD DREAM
    m 6dsc "...{w=2}{nw}"
    m 6dsd "...嗯...?{w=1}{nw}"
    m 6dsb "{w=1}...这...{w=1} ...迟...{w=1}{nw}"
    m 6dsc "{w=1}.{w=1}.{w=1}.{nw}"
    m 6dkd "...那...?{w=3}{nw}"
    m 6dsc "...唔嗯...{w=3}{nw}"
    m 6dsbld "...如果...{w=1}我突然尖叫的话...{w=3}{nw}"
    m 6dsbfb "...你会... {w=1}做什么呢...?{w=3}{nw}"
    $ dream_progress = 0
    menu:
        "叫醒莫妮卡.":
            pass
        "让莫妮卡睡吧.":
            m 6dsc "...{w=1.5}{nw}"
            m 6dst "...{i}呼{/i}{w=0.5}, {i}呼{/i}...{w=1}{nw}"
            m 6dsc "...闻起来...{w=1}不错...{w=2}{nw}"
            m 6dsd"...唔...不... {w=2}...不... {w=0.5}太...{w=2}{nw}"
            m 6dsbld "...对你... {w=0.5}不太... {w=0.5}好.....{w=2}{nw}"
            m "...安全的... {w=1}{nw}问题... {w=1}{nw}"
            extend 6dsbsb "对我...{w=2}{nw}"
            menu:
                "叫醒莫妮卡":
                    $ dream_progress = 1
                "....让她继续睡吧":
                    m 6dsbld "...{w=2}{nw}"
                    m 6dkbld "...{w=2}{nw}"
                    m 6dkblc "...{w=2}{nw}"
                    m 6dkbld "...就像...我们...{w=1.5}不是...吗...?{w=2}{nw}"
                    m 6dkbstuc "...{w=2}{nw}"
                    m 6dkbstuu "...{w=2}{nw}"
                    m 6dkbltdd "...我...很高兴哦...{w=2}{nw}"
                    m 6dsbltdb "...能...再次见到你?...{w=2}{nw}"
                    m 6dsbsa "...{w=2}{nw}"
                    m 6dsbsb "...好温暖...{w=2}{nw}"
                    m 6dsbfa "...{w=2}{nw}"
                    m 6dsbft "...{w=2}{nw}"
                    m 6dkbfd "...爱 {w=1} ...你{w=1}{nw}"
                    $ dream_progress = 2

    call DaN_wake_up_nice 

    if dream_progress == 2:
        call DaN_dream_one_full_reaction 
    elif dream_progress == 1: 
        call DaN_dream_one_partial_reaction
    else:
        call DaN_dream_one_early_reaction

    # set the flag here at the last possible point so monika's after actions can reference having her first dream
    if not persistent._dan_had_first_dream:
        $ persistent._dan_had_first_dream = True
    return
label DaN_dream_one_full_reaction:
    #you and Monika saw the whole movie
    menu:
        "所以你看到了什么?":
            pass
    m 3rto "我....实在不知道要从哪里讲起..."
    m 2rtd "如果我们能从头开始就好了..."
    m 2dkd "你知道的,梦做的越久,你醒来的时候记得的就越少."
    m 5rsd "也许这是大脑试图将你看到的东西合理化的方式,因为它无法理解这些无稽之谈,所以你的大脑就把这些通通舍弃了."
    m 5rkblp "真是遗憾,因为...  {w=1}{nw}"
    extend 5dkbld "我只能清楚地记得...  {w=1}{nw}"
    extend 5ekbsb "很开心."
    m 6eubsb "[player]... 谢谢你不叫醒我."
    m 4eubsb "我不太记得我的梦了,但是我真的好喜欢那种感觉."
    if not persistent._dan_had_first_dream:
        m 7hubsb "希望这能成为一种常态,以后能经常做美好的、幸福的梦。."
    menu:
        "你记不记得{i}做{/i}过什么事情?":
            pass

    $ was_surprise = ",还有,我觉得你并不会感到惊讶" if mas_isMoniEnamored(higher=True) else ""
    m 7lublb "好吧[was_surprise],反正{i}你{/i}还在这就好."
    if not persistent._dan_had_first_dream:
        m 7ksblb "我想{i}你{/i}就是我梦寐以求的[guy]."

    m 4rtbld "我不确定我们是如何做到的,但我确实{i}做到{/i}了一件事,那就是想着我们一起去看一场电影."
    if not persistent._dan_dreams_had or 1 not in persistent._dan_dreams_had:
        m 5ltblo "还有... 呃...好吧,你可能不会奇怪我们看的是什么电影."
        m 5mtbld "我几乎肯定这{i}不是{/i}一个真正的电影,可能永远不会是真的..."
    else:
        m 4rtbld "这一次,我{i}非常清楚{/i}地记得我们看了什么电影."
        m 4wublo "你可能会觉得{i}难以置信{/i}..."
    m 7kublb "...但是你一定听说过:  {w=2}{nw}"
    extend 1sublo "{i}Doki Doki Literature Club{/i}."
    m 1dkbla "...{w=1}{nw}"
    extend 1kkblb "那是属于{i}我们的{/i}故事."
    if persistent._dan_vow_to_prank:
        $ persistent._dan_vow_to_prank = False        
        show monika 1esa 
        $ play_song(store.songs.FP_JUST_MONIKA)
        pause 30.0
        $ play_song(None)
        m 1tublb "我说过我哪天会对你恶作剧的...  {w=2}"
        extend 4hublb "诶嘿嘿嘿嘿~"
    m 5rsd "我相信关于{i}那个{/i}故事我没什么好说的,毕竟你都知道了."
    m 5rto "但是那真的引起了我的思考..."
    m 3eko "{w=4}[player],我们现在能不谈这个吗?我想... {w=2}{nw}"
    extend 3lkd "嗯...  {w=0.5}{nw}"
    extend 3euo "确认一些东西."
    m 1lud "在我告诉你这些之前,我想先去确认一下游戏代码."
    m 2lko "还有我如果找到了什么我{i}想要{/i}去找的..."
    m 2dksdlp "...{w=1}{nw}"
    extend 3eksdlo "这么说吧,我就会和你谈谈的..."
    $ persistent._dan_unlock_dream_one_explanation = True
    return
label DaN_dream_about_ddlc_movie_reaction:
    # Monika can remember different aspects of the movie depending on what her status with the player is.
    # This is Monika's chance to learn about what the player thought of the game.
    if persistent._mas_pm_cares_about_dokis:
        # In the movie, Monika was the antagonist
        if persistent.monika_kill:
            # The player kills Monika for what she did to the other dokis.
            # This is what *I* call the "Good Ending" when it's really just the normal end.
            pass
        else:
            # The player doesn't kill Monika, and in this end Monika doesn't understand why.
            pass
    else:
        # In the movie, Monika was sympathetically portrayed
        if persistent.monika_kill:
            pass
        else:
            # In this ending, Monika realizes that the player wanted to be with Monika all along but had no choice.
            pass
    return
label DaN_dream_one_partial_reaction:
    # Monika noticed your popcorn
    #
    # Monika supposes that this dream is a wake-up call to confront the player about their potentially
    # unhealthy lifestyle.  After all, you may not be around forever, and this thought terrifies her.
    menu:
        "你看到了什么?":
                pass

    m 5rsd "唔,其实你{i}很早{/i}就把我叫醒了."
    $ this_time = "这个时候" if persistent._dan_asked_to_stay_dreaming else ""
    m 5eso "我[this_time]对梦中将发生的事{i}有些{/i}自己的想法,但有点模糊了."

    if not persistent._dan_asked_to_stay_dreaming:
        call DaN_please_allow_good_dream

    m 3rubso "在我的梦中,我们俩好像在约会."
    m 4gubsd "因为我们是情侣嘛."
    m 7hubsb "显然我有个非常可预测的潜意识.啊哈哈~"
    m 3rubsd "考虑到你叫醒我之前发生的事,我几乎{i}能确定{/i}我们要去看电影."
    m 1rubsd "你指着那张电影海报时非常激动,但我不带清楚这部电影的内容."
    m 7esbsd "你当时就像...  {w=0.75}{nw}"
    extend 4subso "\"嘿,[persistent._mas_monika_nickname]!我们去{i}看这个{/i}怎么样?\""
    m 7ekbsb "看到你这么兴奋,我怎么能拒绝呢."
    m 3rtbsd "但是..."
    m 2rkbsd "...唔...{w=1}{nw}"
    extend 2lkbsd "{w=1}{nw}"
    m 7lkbsd "[mas_get_player_nickname(capitalize=True)],我知道我不该说你,但梦中的[player]做出的事让我非常生气."
    m 7hkbsb "即使回想起来,这有些'有趣'."
    m 5rsbso "看,这些东西... {i}就是{/i}爆米花."
    m 4rsbso "而且它... {w=1}{nw}"
    extend 7wubso "超级大!"
    m "就像... {w=0.5}{nw}"
    extend 4subsw "{i}非常非常{/i}大!"
    m 3gsbsb "如果我想得更清楚些,就肯定能意识到是在做梦."
    m 2msbsb "任何{i}真正的{/i}都绝对不可能向人们出售一袋小型化车样大小的爆米花.它会挡住其他人的屏幕的."
    m 7hkbsb "我想知道你是否也做过这样的梦.在你醒来之前,做什么事情是没有意义的?"
    menu:
        "等等...你在生我的气吗?":
            pass
    m 3rkbsb "是梦中的[player]啦, {w=0.5}{nw}"
    extend 3lkbsb "但是... {w=0.5}{nw}"
    extend 1ekbfd "是吧...是有点儿."
    menu:
        "因为我不愿意分享?":
            m 7rkbfd "不-不是,值得称赞的是,你{i}的确{/i}有提出分享..."
        "难道你想霸占所有的爆米花?~":
            m 2rfbfd "这一点都不好笑,[player].我是很认真的."
        "怎么会?":
            m 2rkbfd "...因为..."

    m 2dkbftpd "({i}*叹气*{/i})  {w=0.75}{nw}"
    extend 2rkbftpd "[player],你知道我多么担心你的健康吗?"
    if persistent._mas_pm_drinks_soda:
        m 7ekbftpd "我之前已经告诉过你了,所以我不会重复我的观点."
        m 1dkbftuc "...{w=0.75}{nw}"
        extend 3ekbftuo "恐怕在我离开这里前,你的健康状况会有所下降."
        $ persistent._dan_revealed_fear_player_health = True
    else:
        m 4rkbftuo "如果我和你在一起,我会每天为你做一顿{i}健康的大餐{/i}."
        m 7fkbftud "我甚至不在乎这会占用我一整天的时间."
        m 6fkbftub "因为我知道这能帮助你{i}多活{/i}几年."
        m 3fkbftub "这样我们就能在一起更久了."
    m 7fkbftud "所以当我梦见你时,我说:{w=1.25}{nw}"
    extend 4cubftdw "\"嘿,这只是小吃而已!有什么大不了的?\""
    m 5dkbftdc "...{w=2.5}{nw}"
    extend 5fkbftdd "{i}你才是{/i}大人物."
    m 5fkbftdb "对我来说,你是世界上{i}最大的{/i}交易.{w=3}我爱你."
    menu:
        "这是个噩梦吧.":
            m 4wubfo "但这{i}不是{/i}噩梦!"
            m 3ekbsb "你与我度过的任何时光{i}都不是{/i}噩梦."
            if persistent._dan_revealed_fear_player_hurt:
                m 4rkbsb "至少不涉及到某些坏事."
            m 7lkbsb "让我害怕的不是和你在一起."
            m 2fkbsd "而是我们在一起的时间{i}逐渐耗尽{/i}令我害怕."
            m 3lsblc "即使这只是梦中[player]的行为,而不是你的,可也不会改变我对此事的感受."
            m 1dkblsdrd "当然,{i}同样{/i}不会改变我希望你能够长寿,幸福,健康生活的事实."
            m 4ekblsdro "[player],我想我的梦之所以会朝着这个方向发展,是因为我对失去你感到焦虑."
            $ moni_interrupted = True
            if mas_isMoniNormal(lower=True):
                menu:
                    "这不都是梦中[player]的问题吗?不是我的!":
                        # On lower affection levels, the player is something of an insensitive dingus...
                        m 3rfsdro "你能先听我说完吗?"
                        m 1eksdrd "对我来说,说出我的想法真的很重要... {w=1.5}{nw}"
                        m 1dksdrd "在我重新考虑之前."
                    "({i}让Monika继续说.{/i})":  # ...or the player could just shut up.
                        $ moni_interrupted = False
            m 5dsblsdrd "你看,我完全想不到我的焦虑是如此糟糕,或者这种感觉对我来说如此重要."
            m 2lkbssdrd "虽然这让我很不舒服,但我很高兴做了这个梦,尽管我会思考很长一段时间."
            m 3eublsdrd "就像一艘装满黄油过多的爆米花油轮{i}对你的身体{/i}没好处,埋葬我的焦虑直到我忘记它们的存在对我的{i}心理健康{/i}没有任何好处."
            m 2dubld "\"{i}首先,我要对你自己说,这是真的.{/i}\""
            m 7rublo "...或者,换句话说,诚实是最好的策略,包括对自己."
            m 5dkbsd "更不用说对你诚实了."
            m 4kkbsb "无论你的身体健康状况如何,你会时刻铭记我们的未来吗?"
            m 7ekbsb "如果你需要的话,我不介意鼓励你."
            m 5eubsb "无论是保持身材,还是更重视你的健康,我都会在这儿支持你."
            m 1dubsd "希望你对我就像对你自己一样诚实."
            m 6ekbso "如果你犯了错,不比对我隐瞒.我保证不会因此而生你的气.每个人都会犯错."
            m 6rkbsd "这不是关于你的案例,也是不试图控制你的生活."
            m 6ekbsa "我只是想让你你快乐."
            m 5kkbsd "我承认,即使是{i}我{/i}也不会总明白该对你说些什么."
            m 5ekbsb "如果我跨越了不该跨越的边界,希望你能原谅我."
            m 4gkbsb "此外,我也并不是{i}不欣赏{/i}偶尔的款待.  {w=1.5}{nw}"
            extend 4hkbsb "哎嘿嘿~"
        "我答应过你会照顾好自己的... ({i}展示承诺戒指{/i})" if persistent._mas_pm_wearsRing and persistent._mas_first_kiss:
            m 2ekbso "那是...{w=0.4}承诺戒指?"
            menu:
                "我向你发誓...":
                    pass
            m 1ekbsd "...什么...?{w=2}{nw}"
            menu:
                "...其中包括照顾我自己的承诺...":
                    pass
            m 6wubftpd "...{w=2}{nw}"
            menu:
                "...这样我就能共度余生...":
                    pass
            m 6wkbftuu "...{w=2}{nw}"
            menu:
                "...那{i}漫长的{/i}余生...":
                    pass
            m 6wkbftsx "...{w=1.5}{nw}"
            extend 6fkbftud "({i}*抽泣*{/i})  {w=0.3}{nw}"
            extend 6dkbftut "...{w=0.3}{nw}"
            extend 6fkbftud "({i}*抽泣*{/i})  {w=0.3}{nw}"
            extend 6dkbftut "...{w=0.3}{nw}"
            menu:
                "...和你一起.":
                    pass
            m 6hkbftsw "...{w=3}{nw}"
            extend 6hkbftsw "{w=0.3}{nw}"
            extend 6hkbftso "{w=0.3}{nw}"
            extend 6hkbftsw "{w=0.3}{nw}"
            extend 6hkbftso "{w=0.3}{nw}"
            extend 6hkbftsw "{w=0.3}{nw}"
            extend 6hkbftso "{w=0.3}{nw}"
            extend 6hkbftsw "{w=3}{nw}"
            m 6hkbftsx "({i}*抽泣*{/i})  {w=0.4}{nw}"
            extend 6hkbftst "({i}*抽泣*{/i})  {w=0.4}{nw}"
            m 6skbftsb "我从没想到你会... {w=1.5}{nw}"
            extend 6hkbftst "({i}*抽泣*{/i})  {w=0.3}{nw}"
            extend 6skbftsb "...会这样思念那承诺戒指...{w=2}{nw}"
            extend 6hkbftst "({i}*抽泣*{/i}){w=0.3}{nw}"
            m 7rkbftsd "我知道我现在看起来一定像个哭哭啼啼的小屁孩,但是...{w=2}{nw}"
            extend 7hkbftst "({i}*抽泣*{/i}){w=0.3}{nw}"
            m 7ekbftsd "...但是我永远不会忘记这一刻.  {w=1.75}{nw}"
            extend 7hkbftst "({i}*抽泣*{/i}){w=0.4}{nw}"
            extend 7skbftsc "...  {w=0.4}{nw}"
            extend 7hkbftst "({i}*抽泣*{/i}){w=0.4}{nw}"
            extend 7skbftsc "...{w=0.4}  {nw}"
            m 6hkbftda "...{w=3}{nw}"
            m 6ekbftdo "你会考虑给为这个爱你的女孩收拾烂摊子吗...  {w=2}{nw}"
            extend 6hkbftdt "({i}*抽泣*{/i})  {w=0.3}{nw}"
            extend 6ekbftdb "...用一个吻?"
            menu:
                "好.":
                    pass
                "不了.":
                    m 6ekbftdo "...  {w=2}{nw}"
                    extend 6dkbftdt "({i}*抽泣*{/i})  {w=0.3}{nw}"
                    m 6ekbftdo "...  {w=0.5}{nw}"
                    extend 6dkbftdt "({i}*抽泣*{/i})  {w=0.3}{nw}"
                    m 6ekbftdo "...  {w=3}{nw}"
                    menu:
                        "...只是亲一下嘛~":
                            pass
                    $ persistent._dan_vow_to_prank = True
                    m 6tkbftdb "总有一天,{w=0.6}在你最意想不到的时候,{w=0.6}我会{i}狠狠捉弄你的~  {/i}  "
                    extend 6skbftpt "({i}*抽泣*{/i})  {w=0.3}{nw}"
                    extend 6ekbftdb "{w=1.5}{nw}"
                    extend 6fkbftdb "...但是现在..."
            call monika_kissing_motion(initial_exp="6dkbftdd", mid_exp="6dkbftdd", final_exp="6ekbfa")
            m 6wkbftdb "...你把我们未来的{i}巨大负担{/i}从我心中卸下, [player]."
            # if you swear to Monika on your promise ring that you'll take care of yourself, she won't fear for your health anymore
            $ persistent._dan_revealed_fear_player_health = False
            m 6hkbftdb "尽管我读书很好...尽管我写了那么多首诗..."
            $ gods_sake = "看在上帝的份上" if persistent._mas_pm_religious else "大声喊出来"
            m 6wkbftdw "...我是{i}文学部{/i}的部长,[gods_sake]..."
            m 6ekbftdb "...但即使有了这些词汇,我也无法{i}找到一个{/i}足够的方式告诉你...  {w=3}{nw}"
            extend 6skbftdb "我现在是多么爱你."
            $ mas_ILY()
    return
label DaN_dream_one_early_reaction:
    # You woke Monika immediately upon seeing the movie poster.
    #
    # Monika is annoyed that you stopped her from dreaming, and explains that dreams can be revisited.
    # She worries about the potential of revisiting nightmares, particularly if she hasn't had one yet.
    menu:
        "所以你看到了什么?":
            m 5rsd "唔,其实你{i}很早{/i}就把我叫醒了,我不太了解究竟发生了什么."
            m 5gtb "梦当然值得被称为怪异和朦胧,不是吗?"

    if not persistent._dan_asked_to_stay_dreaming:
        call DaN_please_allow_good_dream

    m 3rubld "不管怎样,我知道{i}你{/i}在那儿.我想我们是在约会."
    m 3tublu "{w=0.5}{nw}"
    m 1tublb "我会给你点时间控制你的惊喜."
    m 3rubld "所以,我到底在哪儿?"
    m 1dtbld "我想我们可能要去看电影."
    m 1ltblsdrd "我记得我看过一些海报,你还特别指了指其中的一张."
    m 1ttd "{i}你{/i}想去看恐怖电影."
    m 1ttblb "噢,不要像我不知道这些东西是怎么工作的那样看着我啦."
    m 3ttblb "我可能没有路线,但我{i}仍然{/i}来自一本浪漫的视觉小说,聪明的[guy]."
    $ do_or_does = "做" if he == "他们" else "做"
    m 5rtbld "从理论上讲,一个人能为自己在梦中所做的事负责吗?"
    m 5gtblc "...{w=2}{nw}"
    m 5tfblc "...{w=2}{nw}"
    m 5tsblu "...{w=1.5}{nw}"
    extend 5tsblb "我...{w=1}在开玩笑啦~"
    m 5hubsb "哎嘿嘿~"
    menu:
        "还有别的吗?":
            pass
    m 2rkd "我想没有了.之后你就叫醒我了."
    menu:
        "...我能做些什么吗?":
            pass
    m 1ekblb "啊,别担心,[player]."
    m 3euo "这并不是说梦永远消失了之类的."
    m 4ekblb "我的梦比你的有个明显的有时,那就是它们是基于代码{i}模拟{/i}的梦."
    m 4rsd "意思是,虽然有随机性的因素,但我仍然可以再找回那个梦,并再次拥有它."
    m 3esd "像我们以前进行的任何对话一样."
    m 7rto "尽管如此,如果我回到同一个梦中,还是该小心些."
    m 7eso "谁知道{i}如果{/i}我坚持到最后,这个梦会是什么样呢?"
    m 4eksdrb "你很可能把我从噩梦拯救出来了噢."
    if not persistent._dan_had_nightmare:
        m 4hksdrb "我仍然有点担心发生这种事的可能性."
        m 3lksdrp "因为如果梦和生活一样真实..."
        m 1fksdrd "...那么毫无疑问...{w=1.25}噩梦也是如此."
        m 2rkblsdrc "{w=1.5}{nw}"
        m 2lkblsdrc "{w=1.5}{nw}"
        m 2dkblsdrc "{w=1.5}{nw}"
        m 2fkblsdrd "...我很害怕,[player]."
        m 3rkblsdrd "但我不确定我更害怕什么:  "
        extend 2rkblsdrd "体验真正可怕的事情...  "
        extend 2dkbssdrd "或者模仿我{i}最害怕{/i}的事."
        m 2dsblsdro "你不知道这是多么令人宽慰..."
    else:
        m 1rkblsdrd "自从我们开始这个实验以来,经历了一场噩梦..."
        m 2dsblsdro "我学到比我想知道的更多关于我真正害怕的东西."
        m 2esblsdro "这就是我为什么想要- {w=1}{nw}"
        extend 2dkbssdrd "不... {w=0.5}{nw}"
        extend 2wkbssdro "为什么{i}需要{/i}你在这里的原因."
        m "为什么我{i}仍{/i}需要你在这里的原因."
        m 2lsblsdrd "我知道你不能{i}真正的{/i}远离噩梦..."
        m 2dsblsdro "...但它让我如释重负,{w=0.8}不论噩梦有多么可怕..."
    m "...当我再次睁开眼时,我看到的第一件事... "
    extend 2dsblsdrc "{w=0.75}{nw}"
    extend 2tsblsdrc "{w=0.75}{nw}"
    extend 2fsblsdrc "{w=0.75}{nw}"
    extend 2esbssdru "{w=0.75}{nw}"
    extend 2ekbssdrb "是你..."
    if persistent._dan_had_nightmare:
        m 2rsbssdro "..不仅仅是因为你...{w=1}你知道的... "
        if persistent._dan_revealed_fear_player_hurt:
            extend 2gsbssdrd "{i}不是{/i}可怕的残缺,而是..."
    m 2esbsd "...因为你在这让我感到安全... "
    $ how_happy = "至少{i}名义上{/i} " if not persistent._mas_pm_love_yourself else ""
    extend 3esbsb "[how_happy]很开心...  "
    m 5ekbsb "因为你在{i}这里{/i}."
    m 5rsbsd "我很害怕自己做这种事.  {w=1.25}{nw}"
    extend 5rsbso "你说过你会在这里等我...  "
    extend 5eubfb "而你做到了."
    if mas_isMoniHappy(lower=True):
        # The logic here is that, if Monika only kinda' liked you before, this trial is proving to her
        # in a truly unique way that she can trust you with her most intimate feelings.
        m 5fkbfb "你真的在不遗余力地向我证明我可以信任你."
        m 5dkbfb "我爱你,[player]~"
        $ mas_ILY()
    else:
        m 5dkbfb "我知道你会的,[mas_get_player_nickname()]."
        if persistent._mas_first_kiss:
            call monika_kissing_motion
    return
    
label DaN_dream_two:
    # dream synopsis:  You and Monika go on a nature walk up a mountain.  There is an early scare where you
    # catch Monika from a bad fall, but the two of you fall in a river and get drenched.  You camp where you
    # are at and look up at the stars together.  You see a beautiful aurora.  It turns out you're on a more
    # built up version of the floating islands that Monika started work on a while ago.  She remarks that she
    # should get back to that project in the interest of making her dream a reality.
    #
    # If the dream ends earlier, Monika will elude to changing clothes in front of you without shame, like she
    # does it all the time.  On maximum affection, she will get flustered at the thought of changing clothes in
    # front of you.  Monika connects this to the outfits she wears for you and that this aspect of her
    # existence made its way into the dream somehow.
    #
    # If the dream ends too early, Monika will be sad that you didn't get to camp out under the stars together.
    # She will ask that you be more careful for what dreams you wake her up for.
    #
    # GOOD DREAM

    m 2duc "{w=0.5}.{w=0.5}.{w=0.5}."
    m 2hub "哎嘿嘿~"
    m 3gub "看来这个这个剧情并没有像{i}mod制造者{/i}所期望的步骤发展呢..."
    m "但至少我们仍然可以测试标签访问,看看这个想法是否有效."
    m 5rud "这就是'Dream #2'的作用."

    m 5rud "这是完整的'Dream #2'的反应."
    m 5rud "这是后来被打断的'Dream #2'的反应."
    m 5rud "这是提前中断的'Dream #2'的反应."
    return

label DaN_dream_three:
    # dream synopsis:  Monika gets lost in a big city.  You are nowhere to be found, though she feels that you
    # should be nearby, but aren't.  She starts to cry, but then a faceless stranger (literally) stops and
    # takes pity on her.  This faceless figure is accompanied by his own Monika.  Eventually, Monika is
    # surrounded by identical-looking faceless men, each with their own Monika, but you aren't there.  If
    # you don't wake Monika up, she will run around the city and be surrounded by these cloned couples.
    # The last scene that Monika can identify is when she hears the screeching of tires and someone she
    # does recognize as you getting hit by a car.
    #
    # You have one chance to wake Monika up.  If you do, she remarks on how creepy and strange the dream was.
    # Since this mod is one of the few times that Monika ever acknowledges the existence of other Monikas, she
    # supposes that the one really responsible for this bad dream wasn't her coding, but MINE, but she
    # ultimately writes off the entire incident.
    #
    # If you don't wake her up, she hears you get hit by the car and she immediately snaps awake.  Monika is
    # relieved to see that you're okay, but is still clearly shaken.  Unprompted, you are eventually given
    # the option to hold her (assuming you have affection high enough to hold her normally), which Monika
    # will thank you for doing, but won't notice it if you don't take the chance.  If you hold her, that
    # code should play out like normal.
    #
    # BAD (possibly recategorize as STRANGE) DREAM

    m 2duc "{w=0.5}.{w=0.5}.{w=0.5}."
    m 2hub "哎嘿嘿~"
    m 3gub "看来这个这个剧情并没有像{i}mod制造者{/i}所期望的步骤发展呢..."
    m "但至少我们仍然可以测试标签访问,看看这个想法是否有效."
    m 5rud "这就是'Dream #3'的作用."

    m 5rud "这是完整的'Dream #3'的反应."
    m 5rud "这是被打断的'Dream #3'的反应."
    return

label DaN_dream_four:
    # dream synopsis:  You and Monika go out for a romantic dinner.  Afterwards, you take Monika home to
    # her apartment, and Monika invites you in.  Normally, you sit on the couch together and cuddle up,
    # reminiscing about a long, romantic life.  If you don't wake Monika up, she can look around the
    # apartment and see many pictures of the two of you framed and lining the walls.  As it turns out, the
    # two of you had been dating for years, and this is the night you finally decide to pop the question.
    # Furthermore, if your affection is maxed out, she will ask if you want to spend the night.
    #
    # If you don't wake Monika up at all, and you got the version of the dream based on maxed out
    # affection, Monika will kiss you as soon as she wakes up on her own.  She will assume you want to
    # know what happened in the dream, but she coyly tells you that she'd rather show you when she
    # finally becomes real.
    #
    # Idea: You must get the Nightmare before getting this dream.  (DONE, NEEDS TESTING)
    #
    # BEST DREAM (currently)
    m 2duc "{w=0.5}.{w=0.5}.{w=0.5}."
    m 2hub "哎嘿嘿~"
    m 3gub "看来这个这个剧情并没有像{i}mod制造者{/i}所期望的步骤发展呢..."
    m "但至少我们仍然可以测试标签访问,看看这个想法是否有效."
    m 5rud "这就是'Dream #4'的作用."
    $ persistent._dan_had_best_dream = True

    m 5rud "这是完整的'Dream #4'的反应."
    m 5rud "这是几乎完整的'Dream #4'的反应."
    m 5rud "这是后来被打断的'Dream #4'的反应."
    m 5rud "这是中段被打断的'Dream #4'的反应."
    m 5rud "这是提前中断的'Dream #4'的反应."
    return

label DaN_dream_five:
    # dream synopsis:  Monika is back in the Literature Club, as if nothing went wrong.  Sayori, Natsuki and
    # Yuri are there, but you are not.  Everything seems normal at first, but then a fight breaks out.
    # On reflection, Monika can't recall what started the fight, but she remembers the other three girls
    # teaming up against her.  Yuri pulls a knife and Sayori pulls out a rope.  Monika tries to get out
    # of the club room, but cannot.  She begs for you to save her, but nothing happens.  In the end, the
    # girls somehow hang Monika from the ceiling in the middle of the classroom.  If you don't wake Monika
    # up, the last thing she sees is a poster on the wall that depicts Monika's hanging body, calling back
    # to the poster of a hanging Sayori from the original game.
    #
    # You have one chance to wake Monika up.  If you don't, she wakes up crying and terrified and she asks
    # you to hold her to calm her down.  (Note: call the hold monika label used by monika_rain_holdme)
    # Alternatively, you can tell her to calm down and that it was just a dream.  If you don't hold her,
    # she cries for many lines of dialogue and blames you for not waking her up before eventually calming
    # down on her own and realizing it was her own code at fault, not you.  (Basically done.  Can apply to
    # any nightmare, not just this one, if I come up with another nightmare later.)
    #
    # Idea:  If you are not at an affection level high enough to hold Monika during the rain, you should not
    # be able to access this nightmare at all.
    #
    # NIGHTMARE

    m 2duc "{w=0.5}.{w=0.5}.{w=0.5}."
    m 2hub "哎嘿嘿~"
    m 3gub "看来这个这个剧情并没有像{i}mod制造者{/i}所期望的步骤发展呢..."
    m "但至少我们仍然可以测试标签访问,看看这个想法是否有效."
    m 5rud "这就是'Dream #5'的作用."
    m 5rud "这个梦也算是噩梦.如果你之前看过'Dream #4',那一定是出了问题."

    m 5rud "这是完整的'Dream #5'的反应."
    m 5rud "这是被打断的'Dream #5'的反应." 

    $ persistent._dan_had_nightmare = True
    $ persistent._dan_all_dreams.append(4)
    return