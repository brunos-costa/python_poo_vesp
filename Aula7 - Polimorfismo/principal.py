from produto import Produto, Eletronico

prod1 = Produto("ARmário",758.99)
eletro1 = Eletronico("Smartphone", 1544.99, 220)

prod1.descrever()
prod1.calcularDesconto(10)

eletro1.descrever()
eletro1.calcularDesconto(30)