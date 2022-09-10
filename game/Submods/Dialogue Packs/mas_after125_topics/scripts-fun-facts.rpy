init 5 python:
    if p_is_old_ver:
        addEvent(
            Event(
                persistent._mas_fun_facts_database,
                eventlabel="mas_fun_fact_maplesyrup1",
            ),
            code="FFF"
        )
init:
    if p_is_old_ver:
        label mas_fun_fact_maplesyrup1:
            m 3hksdlb "为你找到了又一个{w=0.2}{i}甜蜜的 {/i}{w=0.2}小知识..."
            m 1eua "每一种枫树都可以产生能制作枫糖浆的汁液, {w=0.1}{nw}"
            extend 1eud "但是商品枫糖浆通常来自糖枫树."
            m 3eua "你可以很容易地从枫叶的形状判断出枫树的种类..."
            m 3eub "你可能可以辨别出糖枫叶了, 因为它就是加拿大国旗上的图案！"
            m 1euc "即便如此, 糖枫在当地种植范围有限, 并不是在加拿大的哪里{i}都有{/i}种的"
            m 1wud "...然而加拿大却生产了全世界超过四分之三的枫糖浆"
            m 3wud "更令人惊讶的是, 要生产一加仑的枫糖浆需要40加仑的树液！"
            m 1eua "制作它需要花费的精力也比我预想的要多很多..."
            m 1esc "树液要被熬成糖浆...考虑到糖浆的需求, 显然要用很长时间."
            m 3eud "还有, 我听说如果你再煮得久一些然后把它倒在冰冷的接触面上...{w=0.2}{nw}"
            extend 3hub "你甚至可以做出糖果！"
            if mas_isMoniNormal(higher=True):
                if persistent._mas_pm_gets_snow is not False:
                    m 3euu "听起来像是一件我们能一起做的乐事, 嗯哼[player]?"
                    m 1etc "不过我们可能还要再等一阵才有机会了..."
                    m 1eua "不过再多等一会也无妨...{w=0.3}{nw}"
                    extend 1hublu "对我来说你已经够甜了~"
        
                else:
                    m 1eua "这听起来真是太甜蜜了..."
                    m 1rkblu "但是远不如你的甜蜜, 欸嘿嘿~"
            call mas_fun_facts_end
            return