
class SumSolution:
    
    def compute(self, x, y):
        if x.isnumeric() and y.isnumeric():
            return int(x) + int(y)
        else:
            raise ValueError("Both inputs must be intergers")

