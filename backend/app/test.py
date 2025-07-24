from database import db

def upsert_test_row():

    params = {
        "tracking_number": 987654,
    }

    query = f"UPSERT INTO packages (tracking_number, status, warehouse_number, product_name, pickup_address) VALUES (123,123,123,123,123);"

    db.execute(query)
    print("🟢 Test package upserted successfully.")

def select_all_rows():
    query = "SELECT * FROM packages;"

    result = db.execute(query)
    print("📦 All packages in DB:")
    for row in result[0].rows:
        print(row)

if __name__ == "__main__":
    try:
        upsert_test_row()
        select_all_rows()
    except Exception as e:
        print("❌ Error during DB test:", e)
