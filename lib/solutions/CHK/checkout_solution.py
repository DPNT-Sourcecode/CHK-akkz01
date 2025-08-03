
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
            'K': 80,
            'L': 90,
            'M': 15,
            'N': 40,
            'O': 10,
            'P': 50,
            'Q': 30,
            'R': 50,
            'S': 30,
            'T': 20,
            'U': 40,
            'V': 50,
            'W': 20,
            'X': 90,
            'Y': 10,
            'Z': 50
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

        # Handle H discounts: apply 5-for-200 first, then 3-for-130
        h_qty = sku_count['H']
        total += (h_qty // 10) * 80
        a_qty %= 5
        total += (h_qty // 5) * 45
        total += (h_qty % 5) * prices['H']

        # Handle K discounts 
        k_qty = sku_count['K']
        total += (k_qty // 2) * 150
        total += (k_qty % 2) * prices['K']

        # Hande M discounts
        m_qty = sku_count['M']
        free_m = m_qty // 4
        paid_m = m_qty - free_m
        total += paid_m * prices['M']

        # Handle P discounts
        p_qty = sku_count['P']
        total += (p_qty // 5) * 200
        total += (p_qty % 5) * prices['P']

        # Handle Q discounts
        q_qty = sku_count['Q']
        total += (q_qty // 3) * 80
        total += (q_qty % 3) * prices['Q']

        # Handle R discounts
        r_qty = sku_count['R']
        free_r = r_qty // 4
        paid_r = r_qty - free_r
        total += paid_r * prices['R']

        # Handle U discounts
        u_qty = sku_count['U']
        free_u = u_qty // 4
        paid_u = u_qty - free_u
        total += paid_u * prices['U']

        # Handle V discounts
        u_qty = sku_count['U']
        total += (u_qty // 3) * 130
        u_qty %= 2
        total += (u_qty // 2) * 90
        total += (u_qty % 2) * prices['H']

        # C and D have no offers
        total += sku_count['C'] * prices['C']
        total += sku_count['D'] * prices['D']
        total += sku_count['E'] * prices['E']

        return total

