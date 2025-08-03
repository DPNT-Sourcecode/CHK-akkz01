
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        if not isinstance(skus, str):
            return -1  # Illegal Input

        valid_skus = set('ABCDEF')
        if any(c not in valid_skus for c in skus):
            return -1

        prices = {
            'A': 50,
            'B': 30,
            'C': 20,
            'D': 15,
            'E': 40,
            'F': 10
        }

        from collections import Counter
        sku_count = Counter(skus)
        total = 0

        # Handle A discounts: apply 5-for-200 first, then 3-for-130
        a_qty = sku_count['A']
        total += (a_qty // 5) * 200
        a_qty %= 5
        total += (a_qty // 3) * 130
        total += (a_qty % 3) * prices['A']

        # Apply E free B offer: For every 2 E, get one B free
        free_b = sku_count['E'] // 2
        effective_b = max(0, sku_count['B'] - free_b)

        # Apply F free F offer: For every 2 F, get one F free
        f_qty = sku_count['F']
        free_f = f_qty // 3 
        paid_f = f_qty - free_f
        total += paid_f * prices['F']

        # Apply B discount: 2 for 45
        total += (effective_b // 2) * 45
        total += (effective_b % 2) * prices['B']

        # C and D have no offers
        total += sku_count['C'] * prices['C']
        total += sku_count['D'] * prices['D']
        total += sku_count['E'] * prices['E']

        return total
