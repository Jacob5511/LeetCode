class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        pref = strs[0]
        for i in strs[1:]:
            while not i.startswith(pref):
                pref = pref[:-1]
                if not pref:
                    return ''
        return pref
