from pymodbus.client import ModbusTcpClient

# Ustawienia połączenia
client = ModbusTcpClient("192.168.1.20", port=1502)
client.connect()

try:
    # Wysłanie requestu i odczyt rejestrów
    address = 40001
    count = 10
    result = client.read_holding_registers(address=address - 40001, count=count, device_id=126)


    # Wyświetlenie wyników
    if result.isError():
        print(f"Błąd: {result}")
    else:
        print(result.registers)
except Exception as exc:
    print(exc)

# Zamknięcie połączenia
client.close()
