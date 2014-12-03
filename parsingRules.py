import json
 

rules = """
{ 
	    "r1": {
	    "cartTotal": ">=,1000",
		"categoryId" : "!=,15,5,7",   
        "output": {
                "percent_discount": 20,
                "shipping_cost": 0,
                "free_product" : "",
                "flat_discount" : ""
            },
            "expiry" : "17/11/14 23:59"
        },

         "r2": {
            "cartTotal": "<,1000",
            "categoryId" : "20,1,5",
            "output": {
                "percent_discount": "",
                "shipping_cost": 0,
                "free_product" : 23,
                "flat_discount" : 200
            },
            "expiry" : "20/11/14 23:59"
        },

        "r3": {
            "cartTotal": "<=,500",
            "categoryId" : "10,3,6",
            "output": {
                "percent_discount": "",
                "shipping_cost": 50,
                "free_product" : "",
                "flat_discount" : 80

            },
            "expiry" : "16/11/14 23:59"
        },

        "r4": {
            "cartTotal": "=,5000",
            "categoryId" : "1,4,9",
            "output": {
                "percent_discount": 16,
                "shipping_cost": 50,
                "free_product" : 42,
                "flat_discount" : ""
            },
            "expiry" : "14/11/14 23:59"
         }

}

"""

rulesJsonData = json.loads(rules)
 
