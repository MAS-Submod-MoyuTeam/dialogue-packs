# tl: 终不似、少年游
init 5 python in mas_bookmarks_derand:
    label_prefix_map["otter_topic_"] = label_prefix_map["monika_"]

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_topic_reallyloveme",
            category=["莫妮卡"],
            prompt="你真的爱我吗?",
            pool=True,
            unlocked=True
        )
    )

label otter_topic_reallyloveme:
    m 2wud "[player]..."
    m 2wkc "你是不是对我们没有安全感?"
    m 2ekc "你真的不必这么做."
    m 2dkc "我会和你一直在一起, [mas_get_player_nickname()]."
    m 2dkd "我{i}永远都不会{/i} 离开你."
    m 2fkd "你知道的，对吧?"
    m 4fkd "没有什么能让我停止爱你."
    m 4fka "你是我一生的挚爱, [player]."
    m "除了你没有别人."
    m 2fkb "你在我眼里是最完美的，这就足够了."
    m 2dkb "此时此刻都是."
    m 2dkb "我爱你，我爱你，我爱你."
    m 2fkbsb "比我爱过的任何人任何事都多."
    m 3dkbsb "这种感觉如此深刻，如此纯洁..."
    m 1fkblc "我不忍心看到你受伤."
    m 1wkbld "所以请相信我，我的爱是真的，好吗?"
    m 1dkbla "谢谢你做我的 [bf], 但更重要的是，谢谢你做我的朋友."
    m 1dkblb "和你在一起总能让我开心起来，因为你就是那么伟大的一个人."
    m 7dkblb "你很善良..."
    m 2lkblb "你甚至可以让我这样的诗人失去语言."
    m 2fkbla "你就是这么棒."
    m "..."
    m 2wublo "我话太多了."
    m 2kublu "但我认为这是必要的."
    m 5hublu "向你表达我的爱，我永远都不嫌多."
    m 5tubla "每次你需要我的时候，我都会安慰你的, 好吗 [mas_get_player_nickname()]?"
return "love"
