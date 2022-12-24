import marshal
file ='new'
oo =open(file,"r").read()
com =compile(oo,'','exec')
xx=marshal.dumps(com)
cod=open(str(file),"w")
cod.write("import marshal\n")
cod.write('exec(marshal.loads('+repr(xx)+'))')

