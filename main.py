import math
if __name__ == "__main__":
    n = int(input())
    msa = []
    for i in range(n):
        msa.append(input())
    length = len(msa[0])
    final = input()

    # storing possible chars
    chars = []
    for i in msa:
        for j in i:
            if j not in chars:
                chars.append(j)
    for i in final:
        if i not in chars:
            chars.append(i)

    # create matrix of frequencies
    freq = []
    for j in range(len(msa[0])):
        freq.append({})
        for i in range(len(msa)):
            if msa[i][j] in freq[j]:
                freq[j][msa[i][j]] += 1

            else:
                freq[j][msa[i][j]] = 2
    # adding pseudocount
    for i in chars:
        for j in freq:
            if i not in j:
                j[i] = 1
    # calculate score of pseudocount
    for i in freq:
        for j in i:
            i[j] = i[j] / (n + len(chars))

    # calculate overall frequency
    overall_freq = {}
    for i in chars:
        f = 0
        for j in freq:
            if i in j:
                f += j[i]
        overall_freq[i] = f / len(msa[0])

    # dividing freq matrix by overall freq and take log base 2
    for i in freq:
        for j in i:
            i[j] = math.log(i[j]/overall_freq[j], 2)

    max_score = -100000
    max_str = ''
    i = 0
    while i < len(final) - len(msa[0]):
        score = 0
        j = 0
        while j < len(msa[0]):
            score += freq[j][final[i+j]]
            j += 1
        if score > max_score:
            max_score = score
            max_str = final[i:i + len(msa[0])]
        i += 1
    print(max_str)

