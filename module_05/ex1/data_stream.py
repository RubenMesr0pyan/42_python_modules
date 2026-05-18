from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = list()
        self._current_rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        return self._storage.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True
        if isinstance(data, list):
            return all(
                isinstance(item,
                           (int,
                            float)) and not isinstance(item,
                                                       bool) for item in data
                )
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, list):
            for item in data:
                self._storage.append((self._current_rank, str(item)))
                self._current_rank += 1
        else:
            self._storage.append((self._current_rank, str(data)))
            self._current_rank += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise TypeError("Improper text data")

        if isinstance(data, str):
            self._storage.append((self._current_rank, data))
            self._current_rank += 1
        elif isinstance(data, list):
            for item in data:
                self._storage.append((self._current_rank, item))
                self._current_rank += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return all(isinstance(k, str) and isinstance(v, str) for k,
                       v in data.items())
        if isinstance(data, list):
            return all(
                isinstance(item, dict) and
                all(isinstance(k, str) and isinstance(v, str) for k,
                    v in item.items())
                for item in data
            )
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise TypeError("Improper log data")

        if isinstance(data, dict):
            self._storage.append((self._current_rank, str(data)))
            self._current_rank += 1
        elif isinstance(data, list):
            for item in data:
                self._storage.append((self._current_rank, str(item)))
                self._current_rank += 1


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proces: DataProcessor) -> None:
        self._processors.append(proces)

    def process_stream(self, stream: list[Any]) -> None:
        for elm in stream:
            done = False
            for proc in self._processors:
                if proc.validate(elm):
                    proc.ingest(elm)
                    done = True
                    break
            if not done:
                print(f"DataStream error - Can't process element in stream: "
                      f"{elm}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            name = type(proc).__name__.replace("Processor", " Processor")
            total = proc._current_rank
            remaining = len(proc._storage)
            print(f"{name}: total {total} items processed, "
                  f"remaining {remaining} on processor")


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")
    print("Initialize Data Stream...")
    ds = DataStream()
    ds.print_processors_stats()
    print("Registering Numeric Processor")
    num_proc = NumericProcessor()
    ds.register_processor(num_proc)
    data_list = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {'log_level': 'WARNING',
             'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO',
             'log_message': 'User wil is connected'}
        ],
        42,
        ['Hi', 'five']
    ]
    print("Send first batch of data on stream: " + str(data_list))
    ds.process_stream(data_list)
    ds.print_processors_stats()
    print("Registering other data processors")
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    ds.register_processor(text_proc)
    ds.register_processor(log_proc)
    print("Send the same batch again")
    ds.process_stream(data_list)
    ds.print_processors_stats()
    print("Consume some elements from the data processors: "
          "Numeric 3, Text 2, Log 1")
    for _ in range(3):
        num_proc.output()
    for _ in range(2):
        text_proc.output()
    for _ in range(1):
        log_proc.output()
    ds.print_processors_stats()
