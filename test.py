# data/cart.txt
[
    {
        "product_id": "PRD-0000",
        "product_name": "Deep Work Book ",
        "req_quantity": 10,
        "price": 150,
        "product_type": 1,
    },
    {
        "product_id": "PPR-0004",
        "product_name": "Pure Silk White Shirt",
        "req_quantity": 1,
        "price": 4000,
        "product_type": 4,
    },
]

# data/products.txt
[
    {
        "product_id": "PRD-0000",
        "product_name": "Deep Work Book ",
        "quantity": 100,
        "price": 150,
        "product_type": 1,
    },
    {
        "product_id": "PRD-0001",
        "product_name": "A4 Size Papers Sheet",
        "quantity": 200,
        "price": 100,
        "product_type": 1,
    },
    {
        "product_id": "PPR-0002",
        "product_name": "Milk Premium",
        "quantity": 250,
        "price": 90,
        "expiry_date": "10 May 2026",
        "product_type": 2,
    },
    {
        "product_id": "PPR-0003",
        "product_name": "Apple Iphone 17 Pro Max",
        "quantity": 1000,
        "price": 150000,
        "warranty_months": 36,
        "product_type": 3,
    },
    {
        "product_id": "PPR-0004",
        "product_name": "Pure Silk White Shirt",
        "quantity": 1000,
        "price": 4000,
        "size": "M",
        "material": "Silk",
        "product_type": 4,
    },
]

# data/coupons.txt
[
    {
        "coupon_code": "SAVE10",
        "coupon_type": 1,
        "value": 10,
        "min_order": 10000,
        "expiry_date": "2026-05-31",
        "usage_limit": 100,
        "status": "active",
    },
    {
        "coupon_code": "SAVE20",
        "coupon_type": 1,
        "value": 20,
        "min_order": 20000,
        "expiry_date": "2026-05-31",
        "usage_limit": 50,
        "status": "active",
    },
    {
        "coupon_code": "SAVE30",
        "coupon_type": 1,
        "value": 30,
        "min_order": 30000,
        "expiry_date": "2026-05-31",
        "usage_limit": 10,
        "status": "active",
    },
]

# data/coupons_logs.txt
[
    "2026-05-01 22:05:52.323884 | 1777653352.323884 | Coupon SAVE10 created!",
    "2026-05-01 22:06:14.557074 | 1777653374.557074 | Coupon SAVE20 created!",
    "2026-05-01 22:06:38.204840 | 1777653398.20484 | Coupon SAVE30 created!",
]
