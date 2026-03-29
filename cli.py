from rich.console import Console
from rich.table import Table
from bot.orders import place_order
from bot.validators import *
from bot.logging_config import setup_logger
from bot.client import get_client

console = Console()
setup_logger()
client = get_client()

def get_price(symbol):
    try:
        ticker = client.futures_symbol_ticker(symbol=symbol)
        return ticker["price"]
    except:
        return "N/A"

def main():
    console.print("\n[bold cyan]📊 Binance Trading Bot[/bold cyan]")

    table = Table(title="Menu", show_lines=True)

    table.add_column("Option", justify="center", width=10)
    table.add_column("Action", justify="center", width=30)

    table.add_row("1", "Market Order")
    table.add_row("2", "Limit Order")
    table.add_row("3", "View Order History")

    console.print(table)

    choice = input("Enter choice (1/2/3): ")

    try:
        symbol = input("Symbol (BTCUSDT): ").upper()
        side = input("Side (BUY/SELL): ").upper()
        quantity = float(input("Quantity: "))

        live_price = get_price(symbol)
        console.print(f"[yellow]Live Price:[/yellow] {live_price}")

        if choice == "1":
            order_type = "MARKET"
            price = None

        elif choice == "2":
            order_type = "LIMIT"
            price = float(input("Enter price: "))

        elif choice == "3":
            from history import show_logs
            show_logs()
            return
        
        else:
            console.print("[red]Invalid choice[/red]")
            return

        validate_side(side)
        validate_type(order_type)
        validate_qty(quantity)
        validate_price(price, order_type)

        console.print("\n[bold green]📌 Order Summary[/bold green]")
        console.print(f"{symbol} | {side} | {order_type} | Qty: {quantity} | Price: {price}")

        order = place_order(symbol, side, order_type, quantity, price)

        console.print("\n[bold green]✅ SUCCESS[/bold green]")
        console.print(f"Order ID: {order.get('orderId')}")
        console.print(f"Status: {order.get('status')}")

    except Exception as e:
        console.print(f"[bold red]❌ ERROR:[/bold red] {str(e)}")

if __name__ == "__main__":
    main()