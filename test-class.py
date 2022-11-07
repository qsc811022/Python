class IO:
    supporttedSrc=["console","file"]
    def read(src):
        if src not in IO.supporttedSrc:
            print("Not Supported")
        else:
            print("Read from", src)



print(IO.supporttedSrc)

IO.read("file")

IO.read("internet")