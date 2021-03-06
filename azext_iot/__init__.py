# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core import AzCommandsLoader
from azure.cli.core.commands import CliCommandType
from azext_iot._factory import iot_service_provisioning_factory
from azext_iot.constants import VERSION
import azext_iot._help  # noqa: F401


iothub_ops = CliCommandType(operations_tmpl="azext_iot.operations.hub#{}")

iothub_ops_job = CliCommandType(operations_tmpl="azext_iot.iothub.job_commands#{}")

iothub_ops_device = CliCommandType(
    operations_tmpl="azext_iot.iothub.device_commands#{}"
)

iotdps_ops = CliCommandType(
    operations_tmpl="azext_iot.operations.dps#{}",
    client_factory=iot_service_provisioning_factory,
)

iotdigitaltwin_ops = CliCommandType(
    operations_tmpl="azext_iot.operations.digitaltwin#{}"
)

iotpnp_ops = CliCommandType(operations_tmpl="azext_iot.operations.pnp#{}")


class IoTExtCommandsLoader(AzCommandsLoader):
    def __init__(self, cli_ctx=None):
        super(IoTExtCommandsLoader, self).__init__(cli_ctx=cli_ctx)

    def load_command_table(self, args):
        from azext_iot.commands import load_command_table
        from azext_iot.iothub.command_bindings import load_iothub_commands
        from azext_iot.central.command_map import load_central_commands

        load_command_table(self, args)
        load_iothub_commands(self, args)
        load_central_commands(self, args)

        return self.command_table

    def load_arguments(self, command):
        from azext_iot._params import load_arguments
        from azext_iot.central.params import load_central_arguments

        load_arguments(self, command)
        load_central_arguments(self, command)


COMMAND_LOADER_CLS = IoTExtCommandsLoader

__version__ = VERSION
