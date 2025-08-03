
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        if not isinstance(skus, str):
            return -1  # Illegal Input

        valid_skus = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        if any(c not in valid_skus for c in skus):
            return -1

        prices = {
            'A': 50,
            'B': 30,
            'C': 20,
            'D': 15,
            'E': 40,
            'F': 10, 
            'G': 20,
            'H': 10,
            'I': 35,
            'J': 60,
            'K': 70,
            'L': 90,
            'M': 15,
            'N': 40,
            'O': 10,
            'P': 50,
            'Q': 30,
            'R': 50,
            'S': 20,
            'T': 20,
            'U': 40,
            'V': 50,
            'W': 20,
            'X': 17,
            'Y': 20,
            'Z': 21
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

        # Apply B discount: 2 for 45
        total += (effective_b // 2) * 45
        total += (effective_b % 2) * prices['B']

        # Apply F free F offer: For every 2 F, get one F free
        f_qty = sku_count['F']
        free_f = f_qty // 3 
        paid_f = f_qty - free_f
        total += paid_f * prices['F']

        # Handle H discounts: apply 5-for-200 first, then 3-for-130
        h_qty = sku_count['H']
        total += (h_qty // 10) * 80
        h_qty %= 10
        total += (h_qty // 5) * 45
        total += (h_qty % 5) * prices['H']

        # Handle K discounts 
        k_qty = sku_count['K']
        total += (k_qty // 2) * 150
        total += (k_qty % 2) * prices['K']

        # Hande N discounts
        free_m = sku_count['N'] // 3
        effective_m = max(0, sku_count['M'] - free_m)
        total += effective_m * prices['M']

        # Handle P discounts
        p_qty = sku_count['P']
        total += (p_qty // 5) * 200
        total += (p_qty % 5) * prices['P']

        # Handle R discounts
        free_q = sku_count['R'] // 3
        effective_q = max(0, sku_count['Q'] - free_q)
        total += (effective_q // 3) * 80
        total += (effective_q % 3) * prices['Q']

        # Handle Q discounts
        #q_qty = sku_count['Q']
        #total += (q_qty // 3) * 80
        #total += (q_qty % 3) * prices['Q']

        # Handle U discounts
        u_qty = sku_count['U']
        free_u = u_qty // 4
        paid_u = u_qty - free_u
        total += paid_u * prices['U']

        # Handle V discounts
        v_qty = sku_count['V']
        total += (v_qty // 3) * 130
        v_qty %= 3
        # For V, apply 2-for-90 offer
        total += (v_qty // 2) * 90
        total += (v_qty % 2) * prices['V']

        # Handle STXYZ discounts 
        grouped_skus = ['S', 'T', 'X', 'Y', 'Z']
        grouped_sku_prices = {
            'S': 20,
            'T': 20,
            'X': 17,
            'Y': 20,
            'Z': 21
        }
        grouped_sku_count = {sku: sku_count[sku] for sku in grouped_skus}
        total_group_count = sum(grouped_sku_count.values())
        grouped_discounted_sets = total_group_count // 3
        total += grouped_discounted_sets * 45  # 3 for 45 offer

        # Removed remaining grouped skus from total after applying offer 
        # Take out the most expensive sku firt 
        sorted_skus = sorted(grouped_skus, key=lambda sku: -grouped_sku_prices[sku])
        sku_to_remove = grouped_discounted_sets * 3
        for sku in sorted_skus:
            remove = min(sku_to_remove, grouped_sku_count[sku])
            sku_count[sku] -= remove
            sku_to_remove -= remove
            if sku_to_remove <= 0:
                break

        # Add remaining grouped skus to total
        for sku in grouped_skus:
            total += sku_count[sku] * grouped_sku_prices[sku]

        # SKUs with no offers
        total += sku_count['C'] * prices['C']
        total += sku_count['D'] * prices['D']
        total += sku_count['E'] * prices['E']
        total += sku_count['G'] * prices['G']
        total += sku_count['I'] * prices['I']
        total += sku_count['J'] * prices['J']
        total += sku_count['L'] * prices['L']
        total += sku_count['N'] * prices['N']
        total += sku_count['O'] * prices['O']
        total += sku_count['R'] * prices['R']
        total += sku_count['U'] * prices['U']
        total += sku_count['W'] * prices['W']

        return total

