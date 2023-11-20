import operator

# Clase con el manejador de expresiones.
class Parser(object):

    
    # Inicializamos definiendo las operaciones que leera, asi como el orden y la expresion
    def __init__(self, orden: str, expr: str):
        
        self.orden = orden
        self.expr = expr
        self.ops = {
            '+' : operator.add,
            '-' : operator.sub,
            '*' : operator.mul,
            '/' : operator.truediv
        }

    # Funcion que parsea la expresion apra devolver el resultado.
    def parse(self):

        # Si es PRE
        if self.orden == "PRE":
            
            ope = []
            nums = []
            splitted = self.expr

            # Recojemos los numeros y signos
            for i in range(0,len(splitted)):
                try:
                    num = int(splitted[i])
                    nums.append(num)
                except:
                    ope.append(splitted[i])
                    
            prev = nums[0]

            # Operamos en orden, almacenando siempre los resultados
            for i in range(1,len(nums)):
                prev = self.ops[ope[i-1]](prev,nums[i])

            # Devolvemos el resultado final.
            return prev
        
        # Si es POST
        elif self.orden == "POST":
            
            # Creamos una pila
            stack = []

            splitted = self.expr

            # Agregamos valores a la pila, cuando se encuentre un operando, se opera y se almacena en pila
            for i in range(0,len(splitted)):
                try:
                    num = int(splitted[i])
                    stack.append(num)
                except:
                    op1 = stack.pop()
                    op2 = stack.pop()
                    stack.append(self.ops[splitted[i]](op2,op1))

            # Devolvemos el resultado final.
            return stack.pop()

    # Funcion que muestra una representacion de la operacion en el orden matematico
    def mostrar(self):
        
        out = ""

        # Si es pre
        if self.orden == "PRE":

            ope = []
            nums = []
            splitted = self.expr

            for i in range(0,len(splitted)):
                try:
                    num = int(splitted[i])
                    nums.append(splitted[i])
                except:
                    ope.append(splitted[i])

            # Vamos agregando en orden los valore sy sus operandos
            out += nums[0] + ope[0] + nums[1]

            # En caso de haber signo de multiplicacion, vamos parentizando la operacion que llevamos. Agregamos siempre la string vacio en orden.
            for i in range(2,len(nums)):

                if ope[i-1] == "*":
                    out = "("+out+")" + ope[i-1] + nums[i]
                else:
                    out = out + ope[i-1] + nums[i]

            out = " ".join(out)
            out = out.replace("( ","(")
            out = out.replace(" )",")")


            return out.strip()
        
        # Si es post
        elif self.orden == "POST":
            
            # Vamos operando nuevamente en stack pero ahora no se guarda el resultado de la operacion, si no el string de la operacion, por lo que se van agregando en orden todas 
            # Las operaciones
            stack = []

            splitted = self.expr
            for i in range(0,len(splitted)):
                try:
                    num = int(splitted[i])
                    stack.append(str(num))
                except:
                    op1 = stack.pop()
                    op2 = stack.pop()
                    if splitted[i] == "*":
                        stack.append(op2+splitted[i]+"("+op1+")")
                    else:
                        stack.append(op2+splitted[i]+op1)

            out = stack.pop()
            out = " ".join(out)
            out = out.replace("( ","(")
            out = out.replace(" )",")")

            return out




            

            
            

                
