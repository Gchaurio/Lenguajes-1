import operator

class Parser(object):

    

    def __init__(self, orden: str, expr: str):
        
        # Se define la cantidad de bloques
        self.orden = orden
        self.expr = expr
        self.ops = {
            '+' : operator.add,
            '-' : operator.sub,
            '*' : operator.mul,
            '/' : operator.truediv
        }

    def parse(self):

        if self.orden == "PRE":

            ope = []
            nums = []
            splitted = self.expr

            for i in range(0,len(splitted)):
                try:
                    num = int(splitted[i])
                    nums.append(num)
                except:
                    ope.append(splitted[i])
                    
            prev = nums[0]

            for i in range(1,len(nums)):
                prev = self.ops[ope[i-1]](prev,nums[i])
            return prev
        
        elif self.orden == "POST":
            
            stack = []

            splitted = self.expr
            for i in range(0,len(splitted)):
                try:
                    num = int(splitted[i])
                    stack.append(num)
                except:
                    op1 = stack.pop()
                    op2 = stack.pop()
                    stack.append(self.ops[splitted[i]](op2,op1))

            return stack.pop()

    def mostrar(self):
        
        out = ""

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

            out += nums[0] + ope[0] + nums[1]

            for i in range(2,len(nums)):

                if ope[i-1] == "*":
                    out = "("+out+")" + ope[i-1] + nums[i]
                else:
                    out = out + ope[i-1] + nums[i]

            out = " ".join(out)
            out = out.replace("( ","(")
            out = out.replace(" )",")")


            return out.strip()
        
        elif self.orden == "POST":
            
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




            

            
            

                
