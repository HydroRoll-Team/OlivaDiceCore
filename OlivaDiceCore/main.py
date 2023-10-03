# -*- encoding: utf-8 -*-
'''
_______________________    _________________________________________
__  __ \__  /____  _/_ |  / /__    |__  __ \___  _/_  ____/__  ____/
_  / / /_  /  __  / __ | / /__  /| |_  / / /__  / _  /    __  __/   
/ /_/ /_  /____/ /  __ |/ / _  ___ |  /_/ /__/ /  / /___  _  /___   
\____/ /_____/___/  _____/  /_/  |_/_____/ /___/  \____/  /_____/   

@File      :   main.py
@Author    :   lunzhiPenxil仑质
@Contact   :   lunzhipenxil@gmail.com
@License   :   AGPL
@Copyright :   (C) 2020-2021, OlivOS-Team
@Desc      :   None
'''

import OlivOS
import OlivaDiceCore

class Event(object):
    def init(self, Proc):
        OlivaDiceCore.msgReply.unity_init(self, Proc)

    def init_after(self, Proc):
        OlivaDiceCore.msgReply.unity_init_after(self, Proc)

    def private_message(self, Proc):
        OlivaDiceCore.msgReply.unity_reply(self, Proc)

    def group_message(self, Proc):
        OlivaDiceCore.msgReply.unity_reply(self, Proc)

    def poke(self, Proc):
        OlivaDiceCore.msgReply.poke_reply(self, Proc)

    def friend_add_request(self, Proc):
        OlivaDiceCore.ordinaryInviteManager.unity_friend_add_request(self, Proc)

    def group_invite_request(self, Proc):
        OlivaDiceCore.ordinaryInviteManager.unity_group_invite_request(self, Proc)

    def group_member_increase(self, Proc):
        OlivaDiceCore.ordinaryInviteManager.unity_group_member_increase(self, Proc)

    def heartbeat(self, Proc):
        OlivaDiceCore.pulse.unity_heartbeat(self, Proc)

    def save(self, Proc):
        OlivaDiceCore.msgReply.unity_save(self, Proc)
