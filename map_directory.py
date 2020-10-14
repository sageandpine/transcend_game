#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 22:32:37 2020

@author: goodtimes
"""
#scene1 = "Let's see if this works 1"
#scene2 = "Let's see if this works 2"
#scene3 = "Let's see if this works 3"
#scene4 = "Let's see if this works 4"
#scene5 = "Let's see if this works 5"






class Scene(object):

    def enter(self):







class Map(object):
     scenes = {
                        "Death" : Death(),
                        "scene2" : scene2,
                        "scene3" : scene3,
                        "scene4" : scene4,
                        "scene5" : scene5            
                        }
     
    def __init__(self,start_scene):
        self.start_scene = start_scene


    def next_scene(self):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        print(f"{self.scene}")
        return self.next_scene(self.start_scene)
    

m1 = Map(scene1)
m1.opening_scene()

