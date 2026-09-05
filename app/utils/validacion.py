campos_requeridos = ['nombre', 'precio', 'stock', 'categoria']

def validacion_completa(request_data):
    if not validar_campos_requeridos(request_data):
        return False
    if not campos_none(request_data):
        return False
    if not validar_precio(request_data):
        return False
    if not validar_stock(request_data):
        return False
    return True

def validar_campos_requeridos(request_data):
    for campo in campos_requeridos:
        if campo not in request_data:
            return False
    return True

def campos_none(request_data):
    for campo in campos_requeridos:
        if request_data[campo] == None:
            return False
    return True

def validar_precio(request_data):
    if not type(request_data['precio']) == int and not type(request_data['precio']) == float:
        return False
    if request_data['precio'] < 0:
        return False
    return True

def validar_stock(request_data):
    if not type(request_data['stock']) == int:
        return False
    if request_data['stock'] < 0:
        return False
    return True