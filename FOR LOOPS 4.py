fruits= ['apple','litchi']
for fruit in fruits:
     print(f"i like {fruits}")

     for number in range(1,6):
          print(f"count:{number}")

          for index, fruit in enumerate(fruit):
               print(f"index:{index},fruit:{fruits}")