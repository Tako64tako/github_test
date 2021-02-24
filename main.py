import buzz
import fizbuz
import fizz


def main():
  n = input()
  if fizbuz.fizbuz(n):
    print("FIZZBUZZ")
  elif fizz.fizz(n):
    print("FIZZ")
  elif buzz.buzz(n):
    print("BUZZ")
  else:
    print(n)

  #aa



if __name__ == '__main__':
  main()