init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_salad",category=['food'],prompt="Salad",random=True))

label monika_salad:
    m 1eua "[player], 你喜欢沙拉吗?"
    m 1hua "我非常喜欢这道美味佳肴!"
    m 1hub "这也是道健康的佳肴, 你几乎可以把任何东西混合在一起!"
    m 4rub "从西红柿, 生菜, 菠菜, 奶酪, 调味料, 醋中选取-"
    m 1sua "还有这么多!"
    m 1eub "这对健康饮食很有帮助."
    m 1nub "我希望你能做点什么."
return
