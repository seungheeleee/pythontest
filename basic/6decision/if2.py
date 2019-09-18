score = int(input("점수를 입력하세요 :"))
if score >= 90:
    print("A grade")
    if score == 100:
        print("You are PERFECT.")
elif score >= 80:
    print("B grade")
elif score >= 70:
    print("C grade")
else:
    print("F grade")