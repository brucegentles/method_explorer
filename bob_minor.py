__author__ = 'abg'

import method

# this is just plain hunt, which is modified by the plain,bob,or single modifier.
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

method_bm = {
    "name": "Bob Minor",
    "lead": method.lead_to_changes(bob_minor_lead),
    "bob": method.lead_to_changes(bob_minor_bob),
    "single": method.lead_to_changes(bob_minor_single),
    "plain": method.lead_to_changes(bob_minor_plain),
    "b": method.lead_to_changes(bob_minor_bob),
    "s": method.lead_to_changes(bob_minor_single),
    "p": method.lead_to_changes(bob_minor_plain)
}


def get_method():
    return method_bm
