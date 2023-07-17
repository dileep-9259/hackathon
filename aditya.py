user_intention = '''{
 "intent": "Search",
 "attributes": {
  "category": "t-shirt",
  "color": "red",
  "fabric": null,
  "occasion": null,
  "sleeve type": null,
  "neck": null,
  "pattern": null,
  "price": null,
  "size": null
 },
 "next_question": "What fabric do you prefer - cotton, cotton blend or polyester?",
 "product_index": null,
 "size_selection": null,
 "address": null
}'''

user_intention = user_intention.replace("null", "None")
user_intention = user_intention.replace("t-shirt", "tshirt")
user_intention = user_intention.replace("t-shirts", "tshirt")
user_intention = user_intention.replace("kurtis", "kurti")

response = eval(user_intention)
keys = response.keys()
output = {}
if (keys.__contains__("attributes")):
    attributes = response["attributes"]
    if (attributes.keys().__contains__("category")):
        output["category"] = attributes["category"]

    if (attributes.keys().__contains__("color")):
        output["color"] = attributes["color"]

    if (attributes.keys().__contains__("fabric")):
        output["fabric"] = attributes["fabric"]

    if (attributes.keys().__contains__("occasion")):
        output["occasion"] = attributes["occasion"]

    if (attributes.keys().__contains__("sleeve type")):
        output["sleeve type"] = attributes["sleeve type"]

    if (attributes.keys().__contains__("neck")):
        output["neck"] = attributes["neck"]

    if (attributes.keys().__contains__("price")):
        output["price"] = attributes["price"]

    if (attributes.keys().__contains__("size")):
        output["size"] = attributes["size"]

print(output)





