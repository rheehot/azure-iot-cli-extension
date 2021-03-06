# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import json
import re
import yaml

from azext_iot.monitor.base_classes import AbstractBaseEventsHandler
from azext_iot.monitor.parsers.common_parser import CommonParser
from azext_iot.monitor.models.arguments import CommonHandlerArguments


class CommonHandler(AbstractBaseEventsHandler):
    def __init__(self, common_handler_args: CommonHandlerArguments):
        super(CommonHandler, self).__init__()
        self._common_handler_args = common_handler_args

    def parse_message(self, message):
        parser = CommonParser(
            message=message,
            common_parser_args=self._common_handler_args.common_parser_args,
        )

        if not self._should_process_device(parser.device_id):
            return

        result = parser.parse_message()

        if self._common_handler_args.output.lower() == "json":
            dump = json.dumps(result, indent=4)
        else:
            dump = yaml.safe_dump(result, default_flow_style=False)

        print(dump, flush=True)

    def _should_process_device(self, device_id):
        expected_device_id = self._common_handler_args.device_id
        expected_devices = self._common_handler_args.devices

        if expected_device_id and expected_device_id != device_id:
            if "*" in expected_device_id or "?" in expected_device_id:
                regex = (
                    re.escape(expected_device_id)
                    .replace("\\*", ".*")
                    .replace("\\?", ".")
                    + "$"
                )
                if not re.match(regex, device_id):
                    return False
            else:
                return False

        if expected_devices and device_id not in expected_devices:
            return False

        return True
