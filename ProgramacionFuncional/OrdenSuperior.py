def saludar(idioma):
    def saludar_es():
        print("Que mas pana")

    def saludar_en():
        print("What's going on")

    def saludar_fr():
        print("Bonjour")

    f_idioma = {"es": saludar_es,
                "en": saludar_en,
                "fr": saludar_fr}

    return f_idioma[idioma]  # devuelve el valor de la clave del diccionario, clave que es pasada por parametro a la funcion principal


f = saludar("en")
# f()
# Mas simplificado:
saludar("fr")()  # El segundos par de parentesis indican que devuelve una funcion
