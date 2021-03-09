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

EnergyToC02 = lambda e : e - 160 * 1e-6 * 3600
