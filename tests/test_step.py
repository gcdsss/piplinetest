from typing import List

from piplinetest import BaseTestStep, BasePipLineTest


class TestStep(object):
    def test_step_url_format(self):
        class TestStep(BaseTestStep):
            url = "/api/test/{pathology_id}/{case_id}"
            method = "POST"

        class HttpPiplineTest(BasePipLineTest):
            pathology_id = "123"
            case_id = "456"
            description: str = "test"
            test_steps_list: List[TestStep] = [
                TestStep,
            ]

        t = TestStep()
        p = HttpPiplineTest(host="http://127.0.0.1:5000")
        t._format_url(p)
        assert t.url == "/api/test/123/456"

    def test_step_with_exception(self):
        class TestStep(BaseTestStep):
            url = "/api/test1"
            method = "POST"

        class HttpPiplineTest(BasePipLineTest):
            description: str = "test"
            test_steps_list: List[TestStep] = [
                TestStep,
            ]

        t = TestStep()
        p = HttpPiplineTest(host="http://127.0.0.1:5001")
        try:
            t.execute(p)
        except Exception as e:
            pass
            assert t.fail_msg == e.__str__()
