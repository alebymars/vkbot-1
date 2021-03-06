# -*- coding: utf-8 -*-
import command_system


def info(token):
    message = ''
    for c in command_system.command_list:
        message += c.keys[0] + ' - ' + c.description + '\n'
    return message, ''


info_command = command_system.Command()

info_command.keys = [u'помощь', u'помоги', u'help']
info_command.description = u'Покажу список команд'
info_command.process = info
