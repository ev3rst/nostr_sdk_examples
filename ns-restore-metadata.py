#!/usr/bin/env python3

import asyncio
import argparse
import json
from nostr_sdk import Metadata, Client, NostrSigner, Keys, init_logger, LogLevel

async def write_metadata(secret_key, profile_data):
    try:
        init_logger(LogLevel.INFO)
        keys = Keys.parse(secret_key)
        signer = NostrSigner.keys(keys)
        client = Client(signer)
        public_key = keys.public_key()
        print(f"Public key (npub): {public_key.to_bech32()}")

        # Add relays
        await client.add_relay("wss://relay.damus.io")
        await client.connect()

        # Parse profile content
        profile_content = json.loads(profile_data['content'])

        # Update metadata
        new_metadata = Metadata()\
            .set_name(profile_content.get('name', '')) \
            .set_picture(profile_content.get('picture', '')) \
            .set_banner(profile_content.get('banner', '')) \
            .set_about(profile_content.get('about', ''))
        
        await client.set_metadata(new_metadata)
        print("Metadata updated successfully.")
    except Exception as e:
        print(f"An error occurred in update_metadata: {e}")
        raise

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Forcing user metadata using Nostr SDK.')
    parser.add_argument('json_file', type=str, help='Path to the JSON file containing profile data.')
    args = parser.parse_args()

    with open(args.json_file, 'r') as file:
        profile_data_list = json.load(file)

    # Assuming the first profile in the JSON file is the one to be updated
    profile_data = profile_data_list[0]

    # Replace with actual secret key
    secret_key = "nsec_key" 

    asyncio.run(write_metadata(secret_key, profile_data))