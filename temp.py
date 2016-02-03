# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Animal:
    def __init__(self):
        print("Animal __init__()")
class Tiger(Animal):
    def __init__(self):
        super().__init__() #부모 클래스 생성사 호출
        print("Tiger __init__()")

class Lion(Animal):
    def __init__(self):
        super().__init__() #부모 클래스 생성사 호출
        print("Lion __init__()")
        
class Liger(Tiger, Lion):   
    def __init__(self):
        super().__init__() #부모 클래스 생성사 호출
        print("Liger __init__()")
        
