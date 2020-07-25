#!/usr/bin/env python
# -*- coding: utf-8 -*-

bandera = 0
# Este es la variable que verifica quien esta usando la seccion critica
# 0 -> Vacio
# 1 -> Proceso1
# 2 -> Proceso2

class Proceso:
    def __init__(self, _nombre, _id):
        self.id = _id
        self.nombre = _nombre

    def delegar(self):
        if (self.id == 1):
            bandera = 2
        else:
            bandera = 1

    def gestionar_proceso(self):
        print ('Tarea Inicial de Proceso {}'.format(self.id))
        while (bandera != self.id):
            pass
        self.ejecutar()
        self.delegar()
        print('Tarea Final de Proceso {}',format(self.id))

    def ejecutar(self):
        print("Ejecutando proceso: {} con id {}".format(self.nombre, self.format))

def iniciar():
    print('Ejecucion de Inicio de SO')
    # Construimos dos procesos
    proceso1 = Proceso('Proceso1', 1)
    proceso2 = Proceso('Proceso2', 2)

    # Como cuando iniciamos el proceso está vacio tratamos de ejecutar un proceso1 con la misma prioridad
    bandera = 1;
    if (bandera == 1):
        proceso1.gestionar_proceso()
    else:
        proceso2.gestionar_proceso()

iniciar()
