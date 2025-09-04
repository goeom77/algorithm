def solution(expressions):
    def plus_n(a, b, n):
        return make_ten_to_n(make_n_to_ten(a, n) + make_n_to_ten(b, n), n)

    def minus_n(a, b, n):
        return make_ten_to_n(make_n_to_ten(a, n) - make_n_to_ten(b, n), n)

    def make_ten_to_n(a, n):
        if a == 0:
            return 0
        result = ""
        while a > 0:
            result = str(a % n) + result
            a //= n
        return int(result)

    def make_n_to_ten(a, n):
        result = 0
        str_a = str(a)
        for i in range(len(str_a)):
            result += int(str_a[-i - 1]) * (n ** i)
        return result

    def check_min(str_a, min_n):
        for ch in str(str_a):
            min_n = max(min_n, int(ch) + 1)
        return min_n

    min_n = 2
    known = []
    unknown = []
    for ex in expressions:
        a, pm, b, _, c = ex.split()
        min_n = check_min(a, min_n)
        min_n = check_min(b, min_n)
        if c == "X":
            unknown.append((a, pm, b, c))
        else:
            min_n = check_min(c, min_n)
            known.append((a, pm, b, c))

    # 가능한 모든 진법 후보군 탐색
    candidates = []
    for n in range(min_n, 10):
        ok = True
        for a, pm, b, c in known:
            if pm == "+":
                if plus_n(int(a), int(b), n) != int(c):
                    ok = False
                    break
            else:
                if minus_n(int(a), int(b), n) != int(c):
                    ok = False
                    break
        if ok:
            candidates.append(n)

    answer = []
    for a, pm, b, c in unknown:
        results = set()
        for n in candidates:
            if pm == "+":
                results.add(plus_n(int(a), int(b), n))
            else:
                results.add(minus_n(int(a), int(b), n))
        if len(results) == 1:  # 후보군에서 모두 같은 결과 → 확정
            result = results.pop()
            answer.append(f"{a} {pm} {b} = {result}")
        else:  # 후보군마다 다르면 모호 → ?
            answer.append(f"{a} {pm} {b} = ?")

    return answer
