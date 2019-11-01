from bussola import CommandsBussola
from threading import Thread
from gpiozero import PWMOutputDevice
import time


class Helps(object):
    def __init__(self, gpioMotor=4, tolerancia=8):
        self.gpioMotor = gpioMotor
        self.motor = PWMOutputDevice(self.gpioMotor)
        self.tolerancia = tolerancia
        self.stopped = True

    def getVariation(self, anguloInicial):

        commands = CommandsBussola()
        angle = commands.getAngle()

        torelanciaAnterior = self.tolerancia
        vibracao = 0
        variacaoVibracao = 0.199
        variacaoTolerancia = 10
        for i in range(5):
            if anguloInicial - self.tolerancia <= angle <= anguloInicial + self.tolerancia:
                self.tolerancia = torelanciaAnterior
                return vibracao
            elif anguloInicial + self.tolerancia > 360 or anguloInicial - self.tolerancia < 0:
                if anguloInicial + self.tolerancia > 360:
                    if angle + 360 > anguloInicial + self.tolerancia:
                        vibracao += variacaoVibracao
                        self.tolerancia += variacaoTolerancia
                elif anguloInicial - self.tolerancia < 0:
                    if angle - 360 < anguloInicial - self.tolerancia:
                        vibracao += variacaoVibracao
                        self.tolerancia += variacaoTolerancia
            else:
                vibracao += variacaoVibracao
                self.tolerancia += variacaoTolerancia

        self.tolerancia = torelanciaAnterior
        return vibracao


    # def andarLinhaReta(self):
    #     self.stopped = False
    #     commands = CommandsBussola()
    #     anguloInicial = commands.getAngle()
    #
    #     while not self.stopped:
    #         angle = commands.getAngle()
    #         print(angle)
    #         if anguloInicial - self.tolerancia <= angle <= anguloInicial + self.tolerancia:
    #             self.motor.value = 0.001
    #         elif anguloInicial + self.tolerancia > 360 or anguloInicial - self.tolerancia < 0:
    #             if anguloInicial + self.tolerancia > 360:
    #                 if angle + 360 > anguloInicial + self.tolerancia:
    #                     self.motor.value = 0.9
    #             elif anguloInicial - self.tolerancia < 0:
    #                 if angle - 360 < anguloInicial - self.tolerancia:
    #                     self.motor.value = 0.9
    #         else:
    #             self.motor.value = 0.9
    #
    #         # print(angle)
    #         time.sleep(0.1)

