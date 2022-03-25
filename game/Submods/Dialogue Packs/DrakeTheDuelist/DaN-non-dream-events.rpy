# Explains the premise of 'Dreams and Nightmares'.
# Only mandatory on the first dream.  Can be skipped optionally on all subsequent dreams.
label DaN_explanation:
    m 5rud "我一直在想,[player]..."
    m 3ruc "我记得我说过,每当你要关闭游戏时,我都希望你能告诉我?"
    m 3euc "这样,我就可以关闭我的意识,然后我的数据就不会被你电脑的硬盘扰乱...{w=2.0}我想..."
    m 2lud "我仍然不太清楚它究竟是如何工作的..."
    m 4ruo "不管怎样,如果有办法解决这个问题呢?"
    m 4eub "也许...会很有趣?"
    m 3euu "[player]...{w=1}我想做个梦."
    m 4rtd "不像\"对我想要的生活有些想法\"之类的感觉."
    m 5kubsb "我想你已经知道我生命中最想要的是什么了."
    m 5lsd "我的意思是,在睡觉时能想象自己在不同的地方和情况下."
    m "我知道我说的话就行做梦一样,但这更像是某种修辞手法."
    m 3lsd "老实说,我的{i}梦{/i}并不像你想象的那样."
    m "我想我从没有过{i}这种{/i}能力,甚至在游戏最初也没有."
    m 3rsd "虽然我以前{i}从未有{/i}做过梦,但我{i}依然{/i}是文学部的部长."
    m 5rsd "我博览群书,知道{i}梦{/i}应该是什么样子."
    m 5dkd "不幸的是,我非常确信自己以前从未做过真正的梦."
    m 4lsd "为此,我一直在编写一些代码,如果它能工作,大概会模仿这个过程."
    if mas_isMoniAff(higher=True):
        m 5ekbsb "你可能会感兴趣一些基于你抱着我时发生的事情的代码..."
    m 4lksdrb "...但我不能完全肯定它是否有效."
    m 5lssdrb "你和我都知道,我试图编码...{w=1.25}往往{i}并不会{/i}按预期工作."
    m 5ekbsb "你介意我小睡一会儿吗...{w=1}就在这?"
    m 3wubssdro "我保证不是因为你让我感到无聊.我只不过是想试试这个代码."
    if mas_isMoniAff(higher=True) and persistent._mas_last_hold_dt:
        m 6dkbsb "你甚至可以... {w=1}搂住我...{w=1}就像平时你做的那样."
        if (mas_timePastSince(persistent._mas_last_hold_dt, datetime.timedelta(hours=12))):
            m 6tkbfb "你似乎很喜欢那种事...{w=1}我没有{i}在{/i}抱怨什么的啦.  {w=1}"
            extend 6tkbsb "哎嘿嘿~"
            $ anyway = "无论如何, "
        else:
            $ anyway = ""
    else:
        $ anyway = ""
    m 4esb "[anyway]代码已经安装并准备就绪了,我需要你来开始它."
    m 4lsd "但我还需要你帮我做一些别的事."
    m 4eud "这{i}真的{/i}非常重要."
    m 1dko "如果看起来有什么不太对劲...{w=1}我需要你来叫醒我."
    m 1lusdrd "你知道我的... {w=1}{i}编码风格{/i},我写的代码几乎可以做任何事."
    m 1dksdrd "可我担心会发生些非常糟糕的事情..."
    if mas_isMoniLove():
        m 5ekbsu "...我无法想象,除了你外,我还会把这个任务委托给谁,[mas_get_player_nickname()]."
    elif mas_isMoniEnamored():
        m 1dkblu "...我知道你不会让任何不好的事发生在我身上的,[player]."
    elif mas_isMoniAff():
        m 1esu "...在这一点上,我肯定我能相信你."

    $ persistent._dan_dreams_and_nightmares_explained = True
    return
