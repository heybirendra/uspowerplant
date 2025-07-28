from fastapi.responses import JSONResponse
import json

class PrettyJson(JSONResponse):
    def render(self, content: any) -> bytes:
        return json.dumps(
            content,
            ensure_ascii=False,
            allow_nan=False,
            indent=2
        ).encode("utf-8")