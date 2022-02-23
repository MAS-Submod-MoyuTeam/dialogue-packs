init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="eat_with_monika_notseen",
            category=["你", "我们", "浪漫", "其他"],
            prompt="一起去吃东西吧.",
            pool=True,

            unlocked=True

        ),
    )

label eat_with_monika_notseen:

    if not renpy.seen_label("eat_with_monika1"):
        call eat_with_monika1
    else:
        call eat_with_monika2
    return

label eat_with_monika1:
    $ mas_gainAffection(3,bypass=True)
    m 1wud "想一起吃饭吗?{w=0.3}{nw} "
    extend 1subld "真假?"
    m 3ekbla "[player]...{w=0.3}我真的很开心能听到你这么说."
    m 4rkbssdlb "我是说,{w=0.1} 你可以随时去‘再见’选项, 这样我就知道你要去吃东西了."
    m 1ekbsb "但是, 你说要和我一起去吃, 而不是..."
    m 1eka "我知道我实际上是不可能吃到的, 但是...{w=0.3}{nw} "
    extend 1dkbfa "这个小细节让我觉着更贴近你的世界了~"
    m 7rsblu "更不用说它让我尝到了和你一起过家庭生活的滋味~"
    m 1eua "好了好了,{w=0.3} 有点话痨, 让你等太久啦.{w=0.3}{nw} "
    extend 1hua "毕竟你应该有些饿了."
    jump eat_with_monika_main
    return
    