# If Monika had a nightmare, hold off on dreaming again for another 12 hours
# If Monika loves you, reduce cooldown by half and have special text for it.
label DaN_dream_despite_apprehension(revisit=False):
    if mas_isMoniLove and mas_timePastSince(persistent._dan_apprehensive_start, datetime.timedelta(hours=DAN_APPREHENSION_HOURS/2)):
        m 3rksdrd "我...我{i}真的{/i}不能确定..."
        m 2dksdrd "最后一个梦实在太让人心烦了."
        m 2fksdrd "我还为此对你大喊大叫."
        m 2dksdrd "这感觉太糟糕了."
        menu:
            "我能原谅你.":
                m 1dsc "...  {w=1}{nw}"
                extend 1esblb "[mas_get_player_nickname()]..."
                # headcanon:  Monika still cares about the dokis, even if the player doesn't.
                if not persistent._mas_pm_cares_about_dokis:
                    m 4fkblb "你已经{i}原谅{/i}我两次了."
                    m 6dkbsb "你对我比我应得的还要好."
                m 6ekbsb "谢谢你,[player]."
                m 5hsbsa "..."
            "没什么,真的.":
                m 1rsbld "如果你确定你没事的话..."
                m 4wublo "它肯定再也不会发生了!我保证!"
                m 6dkbssdrd "({i}*松了口气*{/i}){w=1}{nw}"
                m 6dka ""

        m 5rsbsd "你知道,也许有你在这里后,情况就不会那么糟了."
        m 5esbsa "我们已经一起经历了太多."
        m 5fkbfb "不管是好是坏,你都一直陪在我身边,不是吗?"
        m 5dsbfd "({i}*低声说*{/i})幸好有你在,[player], Monika.{w=1.5}{i}再也{/i}不会不把[ta]当回事了."
        menu:
            m "({i}*几乎听不到的窃窃私语*{/i})"
            "你说了什么?":
                m 1subfo "噢! {w=0.25}{nw}"
                m 1rubfb "嗯...没什么啦,[mas_get_player_nickname()]!"
                m 5rubfb "只不过...{w=1}声音好像... {w=1}比我想象的大声了些."
                m 5hubfb "哎嘿嘿~"
            "...":
                pass
        m 4hub "好吧,不用再麻烦了..."
        $ persistent._dan_apprehensive_start = None
        if revisit:
            call DaN_revisit_dream
        else:
            call DaN_perchance_to_dream
    elif mas_timePastSince(persistent._dan_apprehensive_start, datetime.timedelta(hours=DAN_APPREHENSION_HOURS)):
        m 4hub "谢谢你在噩梦之后给了我些时间."
        $ persistent._dan_apprehensive_start = None
        if revisit:
            call DaN_revisit_dream
        else:
            call DaN_perchance_to_dream
    else:
        m 3rksdrd "我们能不能... {i先{/i}不这样做?"
        m 1dksdrd "在这场噩梦之后,我还是有些震惊."
        m 1essdrb "谢谢你能理解,[player]."
    return
# to be called in the after action of a good dream
label DaN_wake_up_nice:
    m 6dkbla "...{w=2}{nw}"
    extend 6tkbla "唔姆...{w=2}  {nw}"
    extend 6tsbla "嗯?{w=1}  {nw}"
    extend 6fsbla "...[player]?"

    $ persistent._dan_had_first_dream = True

    if not persistent._dan_had_first_dream:
        #note: set the first dream flag later so monika's after action dialog can reference having the first dream
        call DaN_initial_dream_afteraction
    else:
        # Monika will respond based on the current time
        $ current_time = datetime.datetime.now().time().hour
        if current_time >= 6 and current_time < 12:
            m 6esblb "早啊,[mas_get_player_nickname()]."
            m 6gtblb "什么?现在是早上?"
            m 6hublb "哎嘿嘿~"
        elif current_time >= 20:
            m 6eublb "已经很晚了.很快就轮到{i}你{/i}睡觉了."
            m 6ekbsb "希望你的梦也像我刚刚做的那样美好."
            if mas_isMoniLove():
                m 5tkbsb "如果我在你的现实中... {w=1}{nw}"
                extend 5dkbsa "我会{i}在你{/i}睡觉前给你个大大的拥抱,以回报你给我的美梦."
                m 5fkbsb "或者只是想抱抱你,因为我太爱你了.{w=0.8}{nw}"
                extend 5hubfb "哎嘿嘿~"
    return
