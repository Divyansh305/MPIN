from common_pins import is_common_pin
from demographic_check import check_demographic_patterns

def assess_pin_strength(pin, demographics=None):
    if not (pin.isdigit() and len(pin) in (4, 6)):
        return {'strength': 'WEAK', 'reasons': ['INVALID_INPUT']}
    
    reasons = []
    if is_common_pin(pin):
        reasons.append('COMMONLY_USED')
    if demographics:
        reasons.extend(check_demographic_patterns(pin, demographics))
    
    return {'strength': 'WEAK' if reasons else 'STRONG', 'reasons': reasons}