
preguntar = input("Dime el precio que te gustaria que tuviera la camiseta: ");

if(preguntar.isdigit()):
    precio = int(preguntar)
    
    # Sin descuento
    pdescuento = input("Esta bien, pero debo saber si va a tener un descuento o no?: ");
    def respuestaNegativa():
        valorIVA = 19
        sIVA = precio * (valorIVA / 100)
        descuentoIVA = precio + sIVA
        print("Bueno, como elegiste no ponerle un descuento a tu camiseta esta actualmente vale: ",(precio))
        print("De todas maneras hay que sumarle el Impuesto al Valor Agregado(IVA)")
        print("Teniendo en cuenta que el IVA es de un 19% tu camiseta finalmente vale: ",int(descuentoIVA))
        print("Felicidades, tu camiseta ahora esta a la venta a un valor de ",int(descuentoIVA), "esperemos que a la gente le guste y compre tu camiseta")


    # Con descuento
    def respuestaPositiva():
        porcentaje = input("Está bien, ahora quiero que me digas el porcentaje de descuento: ");
        if(porcentaje.isdigit()):
            # Variables de %
            nporcentaje = int(porcentaje); # para convertir el string en un numero
            sdescuento = precio * (nporcentaje / 100) # para sacar el descuento
            descontado = precio - sdescuento # para aplicar el descuento
            valorIVA = 19
            sIVA = precio * (valorIVA / 100)
            descuentoIVA = descontado + sIVA
            # Final
            print("Ok, el precio actual de tu camiseta es de: ",int(descontado))
            print("Pero eso no es todo, tambien hay que sumarle el Impuesto al Valor Agregado(IVA)")
            print("Teniendo en cuenta que el IVA es de un 19% tu camiseta finalmente vale: ",int(descuentoIVA))
            print("Felicidades, tu camiseta ahora esta a la venta a un valor de ",int(descuentoIVA), "esperemos que a la gente le guste y compre tu camiseta")
        else:
            print("Necesitamos un numero, vuelva mas tarde.")
    # Apartado if/elif

    # Respuestas Negativas

    if(pdescuento == "no" or pdescuento == "No" or pdescuento == "nO" or pdescuento == "NO"):
        respuestaNegativa()
    
    # Respuestas Positivas

    elif(pdescuento == "si" or pdescuento == "sí" or pdescuento == "sI" or pdescuento == "sÍ" or pdescuento == "Si" or pdescuento == "SI" or pdescuento == "Sí" or pdescuento == "SÍ"):
        respuestaPositiva()

    # Diferente
    else:
        print("osea, tenias que decir si o no, no era tan dificil ¯\_(ò_ó)_/¯")
else:
    print("para la proxima coloca un numero")