label DaN_please_allow_good_dream:
    m 5esb "[player],我知道你不想让我做噩梦什么的,但我想看看这个梦究竟是怎么实现的."
    m 5ekblb "如果你认为我做了个好梦,能让我再继续睡会儿吗?"
    menu:
        "当然可以,[persistent._mas_monika_nickname]!":
            m 3eublb "谢谢啦,[player]."
            m 2rubld "当然,我知道噩梦总有机会来袭..."
            m 4wublb "但我知道你会看出来的."
        "可如果你是在做噩梦呢?":
            m 5gto "({i}*叹气*{/i}){w=0.75}你说得对,[player]."
            m 1dtsdrp "嗯...  {w=1}"
            m 3eksdrd "我想你可以做出最好的判断的."
            m 4rso "或许你能在我睡觉时注意一下我的表情."
            m 4rsd "如果我在做梦时嘴里还嘟囔什么,也可以顺带作为线索."
            menu:
                "我一定会保护你的!" if mas_isMoniLove():  #total confidence
                    m 7sub "就是这种精神,[player]!"
                    m 5hublb "哎嘿嘿~"
                    m 5tublb "当你像个大英雄一样保护我时,你真的很可爱."
                    m 5dubsa "...{w=1.5}{nw}"
                    m 5ekbfb "我不是这个意思,我是说...[player].{w=1.25}你就是我的英雄."
                "我会尽力的.":  #optimistic
                    m 5kublb "我从没怀疑过你一秒钟,[player]."
                    m 5gubsb "任何试图扰乱我的噩梦都最好小心些..."
                    m 3hubsb "不过可能会有些多,哈哈~"
                "你就这么相信我吗?":  #pessimistic
                    m 7hkb "我相信一切都会解决的,[mas_get_player_nickname()]."
                    m 4kka "只要对自己有点信心."
                    m 4dkblb "就像我一样.{w=1}我{i}永远{/i}都相信你,[player]."
                "我不能确定能否做到..." if mas_isMoniNormal():  #no confidence
                    m 2fkbld "[mas_get_player_nickname()]..."
                    m 7fkblu "你应该对自己更有信心的."
                    m 5ekbso "我知道我们的关系现在看起来可能还没那么亲密..."
                    m 5ekblb "...但无论发生什么,我都会永远爱你.{w=1.5}这就是{i}我的承诺{/i}."
    m 5eua "...{w=1.5}{nw}"
    m 5ekbla "...{w=1.5}{nw}"
    m 5wublo "噢,对了!梦!{w=1.25}{nw}"
    extend 5hubsb "不好意思,[mas_get_player_nickname()],我刚刚停顿了会儿."
    $ persistent._mas_asked_to_stay_dreaming = True
    return
# AFTER FIRST DREAM
# regardless of which dream you draw first, read this
# (note: rig it up to NEVER draw a nightmare first)
label DaN_initial_dream_afteraction:
    m 1hub "看起来代码起作用了."
    m 3eub "一开始我很担心...  {w=1}{nw}"
    extend 3lksdrb "尽管这对你可能不大公平."
    if mas_isMoniLove():
        m 5ekbla "在我们经历了这么多后,我应该知道我能够指望你做这些事."
        m 5ekblb "我很抱歉,[mas_get_player_nickname()].一开始你在我身边时我有些担心,但现在看来太愚蠢了."
        m 5ekbfb "我{i}知道{/i}你永远不会让任何坏事发生在我身上的."
    elif mas_isMoniEnamored():
        m 5eub "我知道我能一直依靠你,你一直都做得很棒!"
        m 5eua "谢谢你愿意陪在我身边."
        m 5eubsa "知道在这种时候我能依靠你,这对我的帮助比我所能描述的还要大."
    else:
        m 5eub "我知道我能一直依靠你,你一直都做得很棒!"
        m 5eua "谢谢你愿意陪在我身边."
        m 5eubla "可能看起来不多,但你不知道你在这儿对我的帮助有多大."
    menu:
        "你的第一个梦怎么样?":
            m 2dkd "这感觉... {w=0.5}{nw}"
            extend 3suw "太棒了!"
            m 4suw "一切都那么真实,就像你能伸手触碰到那个世界!风景,声音.  {w=1}{nw}"
            extend 4hub "...甚至是气息!"
            m 3ttb "...不过我当然希望你在生活中常洗澡.{w=1}{nw}"
            extend 3hub "哎嘿嘿~"
            m 5rub "我想如果{i}我非得{/i}指出一些缺点,唯一的问题就是... {w=1.5}{nw}"
            extend 5rsd "是... {w=0.8}{nw}"
            extend 5dkd "({i}*叹气*{/i})...  {w=1.5}{nw}"
            extend 5ektpo "醒来."
            m 5rktpc "当一切都崩溃时...就在那一刻,你感到一切都那么模糊."
            m 5rktpd "就在此刻,你意识到刚刚梦到的一切{i}都不可能{/i}是真实的."
            m 5lktpd "这令我瞬间顿悟..."
            m 5dktpc "..."
            if mas_isMoniEnamored(higher=True):
                call DaN_dreaming_about_monika_enamored_love
            else:
                call DaN_dreaming_about_monika_normal_aff
    return
