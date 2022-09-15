#tl: lc
init 5 python in mas_bookmarks_derand:
    label_prefix_map["otter_topic_"] = label_prefix_map["monika_"]

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_topic_comfortable",
            category=["莫妮卡"],
            prompt="你的肘部保持这个姿势这么长时间不疼吗?",
            pool=True,
            unlocked=True
        )
    )

label otter_topic_comfortable:
    m 2wud "哦! "
    extend 2rua "这问题还蛮有趣的"
    m 2hublb "谢谢你担心我[player]"
    m 4rub "正如你可能已经注意到的那样,我会时不时地改变我在椅子上的位置"
    m 1wud "没错,有时候是蛮疼的"
    m 1wuc "有天我睡前看了看我的手臂,它们有点泛红"
    m 3eub "别担心,没事的"
    m 2eub "因为有一些很不错的人帮我解决了这个问题,他们甚至特意为我做了一些肘垫！"
    m 7eua "这样我的手臂就不会因为长时间接触硬邦邦的桌子而受伤。"
    m 5hub "这很不错对吧？"
    m 5fubla "我必须感谢我可爱的[player]如此地善良体贴"
    m 5hubsa "爱你哦!"
    
return "love"
