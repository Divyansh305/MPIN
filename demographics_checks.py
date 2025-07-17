from datetime import datetime

def extract_date_patterns(date_str):
    try:
        date = datetime.strptime(date_str, "%d-%m-%Y")
        day, month, year = f"{date.day:02d}", f"{date.month:02d}", f"{date.year % 100:02d}"
        return {
            day + month, month + day, day + year, year + day,
            month + year, year + month, day + month + year,
            month + day + year, year + month + day
        }
    except ValueError:
        return set()

def check_demographic_patterns(pin, demographics):
    reasons = []
    for field, date in demographics.items():
        if date and pin in extract_date_patterns(date):
            reasons.append(f"DEMOGRAPHIC_{'DOB_SELF' if field == 'dob' else 'DOB_SPOUSE' if field == 'spouse_dob' else 'ANNIVERSARY'}")
    return reasons