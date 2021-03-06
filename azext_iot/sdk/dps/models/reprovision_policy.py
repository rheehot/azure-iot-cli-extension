# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ReprovisionPolicy(Model):
    """The behavior of the service when a device is re-provisioned to an IoT hub.

    :param update_hub_assignment: When set to true (default), the Device
     Provisioning Service will evaluate the device's IoT Hub assignment and
     update it if necessary for any provisioning requests beyond the first from
     a given device. If set to false, the device will stay assigned to its
     current IoT hub. Default value: True .
    :type update_hub_assignment: bool
    :param migrate_device_data: When set to true (default), the Device
     Provisioning Service will migrate the device's data (twin, device
     capabilities, and device ID) from one IoT hub to another during an IoT hub
     assignment update. If set to false, the Device Provisioning Service will
     reset the device's data to the initial desired configuration stored in the
     corresponding enrollment list. Default value: True .
    :type migrate_device_data: bool
    """

    _validation = {
        'update_hub_assignment': {'required': True},
        'migrate_device_data': {'required': True},
    }

    _attribute_map = {
        'update_hub_assignment': {'key': 'updateHubAssignment', 'type': 'bool'},
        'migrate_device_data': {'key': 'migrateDeviceData', 'type': 'bool'},
    }

    def __init__(self, update_hub_assignment=True, migrate_device_data=True):
        super(ReprovisionPolicy, self).__init__()
        self.update_hub_assignment = update_hub_assignment
        self.migrate_device_data = migrate_device_data
