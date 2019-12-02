#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import pygame
from pygame import locals
import RPi.GPIO as GPIO
import time
from time import sleep

# LEFT
PIN_A1A = 27 # gray
PIN_A1B = 22 # white
PIN_B1A = 4  # blue
PIN_B1B = 17 # purple

#RIGHT
PIN2_A1A = 24 # gray
PIN2_A1B = 25 # white
PIN2_B1A = 18 # blue
PIN2_B1B = 23 # purple

#ARM
PIN3_A1A = 13 # gray
PIN3_A1B = 26 # white
PIN3_B1A = 5  # blue
PIN3_B1B = 6  # purple


def motor_init():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(PIN_A1A, GPIO.OUT)
  GPIO.setup(PIN_A1B, GPIO.OUT)
  GPIO.setup(PIN_B1A, GPIO.OUT)
  GPIO.setup(PIN_B1B, GPIO.OUT)
  GPIO.setup(PIN2_A1A, GPIO.OUT)
  GPIO.setup(PIN2_A1B, GPIO.OUT)
  GPIO.setup(PIN2_B1A, GPIO.OUT)
  GPIO.setup(PIN2_B1B, GPIO.OUT)
  GPIO.setup(PIN3_A1A, GPIO.OUT)
  GPIO.setup(PIN3_A1B, GPIO.OUT)
  GPIO.setup(PIN3_B1A, GPIO.OUT)
  GPIO.setup(PIN3_B1B, GPIO.OUT)
  motor_stop()

def motor_forward():
  GPIO.output(PIN_A1A, GPIO.HIGH)
  GPIO.output(PIN_A1B, GPIO.LOW)
  GPIO.output(PIN_B1A, GPIO.HIGH)
  GPIO.output(PIN_B1B, GPIO.LOW)
  GPIO.output(PIN2_A1A, GPIO.HIGH)
  GPIO.output(PIN2_A1B, GPIO.LOW)
  GPIO.output(PIN2_B1A, GPIO.HIGH)
  GPIO.output(PIN2_B1B, GPIO.LOW)
  GPIO.output(PIN3_A1A, GPIO.LOW)
  GPIO.output(PIN3_A1B, GPIO.LOW)
  GPIO.output(PIN3_B1A, GPIO.LOW)
  GPIO.output(PIN3_B1B, GPIO.LOW)


def motor_forward_left():
  GPIO.output(PIN_A1A, GPIO.HIGH)
  GPIO.output(PIN_A1B, GPIO.LOW)
  GPIO.output(PIN_B1A, GPIO.HIGH)
  GPIO.output(PIN_B1B, GPIO.LOW)
  GPIO.output(PIN2_A1A, GPIO.LOW)
  GPIO.output(PIN2_A1B, GPIO.LOW)
  GPIO.output(PIN2_B1A, GPIO.LOW)
  GPIO.output(PIN2_B1B, GPIO.LOW)
  GPIO.output(PIN3_A1A, GPIO.LOW)
  GPIO.output(PIN3_A1B, GPIO.LOW)
  GPIO.output(PIN3_B1A, GPIO.LOW)
  GPIO.output(PIN3_B1B, GPIO.LOW)

def motor_forward_right():
  GPIO.output(PIN_A1A, GPIO.LOW)
  GPIO.output(PIN_A1B, GPIO.LOW)
  GPIO.output(PIN_B1A, GPIO.LOW)
  GPIO.output(PIN_B1B, GPIO.LOW)
  GPIO.output(PIN2_A1A, GPIO.HIGH)
  GPIO.output(PIN2_A1B, GPIO.LOW)
  GPIO.output(PIN2_B1A, GPIO.HIGH)
  GPIO.output(PIN2_B1B, GPIO.LOW)
  GPIO.output(PIN3_A1A, GPIO.LOW)
  GPIO.output(PIN3_A1B, GPIO.LOW)
  GPIO.output(PIN3_B1A, GPIO.LOW)
  GPIO.output(PIN3_B1B, GPIO.LOW)

def motor_left():
  GPIO.output(PIN_A1A, GPIO.HIGH)
  GPIO.output(PIN_A1B, GPIO.LOW)
  GPIO.output(PIN_B1A, GPIO.HIGH)
  GPIO.output(PIN_B1B, GPIO.LOW)
  GPIO.output(PIN2_A1A, GPIO.LOW)
  GPIO.output(PIN2_A1B, GPIO.HIGH)
  GPIO.output(PIN2_B1A, GPIO.LOW)
  GPIO.output(PIN2_B1B, GPIO.HIGH)
  GPIO.output(PIN3_A1A, GPIO.LOW)
  GPIO.output(PIN3_A1B, GPIO.LOW)
  GPIO.output(PIN3_B1A, GPIO.LOW)
  GPIO.output(PIN3_B1B, GPIO.LOW)

