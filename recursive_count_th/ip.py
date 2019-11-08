def count_th(w):
    count = 0

    def c(w):
        nonlocal count
        s = w.split("th", maxsplit=1)
        try:
            if len(s[1]) == len(w):
                pass
            elif len(s[1]) == 0:
                count += 1
                pass
            else:
                count += 1
                return c(s[1])
        except:
            pass

    c(w)
    return count


count_th("theth")
