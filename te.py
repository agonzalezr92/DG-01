class Te:
    duracion = 365

    @staticmethod
    def retorna_tiempo_y_recomendacion(sabor):
        if sabor == 1:
            return (
                3,
                "Al desayunar",
            )
        elif sabor == 2:
            return (
                5,
                "Al medio día",
            )
        elif sabor == 3:
            return (
                6,
                "Al atardecer",
            )
        else:
            return 0

    @staticmethod
    def retorna_precio(formato):
        if formato == 500:
            return 5000
        elif formato == 300:
            return 3000
        else:
            return 0
