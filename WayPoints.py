from djitellopy import Tello

import threading
import keyboard
import os
import time

tello = Tello()
tello.connect()
tello.takeoff()
time.sleep(0.5)

def paro():
    while True:
        if keyboard.is_pressed("p"):
            print("tello.land()")
            tello.land()
            os._exit(1)

def punto_aux(a, b):
    aux = b - a
    return aux
x1, y1, z = 0, 0, 0
dronx, drony = 0, 0

def divide(x, y, z):
    cont = 0
    print("Funcion divide activada")
    while abs(x) > 5 or abs(y) > 5:
        x/=2
        y/=2
        cont += 1
    if abs(x) < 5 and abs(y) < 5:
        for num in range(0, cont):
            dronx=y
            drony=-x
            tello.go_xyz_speed(int(dronx*100), int(drony*100), z, 40)
            print("tello.go_xyz_speed(", int(dronx * 100), int(drony * 100), z, "40)")
            time.sleep(1)
            tello.go_xyz_speed(int(dronx*100), int(drony*100), z, 40)
            print("tello.go_xyz_speed(", int(dronx * 100), int(drony * 100), z, "40)")
            time.sleep(1)

hilo = threading.Thread(target=paro)
hilo.start()

while True:
    time.sleep(2)
    with open('Archivo.txt', 'r') as puntos:
        coor = puntos.readline()
        while coor:
            # Se llama a la función para calcular punto
            x2, y2 = coor.split()
            aux_x = punto_aux(int(x1), int(x2))
            aux_y = punto_aux(int(y1), int(y2))
            if abs(aux_x) > 5 or abs(aux_y) > 5:
                divide(int(aux_x), int(aux_y), z)
                time.sleep(2)
            else:
                # Se llama a la función go_xyz_speed
                dronx=aux_y
                drony=-aux_x
                tello.go_xyz_speed(int(dronx*100), int(drony*100), z, 40)
                print("tello.go_xyz_speed(", int(dronx*100), int(drony*100), z, "40)")
                time.sleep(2)
            x1, y1 = x2, y2
            time.sleep(1)
            coor = puntos.readline()
        tello.land()
        os._exit(1)