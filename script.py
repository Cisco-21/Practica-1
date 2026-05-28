def espacio_elevador (limite, dentro, esperando):

    total=dentro + esperando

    if total <= limite:
        return 0
    else:
            return total - limite

            print(espacio_elevador(8, 3, 4))
            print(espacio_elevador(6, 4, 5))
