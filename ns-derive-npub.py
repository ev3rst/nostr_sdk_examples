import argparse
import asyncio
from nostr_sdk import Keys, init_logger, LogLevel

async def main(nsec):
    init_logger(LogLevel.INFO)
    keys = Keys.parse(nsec)
    public_key = keys.public_key()
    print(f"Public key (hex): {public_key.to_hex()}")
    print(f"Public key (npub): {public_key.to_bech32()}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fetch all relay from a given nsec')
    parser.add_argument('nsec', type=str, help='The nsec of the user')
    args = parser.parse_args()
    asyncio.run(main(args.nsec))
