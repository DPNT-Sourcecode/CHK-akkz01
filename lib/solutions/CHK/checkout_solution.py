
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        if not isinstance(skus, str):
            return -1  # Illegal input

        # Valid items and prices
        prices = {
            'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10,
            'G': 20, 'H': 10, 'I': 35, 'J': 60, 'K': 70, 'L': 90,
            'M': 15, 'N': 40, 'O': 10, 'P': 50, 'Q': 30, 'R': 50,
            'S': 20, 'T': 20, 'U': 40, 'V': 50, 'W': 20, 'X': 17,
            'Y': 20, 'Z': 21
        }

        valid_skus = set(prices.keys())
        if any(c not in valid_skus for c in skus):
            return -1
        
        from collections import Counter
        sku_count = Counter(skus)
        total = 0

        # --------- Apply Free Item Offers ---------

        # E => get one B free for every two E
        free_b = sku_count['E'] // 2
        sku_count['B'] = max(0, sku_count['B'] - free_b)

        # N => get one M free for every three N
        free_m = sku_count['N'] // 3
        sku_count['M'] = max(0, sku_count['M'] - free_m)

        # R => get one Q free for every three R
        free_q = sku_count['R'] // 3
        sku_count['Q'] = max(0, sku_count['Q'] - free_q)

        # F => get one F free for every two Fs (i.e., for every 3 Fs, pay for 2)
        f_qty = sku_count['F']
        free_f = f_qty // 3
        sku_count['F'] = f_qty - free_f

        # U => get one U free for every 3 Us (i.e., for every 4 Us, pay for 3)
        u_qty = sku_count['U']
        free_u = u_qty // 4
        sku_count['U'] = u_qty - free_u

        # --------- Group Discount (STXYZ) ---------

        group_items = ['S', 'T', 'X', 'Y', 'Z']
        group_price = 45
        group_counter = [(item, prices[item]) for item in group_items]
        total_group_items = sum(sku_count[item] for item in group_items)
        num_groups = total_group_items // 3

        for _ in range(num_groups):
            selected = []
            # pick 3 most expensive items
            for item, _ in sorted(group_counter, key=lambda x: -x[1]):
                while sku_count[item] > 0 and len(selected) < 3:
                    selected.append(item)
                    sku_count[item] -= 1
            total += group_price

        # --------- Apply Multibuy Offers ---------

        # A: 5 for 200, 3 for 130
        a_qty = sku_count['A']
        total += (a_qty // 5) * 200
        a_qty %= 5
        total += (a_qty // 3) * 130
        total += (a_qty % 3) * prices['A']

        # B already handled above (2 for 45)
        b_qty = sku_count['B']
        total += (b_qty // 2) * 45
        total += (b_qty % 2) * prices['B']

        # H: 10 for 80, 5 for 45
        h_qty = sku_count['H']
        total += (h_qty // 10) * 80
        h_qty %= 10
        total += (h_qty // 5) * 45
        total += (h_qty % 5) * prices['H']

        # K: 2 for 150
        k_qty = sku_count['K']
        total += (k_qty // 2) * 150
        total += (k_qty % 2) * prices['K']

        # P: 5 for 200
        p_qty = sku_count['P']
        total += (p_qty // 5) * 200
        total += (p_qty % 5) * prices['P']

        # Q: 3 for 80
        q_qty = sku_count['Q']
        total += (q_qty // 3) * 80
        total += (q_qty % 3) * prices['Q']

        # V: 3 for 130, 2 for 90
        v_qty = sku_count['V']
        total += (v_qty // 3) * 130
        v_qty %= 3
        total += (v_qty // 2) * 90
        total += (v_qty % 2) * prices['V']

        # --------- Add Remaining Items ---------
        for item in prices:
            if item in ['A','B','F','H','K','M','P','Q','R','U','V','S','T','X','Y','Z']:
                continue  # already handled
            total += sku_count[item] * prices[item]

        return total

