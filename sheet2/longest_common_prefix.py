def longest_common_prefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    for i in range(1, len(strs)):
        while strs[i].find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

if __name__ == "__main__":
    n = int(input("Enter number of strings: "))
    strs = []
    for _ in range(n):
        strs.append(input("Enter string: "))
    print(f"Longest Common Prefix: '{longest_common_prefix(strs)}'")
