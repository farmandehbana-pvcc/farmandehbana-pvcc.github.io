# dogs.py
# Demonstrating list operations with dog names
# Author: Farmandeh Bana

# Initial list of dog names
dogs = [
    "Sadie", "Gonzo", "Molly", "Ella", "Milo",
    "Sweetie Pie", "Diego", "Buddy", "Rocky", "AnnaBelle"
]

def main():
    # Display the total number of dogs
    how_many = len(dogs)
    print("\nTotal number of dogs:", how_many)
    print("Original list of dogs:", dogs)

    # Reverse the list
    dogs.reverse()
    print("\nList from last to first, using reverse():", dogs)

    # Sort the list alphabetically
    dogs.sort()
    print("\nAlphabetized list, using sort():", dogs)

    # Sort in reverse alphabetical order
    dogs.sort(reverse=True)
    print("\nReverse alphabetized list, using sort(reverse=True):", dogs)

    # Add a new dog to the list
    dogs.append("Ranger")
    print("\nAdded 'Ranger' to the list, using append():", dogs)

    # Remove the first dog from the list
    removed_dog = dogs.pop(0)
    print(f"\nRemoved the first dog ('{removed_dog}'), using pop(0):", dogs)

    # Remove a dog at a specific position
    removed_dog = dogs.pop(3)
    print(f"\nRemoved the dog at position 3 ('{removed_dog}'), using pop(3):", dogs)

    # Remove a dog by name
    if "Milo" in dogs:
        dogs.remove("Milo")
        print("\nRemoved 'Milo' by name, using remove('Milo'):", dogs)
    else:
        print("\n'Milo' is not in the list.")

    # Copy the list
    dogs_copy = dogs[:]
    print("\nCopied list using slicing:", dogs_copy)

    # Modify each dog's name to include a surname
    for i in range(len(dogs)):
        dogs[i] += " Bana"  # Your surname added to each dog's name
    print("\nModified list with last names added:", dogs)

    input("\nPress ENTER to finish...")

if __name__ == "__main__":
    main()
