
class Operations:
    def __init__(self):
        self.__operations__ = dict()
        with open('operations.txt','r') as f:
            operations = f.read()
            for operation in operations.split(','):
                try:
                    name = operation.split(':')[0].strip()
                    define = operation.split(':')[1]
                    # print(f'{name}\t{define}')
                    self.__operations__[name] = define
                except Exception as e:
                    # print(e)
                    pass

    def addOperation(self,name: str, sample: str):
        try:
            a = self.__operations__[name]
            # print('This operation is already defined.')
        except KeyError:
            self.__operations__[name] = sample
            with open('operations.txt','a') as f:
                operation = f'\n{name}:{sample},'
                f.write(operation)
                # print(f'{name} operation is added.')

    def removeOperation(self,index:int):
        print(index)
        names = list(self.__operations__.keys())
        name = names[index]
        try:
            del self.__operations__[name]
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
        return self.__operations__

    def evaluate_expression(self,a:int,b:int,op:str) -> list:
        expression = str(self.__operations__[op])
        expression.replace('a',str(a))
        expression.replace('b',str(b))
        try:
            result = str(eval(expression))
            if result:
                return [1,result]
        except Exception as e:
            return [0,e]
        return [0,result]