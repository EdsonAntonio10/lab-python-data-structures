
products = ["t-shirt", "mug", "hat", "book", "keychain"]

inventory = {}

for product in products:
    quantitz = int(input(f"Cantidad disponible de {product}: "))
    inventory[product] = quantitz

customer_orders = set()
print("Escribe los 3 productos que el cliente quiere ordenar:")

while len(customer_orders) < 3:
    order = input(f"Producto {len(customer_orders)+1}: ")
    if order in products:
        customer_orders.add(order)
    else:
        print("Producto no válido, intenta de nuevo.")

print("\nProductos pedidos por el cliente:", customer_orders)

total_products_ordered = len(customer_orders)
percentage_ordered = (total_products_ordered / len(products)) * 100
order_status = (total_products_ordered, percentage_ordered)

print("\nOrder Statistics:")
print(f"Total Products Ordered: {total_products_ordered}")
print(f"Percentage of Products Ordered: {percentage_ordered:.2f}%")

for product in customer_orders:
    inventory[product] -= 1

print("\nInventario actualizado:")
for product, quantitz in inventory.items():
    print(f"{product}: {quantitz}")
