import pygame as pg
from pygame.locals import *

from random import randint as rand

from mygame.structures.Pos import Pos
import mygame.os.EventHolder as eventHolder
from mygame.structures.Rect import Rect
from mygame.drawables.Object import Object
from mygame.drawables.Container import Container
from mygame.drawables.ScrollView import ScrollView
from mygame.globals import functions
from mython.mylist import mylist
from mygame.structures.Color import Color, ColorConstants
from mygame.os.Window import Window

colors = ColorConstants

pg.init()

content_size = Pos(800,600)
window_size = Pos(1100,800)
window = Window(window_size, content_size)

obj = Object(Rect(0, 0, int(content_size.x), int(content_size.y)))

obj.padding = 10,10,10,10
obj.margin = 50,50,50,50
obj.border = 4,4,4,4

obj.margined_color = ColorConstants.HAPPY_BLUE
obj.padded_color = ColorConstants.DEAD_BLUE
obj.bordered_color = ColorConstants.BLACK
obj.content_color = ColorConstants.DEAD_YELLOW

obj.has_surface = True


just_started = True
clock = pg.time.Clock()
fps = 90
adjust_pos = Pos(0,0)
adjust_step = 4


while not window.event_holder.should_quit :
    window.get_events()

    if window.event_holder.window_size_changed or just_started:
        obj.margined_rect = window.content_rect.copy()

    # if K_a in window.event_holder.keyboard_held_keys:
    #     scroll_view.create_object(Pos(rand(50,50),rand(50,50)))
    # if K_s in window.event_holder.keyboard_pressed_keys:
    #     cube = rand(40,40)
    #     scroll_view.create_object(Pos(cube,cube))
    # if K_d in window.event_holder.keyboard_held_keys or K_c in\
    #         window.event_holder.keyboard_pressed_keys:
    #     scroll_view.resize_objects(0.95)
    # if K_f in window.event_holder.keyboard_held_keys or K_v in\
    #         window.event_holder.keyboard_pressed_keys:
    #     scroll_view.resize_objects(1.05)
    # if K_q in window.event_holder.keyboard_pressed_keys:
    #     scroll_view.object_list.clear()
    #     scroll_view.update()

    # if K_UP in window.keyboard_held_keys: adjust_pos.y -= adjust_step
    # if K_DOWN in window.keyboard_held_keys : adjust_pos.y += adjust_step
    # if K_RIGHT in window.keyboard_held_keys : adjust_pos.x += adjust_step
    # if K_LEFT in window.keyboard_held_keys : adjust_pos.x -= adjust_step

    should_update = False
    should_recenter = False
    #

    last_rect = obj.margined_rect.copy()

    if K_LCTRL in window.event_holder.keyboard_held_keys:
        if K_UP in window.event_holder.keyboard_held_keys:
            obj.alpha += 3
            if obj.alpha > 255: obj.alpha = 255
            # should_update = True

        if K_DOWN in window.event_holder.keyboard_held_keys :
            obj.alpha -= 3
            if obj.alpha < 50 : obj.alpha = 50

        if K_RETURN in window.event_holder.keyboard_pressed_keys:
            obj.has_surface = not obj.has_surface


    elif K_LSHIFT not in window.event_holder.keyboard_held_keys:
        if K_UP in window.event_holder.keyboard_held_keys:
            obj.y -= adjust_step
            # should_update = True

        if K_DOWN in window.event_holder.keyboard_held_keys :
            obj.y += adjust_step
            # should_update = True

        if K_RIGHT in window.event_holder.keyboard_held_keys :
            obj.x += adjust_step
            # should_update = True

        if K_LEFT in window.event_holder.keyboard_held_keys :
            obj.x -= adjust_step
            # should_update = True
    #
    elif K_LSHIFT in window.event_holder.keyboard_held_keys:
        if K_UP in window.event_holder.keyboard_held_keys:
            obj.height += adjust_step / 2
            should_update = should_recenter = True
        if K_DOWN in window.event_holder.keyboard_held_keys:
            obj.height -= adjust_step
            should_update = should_recenter = True

        if K_RIGHT in window.event_holder.keyboard_held_keys:
            obj.width += adjust_step
            should_update = should_recenter = True

        if K_LEFT in window.event_holder.keyboard_held_keys:
            obj.width -= adjust_step
            should_update = should_recenter = True

    if should_update:
        if should_recenter: obj.margined_rect.center = last_rect.center

        # scroll_view.update()

    window.check_events()

    window.render_screen()
    obj.render(window.surface,adjust_pos)

    window.update()
    clock.tick(fps)

    current_fps = clock.get_fps()
    if current_fps < 60:
        print('low fps warning : ',clock.get_fps())


    just_started = False



