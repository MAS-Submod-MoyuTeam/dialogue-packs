init 5 python:
    addEvent(
        Event(
            persistent._mas_fun_facts_database,
            eventlabel="mental_illnesses",
        ),
        code="FFF"
    )

label mental_illnesses:
    m 3euc "你知道吗，精神残疾总共有300多种。"
    m 3eud "真是个疯狂的数字，难道不是吗，[player]？"
    m 2euc "不过这些还只是记录在案了的。"
    m "我觉得一定还有更多没被记录下来吧！"
    m "这意味着还有更多的东西要学了！"
    #Call the end
    call mas_fun_facts_end
return

init 5 python:
    addEvent(
        Event(
            persistent._mas_fun_facts_database,
            eventlabel="mental_misdiagnoseshistory",
        ),
        code="FFF"
    )

label mental_misdiagnoseshistory:
    m 3euc "你知道吗，自闭症在1908年会被诊断为精神分裂症。"
    m 3eud "这是因为，在研究完成并创立自闭症这一术语之前，人们只是觉得它和精神分裂症很相似。"
    m 7eud "很显然，自从20世纪40年代起，也就是在Grunya Sukhareva开始研究此类病例并创立自闭症理论以后，这种情况就几乎不复存在了。"
    m 3euc "虽然说她的研究成果没有被现代自闭症所沿用..."
    m 1eud "而且从古至今自闭症也不少见..." 
    extend 3eub "但这也真的很有趣！"
    call mas_fun_facts_end
return