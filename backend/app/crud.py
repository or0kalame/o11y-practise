from database import db
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

def upsert_package(data: dict):
    with tracer.start_as_current_span("CRUD: Upsert Package") as span:
        span.set_attribute("app.tracking_number", data.get("tracking_number"))
        span.set_attribute("app.status", data.get("status"))
        
        query = """
        DECLARE $tracking_number AS Utf8;
        DECLARE $status AS Utf8;
        DECLARE $warehouse_number AS Utf8;
        DECLARE $product_name AS Utf8;

        UPSERT INTO packages (
            tracking_number,
            status,
            warehouse_number,
            product_name
        ) VALUES (
            $tracking_number,
            $status,
            $warehouse_number,
            $product_name
        );
        """

        params = {
            "$tracking_number": data.get("tracking_number"),
            "$status": data.get("status"),
            "$warehouse_number": data.get("warehouse_number"),
            "$product_name": data.get("product_name"),
        }

        db.execute(query, params)

def get_package(tracking_number: str):
     with tracer.start_as_current_span("CRUD: Get Package") as span:
        span.set_attribute("app.tracking_number", tracking_number)
        
        query = """
        DECLARE $tracking_number As Utf8;

        SELECT * FROM packages WHERE tracking_number = $tracking_number;
        """
        result = db.execute(query, {"$tracking_number": tracking_number})
        return result[0].rows if result else []

def get_all_tracking_numbers():
    with tracer.start_as_current_span("CRUD: Get All Tracking Numbers"):
        query = "SELECT tracking_number FROM packages;"
        result = db.execute(query)
        rows = result[0].rows if result else []
        return [row["tracking_number"] for row in rows if row["tracking_number"] != "string"]