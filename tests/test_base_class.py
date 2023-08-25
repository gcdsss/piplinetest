from typing import List

from piplinetest import BasePipLineTest, BaseTestStep


class TestPiplineTest(object):

    def test_teststep(self):

        class HttpTestStep(BaseTestStep):
            description: str = "test"
            url: str = "/api/request_log"
            method: str = "GET"
            headers: dict = {}

        p = HttpTestStep()
        p.execute({
            "host": "http://127.0.0.1:5001",
        })
        print(p.body)

    def test_pipline_test(self):

        class HttpTestStep(BaseTestStep):
            description: str = "test"
            url: str = "/api/request_log"
            method: str = "GET"
            headers: dict = {}

        class HttpPiplineTest(BasePipLineTest):
            description: str = "pis病例主流程"
            test_steps_list: List[HttpTestStep] = [
                HttpTestStep,
            ]

        p = HttpPiplineTest(
            name="test",
            host="http://127.0.0.1:5001"
        )
        p.execute()
