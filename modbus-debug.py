import logging
from pymodbus.client import ModbusTcpClient

logging.getLogger("pymodbus").setLevel(logging.CRITICAL)

# Ustawienia połączenia
# client = ModbusTcpClient("192.168.1.20", port=1502)
client = ModbusTcpClient("192.168.1.50", port=502, timeout=0.5, retries=0)
client.connect()

# for device_id in range(1, 248):
for device_id in [1, 126]:
    try:
        # Wysłanie requestu i odczyt rejestrów
        address = 40001
        count = 125
        result = client.read_holding_registers(address=address - 40001, count=count, device_id=device_id)

        # Wyświetlenie wyników
        if result.isError():
            print(f"Błąd: {result}")
        else:
            print(f"[ID: {device_id}] {result}")
            # print(f"[DEVICE_ID: {device_id}] {result.registers}")
    except Exception as exc:
        print(f"[ID {device_id}] no device or error")
        pass
        # print(exc)

# Zamknięcie połączenia
client.close()
