
class SumSolution:
    
    def compute(self, x, y):
        if isinstance(x, int) and isinstance(y, int):
            return x + y
        else:
            raise ValueError("Both inputs must be intergers")
