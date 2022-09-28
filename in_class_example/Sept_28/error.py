def calc_square_root(n):
    from my_calculator import sqrt
    
    answer = sqrt(n)
    return answer

def main():
    # print(calc_square_root(2))
    try:
        print(calc_square_root(-4))
    except TypeError:
        print('You sent a string instead')
    except ValueError:
        print("Don't send a negative number.")
    else:
        x = 5
    finally:
        print("Don't with try")

    # print(x)
    print("REached the end")


if __name__ =="__main__":
    main()