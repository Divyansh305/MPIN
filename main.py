from strength_assessor import assess_pin_strength

def main():
    print("MPIN Strength Assessor")
    pin = input("Enter MPIN (4/6 digits): ").strip()
    
    demographics = {}
    print("\nOptional demographic info (leave blank to skip):")
    if dob := input("Your birth date (DD-MM-YYYY): ").strip():
        demographics['dob'] = dob
    if spouse_dob := input("Spouse's birth date (DD-MM-YYYY): ").strip():
        demographics['spouse_dob'] = spouse_dob
    if anniversary := input("Anniversary date (DD-MM-YYYY): ").strip():
        demographics['anniversary'] = anniversary
    
    result = assess_pin_strength(pin, demographics or None)
    
    print("\n=== Assessment Result ===")
    print(f"Strength: {result['strength']}")
    if result['reasons']:
        print("Reasons:")
        for reason in result['reasons']:
            print(f"- {reason.replace('_', ' ').title()}")

if __name__ == "__main__":
    main()