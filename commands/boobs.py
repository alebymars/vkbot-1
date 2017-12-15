# -*- coding: utf-8 -*-
import command_system
import vkapi


def boobs():
   attachment = vkapi.get_random_wall_picture(-35001375)
   message = 'Вот тебе идея для фото ;)\nВ следующий раз я пришлю другую.'
   return message, attachment

boobs_command = command_system.Command()

boobs_command.keys = ['сиськи', 'грудь', 'сосок', 'boobs', 'sexy', 'girl', 'идея для фото']
boobs_command.description = 'Пришлю картинку с идеей для фото'
boobs_command.process = boobs
