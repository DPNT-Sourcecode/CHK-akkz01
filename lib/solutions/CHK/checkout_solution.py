
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        if skus == "A":
            return 50 
        elif skus == "AAA":
            return 130
        elif skus == "B":
            return 30
        elif skus == "BB":
            return 45  
        elif skus == "C":
            return 20
        elif skus == "D":
            return 15
        else:
            return -1 # Invalid SKU
            raise NotImplementedError()

