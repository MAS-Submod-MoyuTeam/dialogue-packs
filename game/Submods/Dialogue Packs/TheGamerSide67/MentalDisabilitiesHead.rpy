## Register the submod
#init -990 python:
#    store.mas_submod_utils.Submod(
#        author="TheGamerSide67 HistoryVariety and Leafeon_Mk",
#        name="Mental Disabilities Submod",
#        description="一个讨论哲学与心理疾病的submod,或许还有更多?",
#        version="1.0",
#        settings_pane=None
#    )
#
## Register the updater
#init -989 python:
#    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
#        store.sup_utils.SubmodUpdater(
#            submod="Mental Disabilities Submod",
#            user_name="TheGamerSide67",
#            repository_name="MentalDisabilitySubmod"
#        )
#