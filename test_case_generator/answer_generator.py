import io
import sys
from contextlib import redirect_stdout
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from submissions.correct_solutions.sol2 import solve


dirs = ("sample", "secret")


def generate_answers() -> None:
    for directory_name in dirs:
        directory = REPOSITORY_ROOT / "data" / directory_name
        for input_path in sorted(directory.glob("*.in")):
            input_stream = io.TextIOWrapper(
                io.BytesIO(input_path.read_bytes()), encoding="utf-8"
            )
            output_stream = io.StringIO()

            previous_stdin = sys.stdin
            sys.stdin = input_stream
            try:
                with redirect_stdout(output_stream):
                    solve()
            finally:
                sys.stdin = previous_stdin
                input_stream.close()

            output = output_stream.getvalue()
            
            input_path.with_suffix(".ans").write_text(output, encoding="utf-8")


if __name__ == "__main__":
    generate_answers()


