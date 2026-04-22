sz = getOutputSize()
lst = []
for i in irange(sz):
    r = json_parse(getOutputDataValue(i))
    for u in r:
        if "bad_nlu" in u:
            a = u["bad_xnu"]
            try:
                a = json_parse(a)
                u["bad_xnu"] = a
            except:
                println("Erreur:", i)
    lst.append(r)
