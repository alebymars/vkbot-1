# -*- coding: utf-8 -*-
import command_system


def hello():
   message = u'Привет, друг!\nЯ новый чат-бот.'
   return message, ''

hello_command = command_system.Command()

hello_command.keys = [u'привет', u'hello', u'дратути', u'здравствуй', u'здравствуйте']
hello_command.description = u'Поприветствую тебя'
hello_command.process = hello
