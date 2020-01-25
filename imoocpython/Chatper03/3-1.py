lisa = {"name":"lisa","age":23,"weight":53.3}
print(lisa)
w =lisa["weight"]
print(w)
lisa["weight"] = 50.3
print(lisa["weight"])
lisa["birthday"] = "1006-01-03"
print(lisa)
lisa.pop("birthday")
print(lisa)