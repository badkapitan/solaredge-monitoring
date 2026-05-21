import logging
import asyncio
from pymodbus.client import AsyncModbusTcpClient

logging.getLogger("pymodbus").setLevel(logging.CRITICAL)

MAX_CONCURRENT = 10
semaphore = asyncio.Semaphore(MAX_CONCURRENT)

async def check_slave(device_id):
    async with semaphore:
        client = AsyncModbusTcpClient("192.168.1.50", port=502, timeout=1, retries=1)
        await client.connect()

        try:
            address = 40001
            count = 10
            result = await client.read_holding_registers(address=address - 40001, count=count, device_id=device_id)

            if result.isError():
                print(f"Błąd: {result}")
            else:
                print(f"[ID: {device_id}] {result}")
                # print(f"[DEVICE_ID: {device_id}] {result.registers}")
        except Exception as exc:
            print(f"[ID {device_id}] no device or error")
            pass
            # print(exc)
        finally:
            client.close()

async def main():
    tasks = [check_slave(i) for i in list(range(1, 10)) + list(range(120, 130))]
    await asyncio.gather(*tasks)
    # results = await asyncio.gather(*tasks)

    # found = [x for x in results if x is not None]
    # print(found)

asyncio.run(main())
