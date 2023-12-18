def calc_tips(bill, tips_pcent):
    tips = bill *(tips_pcent / 100)
    total_bill =  bill + tips
    return tips, total_bill

def main():
    try:
        
        bill = float(input("Enter your bill: N "))
        tips_pcent = int(input("Enter your tip_pcent: "))
    except ValueError:
        print("Enter a valid numeric value")
        
        return 
    tips, total_bill = calc_tips(bill,tips_pcent)
    print(f"\nTips: N{tips: .2f}")
    print(f"total_bill: N{total_bill: .2f}")

if __name__ == "__manin__":
    main()
    