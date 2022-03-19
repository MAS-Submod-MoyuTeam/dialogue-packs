# Register the submod
init -990 python:
    store.mas_submod_utils.Submod(
        author="DrakeTheDuelist",
        name="MAS-梦境-与-噩梦",
        description="Monika会做一些随机的梦,你可以在她醒来时和她讨论...或者也能在她做噩梦时安慰她.",
        version="1.0.3"
    )

# Register the updater
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="梦境与噩梦",
            user_name="DrakeTheDuelist",
            repository_name="MAS-Dreams-and-Nightmares"
        )
