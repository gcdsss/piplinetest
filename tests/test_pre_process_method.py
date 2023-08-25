from piplinetest import BaseTestStep


class TestPreProcessMethod(object):
    def test_pre_process_method(self):
        class HttpTestStep(BaseTestStep):
            description: str = "test"
            url: str = "/api/request_log"
            method: str = "GET"
            headers: dict = {}
            process_methods_prefix = "tests.process_methods."
            pre_process_method = "pre_process:process_nothing"

        p = HttpTestStep()
        p.execute(
            {
                "host": "http://127.0.0.1:5001",
            }
        )

    def test_after_process_method(self):
        class HttpTestStep(BaseTestStep):
            description: str = "test"
            url: str = "/api/request_log"
            method: str = "GET"
            headers: dict = {}
            process_methods_prefix = "tests.process_methods."
            after_process_method = "after_process:process_nothing"

        p = HttpTestStep()
        p.execute(
            {
                "host": "http://127.0.0.1:5001",
            }
        )
        assert not p.body
