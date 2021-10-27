from enigma.machine import EnigmaMachine
import itertools

romans = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII']
other = ['Beta', 'Gamma']
reflectors = ['B-Thin', 'C-Thin']
settings = ['F21', 'L18', 'T16', 'G11']

for r1, r2, r3 in itertools.product(romans, repeat=3):
    for r0 in other:
        for ref in reflectors:
            for perm in itertools.permutations(settings):

                rings = [int(t[1:]) - 1 for t in list(perm)]
                disp = ''.join([t[0] for t in list(perm)])
                rotors = ' '.join([r0, r1, r2, r3])

                machine = EnigmaMachine.from_key_sheet(
                    rotors=rotors,
                    reflector=ref,
                    ring_settings=rings,
                    plugboard_settings='NH CW MK PO ZS QB FU TR'
                )

                machine.set_display(disp)
                ciphertext = 'utogaaxgeonuvkegegddajktikdtvepnkolokj'.upper()
                plaintext = machine.process_text(ciphertext).lower()

                if plaintext.startswith('flg'):
                    print(plaintext)

