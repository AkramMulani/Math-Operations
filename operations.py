
class Operations:
    def __init__(self):
        self._operations_ = dict()
        with open('operations.txt','r') as f:
            operations = f.read()
            for operation in operations.split(','):
                try:
                    name = operation.split(':')[0].strip()
                    define = operation.split(':')[1].replace(',','')
                    self._operations_[name] = define
                except Exception as e:
                    pass
            f.close()

    def addOperation(self,name: str, sample: str):
        try:
            a = self._operations_[name.strip()]
            # if a:
                # print(f'{name} already present in list you can use it')
        except KeyError:
            self._operations_[name.strip()] = sample
            # print(f'{name} added to dictionary')
            with open('operations.txt','a') as f:
                operation = f'\n{name}:{sample},'
                f.write(operation)
                f.close()
                # print('File content added')

    def removeOperation(self,index:int):
        names = list(self._operations_.keys())
        name = names[index]
        try:
            del self._operations_[name.strip()]
            # print(f'{name} deleted from dictionary')
            with open('operations.txt','r') as file:
                lines = file.readlines()
                file.close()
            if 0<=index<len(lines):
                del lines[index]
                with open('operations.txt','w') as file:
                    file.writelines(lines)
                file.close()
                # print('File content removed')
            return 1
        except:
            return 0

    def getOperations(self) -> dict:
        return self._operations_

    def evaluate_expression(self, op, **kwargs) -> list:
        expression = self._operations_[op]
        for key, value in kwargs.items():
            expression = expression.replace(key, str(value))

        try:
            result = eval(expression)
            if result:
                return [1, str(result)]
        except Exception as e:
            return [0, str(e)]
        return [0, str(result)]
