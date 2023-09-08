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

    def test_pipline_test_total_test_round(self):
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

    def test_pipline_test_with_exception(self):
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
            p.execute()
        except Exception as e:
            pass

        assert p.test_steps_instance_list[0].fail_msg
        print(p.test_steps_instance_list[0].fail_msg)

    def test_pipline_test_get_elapsed(self):
        class TestStep(BaseTestStep):
            url = "/api/test"
            method = "POST"

        class HttpPiplineTest(BasePipLineTest):
            description: str = "test"
            test_steps_list: List[TestStep] = [
                TestStep,
            ]

        p = HttpPiplineTest(host="http://127.0.0.1:5001")
        p.execute()
        assert p.test_steps_instance_list[0].elapsed_milliseconds

    def test_pipline_collect_test_step_datas(self):
        class TestStep(BaseTestStep):
            url = "/api/test"
            method = "POST"

        class HttpPiplineTest(BasePipLineTest):
            description: str = "test"
            test_steps_list: List[TestStep] = [
                TestStep,
            ]

        import csv
        from pathlib import Path

        header = [
            "url",
            "method",
            "data",
            "time_elapsed(ms)",
        ]
        with open("files/test.csv", "w", encoding="utf-8") as f:
            f_csv = csv.writer(f)
            f_csv.writerow(header)

        p = HttpPiplineTest(
            host="http://127.0.0.1:5001",
            datas_csv_title_attribute=["url", "method", "body", "elapsed_milliseconds"],
        )
        p.execute()
        p.write_test_steps_http_statics_data(Path("files/test.csv"))

    def test_pipline_test_with_seconds_sleep(self):
        class TestStep(BaseTestStep):
            url = "/api/test"
            method = "POST"

        class HttpPiplineTest(BasePipLineTest):
            description: str = "test"
            sleep_seconds_every_test_step: int = 2
            test_steps_list: List[TestStep] = [TestStep, TestStep]

        p = HttpPiplineTest(host="http://127.0.0.1:5001")
        p.execute()
        assert p.test_steps_instance_list[0].elapsed_milliseconds
