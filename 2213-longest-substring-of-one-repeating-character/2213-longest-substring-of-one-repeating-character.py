class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):

        n = len(s)
        tree = [None] * (4 * n)

        # node = (left_char, right_char,
        #         left_run, right_run, max_run, length)

        def merge(a, b):
            if a is None:
                return b
            if b is None:
                return a

            lc1, rc1, ll1, rl1, mx1, len1 = a
            lc2, rc2, ll2, rl2, mx2, len2 = b

            left_char = lc1
            right_char = rc2

            left_run = ll1
            right_run = rl2

            max_run = max(mx1, mx2)

            if rc1 == lc2:
                max_run = max(max_run, rl1 + ll2)

                # Entire left segment is one character
                if ll1 == len1:
                    left_run = len1 + ll2

                # Entire right segment is one character
                if rl2 == len2:
                    right_run = len2 + rl1

            return (
                left_char,
                right_char,
                left_run,
                right_run,
                max_run,
                len1 + len2
            )

        def build(node, l, r):
            if l == r:
                ch = s[l]
                tree[node] = (ch, ch, 1, 1, 1, 1)
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, l, r, idx, ch):
            if l == r:
                tree[node] = (ch, ch, 1, 1, 1, 1)
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, ch)
            else:
                update(node * 2 + 1, mid + 1, r, idx, ch)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        build(1, 0, n - 1)

        ans = []

        for ch, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, ch)
            ans.append(tree[1][4])

        return ans