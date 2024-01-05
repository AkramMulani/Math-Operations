from datetime import datetime
import os

class Operations:
    def __init__(self):
        self._operations_ = dict()
        self.file_path = os.getcwd()+'\\operations.txt'
        # print(self.file_path)
        with open(self.file_path,'r') as f:
            operations = f.read()
            for i,operation in enumerate(operations.split(',')):
                try:
                    name = operation.split('/')[0].split(':')[0].strip()
                    define = operation.split('/')[0].split(':')[1]
                    time = self._getTimeFromFile_(i)
                    self._operations_[name] = {'define':define,'time':time}
                except Exception as e:
                    pass
            f.close()

    def _getTimeFromFile_(self,row:int):
        with open(self.file_path,'r') as file:
            lines = file.readlines()[row]
        time = lines.split('/')[1].replace(',','').strip()
        return time

    def addOperation(self,name: str, sample: str):
        try:
            a = self._operations_[name.strip()]
            # if a:
                # print(f'{name} already present in list you can use it')
        except KeyError:
            self._operations_[name.strip()] = {'define':sample,'time':datetime.now().strftime('%Y-%m-%d %H:%M')}
            # print(f'{name} added to dictionary')
            with open(self.file_path,'a') as f:
                operation = f'\n{name}:{sample}/{datetime.now().strftime("%Y-%m-%d %H:%M")},'
                f.write(operation)
                f.close()
                # print('File content added')

    def removeOperation(self,index:int):
        names = list(self._operations_.keys())
        name = names[index]
        try:
            del self._operations_[name.strip()]
            # print(f'{name} deleted from dictionary')
            with open(self.file_path,'r') as file:
                lines = file.readlines()
                file.close()
            if 0<=index<len(lines):
                del lines[index]
                with open(self.file_path,'w') as file:
                    file.writelines(lines)
                file.close()
                # print('File content removed')
            return 1
        except:
            return 0

    def getOperations(self) -> dict:
        return self._operations_

    def evaluate_expression(self, op, **kwargs) -> list:
        expression = self._operations_[op]['define']
        for key, value in kwargs.items():
            expression = expression.replace(key, str(value))

        try:
            result = eval(expression)
            if result is not None:
                return [1, str(result)]
        except Exception as e:
            return [0, str(e)]
        return [0, str(result)]
