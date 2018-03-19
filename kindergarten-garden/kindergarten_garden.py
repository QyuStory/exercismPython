dic = {'G': 'Grass', 'C': 'Clover', 'R': 'Radishes', 'V': 'Violets'}

class Garden(object):

    def __init__(self, diagram, students=['Alice', 'Bob', 'Charlie', 'David', 
            'Eve', 'Fred', 'Ginny', 'Harriet', 
            'Ileana', 'Joseph', 'Kincaid', 'Larry']):
        self.diagram = diagram.split("\n")
        self.students = sorted(students)

    def plants(self,  name):
       idx = self.students.index(name)
       result = ''
       for elem in self.diagram:
            result += elem[idx*2: idx*2 + 2]
       return [dic.get(x) for x in result]

