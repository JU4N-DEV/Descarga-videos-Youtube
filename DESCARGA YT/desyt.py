from importlib.resources import path
import pytube

#by:JUANHG (T4RS)

def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Ingresa una opcion: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
 
    print ("1. Descarga Audio MP4")
    print ("2. Descarga video 1080p")
    print ("3. Descarga video 720p")
    print ("4. Salir")
     
    print ("Elige una opcion")
 
    opcion = pedirNumeroEntero()
    path = "Agrega tu ruta de descarga"
    God = ("Descarga completada...:) BY:JU4N")
    if opcion == 1:
        print ("Descarga Audio")
        tarea1 = '1'
        tarea1 = ("Descarga de audio")
        Cancionn = tarea1
        Cancionn = input("Ingresa la url: ")
        print(Cancionn)
 
    
        Cancionn = pytube.YouTube(url=Cancionn)
        Cancionn = Cancionn.streams.get_by_itag("140")
        Cancionn.download(path)
        
        print(God)
    
    elif opcion == 2:
        print ("Descarga video 1080p")
        tarea2 = '2'
        tarea2 = ("Descarga video 1080p...")
        Video1 = tarea2

        Video1 = input("Ingresa la url: ")
        print(Video1)


        Video1 = pytube.YouTube(url=Video1)
        Video1 = Video1.streams.get_by_itag("137")
        Video1.download(path)
        print(God)


    elif opcion == 3:
        print("Descarga video 720p")
        tarea3 = '3'
        tarea3 = ("Descarga video 720p")
        Video3 = tarea3

        Video3 = input("Ingresa la url: ")
        print(Video3)

        Video3 = pytube.YouTube(url=Video3)
        Video3 = Video3.streams.get_by_itag("22")
        Video3.download(path)
        print(God)



    elif opcion == 4:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")
 
print ("Fin")

