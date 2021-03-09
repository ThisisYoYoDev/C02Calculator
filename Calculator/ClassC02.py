from Calculator.Const import *
import pandas as pd


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
    PortableComputer = Client(40, 1362, 227)

    PersonalComputer = Client(150, 2100, 350)

    Projector = Client(135, 384, 64)

    LowCodec = Client(26, 364, 61)

    HighCodec = Client(80, 1120, 187)

    Camera = Client(9.5, 120, 20)

    Speaker = Client(4.1, 374, 62)

    Micro = Client(2.5, 187, 31)

    Router = Client(20, 1000, 167)


class totalConsumption():
    @staticmethod
    def totalEngine(data):
        ClientProP = C02_init_world_for_client()
        evn = 0.24
        lifetime = {
            'laptop': 35040, 
            'desktop' : 35040, 
            'LED screen': 100000, 
            'Plasma screen': 45000, 
            'High performance codec': 87600, 
            'Low performance codec': 87600, 
            'Camera': 70080, 
            'Speaker' : 17520, 
            'Microphone' : 175200, 
            'Router' : 30660
        }
        TotalEnergyUse = 0
        hours = data['Hours']
        operating_seconds = hours * 360

        TotalEnergyUse += data['Number of laptops'] * ClientProP.PortableComputer.Power * operating_seconds
        TotalEnergyUse += data['Number of laptops'] * ClientProP.PortableComputer.EnergyMan * hours/lifetime['laptop']

        TotalEnergyUse += data['Number of desktops'] * ClientProP.PersonalComputer.Power * operating_seconds
        TotalEnergyUse += data['Number of desktops'] * ClientProP.PersonalComputer.EnergyMan * hours/lifetime['desktop']

        TotalEnergyUse += data['Number of desktops'] * (data['Percentage LED and LCD']/100) * ClientProP.ScreenLedLCD(evn).Power
        TotalEnergyUse += data['Number of desktops'] * (data['Percentage LED and LCD']/100) * ClientProP.ScreenLedLCD(evn).EnergyMan * hours/lifetime['LED screen']

        TotalEnergyUse += data['Number of desktops'] * ((100 - data['Percentage LED and LCD'])/100) * ClientProP.Screen_Plasma(evn).Power
        TotalEnergyUse += data['Number of desktops'] * ((100 - data['Percentage LED and LCD'])/100) * ClientProP.Screen_Plasma(evn).EnergyMan * hours/lifetime['Plasma screen']

        TotalEnergyUse += data['Number of extra LCD/LED screens'] * ClientProP.ScreenLedLCD(data['Area of extra LED/LCD screens']).Power
        TotalEnergyUse += data['Number of extra LCD/LED screens'] * ClientProP.ScreenLedLCD(data['Area of extra LED/LCD screens']).EnergyMan * hours/lifetime['LED screen']

        TotalEnergyUse += data['Number of extra plasma screens'] * ClientProP.ScreenLedLCD(data['Area of extra LED/LCD screens']).Power
        TotalEnergyUse += data['Number of extra plasma screens'] * ClientProP.ScreenLedLCD(data['Area of extra plasma screens']).EnergyMan * hours/lifetime['Plasma screen']

        TotalEnergyUse += data['Number of high performance CODECs'] * ClientProP.HighCodec.Power * operating_seconds
        TotalEnergyUse += data['Number of high performance CODECs'] * ClientProP.HighCodec.EnergyMan * hours/lifetime['High performance codec']

        TotalEnergyUse += data['Number of low performance CODECs'] * ClientProP.LowCodec.Power * operating_seconds
        TotalEnergyUse += data['Number of low performance CODECs'] * ClientProP.LowCodec.EnergyMan * hours/lifetime['Low performance codec']

        TotalEnergyUse += data['Number of cameras'] * ClientProP.Camera.Power * operating_seconds
        TotalEnergyUse += data['Number of speakers'] * ClientProP.Speaker.Power * operating_seconds
        TotalEnergyUse += data['Number of microphones'] * ClientProP.Micro.Power * operating_seconds
        TotalEnergyUse += data['Number of routers'] * ClientProP.Router.Power * operating_seconds

        TotalEnergyUse += data['Number of cameras'] * ClientProP.Camera.EnergyMan * hours/lifetime['Camera']
        TotalEnergyUse += data['Number of speakers'] * ClientProP.Speaker.EnergyMan * hours/lifetime['Speaker']
        TotalEnergyUse += data['Number of microphones'] * ClientProP.Micro.EnergyMan * hours/lifetime['Microphone']
        TotalEnergyUse += data['Number of routers'] * ClientProP.Router.EnergyMan * hours/lifetime['Router']

        return TotalEnergyUse