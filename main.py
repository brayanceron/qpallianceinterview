from flask import Flask
import routes.products
from controllers.products import CREATE

app = Flask(__name__)
app.register_blueprint(routes.products.products_router, url_prefix='/product')

if __name__ == '__main__' :#{
    CREATE()
    app.run(debug=True, port=5000)
#}

