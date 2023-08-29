# Piplinetest

基于pydantic的http流水线测试类

## 项目概述

这个项目包含了一些用于构建测试步骤和测试类的基类。

## 安装

pip install piplinetest

你可以使用以下命令安装依赖：

## 使用方法
导入所需的类和函数：
```
# 创建测试步骤：
from piplinetest import BaseTestStep, BasePipLineTest

class HttpTestStep(BaseTestStep):
            description: str = "test"
            url: str = "/api/request_log"
            method: str = "GET"
            headers: dict = {}
            process_methods_prefix = "tests.process_methods."
            pre_process_method = "pre_process:process_nothing"

# 创建测试类实例：
class HttpPiplineTest(BasePipLineTest):
            description: str = "test"
            test_steps_list: List[HttpTestStep] = [
                HttpTestStep,
            ]
# 执行测试类：
t = HttpPiplineTest(host="http://127.0.0.1:5001")
t.execute()
```
贡献
欢迎贡献代码和提出问题。你可以通过以下方式参与项目：

Fork 项目
创建一个新的分支 (git checkout -b feature/your-feature)
提交你的改动 (git commit -am 'Add some feature')
推送到分支 (git push origin feature/your-feature)
提交一个 Pull Request