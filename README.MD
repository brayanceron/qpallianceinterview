# Documentation

## EndpointS

-------------------------------------------
endpoint : /product

method: GET
body : Not
headers :
    - Content-Type : application/json

-------------------------------------------
endpoint : /product/id

method : GET
params : product id
headers :
    - Content-Type : application/json

-------------------------------------------

endpoint : /product

method : POST
body : ```
```
{
	"name" : "name_product",
	"current_stock" : 100,
	"min_stock" : 10
}
```
headers :
    - Content-Type : application/json
-------------------------------------------
endpoint : /product/id

method : PUT
params : product id

body : 
```
{
	"name" : "name_product",
	"current_stock" : 100,
	"min_stock" : 10
}
```
headers :
    - Content-Type : application/json
-------------------------------------------
endpoint : /product/id

method : DELETE
params : product id
headers :
    - Content-Type : application/json

-------------------------------------------


