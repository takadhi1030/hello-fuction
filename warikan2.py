def calculate_warikan(amount, number_of_people):
    quotient = amount // number_of_people
    remainber = amount % number_of_people
    return f"1人あたり: {quotient}円,端数:{remainber}円"

# print(warikan(amount=1500, number_of_people=3))
# print(warikan(amount=2000, number_of_people=3))
# print(warikan(amount=3647, number_of_people=4))
# print(warikan(amount=5000, number_of_people=8))
