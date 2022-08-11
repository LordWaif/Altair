from rom import rom_generate

def secaoCapitulo(num):
    romano = rom_generate(num)
    return "<p>CAPITULO {} -</p>".format(romano)

def secaoSecao(num):
    romano = rom_generate(num)
    return "<p>SECAO {} -</p>".format(romano)

def secaoNumerica(num):
    return "<p>{}.&nbsp;</p>".format(num)

for i in range(1,11):
    #print(secaoCapitulo(i))
    #print(secaoSecao(i))
    print(secaoNumerica(i))