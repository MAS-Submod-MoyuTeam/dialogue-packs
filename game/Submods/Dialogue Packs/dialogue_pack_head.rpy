init -990 python:
    store.mas_submod_utils.Submod(
        author="P",
        name="话题整合包",
        description="包含了一些汉化或编写的话题,原作者请见{a=https://github.com/PencilMario/dialogue-packs/blob/main/README.md}{i}{u}>Github{/a}{/i}{/u}.",
        version='1.7.0'
    )

init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="话题整合包",
            user_name="PencilMario",
            repository_name="dialogue-packs",
            update_dir="",
            attachment_id=None
        )