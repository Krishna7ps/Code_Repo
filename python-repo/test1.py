for f in 'ABC':
    for s in "ABC":
        if f != s:
            for t in 'ABC':
                if f!=t and s!=t:
                    print(f+s+t)