def motor_right():
  GPIO.output(PIN_A1A, GPIO.LOW)
  GPIO.output(PIN_A1B, GPIO.HIGH)
  GPIO.output(PIN_B1A, GPIO.LOW)
  GPIO.output(PIN_B1B, GPIO.HIGH)
  GPIO.output(PIN2_A1A, GPIO.HIGH)
  GPIO.output(PIN2_A1B, GPIO.LOW)
  GPIO.output(PIN2_B1A, GPIO.HIGH)
  GPIO.output(PIN2_B1B, GPIO.LOW)
  GPIO.output(PIN3_A1A, GPIO.LOW)
  GPIO.output(PIN3_A1B, GPIO.LOW)
  GPIO.output(PIN3_B1A, GPIO.LOW)
  GPIO.output(PIN3_B1B, GPIO.LOW)

def motor_reverse():
  GPIO.output(PIN_A1A, GPIO.LOW)
  GPIO.output(PIN_A1B, GPIO.HIGH)
  GPIO.output(PIN_B1A, GPIO.LOW)
  GPIO.output(PIN_B1B, GPIO.HIGH)
  GPIO.output(PIN2_A1A, GPIO.LOW)
  GPIO.output(PIN2_A1B, GPIO.HIGH)
  GPIO.output(PIN2_B1A, GPIO.LOW)
  GPIO.output(PIN2_B1B, GPIO.HIGH)
  GPIO.output(PIN3_A1A, GPIO.LOW)
  GPIO.output(PIN3_A1B, GPIO.LOW)
  GPIO.output(PIN3_B1A, GPIO.LOW)
  GPIO.output(PIN3_B1B, GPIO.LOW)

def motor_reverse_right():
  GPIO.output(PIN_A1A, GPIO.LOW)
  GPIO.output(PIN_A1B, GPIO.LOW)
  GPIO.output(PIN_B1A, GPIO.LOW)
  GPIO.output(PIN_B1B, GPIO.LOW)
  GPIO.output(PIN2_A1A, GPIO.LOW)
  GPIO.output(PIN2_A1B, GPIO.HIGH)
  GPIO.output(PIN2_B1A, GPIO.LOW)
  GPIO.output(PIN2_B1B, GPIO.HIGH)
  GPIO.output(PIN3_A1A, GPIO.LOW)
  GPIO.output(PIN3_A1B, GPIO.LOW)
  GPIO.output(PIN3_B1A, GPIO.LOW)
  GPIO.output(PIN3_B1B, GPIO.LOW)

def motor_reverse_left():
  GPIO.output(PIN_A1A, GPIO.LOW)
  GPIO.output(PIN_A1B, GPIO.HIGH)
  GPIO.output(PIN_B1A, GPIO.LOW)
  GPIO.output(PIN_B1B, GPIO.HIGH)
  GPIO.output(PIN2_A1A, GPIO.LOW)
  GPIO.output(PIN2_A1B, GPIO.LOW)
  GPIO.output(PIN2_B1A, GPIO.LOW)
  GPIO.output(PIN2_B1B, GPIO.LOW)
  GPIO.output(PIN3_A1A, GPIO.LOW)
  GPIO.output(PIN3_A1B, GPIO.LOW)
  GPIO.output(PIN3_B1A, GPIO.LOW)
  GPIO.output(PIN3_B1B, GPIO.LOW)

def motor_stop():
  GPIO.output(PIN_A1A, GPIO.LOW)
  GPIO.output(PIN_A1B, GPIO.LOW)
  GPIO.output(PIN_B1A, GPIO.LOW)
  GPIO.output(PIN_B1B, GPIO.LOW)
  GPIO.output(PIN2_A1A, GPIO.LOW)
  GPIO.output(PIN2_A1B, GPIO.LOW)
  GPIO.output(PIN2_B1A, GPIO.LOW)
  GPIO.output(PIN2_B1B, GPIO.LOW)
  GPIO.output(PIN3_A1A, GPIO.LOW)
  GPIO.output(PIN3_A1B, GPIO.LOW)
  GPIO.output(PIN3_B1A, GPIO.LOW)
  GPIO.output(PIN3_B1B, GPIO.LOW)

