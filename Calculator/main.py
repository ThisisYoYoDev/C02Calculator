from Calculator.ClassC02 import totalConsumption
import pandas as pd

def main():
    print("Saisissez le nombre d'heures pendant lesquelles la visioconférence aura lieu: ")
    hours = int(input())

    print('Combien de PC portable seront utilisés dans la visioconférence ?')
    num_pcs = int(input())
    
    print('Quel pourcentage approximatif d’entre eux sont des ordinateurs de bureau ? (Entrez u pour inconnu)')
    percent_desktop = input()
    
    if percent_desktop == 'u':
        percent_desktop=57.1
    
    num_desktops = num_pcs * int(percent_desktop) / 100
    num_laptops = num_pcs - num_desktops
    
    print('Quel pourcentage de ces ordinateurs de bureau utilisent des écrans LED ou LCD (entrez u pour inconnu)')
    
    per_LED = input()
    if (per_LED == 'u'):
        per_LED = 78.6
    
    print('Combien d\'écrans LCD / LED supplémentaires sont utilisés ?')
    extra_led = int(input())
    
    print('Quelle est la taille de ces écrans (pouces)? Entrez u pour inconnu')
    width_led = input()
    
    if width_led == 'u':
        width_led = 60
    width_led = int(width_led)

    height_led = (width_led / 16) * 9
    area_led = width_led * height_led
    area_led *= 0.00064516
    
    print('Combien d\'écrans plasma supplémentaires sont utilisés ?')
    extra_plasma = int(input())
    
    print('Quelle est la taille de ces écrans (pouces)? Entrez u pour inconnu')
    width_plasma = input()
    
    if width_plasma == 'u':
        width_plasma = 60
    width_plasma = int(width_plasma)
    
    height_plasma = (width_plasma/16) * 9
    area_plasma = width_plasma * height_plasma
    area_plasma *= 0.00064516
    
    print('Nombre de CODEC haut de gamme utilisés :')
    num_high_codecs = int(input())
    
    print('Nombre de CODEC bas de gamme utilisés :')
    num_low_codecs = int(input())
    
    print('Nombre de caméras utilisées :')
    num_cameras = int(input())
    
    print('Nombre de haut-parleurs utilisés :')
    num_speakers = int(input())
    
    print('Nombre de microphones utilisés :')
    num_microphones = int(input())
    
    print('Nombre de routeurs utilisés :')
    num_routers = int(input())
    data = {
        'Hours': hours, 
        'Number of desktops': num_desktops, 
        'Number of laptops': num_laptops, 
        'Percentage LED and LCD': int(per_LED), 
        'Number of extra LCD/LED screens': extra_led, 
        'Area of extra LED/LCD screens': area_led, 
        'Number of extra plasma screens': extra_plasma, 
        'Area of extra plasma screens': area_plasma, 
        'Number of high performance CODECs': num_high_codecs, 
        'Number of low performance CODECs': num_low_codecs,
        'Number of cameras': num_cameras,
        'Number of speakers': num_speakers, 
        'Number of microphones': num_microphones, 
        'Number of routers': num_routers
    }              
    return data

data = main()
print(data)
energy = totalConsumption.totalEngine(data)
co2 = 0.6*(energy/3600000)
print('The carbon dioxide produced by this videoconference is: {:.3f} in kgC02e'.format(co2))

data["Consommation"] = str(co2)
df = pd.DataFrame(data=data, index=[0])
df.to_excel('test.xlsx')

exit(0)