__author__ = 'abg'

import numpy as np

VERBOSE = False
N = 6
PLACE_RANGE = range(0, N)
ROUNDS = range(1, N + 1)


def is_rounds(order):
    for i in PLACE_RANGE:
        if order[i] != ROUNDS[i]:
            return False
    print "found rounds"
    return True


def zeros(n):
    a = list()
    for i in range(0, n):
        a.append(0)
    return a


def print_notes(n):
    for e in n:
        str = ""
        for s in e:
            str += s
        print str


def places_to_order(places):
    n = 0
    for v in places:
        n *= 10
        n += v
    return n


def print_order(cmd, e, i):
    n = places_to_order(e)
    print i, cmd, " : ", n


def print_orders(n):
    i = 0
    for e in n:
        i += 1
        print_order("", e, i)


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


def swap(order, index):
    """
    swap elements [index] and [index+1] of order
    :param order: input order
    :param index:
    :return: none
    """
    tmp = order[index]
    order[index] = order[index + 1]
    order[index + 1] = tmp


def do_change(order, change):
    """
    interpret one change string and apply to place in to make place out
    :param order: places before - modified in-plce
    :param change: change string.
    :return:
    """
    i = 0
    if VERBOSE:
        print "before", order, "change", change
    for c in change:
        if i >= len(order):
            print "got to end of change"
            break
        # print "a:",c,i
        if c == 'X':
            swap(order, i)
            i += 2
        elif c == '|':
            i += 1
        else:
            print "ERROR bad change symbol:", c
            # print "b:",c,i
    if VERBOSE:
        print "after", order, "change", change


def append_order(order, l):
    new = []
    for x in order:
        new.append(x)
    l.append(new)


def copy_order(order):
    new = []
    for x in order:
        new.append(x)
    return new


def check_rounds(order, till_rounds):
    if till_rounds:
        if is_rounds(order):
            return True
    return False


def play_lead(order, lead, cmd, till_rounds, result):
    """
    play a single lead, mofifying the last element with the change for the given cmd.
    if Till_rounds is set, abort if rounds is got to.
    :param order: current order of bells. list of N places
    :param lead: list of changes for plain course
    :param cmd: change for this type of lead - ie the bob change.
    :param till_rounds: boolean, if True, will repeat until order is rounds.
    :param result: resulting list of orders to be appended to
    :return: True if we have not yet come into rounds.
    """
    my_lead = lead
    my_lead[-1] = cmd[0]
    if VERBOSE:
        print lead[-1]
        print my_lead[-1]
    for change in my_lead:
        do_change(order, change)
        append_order(order, result)
        if check_rounds(order, till_rounds):
            return False
    if check_rounds(order, till_rounds):
        return False
    return True


def play_composition(comp, method_info, till_rounds):
    """
    sequences a composition
    :param comp:  composition, a list of verbs from the set plain,bob,single
    :param method_info: map with leads etc
    :param till_rounds: boolean, if True, will repeat until order is rounds.
    :return: list of orders.
    """
    res = []
    order = copy_order(ROUNDS)
    more = True
    i = 0
    while more:
        for cmd in comp:
            print_order(cmd, order, i)
            more = play_lead(order, method_info["lead"], method_info[cmd], till_rounds, res)
            i += len(method_info["lead"])
            if not more:
                print_order(cmd, order, len(res))
                break
        if not till_rounds:
            break
    return res


def check_method(orders):
    """
    checks to see if all changes have been sone, or there are any duplicates
    :param orders: orders, list of places.
    :return: Boolean, True if no repeats
    """
    hist = np.zeros(654321)
    n_rep = 0
    for i in orders:
        n = places_to_order(i)
        idx = n - 1
        hist[idx] += 1
        if (hist[idx] > 1.0):
            n_rep += 1
            print "repeat", n, hist[idx]
    if n_rep == 0:
        print "no repeats"
    return n_rep
