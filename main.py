from fieldgenerator import FieldGenerator
def main():
    field = FieldGenerator('01-comedy.txt')
    field.read()
    print(field.COL)
    print(field.ROW)
    print(field.golden_points)
if __name__ == "__main__":
    main()

