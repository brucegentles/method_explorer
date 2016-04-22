__author__ = 'abg'

# import math;

lead6 = [
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
lead4 = [
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
lead5 = [
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
lead2 = [
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
lead3 = [
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
leads = [lead6, lead4, lead5, lead2, lead3]

plain = [
    512643,
    156234,
    152643,
    512634,
]

bob = [
    512643,
    156234,
    165243,
    615234,
]

single = [
    512643,
    156234,
    156243,
    516234,
]


def changes_to_places(changes, places):
    '''
    converts a series of decimal numbers,
    as the place order in decimal notation, to a 2d array of individual bell places
    :param changes: list of integer bell orders
    :param places: array or places to write to
    :return: nothing
    '''
    for ch in changes:
        # print "change =",ch
        pl = [0, 0, 0, 0, 0, 0]
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


def print_notes(n):
    for e in n:
        str = ""
        for s in e:
            str += s
        print str


def lead_to_changes(lead, changes):
    places = []
    changes_to_places(lead, places)
    n = len(places)
    m = len(places[0])
    for i in range(1, n):
        now = places[i]
        prev = places[i - 1]
        # print "change\n\t",prev, "->\n\t", now
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
        changes.append(note)


def check_leads(leads):
    '''
    Checks the members of leads to see that they all have the same set of changes.
    :return:
    '''
    ch_set = []
    for lead in leads:
        ch = []
        lead_to_changes(lead, ch)
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


ok = check_leads(leads)
print "ok=", ok

notes = []
places = []
method = []
lead_to_changes(lead2, method)
print_notes(method)
