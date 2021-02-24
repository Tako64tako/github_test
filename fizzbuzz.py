def fizzbuzz(num):
    if num % 3 == 0:
        if num % 5 == 0:
            print("fizzbuzz")
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    judge = fizzbuzz(20)
    print(judge)
