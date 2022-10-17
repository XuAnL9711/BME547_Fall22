import requests

# r = requests.get("https://api.github.com/repos/dward2/BME547/brasfefnches")
# print(r)
# print(type(r))
# print(r.text)
# answer = r.json()
# print(type(answer))
# for branch in answer:
#     print(branch["name"])


# output_info = {"name": "Xuan Liu",
#                 "net_id": "xl353",
#                 "e-mail": "xuan.liu115@duke.edu"}

output_info = {"user": "Xuan Liu",
                "message": "Here is another test!"}

r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message", json=output_info)
print(r)
print(r.text)

r2 = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/Xuan Liu")
print(r2.text)