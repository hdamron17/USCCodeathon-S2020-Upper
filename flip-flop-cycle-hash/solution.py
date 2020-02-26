import string

def ds_to_str(ds, b):
    return ''.join([(string.digits + string.ascii_uppercase)[i] for i in ds])

def str_to_ds(s):
    return tuple(int(x, 36) for x in s)

def n_to_ds(n, b):
    if n == 0:
        return tuple([0])
    digits = []
    while n:
        digits.append(n % b)
        n //= b
    return tuple(digits[::-1])

def kaprekar(ds, b):
    alpha = int(ds_to_str(sorted(ds), b), b)
    beta = int(ds_to_str(sorted(ds, reverse=True), b), b)
    nds = n_to_ds(beta - alpha, b)
    nds = tuple(([0] * (len(ds) - len(nds))) + list(nds))
    return nds

def kaprekar_k(n_str, b, k, brute=False):
    ds = str_to_ds(n_str)

    if brute:
        for _ in range(k):
            ds = kaprekar(ds, b)
        return ds_to_str(ds, b)

    seen = set()
    sequence = []
    for _ in range(k):
        ds = kaprekar(ds, b)
        if not any(ds):
            return ds_to_str(ds, b)
        if ds in seen:
            repeat_i = sequence.index(ds)
            repeat_len = len(sequence) - repeat_i
            kp = k - repeat_i - 1
            ret_i = kp % repeat_len
            return ds_to_str(sequence[repeat_i + ret_i], b)  # TODO fix

        seen.add(ds)
        sequence.append(ds)
    return ds_to_str(ds, b)

# Format "k b n" describing the kth application of Kaprekar's routine to n with base b
# Note: n is given in base b using 0-9, A-Z
if __name__ == "__main__":
    k, b, n = input().split()
    k = int(k)
    b = int(b)
    print(kaprekar_k(n, b, k))
