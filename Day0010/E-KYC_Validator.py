
Required_Docs = {"Aadhaar", "PAN", "Photo"}

info_ID_Card = input("Enter Your ID Name: ").capitalize().strip()
info_PAN = input("Enter Your ID Name: ").upper().strip()
info_Photo = input("Enter Your ID Name: ").capitalize().strip()
gain_info = {info_ID_Card , info_PAN, info_Photo}
match_id = gain_info.intersection(Required_Docs)
missing_id = Required_Docs.difference(gain_info)
if gain_info == Required_Docs:
    print("\n✅ Verification Success: 100% documents matched!")
else:
    print(f"\nStatus: {len(match_id)}/3 Documents Found.")
    print(f" Matched: {match_id}")
    print(f" Missing: {missing_id}")
