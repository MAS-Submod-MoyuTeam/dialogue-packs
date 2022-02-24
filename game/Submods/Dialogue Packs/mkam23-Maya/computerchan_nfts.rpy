init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_nft",category=["媒体", "社会", "技术"],prompt="NFTs",random=True))

label monika_nft:
    m 1eua "[player], 你有听说过NFTs吗?"
    m 3eub "如果你还没有, 那让我来解释一下:"
    m 4rub "Non-fungible tokens (非同质化代币) 或NFTs是加密货币的一种形式."
    m 7esb "但有一点不同; 它们不能互换!"
    m 3esa "这意味着你不能用其他东西来交换你的NFT."
    m 2lkc "虽然.. NFT有很多问题."
    m 7esc "有一点是, 它们对地球有很大影响."
    m 4wud "仅是挖掘一枚NFTs就价值约{i}48千克{/i}的二氧化碳!"
    m 7wuo "这相当于一台电脑用636年, 或驾车83.8万公里!"
    m 1rksdlb "天呐, 我在那里跑题了, 对吗?"
    m 1esa "总之.."
    m 7esu "NFTs的另一个问题就是图像质量."
    m 2mtb "它们看起来并不是, 在质量方面是最...{i}好的{/i}."
    m 7etc "你看到的大多数NFTs使用的都是基础, 他们在上面添加东西以使其看起来独特."
    m 2tkc "但说实话, 他们只是非常懒."
    m 1fku "我对你不支持NFTs是足够信任的, [mas_get_player_nickname()]."
    m 5hubsu "我爱你."
return "love"
