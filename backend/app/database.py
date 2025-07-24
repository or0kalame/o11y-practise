import ydb

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

    def execute(self, query: str, params: dict = None):
        result_sets = self.pool.execute_with_retries(query, params)
        return result_sets

db = YDBClient()

