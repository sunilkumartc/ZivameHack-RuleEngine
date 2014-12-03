from parsingRules import rulesJsonData
from adminInfo import category_range

#print rulesJsonData

def fillRulesForCartTotal (ruleId, amountInfo):
	#print "amountInfo" ,amountInfo
	ruleId = str(ruleId)
	applicableAmountInfo = str(amountInfo).split(',');
	if('>' in applicableAmountInfo[0]):
		if str(str(applicableAmountInfo[1])) in cartTotalMapping:
			#print "exists !"
			cartTotalMapping[str(applicableAmountInfo[1])][2] = (cartTotalMapping[str(applicableAmountInfo[1])][2] + "," + ruleId)

	  	else :
	  		cartTotalMapping.update({str(applicableAmountInfo[1]) : ["","",ruleId]})
 			#print "do not exist!"

    #includes case of >= , <= , =
 	if('=' in applicableAmountInfo[0]):
 		if str(str(applicableAmountInfo[1])) in cartTotalMapping:
 			if(cartTotalMapping[str(applicableAmountInfo[1])][1]):
				cartTotalMapping[str(applicableAmountInfo[1])][1] = (cartTotalMapping[str(applicableAmountInfo[1])][1] + "," + ruleId)
			else:
				cartTotalMapping[str(applicableAmountInfo[1])][1] = ruleId
	  	else :
	  		cartTotalMapping.update({str(applicableAmountInfo[1]) : ["",ruleId,""]})
 			


 	if('<' in applicableAmountInfo[0]):
 		if str(str(applicableAmountInfo[1])) in cartTotalMapping:
			if(cartTotalMapping[str(applicableAmountInfo[1])][0]):
				cartTotalMapping[str(applicableAmountInfo[1])][0] = (cartTotalMapping[str(applicableAmountInfo[1])][0] + "," + ruleId)
			else: 
				cartTotalMapping[str(applicableAmountInfo[1])][0] = ruleId
	  	else :
	  		cartTotalMapping.update({str(applicableAmountInfo[1]) : [ruleId,"",""]})
 			

	

def fillRulesForCategory (ruleId, ruleCategories, category_range):
	applicableCategories =  str(ruleCategories).split(',')
	if(applicableCategories[0] == '!='):
		#print "Not in Condition"
		for index in range(category_range):
		  if str(index) not in applicableCategories :
		  	category_mapping[index].append(str(ruleId))
	else:
	 	for index in range(category_range):
		  if str(index) in applicableCategories :
		  	category_mapping[index].append(str(ruleId))



#category_range = input("Enter the total categories  : ")
#category_range = 50 # Importing the variable from adminInfo file
category_mapping = [] #rule mapping info for every category will be saved in this list
for i in range(category_range):
       category_mapping.append([])


cartTotalMapping = {} #rule mapping info for cart amount will be saved in this list
# Example : cartTotal = {'100' : ["r1,r2","r2,r3","r4,r5"], '200' : ["","r1,r3","r5,r6"]}  1st position : "<", 2nd : "=", 3rd : ">"


#Reject expired rules

from datetime import datetime
currentTimeStamp = datetime.now()



for key in rulesJsonData :
 	expiryTimeStamp = datetime.strptime(rulesJsonData[key]['expiry'], "%d/%m/%y %H:%M") 
 	if(currentTimeStamp < expiryTimeStamp):
 		fillRulesForCartTotal(key,rulesJsonData[key]['cartTotal'])
 		fillRulesForCategory(key, rulesJsonData[key]['categoryId'], category_range)

#print "Category Mapping : ", category_mapping
#print "Cart Total Mapping : ", cartTotalMapping