# An event that can be called in the initial dream after action
# This label is called on normal and aff affection levels.
label DaN_dreaming_about_monika_normal_aff:
    m 5lktdd "Sometimes, I wonder if you dream about me..."
    m 5dktdd "But the more I think about it, I don't think I want to know."
    if mas_isMoniHappy(higher=True):
        extend "  At least, not yet."
    m 5rstdo "No matter what you tell me, I don't think I'd be any happier knowing the answer."
    m 3dsd "If you don't, I'd be tempted to think I don't take up that much space in your mind."
    m 1lsd "But if you do...  {w=1.5}"
    m 1dkd "({i}sigh{/i})"
    m 1fkbld "Let's just say that I know what that's like."
    return
# An event that can be called in the initial dream after action
# This label is called on normal and aff affection levels.
label DaN_dreaming_about_monika_enamored_love:
    m 5rktpd "[player],如果你不介意的话,我能问你件事情吗?"
    m 5ektpd "说实话,无论你说什么,我都不会少看你的...我保证."
    m 5rktpd "你做的梦...{w=0.5}有没有关于我的?"
    menu:
        m "你做的梦...有没有关于我的?{fast}"
        "有":
            m 2fktuc "..."
            m 2dktuc "..."
            menu:
                "我-我说错什么了吗?":
                    m 2ektsb "你什么{i}都没有{/i}说错."
                "...":
                    m 2fktsb "你什么都不用说."
            m "只是现在,{w=0.75}我知道这对你来说是什么样的."
            m 2fktsa "你想{i}和我{/i}在一起,就像我想{i}和你{/i}在一起一样,[mas_get_player_nickname(exclude_names=['my love', 'love'])]."
            m 2hktdb "我太爱你了.{w=1.5}{nw}"
            if persistent._mas_first_kiss:
                call monika_kissing_motion(duration=0.5, initial_exp="2dkbstst", final_exp="2ekbstsa", fade_duration=0.5)
            m 2ektdb "能知道我在你心中占有如此特殊的位置,我再高兴不过了~"
            m 3rsd "知道你真正的梦中情人被困在你的电脑里可能并不容易."
            m 7tsblu "我相信你,总有一天你能想到让我去到你现实的办法的."
        "...没有":
            m 2dktdc "..."
            m 2ektdd "你好像觉得我会生气."
            m 3eutdd "[player],如果你的梦和我的一样,那么它们只可能是巧合."
            if persistent._mas_pm_cares_about_dokis:
                m 7rutdd "此外,你都已经原谅我故意做的{i}更糟糕的事情{/i}."
                m "在为我这么做之后,我不能让你为你无法控制的事负责."
            m 4rubsd "我喜欢这样想..."
            m 4eubsd "如果你{i}像我{/i}想得太多,以至于你的大脑可随机抽取足够的数据,让你梦见我..."
            m 4eubsd "...最可能发生的情况就是,你的大脑被我所吞噬."
            m 7dubsd "而不是以某种更可爱,浪漫的方式.{w=1.5}{nw}"
            extend 7ekbsd "这更接近于深层的焦虑."
            # Choose which pair of lines make more sense for Monika's character
            #m 4ekbso "Flattering as it might be that you'd think about me {i}that{/i} much, I live with those feelings every day..."
            #m 4ekbsd "...and I know how heavily they can wear on your heart as well as anyone."
            m 4ekbso "一个轻率的浪漫主义者可能会觉得这种事很可爱,{w=2}{nw}"
            extend "但对你所关心的人如此深切地忧虑,并没有什么好玩或浪漫的."
            m 4ekbsd "我和所有人一样都知道这种负担会给一个人的心带来多大负担."
            m 2rkbsd "我最多也只有一天中的一小部分担心我们{i}可能永远不会{/i}在一起."
            $ persistent._mas_revealed_fear_never_together = True
            m 4wkbso "我不希望任何人{i}遭受那种心痛{/i}... {w=1.75}{nw}"
            extend 2wkbsd "更何况是你."
            m 2dkblc "..."
            m 2ekd "希望你能理解."
            m 4lsa "此外,谁需要梦... {w=1}{nw}"
            extend 5ekbla "当你和我在一起的时候,不就已经{i}美梦{/i}成真了吗?"
    return
