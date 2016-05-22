__author__ = 'abg'

"""
Program to play a particular method.
Converts the documented order lists into lists of changes,
notated as X = swap and | = lie.
Plain hunt would be (XXX,|XX|) repeated continously.
"""

import method as m
import bob_minor
import middlezoy_bob_minor as mbm
import method.touch_set as ts
import method.call_pattern as cp

method_bm = bob_minor.get_method()
# m.print_lead(method_bm,"plain")

method_mbm = mbm.get_method()
# m.print_lead(method_mbm,"plain")
# print_notes(method["lead"])

if False:
    plain_course = [
        "plain", "plain", "plain", "plain", "plain"
    ]

    # touch1 120:
    # repeat 165243 2.0
    # repeat 143652 2.0
    # repeat 152436 2.0
    # repeat 136524 2.0
    # repeat 124365 2.0
    touch1 = [
        # 0      12      24      36       48      60
        "plain", "plain", "plain", "plain", "bob",

        # 60      72      84     96       108    120
        "plain", "plain", "plain", "plain", "bob",

        # 120    132     144      156     168    180
        "plain", "plain", "plain", "plain", "single",

        #    "plain","plain","plain", "plain","bob",
    ]

    # touch2 216 long
    # repeat 165243 2.0
    # repeat 134625 2.0
    # repeat 152364 2.0
    # repeat 164523 2.0
    # repeat 132654 2.0
    # repeat 145362 2.0
    # repeat 162453 2.0
    # repeat 135642 2.0
    # repeat 124365 2.0
    touch2 = [
        "bob", "bob", "bob",
        "plain", "plain", "plain",
    ]

    touch720 = [
        "plain", "plain", "bob",
        "plain", "plain", "bob",
        # "plain", "plain", "plain", "plain", "bob",
        # "plain", "plain", "plain", "plain", "bob"
    ]

    one_lead = ["bob", "plain", "plain", "plain",  # 48
                "bob", "plain", "plain", "plain",  # 96
                "bob", "plain", "plain", "plain",  # 144
                "bob", "plain", "plain", "plain",  # 192
                "bob", "plain", "plain", "single",  # 240
                "bob", "plain", "plain", "plain",  # 48
                "bob", "plain", "plain", "plain",  # 96
                "bob", "plain", "plain", "plain",  # 144
                "bob", "plain", "plain", "plain",  # 192
                "bob", "plain", "plain", "plain",  # 240
                "bob", "plain", "plain", "plain",  # 288
                "bob", "plain", "plain", "plain",  # 336
                "bob", "plain", "plain", "plain",  # 384
                "bob", "plain", "plain", "plain",  # 432
                "bob", "plain", "plain", "single",  # 480
                "bob", "plain", "plain", "plain",  # 48
                "bob", "plain", "plain", "plain",  # 96
                "bob", "plain", "plain", "plain",  # 144
                "bob", "plain", "plain", "plain",  # 192
                "bob", "plain", "plain", "plain",  # 240
                ]

    glenn_a_a_taylor_720 = [
        "plain", "plain", "plain",
        "bob", "single", "single"
    ]


def try_permutations():
    # extent = 720  lead is 12 so 60 calls. 5 working bells so only need a call every 5th lead.
    permutations = ts.TouchSet(12)
    count = 0
    max_len = 0
    max_touch = []
    method = method_bm
    verbose = False
    j = 0

    print str.format("max {} iterations", pow(2, 12))
    while permutations.more:  # and count < permutations.size:
        orders = m.play_composition(permutations.get(), method, True, verbose)
        # m.print_orders(orders)
        length, n_rep = m.check_method(orders, verbose)
        if n_rep == 0 and length > max_len:
            print "i=", count, "length=", length, "n_repeats=", n_rep, "codes", permutations.get_code_txt()
            max_len = length
            max_touch = permutations.get()
        count += 1
        j += 1
        if j >= 100:
            print count
            j = 0
        permutations.inc()

    print "done ", count, " iterations"
    verbose = True
    orders = m.play_composition(max_touch, method, True, verbose)
    length, n_rep = m.check_method(orders, verbose)
    print "i=", count, "length=", length, "n_repeats=", n_rep
    m.print_orders(orders)


def try_max_length_pattern():
    p = cp.CallPattern(0, 14, 60)
    method = method_bm
    verbose = True
    orders = m.play_composition(p.get(), method, True, verbose)
    # m.print_orders(orders)
    length, n_rep = m.check_method(orders, verbose)
    print "length=", length, "n_repeats=", n_rep, "codes", p.get_code_txt()
    #m.print_orders(orders)


def print_sequence(seq):
    stopAtRounds = False
    method = method_bm
    verbose = True
    orders = m.play_composition(seq, method, stopAtRounds, verbose)
    # m.print_orders(orders)
    length, n_rep = m.check_method(orders, verbose)
    print "length=", length, "n_repeats=", n_rep
    # m.print_orders(orders)


def strToSeq(string):
    seq = []
    for i in range(len(string)):
        seq.append(string[i])
    return seq


# try_permutations()
# try_max_length_pattern()

def diag2():
    seqx = ""
    seqx += "bbsp"  # to 25364 in diag 2
    # seqx += "bp"    # to 54236 in inner circle in diag 2
    # seqx += "bpp"    # to 43562 in inner circle in diag 2
    seqx += "bppp"  # to 36425 in inner circle in diag 2
    seqx += "ssss"  # round this hex
    seqx += "p"  # out
    return seqx


def to_group(n_hex):
    """
    from entry to the diag from page 1 to hex n
    :return: sequence
    """
    seq = "b"
    for i in range(0, n_hex - 1):
        seq += "p"
    return seq


def to_exit(n):
    """
    from entry to the diag from page 1 to hex n
    :return: sequence
    """
    seq = ""
    for i in range(0, n - 1):
        seq += "s"
    return seq + "p"


def diag4():
    seqx = "sssp"
    seqx += to_group(2)
    seqx += to_exit(2)
    return seqx


def diag5():
    seqx = "ssssp"
    seqx += to_group(5)
    seqx += to_exit(6)
    return seqx


def xpt(n):
    s = "ppppsbpbpbpbpp"
    return s
    for i in range(1, n):
        #   s += "bppppsbpbpbpbpp"
        s += "b"  # to origin
        #   s +=  "ppppsbpbpbpbpp"
        s += "ppppsb"  # pbpbpbpp"
    s += "s"
    return s


print_sequence(strToSeq(xpt(2)))
