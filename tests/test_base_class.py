from typing import List

from piplinetest import BasePipLineTest, BaseTestStep


class TestPiplineTest(object):
    def test_teststep(self):
        class HttpTestStep(BaseTestStep):
            description: str = "test"
            url: str = "/api/test"
            method: str = "POST"
            headers: dict = {}

        p = HttpTestStep()
        p.execute(
            {
                "host": "http://127.0.0.1:5001",
            }
        )
        assert p.body == {"test": 1}

    def test_pipline_test(self):
        class HttpTestStep(BaseTestStep):
            description: str = "test"
            url: str = "/api/test"
            method: str = "POST"
            body: dict = {"test": 1}
            headers: dict = {}

        class HttpPiplineTest(BasePipLineTest):
            description: str = "pis病例主流程"
            test_steps_list: List[HttpTestStep] = [
                HttpTestStep,
            ]

        p = HttpPiplineTest(name="test", host="http://127.0.0.1:5001")
        p.execute()

    def test_pipline_test_with_body(self):
        class HttpTestStep(BaseTestStep):
            description: str = "test"
            url: str = "/api/test"
            method: str = "POST"
            headers: dict = {}
            body: str = "data_templates/case_store.json"
            process_methods_prefix = "tests.process_methods."

        class HttpPiplineTest(BasePipLineTest):
            description: str = "pis病例主流程"
            test_steps_list: List[HttpTestStep] = [
                HttpTestStep,
            ]

        p = HttpPiplineTest(name="test", host="http://127.0.0.1:5001")
        p.execute()
