with open('day19.in') as f:
    lines = [line.rstrip() for line in f]

rules = {}
words = []

readingWords = False
for l in lines:
    if readingWords:
        words.append(l)
    else:
        if not l.strip():
            readingWords = True
        else:
            a = l.split(": ")
            rules[a[0]] = a[1]

print(rules)
print(words)

def match(text, rule):
    if "|" in rule:
        #print("\n[{}] split rule for {}".format(text, rule))
        gr = rule.split(" | ")
        for g in gr:
            mtched = match(text, g)
            #print("\nin split text: [{}] matched: [{}]".format(text, mtched))
            if mtched != "" and text.startswith(mtched):
                return mtched
        #print("returning empty")
        return ""
    elif "\"" not in rule:
        #print("\n[{}] multi rule for {}".format(text, rule))
        rlz = rule.split(" ")
        soFar = ""
        for r in rlz:
            matched = match(text[len(soFar):], rules[r])
            #print("rule: {}, text: {}, soFar: {},  passed:{}, gotten:{}".format(r, text, soFar, text[len(soFar):], matched))
            if matched == "":
                return ""
            soFar += matched
        #print("returning so far " + soFar)
        return soFar

    elif "\"" in rule:
        #print("\n[{}] char rule for {}".format(text, rule))
        r = rule[1]
        if text[0] == r:
            return r
        else:
            return ""

    else:
        assert False

cnt = 0
for w in words:
    m = match(w, rules["0"])
    if m == w:
        cnt += 1

print(cnt)
