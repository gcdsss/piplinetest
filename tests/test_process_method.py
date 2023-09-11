from typing import List

from piplinetest import BaseTestStep, BasePipLineTest


class TestPreProcessMethod(object):
    def test_pre_process_method(self):
        class HttpTestStep(BaseTestStep):
            description = "test"
            url = "/api/request_log"
            method = "GET"
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
            description = "test"
            url = "/api/test"
            method = "POST"
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
            description = "test"
            url = "/api/test"
            method = "POST"
            process_methods_prefix = "tests.process_methods."
            after_process_method = "after_process:add_something_to_test_step_header"

        class HttpPiplineTest(BasePipLineTest):
            description = "test"
            test_steps_list: List[HttpTestStep] = [
                HttpTestStep,
            ]

        t = HttpPiplineTest(host="http://127.0.0.1:5001")
        t.execute()
        assert t.test_steps_instance_list[0].headers == {"test1": "1"}

    def test_after_process_get_http_token(self):
        class HttpTestStep(BaseTestStep):
            description = "test"
            url = "/api/login"
            method = "POST"
            process_methods_prefix = "tests.process_methods."
            pre_process_method = "pre_process:send_http_token"
            after_process_method = "after_process:add_http_token_to_headers"

        class HttpPiplineTest(BasePipLineTest):
            username = "gui"
            password = "guichangdi"
            description = "test"
            test_steps_list: List[HttpTestStep] = [
                HttpTestStep,
            ]

        t = HttpPiplineTest(host="http://127.0.0.1:5001")
        t.execute()
        assert t.test_steps_instance_list[0].headers["Authorization"]

    def test_mutiple_pre_process_method(self):
        class HttpTestStep(BaseTestStep):
            description: str = "test"
            url: str = "/api/test"
            method: str = "POST"
            process_methods_prefix = "tests.process_methods."
            pre_process_method = [
                "pre_process:modify_body",
                "pre_process:modify_header1",
                "pre_process:modify_header2",
                "pre_process:modify_test_class_attribute",
            ]

        class HttpPiplineTest(BasePipLineTest):
            description: str = "test"
            user_name = "test"
            test_steps_list: List[HttpTestStep] = [
                HttpTestStep,
            ]

        t = HttpPiplineTest(host="http://127.0.0.1:5001")
        t.execute()
        assert t.user_name == "test1"
        assert t.test_steps_instance_list[0].body["data"] == {"test": 1}
        assert t.test_steps_instance_list[0].headers == {"test1": "1", "test2": "2"}

    def test_mutiple_after_process_method(self):
        class HttpTestStep(BaseTestStep):
            description: str = "test"
            url: str = "/api/test"
            method: str = "POST"
            process_methods_prefix = "tests.process_methods."
            after_process_method = [
                "after_process:modify_http_res",
                "after_process:add_something_to_test_step_header",
                "after_process:add_something_to_test_step_header2",
                "after_process:modify_body",
                "pre_process:modify_test_class_attribute",
            ]

        class HttpPiplineTest(BasePipLineTest):
            description: str = "test"
            user_name = "test"
            test_steps_list: List[HttpTestStep] = [
                HttpTestStep,
            ]

        t = HttpPiplineTest(host="http://127.0.0.1:5001")
        t.execute()
        assert t.user_name == "test1"
        assert t.test_steps_instance_list[0].body == {"body_test": 1}
        assert t.test_steps_instance_list[0].headers == {"test1": "1", "test2": "2"}
