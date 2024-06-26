# Description: This file contains the configuration for the application.

# The data dictionary contains the key-value pairs for the replacement.
# Could be copied here from excel or other source.

import re


text = '''
private, rm-0000
confidential, rm-0001
internal, rm-0002
takeda, rm-0003
private, rm-0004
BAX335,AAV8-B.00
PP335,AAV8-B.00
E335,AAV8-B.00
GTFIX,AAV8-B.00
G9,AAV8-B.00
TAK-754,AAV8-A.00
TAK754,AAV8-A.00
SHP654,AAV8-A.00
SHP-654,AAV8-A.00
PP654,AAV8-A.00
BAX888,AAV8-A.00
BAX-888,AAV8-A.00
PCG8,AAV8-A.00
AV,AAV8-A.00
FVIII,AAV8-A.00
HEM A,AAV8-A.00
HEMA,AAV8-A.00
E654,AAV8-A.00
PP654,AAV8-A.00
PP754,AAV8-A.00
P754,AAV8-A.00
E754,AAV8-A.00
TAK-748,AAV8-B2.00
TAK748,AAV8-B2.00
SHP648,AAV8-B2.00
SHP-648,AAV8-B2.00
FIX,AAV8-B2.00
Hem B,AAV8-B2.00
HemB,AAV8-B2.00
Hemophilia B,AAV8-B2.00
PP648,AAV8-B2.00
PP748,AAV8-B2.00
PPSIS,AAV8-B2.01
TAK-686,AAV9-N.00
TAK686,AAV9-N.00
SHP686,AAV9-N.00
SHP-686,AAV9-N.00
Huntingtons Disease,AAV9-N.00
Huntington Disease,AAV9-N.00
Huntington,AAV9-N.00
HD,AAV9-N.00
PP686,AAV9-N.00
EHT2,AAV9-N.00
E686,AAV9-N.00
L686,AAV9-N.00
Venustus,AAV3b-V.00
PPVen,AAV3b-V.00
EVEN,AAV3b-V.00
LVEN,AAV3b-V.00
DP0079,AAV8-A2.00
2nd Gen FVIII,AAV8-A2.00
TAK-709,AAV8-A2.00
TAK709,AAV8-A2.00
PP709,AAV8-A2.00
AAV6 TRAC CD19,AAV6-CT.00
PCT01,AAV6-CT.00
Hunter,AAV8-R.00
TAK-073,AAV8-R.00
TAK073,AAV8-R.00
I2S,AAV8-R.00
pXL026,AAV8-R.00
PP073,AAV8-R.00
E073,AAV8-R.00
pXL029,AAV8-R.01
Sirion,AAV8.PV27-B2.00
PPSI8,AAV8.PV27-B2.00
PPSI5,AAV5-B2.01
FXN,AAV9.C5-X.P12
C5/P12,AAV9.C5-X.P12
Friedreich's Ataxia,AAV9.C5-X.P12
Friedreich,AAV9.C5-X.P12
Frataxin,AAV9.C5-X.P13
PFX01,AAV9.C5-X.P12
PPFXN,AAV9.C5-X.P12
EFXN,AAV9.C5-X.P12
C5/P9,AAV9.C5-X.P9
PFX03,AAV9.C5-X.P9
EFX03,AAV9.C5-X.P9
PFX05,AAV9.C5-X.P9
PFX07,AAV9.C5-X.P9
C5/P2,AAV9.C5-X.P2
PFX02,AAV9.C5-X.P2
EFX02,AAV9.C5-X.P2
PFX04,AAV9.C5-X.P2
EFX04,AAV9.C5-X.P2
AAV9/P9,AAV9-X.P9
PFX06,AAV9-X.P9
Fabry,AAV9-Y.00
TAK-028,AAV9-Y.00
TAK028,AAV9-Y.00
aGal,AAV9-Y.00
pZL028,AAV9-Y.00
PFB04,AAV9-Y.00
EFB04,AAV9-Y.00
pZL034,AAV9-Y.01
PFB05,AAV9-Y.01
pMD039,AAV9-Y.02
PFB03,AAV9-Y.02
EFB03,AAV9-Y.02
pMD009,AAV9-Y.03
PFB02,AAV9-Y.03
EFB02,AAV9-Y.03
pMD007,AAV8-Y.00
PFB01,AAV8-Y.00
GBA-PD,AAV9-P.00
Parkinson Disease,AAV9-P.00
pPD018,AAV9-P.00
pPD019,AAV9-P.01
PGB01,AAV9-P.01
Pompe AAV9,AAV9-E.00
Pompe,AAV9-E.00
Pompe AAV6,AAV6-E.00
Pompe AAVX eng.,AAVX-E.00
GAA,AAV9-E.00
pKD015,AAV9-E.00
PPO02,AAV9-E.00
EPO02,AAV9-E.00
KiT4,AAV.KiT4-E.00
PPO05,AAV.KiT4-E.00
EPO05,AAV.KiT4-E.00
pMY011,AAV9-E.01
PPO03,AAV9-E.01
Hunter 2nd Gen,AAV9-R2.00
AAV9-TJ025,AAV9-R2.00
PHU04,AAV9-R2.00
EHU04,AAV9-R2.00
AAV9-TJ026,AAV9-R2.01
PHU05,AAV9-R2.01
AAV9-SJ075,AAV9-R2.02
PHU03,AAV9-R2.02
AAV9-SJ074,AAV9-R2.03
PHU02,AAV9-R2.03
AAV9-SJ072,AAV9-R2.04
PHU01,AAV9-R2.04
SOP,Document
DP0073,AAVX-YY.ZZ
'''

