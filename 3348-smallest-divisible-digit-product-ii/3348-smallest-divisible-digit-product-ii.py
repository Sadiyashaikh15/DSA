class Solution:

    def smallestNumber(self, num: str, t: int) -> str:
        # Step 1: Factorize t into prime factors 2, 3, 5, 7
        temp = t
        counts = {2: 0, 3: 0, 5: 0, 7: 0}
        for p in (2, 3, 5, 7):
            while temp % p == 0:
                counts[p] += 1
                temp //= p

        # If t has any prime factors other than 2, 3, 5, 7, it's impossible
        if temp > 1:
            return "-1"

        a, b, c, d = counts[2], counts[3], counts[5], counts[7]

        # Helper to get prime factors of a single digit 1..9
        def get_digit_factors(digit):
            f = [0, 0, 0, 0]
            val = digit
            for idx, p in enumerate((2, 3, 5, 7)):
                while val % p == 0:
                    f[idx] += 1
                    val //= p
            return f

        digit_f = {dig: get_digit_factors(dig) for dig in range(1, 10)}

        # Helper to find the minimal multiset of digits required for remaining prime counts
        def get_min_digits(req_a, req_b, req_c, req_d):
            req_a = max(0, req_a)
            req_b = max(0, req_b)
            req_c = max(0, req_c)
            req_d = max(0, req_d)

            best_res = None

            # Try different counts of digit '6' (combining one 2 and one 3)
            for num_6 in range(3):
                rem_a = max(0, req_a - num_6)
                rem_b = max(0, req_b - num_6)

                num_8 = rem_a // 3
                rem_a_mod = rem_a % 3
                num_4 = 1 if rem_a_mod == 2 else 0
                num_2 = 1 if rem_a_mod == 1 else 0

                num_9 = rem_b // 2
                num_3 = rem_b % 2

                num_5 = req_c
                num_7 = req_d

                digits = []
                digits.extend([2] * num_2)
                digits.extend([3] * num_3)
                digits.extend([4] * num_4)
                digits.extend([5] * num_5)
                digits.extend([6] * num_6)
                digits.extend([7] * num_7)
                digits.extend([8] * num_8)
                digits.extend([9] * num_9)

                digits.sort()

                if best_res is None:
                    best_res = digits
                else:
                    if len(digits) < len(best_res):
                        best_res = digits
                    elif len(digits) == len(best_res) and digits < best_res:
                        best_res = digits

            return best_res

        n = len(num)

        # Step 2: Precompute prefix prime factor counts
        pref = [None] * (n + 1)
        pref[0] = (0, 0, 0, 0)
        has_zero = False
        for i in range(n):
            if num[i] == "0" or has_zero:
                has_zero = True
                pref[i + 1] = None
            else:
                f = digit_f[int(num[i])]
                pref[i + 1] = (
                    pref[i][0] + f[0],
                    pref[i][1] + f[1],
                    pref[i][2] + f[2],
                    pref[i][3] + f[3],
                )

        # Step 3: Check if num itself is valid
        if pref[n] is not None:
            pa, pb, pc, pd = pref[n]
            if pa >= a and pb >= b and pc >= c and pd >= d:
                return num

        # Step 4: Search for Case 1 (same length n)
        for i in range(n - 1, -1, -1):
            if pref[i] is None:
                continue

            pa, pb, pc, pd = pref[i]
            cur_digit = int(num[i])

            for d_digit in range(cur_digit + 1, 10):
                df = digit_f[d_digit]
                rem_a = a - pa - df[0]
                rem_b = b - pb - df[1]
                rem_c = c - pc - df[2]
                rem_d = d - pd - df[3]

                min_digits = get_min_digits(rem_a, rem_b, rem_c, rem_d)
                rem_len = n - 1 - i

                if len(min_digits) <= rem_len:
                    ones_count = rem_len - len(min_digits)
                    return (
                        num[:i]
                        + str(d_digit)
                        + ("1" * ones_count)
                        + "".join(map(str, min_digits))
                    )

        # Step 5: Case 2 (length > n)
        min_digits = get_min_digits(a, b, c, d)
        target_len = max(n + 1, len(min_digits))
        ones_count = target_len - len(min_digits)
        return ("1" * ones_count) + "".join(map(str, min_digits))