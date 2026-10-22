# Kitchen Concurrency Coordination Example

This example simulates multiple chefs (threads) working concurrently in a restaurant kitchen. It demonstrates how a simple coordination mechanism, inspired by the "Behind!" command used in real kitchens, prevents collisions and ensures safe access to shared critical zones. Each chef acquires a lock (shouts "Behind!") before entering a narrow passageway, ensuring only one chef is present at a time, thus preventing errors in concurrent operations.

## Language

`python`

## How to Run

Save the code as `main.py`.
Run from your terminal: `python main.py`

## Original Article

This example accompanies the Turkish article: [Restoran Mutfağından Paralel Kodlama Ajanlarına: "Behind!" Komutunun Gücü](https://fatihsoysal.com/blog/restoran-mutfagindan-paralel-kodlama-ajanlarina-behind-komutunun-gucu/).

## License

MIT — see [LICENSE](LICENSE).
