from flask import Blueprint, render_template
import controllers.products

products_router = Blueprint('products_router', __name__)

@products_router.route('/home')
def home() :#{
    return render_template('index.jinja')
#}

@products_router.route('/')
def get() : return controllers.products.GET()

@products_router.route('/<id>')
def get_id(id) : return controllers.products.GET_ID(id)

@products_router.route('/', methods = ['POST'])
def post() : return controllers.products.POST()

@products_router.route('/<id>', methods = ['PUT'])
def put(id) : return controllers.products.PUT(id)


@products_router.route('/<id>', methods = ['DELETE'])
def delete(id) : return controllers.products.DELETE(id)

