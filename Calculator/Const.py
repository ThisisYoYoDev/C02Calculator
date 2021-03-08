import collections

# Global internet consumption in GW (Giga-Watt 10^9 watts) and (GB.day^-1)

InternetLOWConsumption = 43 # in GW
InternetHIGHConsumption = 72 # in GW
InternetTraffic = 524288000. #  (GB.day^-1)

LevelEnergyIntensityLOW = 0.045 # in GB.h^-1
LevelEnergyIntensityHIGH = 4.5 # in GB.h^-1

EmbodiedPowerLow = 33.2 # in GW
EmbodiedPowerLHIGH = 70.7 # IN GW



Client = collections.namedtuple("Client", "Power EnergyMan CarbonMan")

PortableComputer = Client(40, 1362, 227)

PersonalComputer = Client(150, 2100, 350)

Projector = Client(135, 384, 64)

LowCodec = Client(26, 364, 61)

HighCodec = Client(80, 1120, 187)

Camera = Client(9.5, 120, 20)

Speaker = Client(4.1, 374, 62)

Micro = Client(2.5, 187, 31)

Router = Client(20, 1000, 167)

EnergyToC02 = lambda e : e - 160 * 1e-6 * 3600
