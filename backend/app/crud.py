from .schemas import PackageCreate, PackageRead

def create_package(package: PackageCreate):
    with ydb.SessionPool(driver) as session_pool:
        def insert(session):
            session.transaction(ydb.SerializableReadWrite()).execute(
                """
                INSERT INTO packages (tracking_number, status, warehouse_number, product_name, pickup_address)
                VALUES (?, ?, ?, ?, ?)
                """,
                parameters=(
                    package.tracking_number,
                    package.status,
                    package.warehouse_number,
                    package.product_name,
                    package.pickup_address
                ),
                commit_tx=True
            )
        session_pool.retry_operation_sync(insert)
        return package

def get_package_by_tracking(tracking_number: str):
    with ydb.SessionPool(driver) as session_pool:
        def select(session):
            result_sets = session.transaction().execute(
                """
                SELECT * FROM packages WHERE tracking_number = ?
                """,
                parameters=(tracking_number,),
                commit_tx=True
            )
            result = list(result_sets[0].rows)
            return result[0] if result else None
        return session_pool.retry_operation_sync(select)
