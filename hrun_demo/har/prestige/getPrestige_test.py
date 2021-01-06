# NOTE: Generated By HttpRunner v3.1.4
# FROM: har/prestige/getPrestige.har


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from hrun_demo.loginByEmailPassword_test import TestCaseLoginbyemailpassword


class TestCaseGetprestige(HttpRunner):

    config = Config("testcase description").base_url("${ENV(BASE_URL_PRE)}").verify(False)

    teststeps = [
        Step(
            RunTestCase("登录")
                .call(TestCaseLoginbyemailpassword)

        ),
        Step(
            RunRequest("获取个人声望")
            .get(
                "/1/7.5.28/bplapi/fame/v1/getUserFameLogDetails/52498468"
            )
            .with_params(**{"lastlogid": "0", "limit": "20"})
            .with_headers(
                **{
                    "content-type": "application/json;charset=UTF-8",
                    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 isp/unknown network/WIFI prokanqiu/7.5.28 iPhone11,6 hpweb_request",
                }
            )
            .validate()
            .assert_equal("body.status", 200)
            .assert_equal("body.msg", "success")
        ),
    ]


if __name__ == "__main__":
    TestCaseGetprestige().test_start()