def arm_up():
  GPIO.output(PIN_A1A, GPIO.LOW)
  GPIO.output(PIN_A1B, GPIO.LOW)
  GPIO.output(PIN_B1A, GPIO.LOW)
  GPIO.output(PIN_B1B, GPIO.LOW)
  GPIO.output(PIN2_A1A, GPIO.LOW)
  GPIO.output(PIN2_A1B, GPIO.LOW)
  GPIO.output(PIN2_B1A, GPIO.LOW)
  GPIO.output(PIN2_B1B, GPIO.LOW)
  GPIO.output(PIN3_A1A, GPIO.HIGH)
  GPIO.output(PIN3_A1B, GPIO.LOW)
  GPIO.output(PIN3_B1A, GPIO.LOW)
  GPIO.output(PIN3_B1B, GPIO.LOW)

def arm_down():
  GPIO.output(PIN_A1A, GPIO.LOW)
  GPIO.output(PIN_A1B, GPIO.LOW)
  GPIO.output(PIN_B1A, GPIO.LOW)
  GPIO.output(PIN_B1B, GPIO.LOW)
  GPIO.output(PIN2_A1A, GPIO.LOW)
  GPIO.output(PIN2_A1B, GPIO.LOW)
  GPIO.output(PIN2_B1A, GPIO.LOW)
  GPIO.output(PIN2_B1B, GPIO.LOW)
  GPIO.output(PIN3_A1A, GPIO.LOW)
  GPIO.output(PIN3_A1B, GPIO.HIGH)
  GPIO.output(PIN3_B1A, GPIO.LOW)
  GPIO.output(PIN3_B1B, GPIO.LOW)

def arm2_up():
  GPIO.output(PIN_A1A, GPIO.LOW)
  GPIO.output(PIN_A1B, GPIO.LOW)
  GPIO.output(PIN_B1A, GPIO.LOW)
  GPIO.output(PIN_B1B, GPIO.LOW)
  GPIO.output(PIN2_A1A, GPIO.LOW)
  GPIO.output(PIN2_A1B, GPIO.LOW)
  GPIO.output(PIN2_B1A, GPIO.LOW)
  GPIO.output(PIN2_B1B, GPIO.LOW)
  GPIO.output(PIN3_A1A, GPIO.LOW)
  GPIO.output(PIN3_A1B, GPIO.LOW)
  GPIO.output(PIN3_B1A, GPIO.HIGH)
  GPIO.output(PIN3_B1B, GPIO.LOW)

def arm2_down():
  GPIO.output(PIN_A1A, GPIO.LOW)
  GPIO.output(PIN_A1B, GPIO.LOW)
  GPIO.output(PIN_B1A, GPIO.LOW)
  GPIO.output(PIN_B1B, GPIO.LOW)
  GPIO.output(PIN2_A1A, GPIO.LOW)
  GPIO.output(PIN2_A1B, GPIO.LOW)
  GPIO.output(PIN2_B1A, GPIO.LOW)
  GPIO.output(PIN2_B1B, GPIO.LOW)
  GPIO.output(PIN3_A1A, GPIO.LOW)
  GPIO.output(PIN3_A1B, GPIO.LOW)
  GPIO.output(PIN3_B1A, GPIO.LOW)
  GPIO.output(PIN3_B1B, GPIO.HIGH)


