
from Calculator.Const import *

class C02_init_world_for_server():
    VideoLOWConsumption = InternetLOWConsumption * LevelEnergyIntensityLOW # GB.h^-1
    VideoHIGHConsumption = InternetHIGHConsumption * LevelEnergyIntensityHIGH # GB.h^-1

    EmbodiedPowerIntesityLOW = EmbodiedPowerLow * 1e6 / (InternetTraffic / 24.) # kWh.GB^-1
    EmbodiedPowerIntesityHIGHs = EmbodiedPowerLHIGH * 1e6 / (InternetTraffic / 24.) # kWh.GB^-1

class C02_init_world_for_client():
    @staticmethod
    def Screen_Plasma(env):
        return Client(20 + env * 203, 5096 * env, 849 * env)
    
    @staticmethod
    def ScreenLedLCD(env):
        return Client(20 + env * 172, 3218 * env, 536 * env)