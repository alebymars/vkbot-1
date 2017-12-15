# -*- coding: utf-8 -*-
import command_system
import vkapi


def boobs(token):
   attachment = vkapi.get_random_wall_picture(-58312088)
   message = 'Вот тебе идея для фото ;)\nВ следующий раз я пришлю другую.'
   return message, attachment

boobs_command = command_system.Command()
boobs_command.keys = ['идея для фото']
boobs_command.description = 'Пришлю картинку с идеей для фото'
boobs_command.process = boobs
