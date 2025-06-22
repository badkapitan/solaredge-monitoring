from pymodbus.client import ModbusTcpClient

# Ustawienia połączenia
client = ModbusTcpClient("192.168.1.50", port=1502)
client.connect()

# Wysłanie requestu i odczyt rejestrów
address = 40001
count = 10
result = client.read_holding_registers(address - 40001, count, unit=1)

# Wyświetlenie wyników
if result.isError():
    print(f"Błąd: {result}")
else:
    print(result.registers)

# Zamknięcie połączenia
client.close()
