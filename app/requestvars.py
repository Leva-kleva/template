import contextvars
import types
import typing

request_global = contextvars.ContextVar("request_global",
                                        default=types.SimpleNamespace())


def g():
    return request_global.get()
