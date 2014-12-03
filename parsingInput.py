import json
 

cartItems = """
{ 
	"p1": {
        "productId" : "123",
	"categoryId" : "8,2,3", 
        "price" : "300"  
        },

        "p2": {
        "productId" : "456",
        "categoryId" : "5", 
        "price" : "350"  
        },

        "p3": {
        "productId" : "567",
        "categoryId" : "20,12,16", 
        "price" : "270"  
        },

        "p4": {
        "productId" : "435",
        "categoryId" : "1,2", 
        "price" : "280"  
        },

        "extraInfo": {
        "paymentType" :"COD",
        "rechargeCode" : "ABCD",
        "userType" : "FirstTime"
        }
}

"""

cartItemsData = json.loads(cartItems)
#print cartItemsData
 
