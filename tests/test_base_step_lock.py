from typing import List

from piplinetest import BasePipLineTest, BaseTestStep, lock_decorator


class TestBaseStepLock(object):
    def test_base_step_lock(self):
        @lock_decorator(lock_type="thread")
        class HttpTestStep(BaseTestStep):
            description = "test"
            url = "/api/test"
            method = "POST"

        class HttpPiplineTest(BasePipLineTest):
            description = "test"
            test_steps_list: List[HttpTestStep] = [
                HttpTestStep,
            ]

        t = HttpPiplineTest(host="http://127.0.0.1:5001")
        t.execute()
