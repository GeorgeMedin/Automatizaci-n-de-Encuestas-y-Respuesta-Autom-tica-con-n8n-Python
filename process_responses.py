# obtenga los datos de la encuesta respondida por el cliente
datos = items[0]['json'] 

# Extraer respuestas con valores por defecto si no existenn
respuestas = {
    "experiencia_general": datos.get('¿Cómo calificaría su experiencia general en nuestro hotel?', ""),
    "limpieza": datos.get('¿Qué tan satisfecho estuvo con la limpieza y comodidad de la habitación?', ""),
    "personal": datos.get('¿Cómo fue la atención del personal durante su estancia?', ""),
    "servicios": datos.get('¿Qué tan satisfecho estuvo con los servicios adicionales (restaurante, piscina, gimnasio, etc.)?', "")
}

def generar_disculpa(respuestas):
    problemas = []

    if respuestas["experiencia_general"] in ["Insatisfecho", "Muy insatisfecho"]:
        problemas.append("su experiencia general en nuestro hotel")
    if respuestas["limpieza"] in ["Insatisfecho", "Muy insatisfecho"]:
        problemas.append("la limpieza y comodidad de la habitación")
    if respuestas["personal"] in ["Mala", "Muy mala"]:
        problemas.append("la atención del personal")
    if respuestas["servicios"] in ["Insatisfecho", "Muy insatisfecho"]:
        problemas.append("los servicios adicionales")

    if not problemas:
        mensaje = "Gracias por su calificación. Seguiremos trabajando para brindarle la mejor experiencia." #En caso de no obtener ninguna respuesta insatisfecha, simplemente agradezca en el mensaje
    else:
        mensaje = "Lamentamos que haya tenido problemas con "
        if len(problemas) == 1:
            mensaje += problemas[0]
        elif len(problemas) == 2:
            mensaje += " y ".join(problemas)
        else:
            mensaje += ", ".join(problemas[:-1]) + " y " + problemas[-1]
        mensaje += ". Nos esforzaremos por mejorar estos aspectos para brindarle una mejor experiencia en el futuro."

    return [{"json": {"mensaje": mensaje}}]  # Retornar en el formato correcto

# Retornar msj a n8n
return generar_disculpa(respuestas)
