__author__ = 'abg'

"""
Program to play a particular method.
Converts the documented order lists into lists of changes,
notated as X = swap and | = lie.
Plain hunt would be (XXX,|XX|) repeated continously.
"""

import method

bob_minor_lead = [
    123456,
    214365,
    241635,
    426153,
    462513,
    645231,
    654321,
    563412,
    536142,
    351624,
    315264,
    132546,
    123456,
]
bob_minor_plain = [
    132546,
    135264,
]
bob_minor_bob = [
    132546,
    123564,
]
bob_minor_single = [
    132546,
    132564,
]

# 13 orders, 12 changes. 5 x 12 = 60
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
    # 512643,
    156234,
    165243,
    # 615234,
]

single_order = [
    # 512643,
    156234,
    156243,
    # 516234,
]

method_bm = {
    "lead": method.lead_to_changes(bob_minor_lead),
    "bob": method.lead_to_changes(bob_minor_bob),
    "single": method.lead_to_changes(bob_minor_single),
    "plain": method.lead_to_changes(bob_minor_plain)
}

for s in method_bm["lead"]:
    print s

method_mpm = {
    "lead": method.lead_to_changes(lead2_order),
    "bob": method.lead_to_changes(bob_order),
    "single": method.lead_to_changes(single_order),
    "plain": method.lead_to_changes(plain_order)
}

for s in method_mpm["lead"]:
    print s
exit()


if False:
    ok = method.check_leads(leads)
    print "ok=", ok

# print_notes(method["lead"])

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
    "bob", "plain",
    "bob", "plain",
    "bob", "plain",
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
orders = method.play_composition(one_lead, method_bm, True)
method.print_orders(orders)
method.check_method(orders)
