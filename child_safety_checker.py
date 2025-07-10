from typing import Optional, List, Tuple

class Child:
    def __init__(self, name: str, age_months: int, weight_kg: float, height_cm: float):
        self.name = name
        self.age_months = age_months
        self.weight_kg = weight_kg
        self.height_cm = height_cm

    def age_years(self) -> float:
        """Return age in years (rounded to 2 decimals)."""
        return round(self.age_months / 12, 2)

    def __str__(self):
        return f"{self.name} (Age: {self.age_months} months / {self.age_years()} years, Weight: {self.weight_kg} kg, Height: {self.height_cm} cm)"

class ProductRequirement:
    def __init__(self,
                 min_age_months: Optional[int] = None,
                 max_age_months: Optional[int] = None,
                 min_weight_kg: Optional[float] = None,
                 max_weight_kg: Optional[float] = None,
                 min_height_cm: Optional[float] = None,
                 max_height_cm: Optional[float] = None):
        self.min_age_months = min_age_months
        self.max_age_months = max_age_months
        self.min_weight_kg = min_weight_kg
        self.max_weight_kg = max_weight_kg
        self.min_height_cm = min_height_cm
        self.max_height_cm = max_height_cm

    def __str__(self):
        parts = []
        if self.min_age_months is not None:
            parts.append(f"Min Age: {self.min_age_months} mo")
        if self.max_age_months is not None:
            parts.append(f"Max Age: {self.max_age_months} mo")
        if self.min_weight_kg is not None:
            parts.append(f"Min Weight: {self.min_weight_kg} kg")
        if self.max_weight_kg is not None:
            parts.append(f"Max Weight: {self.max_weight_kg} kg")
        if self.min_height_cm is not None:
            parts.append(f"Min Height: {self.min_height_cm} cm")
        if self.max_height_cm is not None:
            parts.append(f"Max Height: {self.max_height_cm} cm")
        return ", ".join(parts) if parts else "No requirements"

class Product:
    def __init__(self, name: str, category: str, requirements: ProductRequirement, description: str = ""):
        self.name = name
        self.category = category
        self.requirements = requirements
        self.description = description

    def __str__(self):
        return f"{self.name} ({self.category}): {self.description} | Requirements: {self.requirements}"

class SafetyChecker:
    def __init__(self, products: Optional[List[Product]] = None):
        self.products = products if products is not None else self.load_sample_products()

    def check_compatibility(self, child: Child, product: Product) -> Tuple[bool, List[str]]:
        """
        Returns (is_compatible, issues_list)
        """
        req = product.requirements
        issues = []
        if req.min_age_months is not None and child.age_months < req.min_age_months:
            issues.append(f"Child is too young (min {req.min_age_months} mo)")
        if req.max_age_months is not None and child.age_months > req.max_age_months:
            issues.append(f"Child is too old (max {req.max_age_months} mo)")
        if req.min_weight_kg is not None and child.weight_kg < req.min_weight_kg:
            issues.append(f"Child is too light (min {req.min_weight_kg} kg)")
        if req.max_weight_kg is not None and child.weight_kg > req.max_weight_kg:
            issues.append(f"Child is too heavy (max {req.max_weight_kg} kg)")
        if req.min_height_cm is not None and child.height_cm < req.min_height_cm:
            issues.append(f"Child is too short (min {req.min_height_cm} cm)")
        if req.max_height_cm is not None and child.height_cm > req.max_height_cm:
            issues.append(f"Child is too tall (max {req.max_height_cm} cm)")
        return (len(issues) == 0, issues)

    def load_sample_products(self) -> List[Product]:
        """Load a list of sample products with realistic requirements."""
        return [
            Product(
                name="Infant Car Seat",
                category="Car Seat",
                requirements=ProductRequirement(
                    min_age_months=0, max_age_months=12,
                    min_weight_kg=2.3, max_weight_kg=13.6,
                    max_height_cm=76
                ),
                description="Rear-facing seat for infants."
            ),
            Product(
                name="Convertible Car Seat",
                category="Car Seat",
                requirements=ProductRequirement(
                    min_age_months=0, max_age_months=48,
                    min_weight_kg=2.3, max_weight_kg=18.1,
                    max_height_cm=102
                ),
                description="Can be used rear- or forward-facing."
            ),
            Product(
                name="High Chair",
                category="High Chair",
                requirements=ProductRequirement(
                    min_age_months=6, max_age_months=36,
                    min_weight_kg=7, max_weight_kg=15,
                    min_height_cm=65
                ),
                description="For feeding infants and toddlers."
            ),
            Product(
                name="Umbrella Stroller",
                category="Stroller",
                requirements=ProductRequirement(
                    min_age_months=6, max_age_months=48,
                    min_weight_kg=7, max_weight_kg=22.7,
                    min_height_cm=65
                ),
                description="Lightweight stroller for travel."
            ),
        ]

    def find_product_by_name(self, name: str) -> Optional[Product]:
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
        return None

    def list_products(self) -> List[Product]:
        return self.products