dc_replacements = {"private": " ",
                   "confidential": "  ",
                   "internal": "    ",
                   "takeda": "     ",
                   "BAX335": "AAV8-B.00",
                   "PP335": "AAV8-B.00",
                   "E335": "AAV8-B.00",
                   "GTFIX": "AAV8-B.00",
                   "G9": "AAV8-B.00",
                   "TAK-754": "AAV8-A.00",
                   "TAK754": "AAV8-A.00",
                   "SHP654": "AAV8-A.00",
                   "SHP-654": "AAV8-A.00",
                   "PP654": "AAV8-A.00",
                   "BAX888": "AAV8-A.00",
                   "BAX-888": "AAV8-A.00",
                   "PCG8": "AAV8-A.00",
                   "AV": "AAV8-A.00",
                   "FVIII": "AAV8-A.00",
                   "HEM A": "AAV8-A.00",
                   "HEMA": "AAV8-A.00",
                   "E654": "AAV8-A.00",
                   "PP754": "AAV8-A.00",
                   "Pp954": "AAV8-A.00",
                   "P754": "AAV8-A.00",
                   "E754": "AAV8-A.00",
                   "TAK-748": "AAV8-B2.00",
                   "TAK748": "AAV8-B2.00",
                   "SHP648": "AAV8-B2.00",
                   "SHP-648": "AAV8-B2.00",
                   "FIX": "AAV8-B2.00",
                   "Hem B": "AAV8-B2.00",
                   "HemB": "AAV8-B2.00",
                   "Hemophilia B": "AAV8-B2.00",
                   "Hemophilia": "AAV8-B2.00",
                   "PP648": "AAV8-B2.00",
                   "PP748": "AAV8-B2.00",
                   "PPSIS": "AAV8-B2.01",
                   "TAK-686": "AAV9-N.00",
                   "TAK686": "AAV9-N.00",
                   "SHP686": "AAV9-N.00",
                   "SHP-686": "AAV9-N.00",
                   "Huntingtons Disease": "AAV9-N.00",
                   "Huntington Disease": "AAV9-N.00",
                   "Huntington": "AAV9-N.00",
                   "HD": "AAV9-N.00",
                   "PP686": "AAV9-N.00",
                   "EHT2": "AAV9-N.00",
                   "E686": "AAV9-N.00",
                   "L686": "AAV9-N.00",
                   "Venustus": "AAV3b-V.00",
                   "PPVen": "AAV3b-V.00",
                   "EVEN": "AAV3b-V.00",
                   "LVEN": "AAV3b-V.00",
                   "DP0079": "AAV8-A2.00",
                   "2nd Gen FVIII": "AAV8-A2.00",
                   "TAK-709": "AAV8-A2.00",
                   "TAK709": "AAV8-A2.00",
                   "PP709": "AAV8-A2.00",
                   "AAV6 TRAC CD19": "AAV6-CT.00",
                   "PCT01": "AAV6-CT.00",
                   "Hunter": "AAV8-R.00",
                   "TAK-073": "AAV8-R.00",
                   "TAK073": "AAV8-R.00",
                   "I2S": "AAV8-R.00",
                   "pXL026": "AAV8-R.00",
                   "PP073": "AAV8-R.00",
                   "E073": "AAV8-R.00",
                   "pXL029": "AAV8-R.01",
                   "Sirion": "AAV8.PV27-B2.00",
                   "PPSI8": "AAV8.PV27-B2.00",
                   "PPSI5": "AAV5-B2.01",
                   "FXN": "AAV9.C5-X.P12",
                   "C5/P12": "AAV9.C5-X.P12",
                   "Friedreich's Ataxia": "AAV9.C5-X.P12",
                   "Friedreich Ataxia": "AAV9.C5-X.P12",
                   "Friedreich": "AAV9.C5-X.P12",
                   "Frataxin": "AAV9.C5-X.P13",
                   "PFX01": "AAV9.C5-X.P12",
                   "PPFXN": "AAV9.C5-X.P12",
                   "EFXN": "AAV9.C5-X.P12",
                   "C5/P9": "AAV9.C5-X.P9",
                   "PFX03": "AAV9.C5-X.P9",
                   "EFX03": "AAV9.C5-X.P9",
                   "PFX05": "AAV9.C5-X.P9",
                   "PFX07": "AAV9.C5-X.P9",
                   "C5/P2": "AAV9.C5-X.P2",
                   "PFX02": "AAV9.C5-X.P2",
                   "EFX02": "AAV9.C5-X.P2",
                   "PFX04": "AAV9.C5-X.P2",
                   "EFX04": "AAV9.C5-X.P2",
                   "AAV9/P9": "AAV9-X.P9",
                   "PFX06": "AAV9-X.P9",
                   "Fabry": "AAV9-Y.00",
                   "TAK-028": "AAV9-Y.00",
                   "TAK028": "AAV9-Y.00",
                   "aGal": "AAV9-Y.00",
                   "pZL028": "AAV9-Y.00",
                   "PFB04": "AAV9-Y.00",
                   "EFB04": "AAV9-Y.00",
                   "pZL034": "AAV9-Y.01",
                   "PFB05": "AAV9-Y.01",
                   "pMD039": "AAV9-Y.02",
                   "PFB03": "AAV9-Y.02",
                   "EFB03": "AAV9-Y.02",
                   "pMD009": "AAV9-Y.03",
                   "PFB02": "AAV9-Y.03",
                   "EFB02": "AAV9-Y.03",
                   "pMD007": "AAV8-Y.00",
                   "PFB01": "AAV8-Y.00",
                   "GBA-PD": "AAV9-P.00",
                   "Parkinson Disease": "AAV9-P.00",
                   "Parkinson": "AAV9-P.00",
                   "pPD018": "AAV9-P.00",
                   "pPD019": "AAV9-P.01",
                   "PGB01": "AAV9-P.01",
                   "Pompe AAV9": "AAV9-E.00",
                   "Pompe": "AAV9-E.00",
                   "Pompe AAV6": "AAV6-E.00",
                   "Pompe AAVX eng.": "AAVX-E.00",
                   "GAA": "AAV9-E.00",
                   "pKD015": "AAV9-E.00",
                   "PPO02": "AAV9-E.00",
                   "EPO02": "AAV9-E.00",
                   "KiT4": "AAV.KiT4-E.00",
                   "PPO05": "AAV.KiT4-E.00",
                   "EPO05": "AAV.KiT4-E.00",
                   "pMY011": "AAV9-E.01",
                   "PPO03": "AAV9-E.01",
                   "Hunter 2nd Gen": "AAV9-R2.00",
                   "Hunter": "AAV9-R2.00",
                   "AAV9-TJ025": "AAV9-R2.00",
                   "PHU04": "AAV9-R2.00",
                   "EHU04": "AAV9-R2.00",
                   "AAV9-TJ026": "AAV9-R2.01",
                   "PHU05": "AAV9-R2.01",
                   "AAV9-SJ075": "AAV9-R2.02",
                   "PHU03": "AAV9-R2.02",
                   "AAV9-SJ074": "AAV9-R2.03",
                   "PHU02": "AAV9-R2.03",
                   "AAV9-SJ072": "AAV9-R2.04",
                   "PHU01": "AAV9-R2.04",
                   "SOP": "Document",
                   "DP0073": "AAV8-R.00"}


NEW_DOC_SUFFIX = '_N-e-W_'


def replace_data(from_txt=False) -> dict:
    """ Replace text in a Word document
    """
    if from_txt:
        data = {}
        lines = text.strip().split('\n')
        for line in lines:
            key, value = line.split(',')
            data[key.strip()] = value.strip()

        for k, v in data.items():
            print(f'"{k}": "{v}",')
        return data
    else:
        return dc_replacements


def replace_substring(txt, k, v, flags=re.MULTILINE | re.IGNORECASE):
    """ Replace substring in a text
        k: substring to be replaced
        v: new substring
    """
    return re.subn(r'(?i)'+k, v, txt, flags=flags)
