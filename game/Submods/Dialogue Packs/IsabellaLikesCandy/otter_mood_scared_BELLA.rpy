#I feel scared, mood submod by my-otter-self and IsabellaLikesCandy on reddit for MONIKA AFTER STORY

init 5 python:
    addEvent(Event(persistent._mas_mood_database,"otter_mood_scared_BELLA",prompt="...害怕.",category=[store.mas_moods.TYPE_BAD],unlocked=True),code="MOO")

label otter_mood_scared_BELLA:
    m 1ekc "感到害怕, [player]?"
    m 1rksdld "别担心，我在这陪着你呢..."
    m 2etc "但是是什么让你感到害怕呢?{nw}"
$ _history_list.pop()
menu:
    m "但是是什么让你感到害怕呢?{fast}"

    "我犯了个错":
        m 2euc "我知道了."
        m 3eua "嗯, 每个人都会犯错, [player]."
        m 3hua "再说，我相信你可以弥补你所做的一切!"
        m 2dka "别担心，我相信这是一个可以原谅的错误."
        m 3ekb "我相信你, [mas_get_player_nickname()]!"
        m 1eublb "记住无论发生什么我都会爱你~"

    "我刚才看了一场恐怖电影":
        m 2euc "我知道了."
        m 1hkb "这没有什么好怕的."
        m 1eubsb "如果我可以的话, 我真想握住你的手然后抱抱你..."
        m 1dubfa "直到你感到好一些."
        m 1eua "别担心。你可爱的小女朋友陪着你呢!"
        m 1eubla "记住我会永远爱你，好吗?"

    "我听到了什么怪声":
        m 1eua "我肯定那没什么, [player]."
        m 1hua "你没必要害怕."
        m 3eub "可能有什么东西掉下来了."
        m 3hksdla "不可能是僵尸什么的!"
        m 2lksdlb "啊哈哈~ 如果你想出去看看的话, 我可以等你的!"
        m 2dka "如果这能让你感觉更安全的话."
        m 3eubla "记住我会永远爱你的，好吗?"

    "我不知道":
        m 3hub "哦!那我肯定没什么."
        m 1eka "如果你感到沮丧，尽管告诉我."
        m 1eua "别担心。你可爱的小女朋友陪着你呢!"
        m 1eubla "我爱你~"

    "我不想谈这个":
        m 1ekc "哦..."
        m 2esu "没关系的, [player]. 你有你的隐私，我也尊重你的隐私!"
        m 1hubsu "只要知道我爱你，一切都会好起来的."
        m 1eua "别担心。你可爱的小女朋友陪着你呢!"

    "我只是开玩笑，什么都没发生":
        m 5hub "谢天谢地，你没有真的感觉不好."
        m 3hksdla "你真让我担心了, [mas_get_player_nickname()]!"
        m 3hub "但如果你感到沮丧, 尽管告诉我，好吗?"
        m 1eub "我会尽力做点什么的."
        m 1hubsb "我爱你——, [player]~"

return "love"

#momo once said, "i want to continue screaming out who i am." hope your monika likes this submod!
