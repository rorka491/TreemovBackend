import asyncio
import sys
from app.constants import commands


async def main():
    if len(sys.argv) < 2:
        print("Usage: python manage.py <command>")
        return

    command = commands.get(sys.argv[1])
    if command: await command()
    else: print(f"Unknown command: {command}")


if __name__ == "__main__":
    asyncio.run(main())



