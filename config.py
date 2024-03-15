# Description: This file contains the configuration for the application.

# The data dictionary contains the key-value pairs for the replacement.
# Could be copied here from excel or other source.

import re


text = '''
BAX335, AAV8-B.00
PP335, AAV8-B.00
TAK-754, AAV8-A.00
TAK754, AAV8-A.00
SHP654, AAV8-A.00
BAX888, AAV8-A.00
FVIII, AAV8-A.00
HEM A, AAV8-A.00
PP654, AAV8-A.00
PP754, AAV8-A.00
TAK-748, AAV8-B2.00
TAK748, AAV8-B2.00
SPH648, AAV8-B2.00
FIX, AAV8-B2.00
Hem B, AAV8-B2.00
Hemophilia B, AAV8-B2.00
PP648, AAV8-B2.00
PP748, AAV8-B2.00
PPSIS, AAV8-B2.01
TAK-686, AAV9-N.00
GT, AAV9-N.00
TAK686, AAV9-N.00
SHP686, AAV9-N.00
Huntingtons Disease, AAV9-N.00
HD, AAV9-N.00
PP686, AAV9-N.00
Venustus, AAV3b-V.00
PPVen, AAV3b-V.00
DP0079, AAV8-A2.00
TAK-709, AAV8-A2.00
2nd Gen FVIII, AAV8-A2.00
TAK-709, AAV8-A2.00
TAK709, AAV8-A2.00
PP709, AAV8-A2.00
AAV6 TRAC CD19 (CT01), AAV6-CT.00
PCT01, AAV6-CT.00
Hunter, AAV8-R.00
TAK-073, AAV8-R.00
TAK073, AAV8-R.00
I2S, AAV8-R.00
pXL026, AAV8-R.00
PP073, AAV8-R.00
pXL029, AAV8-R.01
Sirion, AAV8.PV27-B2.00
PPSI8, AAV8.PV27-B2.00
PPSI5, AAV5-B2.01
FXN, AAV9.C5-X.P12
C5/P12, AAV9.C5-X.P12
Friedreich's Ataxia, AAV9.C5-X.P12
PFX01, AAV9.C5-X.P12
PPFXN, AAV9.C5-X.P12
C5/P9, AAV9.C5-X.P9
PFX03, AAV9.C5-X.P9
PFX05, AAV9.C5-X.P9
PFX07, AAV9.C5-X.P9
C5/P2, AAV9.C5-X.P2
PFX02, AAV9.C5-X.P2
PFX04, AAV9.C5-X.P2
AAV9/P9, AAV9-X.P9
PFX06, AAV9-X.P9
Fabry, AAV9-Y.00
TAK-028, AAV9-Y.00
TAK028, AAV9-Y.00
aGal, AAV9-Y.00
pZL028, AAV9-Y.00
PFB04, AAV9-Y.00
pZL034, AAV9-Y.01
PFB05, AAV9-Y.01
pMD039, AAV9-Y.02
PFB03, AAV9-Y.02
pMD009, AAV9-Y.03
PFB02, AAV9-Y.03
pMD007, AAV8-Y.00
PFB01, AAV8-Y.00
GBA-PD, AAV9-P.00
Parkinson Disease, AAV9-P.00
pPD018, AAV9-P.00
pPD019, AAV9-P.01
PGB01, AAV9-P.01
Pompe, AAV9-E.00
GAA, AAV9-E.00
pKD015, AAV9-E.00
PPO02, AAV9-E.00
KiT4, AAV.KiT4-E.00
PPO05, AAV.KiT4-E.00
pMY011, AAV9-E.01
PPO03, AAV9-E.01
Hunter 2nd Gen, AAV9-R2.00
AAV9-TJ025, AAV9-R2.00
PHU04, AAV9-R2.00
AAV9-TJ026, AAV9-R2.01
PHU05, AAV9-R2.01
AAV9-SJ075, AAV9-R2.02
PHU03, AAV9-R2.02
AAV9-SJ074, AAV9-R2.03
PHU02, AAV9-R2.03
AAV9-SJ072, AAV9-R2.04
PHU01, AAV9-R2.04
confidential, rm-0001
for internal use only, rm-0002
'''


NEW_DOC_SUFFIX = '_N-e-W_'


def replace_data() -> dict:
    """ Replace text in a Word document
    """
    data = {}
    lines = text.strip().split('\n')
    for line in lines:
        key, value = line.split(',')
        data[key.strip()] = value.strip()
    return data


def replace_substring(txt, repl, subs):
    # Replacing all occurrences of substring s1 with s2
    return re.sub(r'(?i)'+subs, repl, txt)
