from abc import ABC, abstractmethod
from typing import Any, Protocol


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
            msg = f"{data['log_level']}: {data['log_message']}"
            self._storage.append((self._current_rank, msg))
            self._current_rank += 1
        elif isinstance(data, list):
            for item in data:
                msg = f"{item['log_level']}: {item['log_message']}"
                self._storage.append((self._current_rank, msg))
                self._current_rank += 1


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            extracted_data = []
            items_to_pop = min(nb, len(proc._storage))
            for _ in range(items_to_pop):
                extracted_data.append(proc.output())
            if extracted_data:
                plugin.process_output(extracted_data)


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        if not data:
            return
        print("CSV Output:")
        value = [item[1] for item in data]
        print(",".join(value))


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        if not data:
            return
        print("JSON Output:")
        json_parts = []
        for rank, value in data:
            json_parts.append(f'"item_{rank}": "{value}"')
        json_str = "{" + ", ".join(json_parts) + "}"
        print(json_str)


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")
    print("Initialize Data Stream...")
    ds = DataStream()
    ds.print_processors_stats()

    print("Registering Processors")
    ds.register_processor(NumericProcessor())
    ds.register_processor(TextProcessor())
    ds.register_processor(LogProcessor())

    batch_1 = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING', 'log_message':
          'Telnet access! Use ssh instead'},
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five']
    ]

    print("Send first batch of data on stream: " + str(batch_1))
    ds.process_stream(batch_1)
    ds.print_processors_stats()

    print("Send 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExportPlugin()
    ds.output_pipeline(3, csv_plugin)
    ds.print_processors_stats()

    batch_2 = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [{'log_level': 'ERROR', 'log_message': '500 server crash'},
         {'log_level': 'NOTICE', 'log_message':
          'Certificate expires in 10 days'}],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]

    print("Send another batch of data: " + str(batch_2))
    ds.process_stream(batch_2)
    ds.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONExportPlugin()
    ds.output_pipeline(5, json_plugin)
    ds.print_processors_stats()
