from typing import List

from piplinetest import BasePipLineTest, BaseTestStep


class TestPiplineTest(object):
    def test_pipline_test(self):
        class HttpTestStep(BaseTestStep):
            description: str = "test"
            url: str = "/api/test"
            method: str = "POST"
            headers: dict = {}

        class HttpPiplineTest(BasePipLineTest):
            description: str = "test"
            test_steps_list: List[HttpTestStep] = [
                HttpTestStep,
            ]

        t = HttpPiplineTest(host="http://127.0.0.1:5001")
        t.execute()
        assert t.test_steps_instance_list[0].body == {
            "status_code": 200,
            "code": 1,
            "data": {},
            "message": None,
            "meta": None,
        }

    def test_pipline_test_with_body(self):
        class HttpTestStep(BaseTestStep):
            description: str = "test"
            url: str = "/api/test"
            method: str = "POST"
            headers: dict = {}
            body_template_json_path: str = "data_templates/case_store.json"
            process_methods_prefix = "tests.process_methods."

        class HttpPiplineTest(BasePipLineTest):
            description: str = "test"
            test_steps_list: List[HttpTestStep] = [
                HttpTestStep,
            ]

        t = HttpPiplineTest(name="test", host="http://127.0.0.1:5001")
        t.execute()
        assert t.test_steps_instance_list[0].body
        print(t.test_steps_instance_list[0].body)

    def test_piplien_test_total_test_round(self):
        class HttpTestStep(BaseTestStep):
            description: str = "test"
            url: str = "/api/test"
            method: str = "POST"
            headers: dict = {}
            body_template_json_path: str = "data_templates/case_store.json"
            process_methods_prefix = "tests.process_methods."

        class HttpPiplineTest(BasePipLineTest):
            description: str = "test"
            total_execute_round = 2
            test_steps_list: List[HttpTestStep] = [
                HttpTestStep,
            ]

        t = HttpPiplineTest(name="test", host="http://127.0.0.1:5001")
        t.execute()
        assert len(t.test_steps_instance_list) == 2
