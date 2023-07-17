if(indexx==1):
    response = '''{
         "intent": "Search",
         "attributes": {
          "category": "kurti",
          "color": "red",
          "fabric": None,
          "occasion": None,
          "sleeve type": None,
          "neck": None,
          "pattern": None,
          "price": None,
          "size": None
         },
         "next_question": "What fabric do you prefer - cotton, cotton blend or polyester?",
         "product_index": None,
         "size_selection": None,
         "address": None
        }'''
elif (indexx ==2):
    response = '''{
         "intent": "Search",
         "attributes": {
          "category": "kurti",
          "color": "red",
          "fabric": "cotton",
          "occasion": None,
          "sleeve type": None,
          "neck": None,
          "pattern": None,
          "price": None,
          "size": None
         },
         "next_question": "Did you like any thing or you want to see few more?",
         "product_index": None,
         "size_selection": None,
         "address": None
        }'''
elif (indexx==3):
    response = '''{
         "intent": "scroll down",
         "attributes": {
          "category": "kurti",
          "color": "red",
          "fabric": "cotton",
          "occasion": None,
          "sleeve type": None,
          "neck": None,
          "pattern": None,
          "price": None,
          "size": None
         },
         "next_question": "Did you find anything looking for?",
         "product_index": None,
         "size_selection": None,
         "address": None
        }'''
elif (indexx==4):
    response = '''{
         "intent": "pick",
         "attributes": {
          "category": "kurti",
          "color": "red",
          "fabric": "cotton",
          "occasion": None,
          "sleeve type": None,
          "neck": None,
          "pattern": None,
          "price": None,
          "size": None
         },
         "next_question": "What is the size you want to buy?",
         "product_index": 2,
         "size_selection": None,
         "address": None
        }'''
elif (indexx==5):
    response = '''{
         "intent": "size_selection",
         "attributes": {
          "category": "kurti",
          "color": "red",
          "fabric": "cotton",
          "occasion": None,
          "sleeve type": None,
          "neck": None,
          "pattern": None,
          "price": None,
          "size": None
         },
         "next_question": "On which of the saved adresses you want to get this delivered?",
         "product_index": None,
         "size_selection": "M",
         "address": None
        }'''
elif (indexx==6):
    response = '''{
         "intent": "ADDRESS",
         "attributes": {
          "category": "kurti",
          "color": "red",
          "fabric": "cotton",
          "occasion": None,
          "sleeve type": None,
          "neck": None,
          "pattern": None,
          "price": None,
          "size": None
         },
         "next_question": "Would you like to pay cash on delivery?",
         "product_index": None,
         "size_selection": None,
         "address": 1
        }'''
elif (indexx==7):
    response = '''{
         "intent": "PLACE_ORDER",
         "attributes": {
          "category": "kurti",
          "color": "red",
          "fabric": "cotton",
          "occasion": None,
          "sleeve type": None,
          "neck": None,
          "pattern": None,
          "price": None,
          "size": None
         },
         "next_question": "Would you like to pay cash on delivery?",
         "product_index": None,
         "size_selection": None,
         "address": 1
        }'''
else :
    response = '''{
         "intent": "EXIT",
         "attributes": {
          "category": "kurti",
          "color": "red",
          "fabric": "cotton",
          "occasion": None,
          "sleeve type": None,
          "neck": None,
          "pattern": None,
          "price": None,
          "size": None
         },
         "next_question": "Would you like to pay cash on delivery?",
         "product_index": None,
         "size_selection": None,
         "address": 1
        }'''