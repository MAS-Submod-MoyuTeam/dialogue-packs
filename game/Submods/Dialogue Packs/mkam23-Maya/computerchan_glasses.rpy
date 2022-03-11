init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_glasses",category=["生活", "你"],prompt="眼镜和隐形眼镜",random=True))

label monika_glasses:
    m 1eub "嘿 [player], 你戴眼镜吗?隐形的也算."
    $_history_list.pop()
    menu:
     "我戴眼镜.":
        m 4hub "真好!"
        m 7ruc "你也知道很多人比起隐形眼镜更喜欢普通的眼镜.."
        m 2mku "对他们而言, 让什么东西从眼眶中进进出出这种念头多少有点难以接受."
        m 3hubla "不管怎样,我希望透过它能让你看到更好的我~"
        m 5hubsb "啊哈哈!"
     "我戴隐形眼镜.":
        m 1eub "真好!"
        m 7lub "因为许多原因...不是所有人都能接受隐形眼镜."
        m 3hubla "不管怎样,我希望透过它能让你看到更好的我~"
        m 5hubsb "啊哈哈!"
     "我不戴眼镜.":
        m 1esb "没关系的, [player]!"
        m 4rsu "因为各种原因而戴上眼镜的人太多了."
        m 5hublu "而你是很特别的那一个~"
        m 7esb "不过如果你的视力突然变差, 一定要记得及时告知给谁, 好吗?"
return