from flask import Blueprint, Response

products = Blueprint('products', __name__, url_prefix='/products')

@products.route('/all', methods=['GET', 'POST'])
def get_products():
    """ 
    Description 
    params:
    return:
    """
    if request.method == 'POST':
        return "<b> Bienvenido a la pagina de productos"
    return "<b> Super bienvenido a la pagina de productos"


@products.route('/grooming', methods=['GET'])
def get_products_grooming():
    """ 
    Description: Redirect to section of grooming  
    params:
    return: Section of grooming
    """
    return "<h1><b> Bienvenido a la pagina de productos de aseo"

@products.route('/dairy', methods=['GET'])
def get_products2():
    """ 
    Description: Redirect to section of grooming
    params:
    return: Section of dairy
    """
    return "<h1><b> Bienvenido a la pagina de productos lacteos</h1>"

@products.route('/<string:name>', methods=['POST'])
def get_ProductsB(name):
    """ 
    Description: Inform if a product is available or not in the store
    params: name Name of product
    return: if name is coffee the product isn't available
            if name isn't coffee the product is available only phisycal store
    """
    if name != 'coffee':
        return Response("El producto {} aun no esta disponible en nuestra tienda".format(name), status=400)
    else:
        return Response("El producto se encuentra disponible unicamente en la tienda fisica", status=200)

@products.route('/<string:name>', methods=['GET'])
def get_productsA(name):
    """ 
    Description: Example of response 
    """
    if name != 'pygroup':
        return Response("Felicitaciones, trabajo exitoso {} ".format(name), status=200)
    else:
        return Response("Error, el nombre no lo entiendo <(^_^<)", status=400)


"""
render_template:
Permite usar plantillas para el contenido dinámico de páginas web. 
En ejemplos mostrados en la busqueda realizada se observa la ruta y el metodo como lo hemos trabajado hasta el momento pero en el retorno
se usa el metodo render_template(), en el cual como parametros, pasan el nombre del archivo .html y dos variables, las cuales en el codigo
del archivo .html se van a actualizar dependiendo de los enviados como argumentos en el metodo render_template().
En otros ejemplos mostraban el uso de comparaciones if-else o bucles para iterar sobre conjuntos de tuplas enviadas por medio del mismo 
metodo. 
"""