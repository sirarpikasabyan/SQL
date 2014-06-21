f = open("abc.txt", "wt", encoding="utd-8")
f.write("Imagine non=English language here ")
f.close()

text = open("abc.txt", encoding="utf-8").read()
