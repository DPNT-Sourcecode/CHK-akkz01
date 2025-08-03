from collections import Counter

class CheckoutSolution:
    def checkout(self, skus):
        if not isinstance(skus, str):
            return -1
        
        # Item prices
        prices = {
            'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10,
            'G': 20, 'H': 10, 'I': 35, 'J': 60, 'K': 70, 'L': 90,
            'M': 15, 'N': 40, 'O': 10, 'P': 50, 'Q': 30, 'R': 50,
            'S': 20, 'T': 20, 'U': 40, 'V': 50, 'W': 20, 'X': 17,
            'Y': 20, 'Z': 21
        }

        # Validate input
        if any(c not in prices for c in skus):
            return -1

        count = Counter(skus)
        total = 0

        # --- Apply free item promotions ---
        # 2E -> get one B free
        free_b = count['E'] // 2
        count['B'] = max(0, count['B'] - free_b)

        # 3N -> get one M free
        free_m = count['N'] // 3
        count['M'] = max(0, count['M'] - free_m)

        # 3R -> get one Q free
        free_q = count['R'] // 3
        count['Q'] = max(0, count['Q'] - free_q)

        # F: 2 get 1 free (so for every 3 Fs, pay for 2)
        if count['F'] >= 3:
            num_free = count['F'] // 3
            count['F'] -= num_free

        # U: 3 get 1 free (so for every 4 Us, pay for 3)
        if count['U'] >= 4:
            num_free = count['U'] // 4
            count['U'] -= num_free

        # --- Apply group discounts: STXYZ any 3 for 45 ---
        group_items = ['S', 'T', 'X', 'Y', 'Z']
        group_prices = {k: prices[k] for k in group_items}

        # Create a sorted list of (item, price) in descending order
        group_sorted = sorted(group_prices.items(), key=lambda x: -x[1])
        group_total_items = sum(count[i] for i in group_items)
        group_sets = group_total_items // 3

        for _ in range(group_sets):
            picked = 0
            for item, _ in group_sorted:
                while count[item] > 0 and picked < 3:
                    count[item] -= 1
                    picked += 1
                    if picked == 3:
                        break
            total += 45

        # --- Multibuy offers ---

        # A: 5 for 200, 3 for 130
        q = count['A']
        total += (q // 5) * 200
        q %= 5
        total += (q // 3) * 130
        total += (q % 3) * prices['A']

        # B: 2 for 45
        q = count['B']
        total += (q // 2) * 45
        total += (q % 2) * prices['B']

        # H: 10 for 80, 5 for 45
        q = count['H']
        total += (q // 10) * 80
        q %= 10
        total += (q // 5) * 45
        total += (q % 5) * prices['H']

        # K: 2 for 120
        q = count['K']
        total += (q // 2) * 120
        total += (q % 2) * prices['K']

        # P: 5 for 200
        q = count['P']
        total += (q // 5) * 200
        total += (q % 5) * prices['P']

        # Q: 3 for 80
        q = count['Q']
        total += (q // 3) * 80
        total += (q % 3) * prices['Q']

        # V: 3 for 130, 2 for 90
        q = count['V']
        total += (q // 3) * 130
        q %= 3
        total += (q // 2) * 90
        total += (q % 2) * prices['V']

        # --- Remaining items with no special offer ---
        for item in prices:
            if item in ['A', 'B', 'H', 'K', 'P', 'Q', 'V']:
                continue  # already handled
            total += count[item] * prices[item]

        return total


