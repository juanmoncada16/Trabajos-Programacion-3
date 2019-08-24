if __name__ == "__main__":
    #Leer Archivos de Python r= lectura w= escritura a= agrega x= lectura/escritura
    dias_semana = open("dia.txt",'r')
    print(dias_semana)
    for dia in dias_semana:
        print(dia.rstrip())
        if dia.rstrip() == "Lunes":
            print("Que pereza!")

    dias_semana.close()

    dias_laborales = open("diasl.txt", 'w')
    dias_laborales.write("Lunes\n")
    dias_laborales.write("Martes\n")
    dias_laborales.write("Miercoles\n")
    dias_laborales.write("Jueves\n")
    dias_laborales.write("Viernes\n")

    dias_laborales.close()

