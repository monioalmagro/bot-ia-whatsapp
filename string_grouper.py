import threading
import time


class StringGrouper:
    def __init__(self):
        self.strings = []
        self.lock = threading.Lock()

    def collect_strings(self, string):
        with self.lock:
            self.strings.append(string)

    def gather_strings(self):
        time.sleep(5)
        with self.lock:
            grouped_strings = self.strings.copy()
            self.strings.clear()
        return grouped_strings


def string_input_thread(string_grouper):
    while True:
        user_input = input(
            "Ingrese una cadena (o presione Enter para finalizar): "
        )
        if user_input == "":
            break
        string_grouper.collect_strings(user_input)


if __name__ == "__main__":
    string_grouper = StringGrouper()
    input_thread = threading.Thread(
        target=string_input_thread, args=(string_grouper,)
    )
    input_thread.start()

    print("Recopilando cadenas durante 5 segundos...")
    input_thread.join(timeout=5)

    grouped_strings = string_grouper.gather_strings()
    print(f"Cadenas recopiladas: {grouped_strings}")
