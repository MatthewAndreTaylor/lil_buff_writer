# Example usage
async def main():
    messages = [
        ("test", b"hello"),
        ("data", b"world"),
        ("chunked", b"message"),
        ("another", b""),
        ("last", b"bye"),
    ]
    await write_messages(messages, "data.bin")

    with open("data.bin", "rb") as f:
        for i, (name, content) in enumerate(each_chunk(f)):
            print(name.decode(), content.decode())

            assert name == messages[i][0].encode() and content == messages[i][1]


if __name__ == "__main__":
    asyncio.run(main())