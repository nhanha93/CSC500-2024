book_purchased = int(input("How many book(s) did you buy this month? "))
def point_cal(book_purchased):
    if book_purchased == 0 or book_purchased < 2:
        print("You've earned 0 points this month!")
    elif book_purchased == 2 or book_purchased < 4:
        print("You've earned 5 points this month!")
    elif book_purchased == 4 or book_purchased < 6:
        print("You've earned 15  points this month!")
    elif book_purchased == 6 or book_purchased < 8:
        print("You've earned 30 points this month!")
    elif book_purchased >= 8:
        print("You've earned 60 points this month!")

point_cal(book_purchased)



