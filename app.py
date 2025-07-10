import os
from flask import Flask, render_template, request
from child_safety_checker import SafetyChecker, Child

app = Flask(__name__)
checker = SafetyChecker()

@app.route("/", methods=["GET"])
def home():
    products = checker.list_products()
    return render_template('index.html', products=products)

@app.route("/results", methods=["POST"])
def check():
    # Get form data
    name = request.form.get('name', 'Child')
    age_months = int(request.form.get('age_months', 0))
    weight_kg = float(request.form.get('weight_kg', 0))
    height_cm = float(request.form.get('height_cm', 0))
    product_name = request.form.get('product')

    # Create child and find product
    child = Child(name, age_months, weight_kg, height_cm)
    product = checker.find_product_by_name(product_name)

    # Run safety check
    is_compatible, issues = checker.check_compatibility(child, product)

    return render_template(
        'results.html',
        child=child,
        product=product,
        is_compatible=is_compatible,
        issues=issues
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False) 