# Importar e inicializar colorama:
from colorama import init, Fore, Back, Style

# Saludo de cortesía al usuario:
print("\n¡Hola, oficial! Determinaremos tus datos.\n")

# Se solicitan datos al usuario:
name = input("Ingrese su nombre completo: ")
age = int(input("Ingrese su edad: "))
exp = int(input("Ingrese tiempo de experiencia (Años): "))

# Estructura lógica para determinar rango:
if exp >= 1 and exp <= 3:
    rng = 'Cadete'
elif exp >= 4 and exp <= 10:
    rng = 'Profesional'
elif exp > 10:
    rng = 'Intendente'

# Lista para datos de usuario:
ls1 = []

# Se solicitan ciudades de trabajo al usuario (bucle para varias):
ls2 = [] # Lista para ciudades
note = '''\nNOTA: Ahora, por favor, ingrese todas las 
ciudades donde ha prestado servicio. Al finalizar de 
ingresarlas, digite la palabra: 'Salir'.\n'''
print(Style.BRIGHT + Fore.GREEN + note + Style.RESET_ALL)
cts = ''
# Bucle para ciudades:
while cts.lower() != 'salir':
    cts = input('Ingrese ciudad: ')
    if cts.lower() != 'salir':
        ls2.append(cts)

# Diccionario para almacenar datos del usuario:
officer = {'Nombre': name, 'Edad': age, 'Experiencia': exp, 'Rango': rng, 'Ciudades': ls2}  

# Guardamos datos en un archivo:
with open('DatosOficial.txt', 'w') as file:
    print(Style.BRIGHT + Fore.GREEN +'\n\nSus datos son los siguientes:\n' + Style.RESET_ALL)
    file.write(f'Nombre: {officer["Nombre"]}\n')
    file.write(f'Edad: {officer["Edad"]}\n')
    file.write(f'Experiencia: {officer["Experiencia"]} años.\n')
    file.write(f'Rango: {officer["Rango"]}\n')
    file.write('Ciudades:\n')

    # Bucle 'for' anidado para imprimir ciudades en listado individual;
    # PD: Casi se me quema el cerebro haciendo eso, me demoré 30 mins
    # pensando en cómo insertarlo, ¡valóralo, master! XD:
    for ciudad in officer["Ciudades"]:  
        file.write(f'- {ciudad}\n')

with open('DatosOficial.txt', 'r') as s_file:
    print(s_file.read())  # Lee e imprime todo el archivo


str(age)
str(exp) 

print() 