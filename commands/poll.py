# -*- coding: utf-8 -*-
import command_system
import vkapi


def poll(token):
    attachment = ""
    message = 'Сейчас всё будет сделано'
    # vkapi.post_poll(token=token, message="poll_message")
    return message, attachment

poll_command = command_system.Command()

poll_command.keys = ['опрос']
poll_command.description = 'Создание опроса'
poll_command.process = poll