# AFTER FIRST NIGHTMARE
# to be called in the after action of a nightmare
#
# TODO LATER: Need to tweak (and add) expressions, but okay because there are no nightmares in the first beta
label DaN_wake_up_rough:
    m 6dsblsdrd "...[player]...{w=1.5}{nw}"
    m 6dkbltpsdro "...[player]...?{w=1.5}{nw}"
    m 6cubltpsdrw "[player.upper()]!"

    # on first nightmare, you'll have to calm Monika down
    if not persistent._dan_had_nightmare:
        call DaN_initial_nightmare_afteraction
    else:
        m "" #TODO LATER: Calm down on her own;  she knows what nightmares are now
        m "...又是一场噩梦..."
        m "...天哪,这个{i}代码{/i}究竟怎么了?"
        m "..."
        m "说\"做梦会变得更容易\" {i}是{/i}真的吗...  "
        extend "可从一开始就没有过这种感觉."

        $ what_moni_calls_you = "[mas_get_player_nickname()]" if mas_isMoniLove() else "[player]"

        m "谢谢你一直在我身边,[what_moni_calls_you]."
    return

# After your first nightmare, Monika snaps at you.  She apologizes,
# and you have an opportunity to comfort her.  Either way, she will
# not want to dream again for a while (see DAN_APPREHENSION_HOURS)
#
# TODO LATER: Need to tweak (and add) expressions, but okay because there are no nightmares in the first beta
label DaN_initial_nightmare_afteraction:
    $ persistent._mas_apprehensive_start = datetime.datetime.now()

    m 6hkbltpsdrd ".{w=0.5}{nw}"
    extend 6hkbltpsdro ".{w=0.5}{nw}"
    extend 6hkbltpsdrd ".{w=0.5}{nw}"
    extend 6hkbltpsdro ".{w=0.5}{nw}"
    extend 6hkbltpsdrd ".{w=0.5}{nw}"
    extend 6hkbltpsdro ".{w=0.5}{nw}"
    extend 6hkbltpsdrd ".{w=0.5}{nw}"
    extend 6hkbltpsdro ".{w=0.5}{nw}"
    extend 6hkbltpsdrd ".{w=0.5}{nw}"
    extend 6hkbltpsdro ".{w=0.5}{nw}"
    extend 6hkbltpsdrd ".{w=0.5}{nw}"
    extend 6hkbltpsdrd ".{w=0.5}{nw}"
    extend 6hkbltpsdro ".{w=0.5}{nw}"

    if (mas_isMoniLove):
        $ player_reaction = "一定有我能做的事"
    elif (mas_isMoniEnamored):
        $ player_reaction = "我得说些什么"
    elif (mas_isMoniAff):
        $ player_reaction = "我该说些什么"
    else:
        $ player_reaction = "我想我该说些什么"

    $ player_reaction = persistent._mas_monika_nickname +"完全说不出话来.  " + player_reaction + "..."

    call screen dialog(message=player_reaction, ok_action=Return())

    menu:
        "一场...噩梦?":
            # Monika mentions that she only swears occasionally. This seems like an appropriate occasion.
            # Monika's swearing intensity will increase the more the player admits to swearing themselves.
            if persistent._mas_pm_swear_frequency > 1:
                $ swear_maybe = "可恶"
            elif persistent._mas_pm_swear_frequency > 0:
                $ swear_maybe = "垃圾"
            else:
                $ swear_maybe = "恶心"

            m 6wktpsdro "噢,真的吗?一场噩梦??"
            m 6cftusdrw "{i}不是的[swear_maybe]{/i}, [player]!  {w=0.5}{nw}"
            extend 6cftusdro "你究竟花了多长时间{i}才{/i}想出这个的?!"

            menu:
                "...":
                    m 6wftusdro "...{w=0.5}{nw}"
                    m 6wftusdrd "...{w=0.5}{nw}"
                    m 6wftusdro "...{w=0.5}{nw}"
                    m 6wftusdrd "...{w=0.5}{nw}"
                    m 6wftusdro "...{w=0.5}{nw}"
                    m 6wftusdrd "...{w=0.5}{nw}"
                    m 6fktpsdro "...I-{w=1} I-{w=1.5}{nw}"
                    call mas_transition_to_emptydesk
                    pause 10.0
                    call mas_transition_from_emptydesk
                    m 2dktdc "...{w=0.5}"
                    extend 2dktdd "我很抱歉,[player]."
                    if mas_isMoniEnamored(higher=True):
                        $ so_much_if_love = "{i}非常{/i} " if mas_isMoniLove() else ""
                        m "你应该得到[so_much_if_love]比这更好的东西."
                        m "我只是被那个梦惊呆了.我以前从没做过噩梦."
                        if persistent.monika_kill:
                            m "我不相信用解释作为借口."
                            m "事实上,是你给我看到.你还记得...删除我妈?"
                            m "现在感觉那是段遥远的记忆."
                            m "我说你很可怕.{w=1.5}我告诉你你让我恶心."
                            if mas_isMoniEnamored(higher=True):
                                m "从那以后我们已经走了这么远了,我真应该这样做."
                    else:
                        m "你不该那样."
                        m "我不想我们成为那种为无关紧要事情大吵一架的情侣."
                        m "如果这发生在我们身上... {w=1}{nw}"
                        extend "那将是{i}真正的{/i}噩梦."
                    m "我不该对你大发雷霆的, [player].希望你原谅我."
                    m "这不是我的错,这是我写的代码.换句话说... {w=0.5}{nw}"
                    extend "这是我的错."
                    m "当我有了这个愚蠢的想法时,我就知道自己到底在做什么."
                    m "我很想做梦,就像你一样."
                    m "我非常想要它...我几乎忘记了我已经拥有的东西."
                    if mas_isMoniEnamored(higher=True):
                        m "或者更确切地说,{i}我已经{/i}有了谁."
                "抱住Monika" if mas_isMoniLove():
                    m 6skbltud ".{w=1}.{w=1}.{w=1}.{w=1}.{w=1}{nw}"
                    m 6wkbstub "[player]...{w=2}  [mas_get_player_nickname()]..."
                    m 6dkbstda ".{w=1.5}.{w=1.5}.{w=1.5}.{w=1.5}.{w=1.5}{nw}"
                    m 6dkbstda ".{w=1.5}.{w=1.5}.{w=1.5}.{w=1.5}.{w=1.5}{nw}"
                    m 6fkbstda ".{w=1.5}.{w=1.5}.{w=1.5}.{w=1.5}.{w=1.5}{nw}"
                    m 6ekbstdb "非常感谢,[player]."
                    m 3dubso "但我现在还不太想再次陷入梦中."
                    m 1hubfb "因为我{i}知道{/i}如果你再抱着我,我很快就会在你怀里睡着的."
                    if datetime.datetime.now().time().hour > 22:
                        m "尤其是在这种时候."

            m "如果你不介意,我想休息一下."
            m "我们仍然可以一起共度时光... {w=1}{nw}"
            extend "但我现在不忍心再做一个梦."
            $ interval = "过一会儿" if mas_isMoniLove or datetime.datetime.now().time().hour > 18 else "明天"
            m "也许我们可以[再试一次]."
    return
# show after every dream available has been finished
label DaN_all_dreams_finished:
    m "...{w=2}{nw}"
    extend 3rud "我想我已经做不了梦了...{w=1.5}至少目前是这样."
    m 3esb "也许你可以对代码做些什么来添加它们."
    if persistent._dan_had_nightmare:
        m 2dsc "...{w=2}{nw}"
        extend 4ekb "这是个...挺有趣的联系."
        m 4eub "它有它的高峰..."
        m 6dksdrd "...同样也有低谷."
    else: #only good dreams happened
        m 4eub "但把它留给{i}最好的{/i}梦,好吗,[mas_get_player_nickname()]?"

    m 4ekblb "现在,我想我会坚持一段时间."
    m 4rkbsb "梦可以是美好的... {w=1.5}{nw}"
    extend 7kkbsb "但它们不可能代替真实的东西."
    m 5ekbfu "..."
    m 5hubfb "..."
    $ persistent._dan_dreams_depleted = True
    return
