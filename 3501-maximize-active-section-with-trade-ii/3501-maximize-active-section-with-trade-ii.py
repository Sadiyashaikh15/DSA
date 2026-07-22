class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries):
        ones = s.count('1')

        # 1. Run-length encode the zero-groups
        starts, lengths = [], []
        zgi = [-1] * len(s)          # zgi[i] = index of most-recent zero-group starting at/before i
        for i, ch in enumerate(s):
            if ch == '0':
                if i > 0 and s[i - 1] == '0':
                    lengths[-1] += 1
                else:
                    starts.append(i)
                    lengths.append(1)
            zgi[i] = len(starts) - 1

        if not starts:                        # no '0' anywhere -> no trade ever possible
            return [ones] * len(queries)

        # 2. pairSums + sparse table for O(1) range-max
        pairSums = [lengths[i] + lengths[i + 1] for i in range(len(starts) - 1)]
        if pairSums:
            st, k = [pairSums[:]], 1
            while (1 << k) <= len(pairSums):
                prev, half = st[-1], 1 << (k - 1)
                st.append([max(prev[j], prev[j + half]) for j in range(len(pairSums) - (1 << k) + 1)])
                k += 1
            log2 = [0] * (len(pairSums) + 1)
            for i in range(2, len(log2)):
                log2[i] = log2[i // 2] + 1

            def rangeMax(l, r):
                k = log2[r - l + 1]
                return max(st[k][l], st[k][r - (1 << k) + 1])
        else:
            def rangeMax(l, r):
                return 0

        ans = []
        for l, r in queries:
            gl, gr = zgi[l], zgi[r]
            left  = (lengths[gl] - (l - starts[gl])) if s[l] == '0' else -1
            right = (r - starts[gr] + 1)              if s[r] == '0' else -1

            SG = gl + 1
            EG = gr if s[r] == '1' else gr - 1        # last fully-contained zero-group

            best = ones
            if s[l] == '0' and s[r] == '0' and gl + 1 == gr:      # single 1-block between two partial groups
                best = max(best, ones + left + right)
            elif SG <= EG - 1:                                     # both neighbors fully contained
                best = max(best, ones + rangeMax(SG, EG - 1))

            if s[l] == '0' and SG <= EG:                           # X = first block after l's partial group
                best = max(best, ones + left + lengths[SG])
            if s[r] == '0' and gl < gr - 1:                        # X = last block before r's partial group
                best = max(best, ones + right + lengths[gr - 1])

            ans.append(best)

        return ans