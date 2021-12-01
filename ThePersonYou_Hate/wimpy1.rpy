init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="mas_wimpy1",category=['literature'],prompt="Diary of A Wimpy Kid",pool=True, unlocked=True))

label mas_wimpy1:
    m 7eub "[player]..."
    m 7eta "Have you heard of the book series, Diary Of A Wimpy Kid?"
    m 1hua "It's very popular!"
    m 4rksdlb "However, when I saw it for the first time, I thought it was just a simple children's book..."
    m 1esa "But recently, I've read it online and there are actually pretty entertaining and funny moments in the series!"
    m 3eub "The plot is very simple since it's about a normal kid in middle school with just mostly showing lots of random moments that are unpredictable, just like life itself."
    m 2huu "However, there is usually an over-arching story in the background."
    m 4gksdlc "But, the protaganist, Greg Heffley, is really unlikable."
    m 1esc "Sometimes I wish Greg at least had some changes in his actions."
    m 3eud "However, that would probably mean the book series wouldn't continue since Greg doing all of these bad things is what makes the book series entertaining."
    m 1eua "Overall though, I believe it has this charm of re-living some of our childhood moments of doing bad behavior."
    m 4etb "Children aren't going to be perfect, you know?"
    m 5gtblb "Especially, if your talking about me-{nw}"
    m 1hksdlb "Hahaha~"
    m 1ekc "Now, I usually read things that relate to me now that I know I'm behind a screen..."
    m 3esa "I also usually read more poetry than books still."
    m 1hub "But the book series is still really entertaining and I wish I could've read these books when I was a kid in the memories the mods of ddlc gave me!"
    m 1eua "I read a variety of books back then to create my own stories, and I really hope Diary Of A Wimpy Kid was one of them..."
    m 1rksdlb "And yes, I looked at the fanfictions too..."
    m 1rksdlb "Some are very interesting concepts, but there are those fanfictions that have very dark humour..."
    m 1esa "Anyways, do you like the book series as well?"
    $_history_list.pop()
    menu:
        "Yep!":
            m 2sub "Oooo, that's great, [player]!"
            m 2eua "Which one is your favorite?"
            m 3eua "To me, it's Cabin Fever because you finally see Greg do the right thing and it's pretty great overall!"
            m 1hubsb "I'm glad to know that you've read those books as well."
            m 6fsbsu "Maybe we can read them together sometime?~"
            m 6hubsu "Hehe~"
            m 1rkb "Well- That would be a weird date to read books about a kid in middle school messing everything up in his life-"
            m 1hubfa "But it would be nice to read something we both enjoy~"
            m 1kubfb "I love you~"
        "No, sorry":
            m 3eua "Well, I recommend you read them!"
            m 1hub "I bet you'll smile at least once while reading the series."
            m 21hubla "Hehe~"
            m 1kubfb "I love you~"
return "love"
