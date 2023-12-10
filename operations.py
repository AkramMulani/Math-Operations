
class Operations:
    def __init__(self):
        self._operations_ = dict()
        with open('operations.txt','r') as f:
            operations = f.read()
            for operation in operations.split(','):
                try:
                    name = operation.split(':')[0].strip()
                    define = operation.split(':')[1]
                    self._operations_[name] = define
                except Exception as e:
                    pass

    def addOperation(self,name: str, sample: str):
        try:
            a = self._operations_[name]
        except KeyError:
            self._operations_[name] = sample
            with open('operations.txt','a') as f:
                operation = f'\n{name}:{sample},'
                f.write(operation)

    def removeOperation(self,index:int):
        names = list(self._operations_.keys())
        name = names[index]
        try:
            del self._operations_[name]
            with open('operations.txt','r') as file:
                lines = file.readlines()
            if 0<=index<len(lines):
                del lines[index]
                with open('operations.txt','w') as file:
                    file.writelines(lines)
            return 1
        except:
            return 0

    def getOperations(self) -> dict:
        return self._operations_

    def evaluate_expression(self,a:int,b:int,op:str) -> list:
        expression = str(self._operations_[op])
        expression.replace('a',str(a))
        expression.replace('b',str(b))
        try:
            result = str(eval(expression))
            if result:
                return [1,result]
        except Exception as e:
            return [0,e]
        return [0,result]