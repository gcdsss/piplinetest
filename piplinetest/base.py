from typing import Union, List, Any
from enum import Enum
from json import load

from pydantic import BaseModel, Field
from requests import Response

from .import_utils import import_lib
from .http_request import http_request


class TestStepTypeEnum(Enum):
    http_api = "http_api"
    ui = "ui"


class BaseTestStep(BaseModel):
    """base test step

    Args:
        BaseModel (_type_): every http test step
    """

    name: str = Field(title="test step name", default=None)
    url: str = Field(title="http api url")
    method: str = Field(title="http method like: GET|POST|PATCH")
    headers: Union[dict, None] = Field(title="http header", default=None)
    body_template_json_path: Union[str, None] = Field(
        title="if given, replace body with file path content", default=None
    )
    body: Union[dict, str, None] = Field(title="http body", default={})

    process_methods_prefix_split_char: str = Field(default=".")
    process_methods_prefix: str = Field(
        title="process method import prefix", default=None
    )
    pre_process_method: Union[str, None] = Field(
        title="process method call before send http", default=None
    )
    after_process_method: Union[str, None] = Field(
        title="process method call after send http", default=None
    )

    def _read_http_body(self):
        if self.body_template_json_path:
            with open(
                "/".join(
                    self.process_methods_prefix.split(
                        self.process_methods_prefix_split_char
                    )
                )
                + self.body_template_json_path,
                "r",
            ) as f:
                self.body = load(f)
        else:
            pass

    def _send_request_data(self, cls: "BasePipLineTest") -> Response:
        request_kwargs = {
            "http_url": cls.host + self.url,
            "method": self.method if self.method else None,
            "headers": self.headers,
        }
        if isinstance(self.body, (dict, list)):
            request_kwargs["json"] = self.body
        elif isinstance(self.body, str):
            request_kwargs["data"] = self.body
        else:
            pass

        return http_request(**request_kwargs)

    def execute(self, cls: "BasePipLineTest"):
        if self.pre_process_method is not None:
            pre_process_method = import_lib(
                self.process_methods_prefix + self.pre_process_method
            )
            if self.body_template_json_path:
                self._read_http_body()
            pre_process_method(piplinetest=cls, test_step=self)

        res = self._send_request_data(cls)

        if self.after_process_method is not None:
            after_process_method = import_lib(
                self.process_methods_prefix + self.after_process_method
            )
            self.body = after_process_method(
                piplinetest=cls,
                test_step=self,
                http_res_dict=res.json(),
            )
        else:
            self.body = res.json()


class BasePipLineTest(BaseModel):
    """base test class"""

    name: str = Field(title="test name", default=None)
    host: str = Field(title="http host")
    total_execute_round: int = Field(title="total execute round", default=1)
    test_arguments: Union[dict, None] = Field(title="execute arguments", default=None)
    test_steps_list: List[Any] = Field(title="test step lists to execute", default=[])
    test_steps_instance_list: List[Any] = Field(
        title="test step instance list", default=[]
    )

    def execute(self, http_headers={}, http_body={}):
        headers = http_headers
        body = http_body
        # init_dict.pop("test_steps_list")
        for x in self.test_steps_list:
            per_test_step = x(headers=headers, body=body)
            per_test_step.execute(self)
            headers = per_test_step.headers
            body = per_test_step.body
            self.test_steps_instance_list.append(per_test_step)
