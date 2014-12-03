from parsingInput import cartItemsData

from fillRulesInfo import category_mapping, cartTotalMapping, rulesJsonData

from adminInfo import *



def fillCartTotalMatchingRules(cartTotalMatchingRules, cartTotalMapping, cartTotal):
	for key in cartTotalMapping:
		if int(key) == cartTotal:
			index=1	

		elif int(key) > cartTotal:
			index=0
			
		else:
			index=2
		
		value = str(cartTotalMapping[key][index])
		if(value):
			if(',' in value):
				tmpStr = value.split(',');
				for v in tmpStr:
					cartTotalMatchingRules.add(v)
			else:
				cartTotalMatchingRules.add(value) 


def fillCategoryMatchingRules(productCategoryMatchingRules, category_mapping, cartItemsData):
	for key in cartItemsData:
		if key != 'extraInfo' :
			product_Catid = cartItemsData[key]['categoryId']
			#print category_mapping[product_Catid]
			if(',' not in  product_Catid):
				for value in category_mapping[int(product_Catid)]:
					productCategoryMatchingRules.add(value)
			else:
		 		product_Catid = product_Catid.split(',');
		 		#print product_Catid
		 		for catid in product_Catid:
		 			for value in category_mapping[int(catid)]:
						productCategoryMatchingRules.add(value)

		


#print "CartItemsData ", cartItemsData
#print "Category Mapping : ", category_mapping
#print "Cart Total Mapping : ", cartTotalMapping


cartTotal = 0;
for key in cartItemsData:
	if key != 'extraInfo' :
		cartTotal += int(cartItemsData[key]['price'])


#print cartTotal;


cartTotalMatchingRules = set();
productCategoryMatchingRules = set();

fillCartTotalMatchingRules(cartTotalMatchingRules, cartTotalMapping, cartTotal)
fillCategoryMatchingRules(productCategoryMatchingRules, category_mapping, cartItemsData)


#Clearing the Screen
import os
clear = lambda: os.system('cls')
clear()

#Current TimeStamp

from datetime import datetime
currentTimeStamp = datetime.now()


print "######################  WELCOME TO E-COMMERCE RULE ENGINE  ######################\n\n\n"

print "~~~~~ CartTotal Matching Rules: ~~~~~\n\n" , cartTotalMatchingRules , "\n\n"

print "~~~~~ Product Category Matching Rules : ~~~~~\n\n" , productCategoryMatchingRules, "\n\n"

finalRules = cartTotalMatchingRules.intersection(productCategoryMatchingRules)

print "~~~~~ Final Rules Matched:  ~~~~~\n\n", finalRules , "\n\n"

if len(finalRules) > 1:
	print "~~~~~ Consulting Priority List ~~~~~ \n"
	minIndex = 10000
	for var in finalRules: 
		if priorityList.index(var) < minIndex:
			minIndex = priorityList.index(var)
			maxPriorityRule = var
	print "~~~~~ Max Priority Rule : ~~~~~\n\n" ,maxPriorityRule
else :
	maxPriorityRule = finalRules.pop()


print "\n\n $$$$  Output: $$$$ \n\n"

#maxPriorityRule = "r1"

if(rulesJsonData[maxPriorityRule]['output']['percent_discount']):
	print "Discount Percentage: " ,rulesJsonData[maxPriorityRule]['output']['percent_discount']

if(rulesJsonData[maxPriorityRule]['output']['flat_discount']):
	print "Flat Discount: " ,rulesJsonData[maxPriorityRule]['output']['flat_discount']

if(rulesJsonData[maxPriorityRule]['output']['shipping_cost']):
	print "Shipping Charges : " ,rulesJsonData[maxPriorityRule]['output']['shipping_cost']

if(rulesJsonData[maxPriorityRule]['output']['free_product']):
	print "Free Product ID: " ,rulesJsonData[maxPriorityRule]['output']['free_product']


print "\n\n $$$$ Extra Discount/Charges if Applicable $$$$\n\n"

for key in paymentOffers:
	paymentTypeString = str(cartItemsData['extraInfo']['paymentType']) 
	offerTimeStamp = datetime.strptime(paymentOffers[paymentTypeString][1], "%d/%m/%y %H:%M") 
	if (key == paymentTypeString and ( currentTimeStamp <= offerTimeStamp )) :
		print "Payment Type: " ,paymentTypeString , " , Discount: " , paymentOffers[paymentTypeString][0] , "\n"


for key in rechargeCodes:
	rechargeCodeString = str(cartItemsData['extraInfo']['rechargeCode']) 
	offerTimeStamp = datetime.strptime(rechargeCodes[rechargeCodeString][1], "%d/%m/%y %H:%M") 
	if (key == rechargeCodeString and ( currentTimeStamp <= offerTimeStamp )) :
		print "Recharge Code: " , cartItemsData['extraInfo']['rechargeCode'] , " , Discount: " , rechargeCodes[rechargeCodeString][0] , "\n"


for key in userType:
	userTypeString = str(cartItemsData['extraInfo']['userType']) 
	offerTimeStamp = datetime.strptime(userType[userTypeString][1], "%d/%m/%y %H:%M") 
	if key == userTypeString and ( currentTimeStamp <= offerTimeStamp ):
		print "User Type: " , cartItemsData['extraInfo']['userType'] , " , Discount: " , userType[userTypeString][0], "\n"







	




	 











