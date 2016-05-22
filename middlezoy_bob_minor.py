__author__ = 'abg'

import method

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

method_mpm = {
    "name": "Middlezoy Bob Minor",
    "lead": method.lead_to_changes(lead2_order),
    "bob": method.lead_to_changes(bob_order),
    "single": method.lead_to_changes(single_order),
    "plain": method.lead_to_changes(plain_order),
    "b": method.lead_to_changes(bob_order),
    "s": method.lead_to_changes(single_order),
    "p": method.lead_to_changes(plain_order)
}


def get_method():
    return method_mpm
