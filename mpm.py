__author__ = 'abg'

"""
Program to play a particular method.
Converts the documented order lists into lists of changes,
notated as X = swap and | = lie.
Plain hunt would be (XXX,|XX|) repeated continously.
"""

lead6_order = [
    123456,
    213465,
    231456,
    324165,
    342615,
    432651,
    423561,
    245316,
    254136,
    521463,
    512643,
    156234,
    152643,
]
lead4_order = [
    152643,
    512634,
    521643,
    256134,
    265314,
    625341,
    652431,
    564213,
    546123,
    451632,
    415362,
    143526,
    145362,
]
lead5_order = [
    145362,
    415326,
    451362,
    543126,
    534216,
    354261,
    345621,
    436512,
    463152,
    641325,
    614235,
    162453,
    164235,
]
lead2_order = [
    164235,
    614253,
    641235,
    462153,
    426513,
    246531,
    264351,
    623415,
    632145,
    361254,
    316524,
    135642,
    136524,
]
lead3_order = [
    136524,
    316542,
    361524,
    635142,
    653412,
    563421,
    536241,
    352614,
    325164,
    231546,
    213456,
    124365,
    123456,
]
leads = [lead6_order, lead4_order, lead5_order, lead2_order, lead3_order]

plain_order = [
    # 512643,
    156234,
    152643,
    # 512634,
]

bob_order = [
    #512643,
    156234,
    165243,
    #615234,
]

single_order = [
    #512643,
    156234,
    156243,
    #516234,
]

N = 6
PLACE_RANGE = range(0, N)


def zeros(n):
    a = list()
    for i in range(0, n):
        a.append(0)
    return a


def order_to_places(order):
    """
    converts a series of decimal numbers,
    as the place order in decimal notation, to a 2d array of individual bell places
    :param order: list of integer bell orders
    :return: array or places to write to
    """
    places = []
    for ch in order:
        # print "order =",ch
        pl = zeros(N)
        i = 5
        while ch > 0:
            p2 = int(ch / 10)
            p3 = p2 * 10
            p = ch - p3
            ch = p2
            # print "place =",p
            pl[i] = p
            i -= 1
        places.append(pl)
    return places

def print_notes(n):
    for e in n:
        str = ""
        for s in e:
            str += s
        print str


def lead_to_changes(lead):
    """
    takes a list of orders, as a lead end, and translates into a list of changes.
    :param lead:
    :return: changes
    """
    changes = []
    pls = order_to_places(lead)
    n = len(pls)
    for i in range(1, n):
        now = pls[i]
        prev = pls[i - 1]
        # print "change\n\t",prev, "->\n\t", now
        note = calc_change(prev, now)
        changes.append(note)
    return changes


def calc_change(prev, now):
    """
    calculate the change notation for a pair of places
    :param prev:  places before
    :param now:   places after change
    :return: note string.
    """
    m = len(prev)
    note = []
    pl = 0
    while pl < m:
        if prev[pl] == now[pl]:
            note.append("|")
        elif prev[pl] == now[pl + 1] and prev[pl + 1] == now[pl]:
            note.append("X")
            pl += 1
        else:
            print "illegal change", prev[pl], now[pl + 1], prev[pl + 1], now[pl]
        pl += 1
    return note


def check_leads(leads):
    """
    Checks the members of leads to see that they all have the same set of changes.
    :return:
    """
    ch_set = []
    for lead in leads:
        ch = lead_to_changes(lead)
        ch_set.append(ch)
    nx = len(ch_set)
    ny = len(ch_set[0])
    ok = 0
    bad = 0
    done = 0
    for x in range(1, nx):
        for y in range(0, ny):
            done += 1
            if ch_set[x][y] != ch_set[x - 1][y]:
                bad += 1
            else:
                ok += 1
    if bad > 0:
        print ok, "/", done, " good, ", bad, "/", done, " bad"
    return bad == 0


def swap(p, index):
    """
    swap elements [index] and [index+1] of p
    :param p:
    :param index:
    :return: modified p
    """
    tmp = p[index]
    p[index] = p[index + 1]
    p[index + 1] = tmp
    return p


def do_change(pin, pout, change):
    """
    interpret one change string and apply to place in to make place out
    :param in: places before
    :param out: places after
    :param change: change string.
    :return:
    """
    i = 0
    print "before", pin, "change", change
    for c in change:
        if i == N:
            return
        print c
        if c == 'X':
            pout = swap(pin, i)
            i += 2
        elif c == '|':
            i += 1
        else:
            print "ERROR bad change symbol:", c
    print "after", pin, "change", change


if False:
    do_change([1, 2, 3, 4, 5, 6], [0, 0, 0, 0, 0, 0], "XXX")
    exit()

ok = check_leads(leads)
print "ok=", ok

method = lead_to_changes(lead2_order)
bob_change = lead_to_changes(bob_order)
single_change = lead_to_changes(single_order)
plain_change = lead_to_changes(plain_order)


print_notes(method)
