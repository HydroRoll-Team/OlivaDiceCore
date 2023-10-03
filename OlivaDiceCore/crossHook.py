# -*- encoding: utf-8 -*-
'''
_______________________    _________________________________________
__  __ \__  /____  _/_ |  / /__    |__  __ \___  _/_  ____/__  ____/
_  / / /_  /  __  / __ | / /__  /| |_  / / /__  / _  /    __  __/   
/ /_/ /_  /____/ /  __ |/ / _  ___ |  /_/ /__/ /  / /___  _  /___   
\____/ /_____/___/  _____/  /_/  |_/_____/ /___/  \____/  /_____/   

@File      :   crossHook.py
@Author    :   lunzhiPenxil仑质
@Contact   :   lunzhipenxil@gmail.com
@License   :   AGPL
@Copyright :   (C) 2020-2021, OlivOS-Team
@Desc      :   None
'''

import OlivOS
import OlivaDiceCore

listModel = [
    ['OlivaDiceCore', OlivaDiceCore.data.OlivaDiceCore_ver_short]
]

listPrefix = [
    '.',
    '。',
    '/'
]

listReplyContextFliter = []

listReplyContextPrefixFliter = []

dictReplyContextReg = {}

def msgHook(event, funcType, sender, dectData, message):
    [host_id, group_id, user_id] = dectData
    tmp_name = sender['name'] if 'name' in sender else 'N/A'
    tmp_id = sender['id'] if 'id' in sender else -1
    return None

def pokeHook(plugin_event, type = 'group'):
    return OlivaDiceCore.data.bot_info

def msgFormatHook(data:str, valDict:dict):
    return data

def drawFormatHook(data:str, plugin_event:OlivOS.API.Event):
    return data

#跨模块注入点
dictHookList = {
    'model': listModel,
    'prefix': listPrefix,
    'replyContextFliter': listReplyContextFliter,
    'replyContextPrefixFliter': listReplyContextPrefixFliter,
    'replyContextReg': dictReplyContextReg
}

dictHookFunc = {
    'msgHook': msgHook,
    'pokeHook': pokeHook,
    'msgFormatHook': msgFormatHook,
    'drawFormatHook': drawFormatHook
}
