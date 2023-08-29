from typing import List

from piplinetest import BaseTestStep, BasePipLineTest


class TestPreProcessMethod(object):
    def test_pre_process_method(self):
        class HttpTestStep(BaseTestStep):
            description: str = "test"
            url: str = "/api/request_log"
            method: str = "GET"
            headers: dict = {}
            process_methods_prefix = "tests.process_methods."
            pre_process_method = "pre_process:process_nothing"

        class HttpPiplineTest(BasePipLineTest):
            description: str = "test"
            test_steps_list: List[HttpTestStep] = [
                HttpTestStep,
            ]

        t = HttpPiplineTest(host="http://127.0.0.1:5001")
        t.execute()

    def test_after_process_method(self):
        class HttpTestStep(BaseTestStep):
            description: str = "test"
            url: str = "/api/test"
            method: str = "POST"
            headers: dict = {}
            process_methods_prefix = "tests.process_methods."
            after_process_method = "after_process:process_nothing"

        class HttpPiplineTest(BasePipLineTest):
            description: str = "test"
            test_steps_list: List[HttpTestStep] = [
                HttpTestStep,
            ]

        t = HttpPiplineTest(host="http://127.0.0.1:5001")
        t.execute()
        assert not t.test_steps_instance_list[0].body

    def test_after_process_method_modify(self):
        class HttpTestStep(BaseTestStep):
            description: str = "test"
            url: str = "/api/test"
            method: str = "POST"
            headers: dict = {}
            process_methods_prefix = "tests.process_methods."
            after_process_method = "after_process:add_something_to_test_step_header"

        class HttpPiplineTest(BasePipLineTest):
            description: str = "test"
            test_steps_list: List[HttpTestStep] = [
                HttpTestStep,
            ]

        t = HttpPiplineTest(host="http://127.0.0.1:5001")
        t.execute()
        assert t.test_steps_instance_list[0].headers["test"] == 1

    def test_after_process_get_http_token(self):
        class HttpTestStep(BaseTestStep):
            description: str = "test"
            url: str = "/api/login"
            method: str = "POST"
            headers: dict = {}
            process_methods_prefix = "tests.process_methods."
            pre_process_method = "pre_process:send_http_token"
            after_process_method = "after_process:add_http_token_to_headers"

        class HttpPiplineTest(BasePipLineTest):
            username: str = "gui"
            password: str = "guichangdi"
            description: str = "test"
            test_steps_list: List[HttpTestStep] = [
                HttpTestStep,
            ]

        t = HttpPiplineTest(host="http://127.0.0.1:5001")
        t.execute()
        assert t.test_steps_instance_list[0].headers["Authorization"]
