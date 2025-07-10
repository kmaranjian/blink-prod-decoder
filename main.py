from child_safety_checker import SafetyChecker, Child
from colorama import init, Fore, Style
from tabulate import tabulate

init(autoreset=True)

def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print(Fore.RED + "Please enter a non-negative integer.")
            else:
                return value
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a valid integer.")

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print(Fore.RED + "Please enter a positive number.")
            else:
                return value
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a valid number.")

def get_child_info():
    print(Style.BRIGHT + "\nEnter child information:")
    name = input("Child's name: ").strip() or "Child"
    age_months = get_positive_int("Age (in months): ")
    weight_kg = get_positive_float("Weight (in kg): ")
    height_cm = get_positive_float("Height (in cm): ")
    return Child(name, age_months, weight_kg, height_cm)

def display_products(products):
    table = []
    for idx, p in enumerate(products, 1):
        table.append([
            idx, p.name, p.category, str(p.requirements)
        ])
    print("\nAvailable Products:")
    print(tabulate(table, headers=["#", "Product", "Category", "Requirements"], tablefmt="fancy_grid"))

def select_product(products):
    while True:
        try:
            choice = int(input("Select a product by number: "))
            if 1 <= choice <= len(products):
                return products[choice - 1]
            else:
                print(Fore.RED + f"Please enter a number between 1 and {len(products)}.")
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a valid number.")

def display_result(child, product, is_compatible, issues):
    print(f"\nChecking {child.name} for {product.name}...")
    if is_compatible:
        print(Fore.GREEN + Style.BRIGHT + "SAFE: This product is suitable for the child!")
    else:
        print(Fore.RED + Style.BRIGHT + "UNSAFE: This product is NOT suitable for the child.")
        print(Fore.RED + "Reasons:")
        for issue in issues:
            print(Fore.RED + f"- {issue}")
    print("\nRequirement Comparison:")
    req = product.requirements
    print(f"  Age: {child.age_months} mo (Required: {req.min_age_months or '-'} - {req.max_age_months or '-'})")
    print(f"  Weight: {child.weight_kg} kg (Required: {req.min_weight_kg or '-'} - {req.max_weight_kg or '-'})")
    print(f"  Height: {child.height_cm} cm (Required: {req.min_height_cm or '-'} - {req.max_height_cm or '-'})")

def main():
    print(Style.BRIGHT + Fore.CYAN + "\nWelcome to the Child Safety Checker!\n")
    checker = SafetyChecker()
    products = checker.list_products()
    child = get_child_info()
    while True:
        display_products(products)
        product = select_product(products)
        is_compatible, issues = checker.check_compatibility(child, product)
        display_result(child, product, is_compatible, issues)
        again = input("\nCheck another product for the same child? (y/n): ").strip().lower()
        if again != 'y':
            print(Fore.CYAN + "\nThank you for using the Child Safety Checker! Stay safe!\n")
            break

if __name__ == "__main__":
    main()
