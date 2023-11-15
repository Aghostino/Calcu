def somma(x,y):

    return x + y

def sottrazione(x,y):

    return x - y

def moltiplicazione(x,y):

    return x * y

def divisione(x,y):

    if(y==0):
        print("divisione impossibile")

    else:
        return x / y



num1 = float(input("inserisci il primo numero: "))
num2 = float(input("inserisci il secondo numero: "))

scelta = input("inserisci la tua scelta tra 1/2/3/4: ")

if(scelta == '1'):

    print(somma(num1,num2));

if(scelta == '2'):

    print(sottrazione(num1,num2));

if(scelta == '3'):

    print(moltiplicazione(num1,num2));

if(scelta == '4'):

    print(divisione(num1,num2));
