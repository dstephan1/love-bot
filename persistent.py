import shelve

d = shelve.open("myshelf", writeback=True)

d["hats"] = 100
d["list"] = [13, 15, 16]
d["list"].append(100)
