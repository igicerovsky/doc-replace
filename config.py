# Description: This file contains the configuration for the application.

# The data dictionary contains the key-value pairs for the replacement.
# Could be copied here from excel or other source.
text = '''
Fabry, AAV9-Y
PFB, P-Y
EFB, E-Y
Pompe, AAV9-E
PPO, P-E
EPO, E-E
rE-Ert, report
PP648, PRPL1
PP073, PRPL2
PP5786, PRPL2
PHCP, PHCP1
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
