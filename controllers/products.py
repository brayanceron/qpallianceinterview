from flask import request
import sqlite3


def GET() :#{
    try :#{
        conn = get_connection()
        if not conn : return {"message" : "Error on db"}, 500
        cursor = conn.cursor()

        cursor.execute('SELECT id, name, current_stock, min_stock from product;')
        results = cursor.fetchall()
        products = []
        for item in results :#{
            products.append(
                {
                    'id' : item[0],
                    'name' : item[1],
                    'current_stock' : item[2],
                    'min_stock' : item[3]
                }
            )
        #}
        
        return products, 200
    #}
    except Exception:#{
        return {"message" : "Error on server"}, 500
    #}
    
#}

def GET_ID(id) :#{
    if not id : return {"message" : "id required"}, 400
    try :#{
        conn = get_connection()
        if not conn : return {"message" : "Error on db"}, 500
        cursor = conn.cursor()

        cursor.execute('SELECT id, name, current_stock, min_stock from product WHERE id = ?;', (id,))
        

        results = cursor.fetchall()
        products = []
        for item in results :#{
            products.append(
                {
                    'id' : item[0],
                    'name' : item[1],
                    'current_stock' : item[2],
                    'min_stock' : item[3]
                }
            )
        #}
        if len(products) == 0: return {"message" : "product not found"}, 404;
        return products, 200
    #}
    except Exception:#{
        return {"message" : "Error on server"}, 500
    #}
#}

def POST() :#{
    try :#{
        name, current_stock, min_stock, message, status = validate_data(request.get_json())
        if(status != 200) : return {"message" : message}, status
        conn = get_connection()
        
        if not conn : return {"message" : "Error on db"}, 500
        cursor = conn.cursor()

        # print(data, name, current_stock, min_stock)
        cursor.execute("INSERT INTO product(name, current_stock, min_stock) VALUES(?, ?, ?)", (name, current_stock, min_stock))
        id = cursor.lastrowid
        conn.commit()
        return {"message": "product register successfully", "id" : id}, 200
    #}
    except Exception as err: #{
        print(err)
        return {"message" : "Error on server"}, 500
    #}
#}

def PUT(id) :#{
    if not id : return {"message" : "id required"}, 400
    try :#{
        conn = get_connection()
        if not conn : return {"message" : "Error on db"}, 500
        cursor = conn.cursor()

        name, current_stock, min_stock, message, status = validate_data(request.get_json())
        if(status != 200) : return {"message" : message}, status

        cursor.execute('SELECT id, name, current_stock, min_stock from product WHERE id = ?;', (id,))
        results = cursor.fetchall()
        if len(results) == 0 : return {"message" : "product not found"}, 404;

        cursor.execute("UPDATE product SET name = ?, current_stock = ?, min_stock = ? WHERE id = ?;", (name, current_stock, min_stock, id))
        conn.commit()

        if (cursor.rowcount == 0) : return {"message" : "product not updated"}, 500
        return {"message" : "product updated"}, 200
        
    #}
    except Exception:#{
        return {"message" : "Error on server"}, 500
    #}
#}

def SELL(id) :#{
    if not id : return {"message" : "id required"}, 400
    try :#{
        conn = get_connection()
        if not conn : return {"message" : "Error on db"}, 500
        cursor = conn.cursor()

        data = request.get_json()
        number = data.get('number')

        if not number :#{
            return {"message" : "All fields are required" }, 400
        #}

        cursor.execute('SELECT current_stock, min_stock from product WHERE id = ?;', (id,))
        results = cursor.fetchall()
        if len(results) == 0 : return {"message" : "product not found"}, 404;
        current_stock = results[0][0]
        if(current_stock - number < 0) : return {"message" : "insufficient products" }, 400
        new_stock = current_stock - int(number)

        cursor.execute("UPDATE product SET current_stock = ? WHERE id = ?;", (current_stock, id))
        conn.commit()

        if (cursor.rowcount == 0) : return {"message" : "product not updated"}, 500
        return {"message" : "product updated"}, 200
        
    #}
    except Exception:#{
        return {"message" : "Error on server"}, 500
    #}
#}

def DELETE(id) :#{
    if not id : return {"message" : "id required"}, 400
    try :#{
        conn = get_connection()
        if not conn : return {"message" : "Error on db"}, 500
        cursor = conn.cursor()

        cursor.execute('DELETE FROM  product WHERE id = ?;', (id,))
        conn.commit()
        if cursor.rowcount == 0 : return {"message" : "product not found"}, 404
        return {"message" : "product deleted successfully"}, 200
    #}
    except Exception:#{
        return {"message" : "Error on server"}, 500
    #}
#}

def CREATE():#{
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS product (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        current_stock INTEGER NOT NULL,
        min_stock INTEGER NOT NULL
    )
    ''')
    # print("DATABASE CREATED")
    conn.commit()
#}


def get_connection() :#{
    conn = sqlite3.connect('company.db')
    # cursor = conn.cursor()
    return conn
#}


def validate_data(data) :#{
    try :#{
        name = data.get('name')

        current_stock = data.get('current_stock', None)
        min_stock = data.get('min_stock',None)
        current_stock = int(current_stock)
        min_stock = int(min_stock)

        if not name or not current_stock or not min_stock :#{
            # return {"message" : "All fields are required" }, 400
            return name, current_stock, min_stock, "All fields are required", 400
        #}
        return name, current_stock, min_stock, "data ok", 200
    #}
    except Exception as err :#{
        print(err)
        return name, current_stock, min_stock, "invalid data", 400
    #}
#}
