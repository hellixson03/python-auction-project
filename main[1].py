def place_bid(name1):
  item_price = 100.00
  option = 'Y'

  while option != 'N':
      print(f"Minimum bid is ${item_price:.2f}")

      option = input("Would you like to bid? Y or N\n")
      if option == 'N':
          print("Goodbye")
          break

      user_bid = float(input("How much will you bid?\n"))
      print(f"Placed the bid for ${user_bid:.2f}")

      if user_bid >= item_price:
          print(f"{name1}, You won the item!")
          print("Please pay for your item within 24 hours.")
          break
      else:
          print("You lost the item. :(\n")

def main():
  item_price = 100.00
  name = ""
  name1 = input("What is your name?\n")

  print("Let's list an item.")

  name = input("What do you want to list?\n")

  item_price = float(input("How much is the item?\n"))
  print(f"Listed the item for ${item_price:.2f}")

  place_bid(name1)

if __name__ == "__main__":
  main()