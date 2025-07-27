import ydb
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

class YDBClient:
    def __init__(self, endpoint="grpc://ydb:2136", database="/local"):
        self.driver_config = ydb.DriverConfig(
            endpoint=endpoint,
            database=database,
            credentials=ydb.AnonymousCredentials(),
        )
        self.driver = ydb.Driver(self.driver_config)
        self.driver.wait(timeout=10)
        self.pool = ydb.QuerySessionPool(self.driver)

    with tracer.start_as_current_span("YDB Query Execution") as span:
        span.set_attribute("db.system", "ydb")
        
        def execute(self, query: str, params: dict = None):
            result_sets = self.pool.execute_with_retries(query, params)
            return result_sets

db = YDBClient()