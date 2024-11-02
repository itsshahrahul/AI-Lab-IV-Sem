def is_sibling( person1, person2):
    siblings = {
        ("Alice", "Bob"),
        ("Bob", "Alice"),
        ("Charlie", "David"),
        ("David", "Charlie"),
        ("Eve", "Frank"),
        ("Frank", "Eve")
    } 
    return (person1, person2) in siblings or (person2, person1) in siblings

def main():
    person1 = input("Enter the name of the first person: ")
    person2 = input("Enter the name of the second person: ")
    if is_sibling(person1, person2):
        print(f"{person1} and {person2} are siblings")
    else:
        print(f"{person1} and {person2} are not siblings")

if __name__ == "__main__":
            main()