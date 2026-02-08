from engine import EtcherEngine

engine = EtcherEngine()

options = {
    "add": engine.add_text,
    "undo": engine.undo,
    "redo": engine.redo,
    "state": engine.get_state,
}

while True:
    command = input("Enter command (add/undo/redo/state/exit): ").strip()
    if command == "exit":
        break
    elif command == "add":
        text = input("Enter text to add: ")
        options[command](text) 
        print("Text added.")
    elif command in options:
        result = options[command]()
        if result is not None:
            print(f"Result: {result}")
        else:
            print("No history/nothing to show.")
    else:
        print("Invalid command.")