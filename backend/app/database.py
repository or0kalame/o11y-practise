import ydb
import ydb.iam

with open('/home/user/ydbd/ydb_certs/cert.pem') as f:
    root_cert = f.read()

driver_config = ydb.DriverConfig(
    endpoint="grpc://localhost:2136/",
    database="/local",
    credentials=ydb.AnonymousCredentials()
)

with ydb.Driver(driver_config) as driver:
    try:
        driver.wait(fail_fast=True, timeout=10)
    except TimeoutError:
            print("Connect failed to YDB")
            print("Last reported errors by discovery:")
            print(driver.discovery_debug_details())
            exit(1)