def main():
  # Gamepad Wait
  while 1:
    print("Wait Gamepad")
    pygame.init()
    pygame.joystick.init()
    print(pygame.joystick.get_count())
    if pygame.joystick.get_count() > 0:
      print("Gamepad Found count=" + str(pygame.joystick.get_count()))
      break 
    else:
      pygame.quit()

  # Gamepad Initialize
  joystick = pygame.joystick.Joystick(0)
  joystick.init()
  pygame.event.set_allowed(pygame.locals.JOYAXISMOTION)
  pygame.event.set_allowed(pygame.locals.JOYBUTTONDOWN)
  pygame.event.set_allowed(pygame.locals.JOYBUTTONUP)
  pygame.event.set_allowed(pygame.locals.JOYHATMOTION)

  # Axis Count
  n_ax = joystick.get_numaxes()
  print("axis:" + str(n_ax))

  # Button Count
  n_bu = joystick.get_numbuttons()
  print("buttons:" + str(n_bu))

  # Hat Count
  n_ha = joystick.get_numhats()
  print("hat:" + str(n_ha))

  axis_l_lr = 0
  axis_l_ud = 1
  axis_r_lr = 2 
  axis_r_ud = 3 

  if joystick.get_name() == "Microsoft X-Box 360 pad":
    print("Microsoft X-Box 360 pad")
    axis_l_lr = 0
    axis_l_ud = 1
    axis_r_lr = 3 
    axis_r_ud = 4 
  elif joystick.get_name() == "Smart JC-U3912T":
    print("Smart JC-U3912T")
    axis_l_lr = 0
    axis_l_ud = 1
    axis_r_lr = 3 
    axis_r_ud = 2 
  elif joystick.get_name() == "Nintendo Wii Remote Pro Controller":
    print( "Nintendo Wii Remote Pro Controller")
    axis_l_lr = 0
    axis_l_ud = 1
    axis_r_lr = 2 
    axis_r_ud = 3 
  elif joystick.get_name() == "PC Game Controller       ":
    print("JC-FU2912F")
    axis_l_lr = 0
    axis_l_ud = 1
    axis_r_lr = 2
    axis_r_ud = 3 
  elif joystick.get_name() == "Sony PLAYSTATION(R)3 Controller":
    print("Sony PLAYSTATION(R)3 Controller")
    axis_l_lr = 0
    axis_l_ud = 1
    axis_r_lr = 3 
    axis_r_ud = 4 
  else:
    print("unknown gamepad")

  print(axis_l_lr)
  print(axis_l_ud)

  # 状態データの保管場所
  hat    = [0, 0]
  axis   = [0.0] * n_ax
  button = [0] * n_bu

  # Motor Initialize
  motor_init()

  # Main Loop
  while 1:
    # Gamepad Event Check
    event = False
    for e in pygame.event.get():
      event = True
      if e.type == pygame.locals.JOYAXISMOTION:
        # Axises
        for a in range(n_ax):
          axis[a] = joystick.get_axis(a)
      elif e.type == pygame.locals.JOYBUTTONDOWN or e.type == pygame.locals.JOYBUTTONUP:
        # Buttons
        for b in range(n_bu):
          button[b] = joystick.get_button(b)
      elif e.type == pygame.locals.JOYHATMOTION:
        # ハットスイッチ（十字ボタン）
        hat[0], hat[1] = joystick.get_hat(0)

    if event == False:
      # No Event
  #    time.sleep(0.05)
      continue

    move_l_ud = 0
    move_l_lr = 0
    move_r_ud = 0
    move_r_lr = 0

#    print(axis[axis_l_lr], axis[axis_l_ud], axis[axis_r_lr], axis[axis_r_ud])

    if axis[axis_l_lr] > 0.5:
      move_l_lr = 1
    if axis[axis_l_lr] < -0.5:
      move_l_lr = -1
    if axis[axis_l_ud] > 0.5:
      move_l_ud = 1
    if axis[axis_l_ud] < -0.5:
      move_l_ud = -1
    if axis[axis_r_ud] > 0.5:
      move_r_ud = 1
    if axis[axis_r_ud] < -0.5:
      move_r_ud = -1
    if axis[axis_r_lr] > 0.5:
      move_r_lr = 1
    if axis[axis_r_lr] < -0.5:
      move_r_lr = -1

    if   (move_r_ud == -1): # arm up
      print("arm up")
      arm_up()
    elif (move_r_ud ==  1): # arm down 
      print("arm down")
      arm_down()
    if   (move_r_lr == -1): # arm2 up
      print("arm2 up")
      arm2_up()
    elif (move_r_lr ==  1): # arm2 down
      print("arm2 down")
      arm2_down()
    else:
      if   (move_l_lr ==  0) and (move_l_ud ==  0): # 0  0  nop
        print("stop")
        motor_stop()
      elif (move_l_lr ==  0) and (move_l_ud ==  1): # 0  1 up
        print("reverse")
        motor_reverse()
      elif (move_l_lr ==  0) and (move_l_ud == -1): # 0 -1 down
        print("forward")
        motor_forward()
      elif (move_l_lr ==  1) and (move_l_ud ==  0): # 1  0  right
        print("right")
        motor_right()
      elif (move_l_lr ==  1) and (move_l_ud ==  1): # 1  1  up right
        print("reverse right")
        motor_reverse_right()
      elif (move_l_lr ==  1) and (move_l_ud == -1): # 1 -1  down right
        print("forward_right")
        motor_forward_right()
      elif (move_l_lr == -1) and (move_l_ud ==  0): # -1  0 left
        print("left")
        motor_left()
      elif (move_l_lr == -1) and (move_l_ud ==  1): # -1  1  up left
        print("reverse_left")
        motor_reverse_left()
      elif (move_l_lr == -1) and (move_l_ud == -1): # -1 -1 down left
        print("forward_left")
        motor_forward_left()
      else:
        print("stop2")
        motor_stop()







main()
