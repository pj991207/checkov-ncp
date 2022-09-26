
from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck


class NCP_LBTargetGroupDefinesHealthCheck(BaseResourceCheck):
    def __init__(self):
        name = "Ensure HTTP HTTPS Target group defines Healthcheck"
        id = "NCP_LBTargetGroupDefinesHealthCheck"
        supported_resources = ['ncloud_lb_target_group']
        categories = [CheckCategories.GENERAL_SECURITY]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        if conf.get("protocol") in (["HTTP"], ["HTTPS"]):
            health_checks = conf.get("health_check")
            if health_checks and isinstance(health_checks, list):
                healthcheck = health_checks[0]
                if isinstance(healthcheck, dict) and healthcheck.get("url_path"):
                    return CheckResult.PASSED
            #self.evaluated_keys = ["health_check"]
            return CheckResult.FAILED
        return CheckResult.UNKNOWN

scanner = NCP_LBTargetGroupDefinesHealthCheck()