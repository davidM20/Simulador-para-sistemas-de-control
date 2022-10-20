#Valores Optimos
temperatura_deseada = 105 # La temeperatura optima de trabajo es de 105 Grados celsius 
flujo_vapor_deseado = 63 #Estoy tomando como referencia el valor medio para una entrada entre 10-90Lt de vapor por segundo
psi_deseado= 110 # Se trabaja en psi y debe ser el ideal en 110 psi


#Valores default
flujo_lacteo= 100 # Estoy tomando una entrada de 100 litors de leche que esta dentro de un rango de 0 a 200 litos por segundo
nivel_tanque =50 # El tanque se trabaja en porcentaje y el optimo debe estar en 90%
flujo_vaper= 45
temperatura_actual = 90
apertura_de_la_valvula= 100 # Esta indica el grado de apertura de la misma en porcentaje  ES ATC POR QUE COMIENZA EN 100
apertura_de_la_valvula_dos =0 # Es ATO por que inicia en 0
psi = 115
aux = True
acum =0

#Aqui Guardo los valores iniciales para mas a adelante mostrar en pantalla 
temperatura_actual_print = temperatura_actual
psi_print= psi
flujo_print= flujo_vaper

#Ecuacion que relaciona la temperatura con el flujo de vapor 
temperatura_actual = (105/63)*flujo_vaper

def selector(temp, psi_var): #Este siempre escoje el valor mas bajo 
    global temperatura_deseada, psi_deseado, aux

    if (temp > temperatura_deseada):
        aux= False
    if (temp < temperatura_deseada):
        aux= True
        print("El selector esta saturando en: Temperatura")


    if (psi_var > psi_deseado):
        aux= False
    if (psi_var < psi_deseado):
        aux = True
        print("El selector esta saturando en: Presion PSI")

def salida_pasteurizada():
    global nivel_tanque, acum
    if nivel_tanque >0:
        nivel_tanque = nivel_tanque - 1
        acum+=1

def valvula_Uno_ATO():
    global flujo_vaper, temperatura_actual,psi, aux, apertura_de_la_valvula


    if ( aux == True):
        apertura_de_la_valvula = apertura_de_la_valvula +1

    if ( aux == False):

        if (flujo_vaper >= 0):
            apertura_de_la_valvula = apertura_de_la_valvula-1

    temperatura_actual = (105/63)*flujo_vaper

    psi= (110/105)*temperatura_actual

def valvula_ato_dos():
    global nivel_tanque
    nivel_tanque= nivel_tanque+1
    
def LT():
    global nivel_tanque
    if nivel_tanque != 90:
        FIC2()

def FIC():
    global flujo_vaper, apertura_de_la_valvula
    flujo_vaper = apertura_de_la_valvula*0.8

def FIC2():
    global apertura_de_la_valvula_dos, flujo_lacteo, nivel_tanque

    flujo_lacteo = apertura_de_la_valvula_dos*(200/90)

    if nivel_tanque<90:
        apertura_de_la_valvula_dos= apertura_de_la_valvula_dos+1
        valvula_ato_dos()

    if nivel_tanque>90:
        apertura_de_la_valvula_dos= apertura_de_la_valvula_dos -1

# Aqui iniciamos el sistema 

def maint():
    selector(temperatura_actual,psi)
    FIC()
    valvula_Uno_ATO()
    LT()
    salida_pasteurizada()
    print("Datos Iniciales\n")
    print("Flujo inicial:", flujo_print, "Temperatura Inicial: ", temperatura_actual_print,"PSI inicio: ",psi_print,"\n\n" )
    print("RESULTADOS\n")
    print(temperatura_actual," Grados celsius\n", flujo_vaper, " Flujo de vapor al tanque \n", "Litros entregados:",acum,"\nNivel de presion de vapor:",psi,"\n"  ,"Nivel tanque:",nivel_tanque, "\n\n\n\n\n\n\n\n" )

for i in range (120):
    maint()

    
        



