label eat_with_monika_main:
    m 1eub "所以, 我们吃什么呢?{nw}"
    $ _history_list.pop()
    menu:
        m "所以, 我们吃什么呢?{fast}"
        "早饭":
            m 3hub "耶~精致早饭!"
            m 4tsb "毕竟,{w=0.1} 早餐是三餐中最重要的一餐."
            m 2lksdra "我希望你不会经常翘掉早餐, [mas_get_player_nickname()]."
            m 7esa "早就有研究标兵, 早餐有助于使整体健康状况更好,{w=0.1} 因为它可以减少患糖尿病和心脏病的可能性."
            m 7eub "而且还能帮助提高你的记忆力和精神力!{w=0.3}{nw} "
            extend 3wub "这不是很神奇吗?"
        "午饭":
            m 3rua "现在吃午饭也是不错的选择哦~"
            m 7eub "如果我和你在一起,{w=0.1} 我会为你做一碟健康的沙拉~"
            m 1rtd "你喜欢什么样的沙拉呢?{w=0.3}{nw} "
            extend 3esa "就我而言, 我是蔬菜沙拉的忠实粉丝."
            m 4eub "但水果沙拉也许也不错,{w=0.1} 特别是如果你想吃点甜食的话."
            m 1eka "于此同时, 你也要为你自己做些什么{w=0.1}, 不要吃不健康的饰品哦, [player]."
        "晚饭":
            m 1ttb "晚饭?{w=0.1} 或许这就像一个...{w=0.3}{nw}"
            extend 1tsblu "约会."
            m 3gsblb "我要去换身更漂亮的衣服吗?"
            m 1hublu "欸嘿嘿~{w=0.3}{nw} "
            extend 3lsbla "只是开个玩笑, [player]."
            m 5ksbsu "不过你想的话, 我们随时都可以去约会~"
        "零食":
            m 1ruc "呃...{w=0.3}{nw}"
            extend 7eud "吃的准备好了吗?{w=0.3} 或者说,{w=0.1} 要喝什么东西吗?{nw}"
            $_history_list.pop()
            menu:
                m "吃的准备好了吗?{w=0.3} 或者说,{w=0.1} 要喝什么东西吗?{fast}"
                "我准备了些吃的~":
                    m 1hub "好的, 我只是想确认一下!"
                    m 3eua "如果你想和我一起喝点什么, 你可以随时回到之前的菜单, 按'喝点什么'."
                    m 4esb "总之, {w=0.1}你知道吗, 一天中吃点东西其实对你有好处"
                    m 7lksdla "我们先说清楚, 我指的是健康的零食, {w=0.1}不是垃圾食品"
                    m 1ekb "所以帮我一个忙, 选择一些至少是健康的东西, 好吗"
                "我准备了些饮料~":
                    m 1wuo "哇哦!{w=0.3}{nw} "
                    extend 3wub "你要喝什么?{nw}"
                    $_history_list.pop()
                    menu:
                        m "哇偶! 你要喝什么?{fast}"
                        "咖啡":
                            m 7hub "你喜欢咖啡真是太好了, [player]~"
                            m 1tua "这表示我们真的很般配,{w=0.1} 对吧?"
                            m 2dkbfb "我真的很想很想在某天早上醒来, 看着你坐在桌子旁, 等着和我...{nw}"
                            extend 5dkbfa "分享一杯咖啡~"
                            m 5ekblu "没有比这开始一天更好的方式了~"
                        "热可可":
                            m 1lub "那还不错, 是什么类型的?"
                            m 3eua "我是普通热巧克力味的头号粉丝{w=0.3} 但我也很喜欢薄荷味的."
                            m 7rsa "你知道我喜欢热天而不是冷天,{w=0.1} 但,{w=0.3}{nw} "
                            extend 1ekblu "和你一起依偎在沙发上, 啜饮着一杯热可可, 也是很好的选择呢~"
                        "茶":
                            m 1rtb "你要睡觉吗?{w=0.3} 或许你要读基本书?"
                            m 3lksdra "也许你只是喜欢茶, 啊哈哈."
                            m 4eub "茶有些惊人的益处,{w=0.1} 所以我不会抱怨这些啦."
                            m 7esa "我自己更喜欢咖啡, 不过睡前来杯茶也不错."
                        "水":
                            m 1sub "多喝水总是好事, [player]!"
                            m 7eua "挑喝的话, 水总是最佳选择不是吗."
                            m 3hua "如果你真的想的话,{w=0.1} 我可以为你倒一杯水哦~"
                        "别的":
                            m 1eub "好吧,{w=0.1} 不管你选了什么,{w=0.1} 那就喝吧~"
                            m 1hublu "这也是我喜欢的."
    m 2esb "OK, {w=0.1}我准备好了.{nw}"
    $ _history_list.pop()
    menu:
        m "OK, {w=0.1}我准备好了.{fast}"
        "我去准备一下.":
            m 2hub "好的, [mas_get_player_nickname()]."
            m 3eub "慢慢来, 准备好了叫我一下就好了~"
            m 1eua ".{w=0.3}.{w=0.3}.{w=0.3}{nw}"
            $ _history_list.pop()
            pause 5
            menu:
                "我回来了":
                    m 1hua "嗯嗯!"
                    m 2eub "继续吧, [mas_get_player_nickname()]."
                    m 7eua "吃完了叫我一下,{w=0.1}好吗?"
                    m 5esu ".{w=0.3}.{w=0.3}.{w=0.3}{nw}"
                    $ _history_list.pop()
                    menu:
                        "我吃完了!":
                            m 5eub "都吃完了?{w=0.5}{nw} "
                            extend 1hub "欢迎回来!"
                            m 1ekbla "谢谢你每天都花时间陪我,{w=0.1} 你真是个小甜心~."
                            m 1ekbfu "我爱你, [mas_get_player_nickname()]."
                            m 3hubla "我已经开始期待下次了~"
        
        "我准备好了!":
            m 1hua "嗯嗯!"
            m 2eub "继续吧, [mas_get_player_nickname()]."
            m 7eua "吃完了叫我一下,{w=0.1}好吗?"
            m 5esu ".{w=0.3}.{w=0.3}.{w=0.3}{nw}"
            $ _history_list.pop()
            menu:
                "我吃完了!":
                    m 5eub "都吃完了?{w=0.5}{nw} "
                    extend 1hub "欢迎回来!"
                    m 1ekbla "谢谢你每天都花时间陪我,{w=0.1} 你真是个小甜心~."
                    m 1ekbfu "我爱你, [mas_get_player_nickname()]."
                    m 3hubla "我已经开始期待下次了~"
return "love"

label eat_with_monika2:

    m 1wub "啊,{w=0.1}想一起吃东西吗, [player]?"
    jump eat_with_monika_main
    return