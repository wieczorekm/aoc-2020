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

current = None
exitedByOverflow = set()

notendingproperly = set()

matchedWith = {}
matchedWith["0"] = rules["0"]
def match(text, rule):
    if len(text) == 0:
        exitedByOverflow.add(current)
        return ""
    if "|" in rule:
        print("\n[{}] split rule for {}".format(text, rule))
        gr = rule.split(" | ")
        for g in gr:
            mtched = match(text, g)
            print("\nin split text: [{}] matched: [{}]".format(text, mtched))
            if mtched != "" and text.startswith(mtched):
                return mtched
        print("returning empty")
        return ""
    elif "\"" not in rule:
        print("\n[{}] multi rule for {}".format(text, rule))
        rlz = rule.split(" ")
        soFar = ""
        for r in rlz:
            if text[len(soFar):] == "":
                if "8" in rlz or "11" in rlz:
                    if r != rlz[-1]:
                        notendingproperly.add(current)
                        print("xxempty {} {}".format(r, rlz))
            matched = match(text[len(soFar):], rules[r])
            if r == "8" or r == "11":
                print("rule: {}, matched: {} ".format(r, matched))
            print("rule: {}, text: {}, soFar: {},  passed:{}, gotten:{}".format(r, text, soFar, text[len(soFar):], matched))
            if matched == "":
                return ""
            matchedWith[r] = rules[r]
            soFar += matched
        print("returning so far " + soFar)
        return soFar

    elif "\"" in rule:
        print("\n[{}] char rule for {}".format(text, rule))
        r = rule[1]
        if text[0] == r:
            return r
        else:
            return ""

    else:
        assert False

cnt = 0
normalExit = set()
for w in words:
    current = w
    m = match(w, rules["0"])
    if m == w:
        cnt += 1
        normalExit.add(current)

print(cnt)
print("exitedByOverflow {}".format(len(exitedByOverflow)))
print("normalExit {}".format(len(normalExit)))
print("union {}".format(len(normalExit | exitedByOverflow)))
print("notedingproperly {}".format(len(notendingproperly)))
print("subtracted {}".format(len((normalExit | exitedByOverflow) - notendingproperly)))

# print(match("aaaabbaaaabbaaa", rules["0"]))
# print(matchedWith)
