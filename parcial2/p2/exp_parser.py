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

            print(nums)
            print(ope)

            prev = nums[0]

            for i in range(1,len(nums)):

                prev = self.ops[ope[i-1]](prev,nums[i])

            return prev
        
        elif self.orden == "POST":
            pass




            

            
            

                
