
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):

        if not isinstance(skus, str):
            return -1 #Illegal Input 
        
        valid_skus = set('ABCDE')
        if any(c not in valid_skus for c in skus):
            return -1
        
        prices = {
            'A': 50,
            'B': 30,
            'C': 20,
            'D': 15,
            'E': 40
        }
        total = 0 

        # Count SKUs 
        from collections import Counter

        sku_count = Counter(skus)

        # Apply this week's discounts 
        if sku_count['A'] >= 3:
            total += (sku_count['A'] // 3) * 130 + (sku_count['A'] % 3) * prices['A']
        else:
            total += sku_count['A'] * prices['A']
        
        #if sku_count['B'] >= 2:
         #   total += (sku_count['B'] // 2) * 45 + (sku_count['B'] % 2) * prices['B']
        #else:
         #   total += sku_count['B'] * prices['B']

        # Always add price for E
        total += sku_count['E'] * prices['E']

        # Calculate free B from E
        free_b = min(sku_count['B'], sku_count['E'] // 2)
        b_to_pay = sku_count['B'] - free_b
        total += (b_to_pay // 2) * 45 + (b_to_pay % 2) * prices['B']


        total += sku_count['C'] * prices['C']
        total += sku_count['D'] * prices['D']   

        return total 

