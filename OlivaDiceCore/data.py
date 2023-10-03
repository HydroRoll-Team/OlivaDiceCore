# -*- encoding: utf-8 -*-
'''
_______________________    _________________________________________
__  __ \__  /____  _/_ |  / /__    |__  __ \___  _/_  ____/__  ____/
_  / / /_  /  __  / __ | / /__  /| |_  / / /__  / _  /    __  __/   
/ /_/ /_  /____/ /  __ |/ / _  ___ |  /_/ /__/ /  / /___  _  /___   
\____/ /_____/___/  _____/  /_/  |_/_____/ /___/  \____/  /_____/   

@File      :   data.py
@Author    :   lunzhiPenxil仑质
@Contact   :   lunzhipenxil@gmail.com
@License   :   AGPL
@Copyright :   (C) 2020-2021, OlivOS-Team
@Desc      :   None
'''


import sys
import platform
import os
import uuid

import OlivOS

OlivaDiceCore_name = 'OlivaDice核心模块'
OlivaDiceCore_ver = '3.3.18'
OlivaDiceCore_svn = 1068
OlivaDiceCore_ver_short = f'{OlivaDiceCore_ver}({OlivaDiceCore_svn})'

exce_path = os.getcwd()

global_Proc = None

bot_info_Ver = f'{OlivaDiceCore_ver}({OlivaDiceCore_svn})'

bot_info_basic = f'OlivaDice By lunzhiPenxil Ver.{bot_info_Ver}'

bot_info_basic_short = f'OlivaDice Ver.{bot_info_Ver}'

bot_info = f'{bot_info_basic} [Python {str(platform.python_version())} For OlivOS {OlivOS.infoAPI.OlivOS_Version}]'
bot_info_auto = '%s [Python %s For OlivOS %s {tAdapter}]' % (bot_info_basic, str(platform.python_version()), OlivOS.infoAPI.OlivOS_Version)

bot_version_short = f'OlivaDice {bot_info_Ver}'

bot_version_short_header = f'OlivaDice/{OlivaDiceCore_ver}'

bot_summary = bot_info_basic + '\n'
bot_summary += '%s %s\n' % (str(platform.python_implementation()), str(sys.version))
bot_summary += '%s : %s : %s\n' % (
    os.name,
    ' '.join(platform.architecture()),
    str(platform.platform()),
)
bot_summary += f'{str(platform.machine())} - {str(platform.processor())}'

bot_content = {
    'masterKey': str(uuid.uuid4())
}

dataDirRoot = './plugin/data/OlivaDice'

defaultOlivaDicePulseUrl = 'https://api.dice.center/dicestatusup/'
