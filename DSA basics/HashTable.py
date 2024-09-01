# Insert Lock up and remove

def encode(strs:list[str]):
    strin_encoded = ""
    encode_hash = {}
    for i in range(len(strs)):
        encode_hash[i] = len(strs[i])
        strin_encoded += strs[i] 
    
    return (strin_encoded,encode_hash)

class Solution:
    
    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        print(res)
        return res

    def decode(self, s: str) -> list[str]:
        res = []
        i=0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            print("After traversing {} and {} are i and j".format(i,j))
            length = int(s[i:j])
            print("and length would be {}".format(length))
            i = j + 1
            j = i + length
            print("After moving pointers i is {} and j is {} in {}".format(i,j,s))
            res.append(s[i:j])
            i = j
        print(res)
        return res

obj = Solution()
res = obj.encode(["neet","code","love","you"])
obj.decode(res)