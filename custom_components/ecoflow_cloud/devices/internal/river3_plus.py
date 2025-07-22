from custom_components.ecoflow_cloud.api import EcoflowApiClient
from custom_components.ecoflow_cloud.devices import const, BaseDevice
from custom_components.ecoflow_cloud.devices.const import ATTR_DESIGN_CAPACITY, ATTR_FULL_CAPACITY, ATTR_REMAIN_CAPACITY, BATTERY_CHARGING_STATE, \
    MAIN_DESIGN_CAPACITY, MAIN_FULL_CAPACITY, MAIN_REMAIN_CAPACITY
from custom_components.ecoflow_cloud.entities import BaseSensorEntity, BaseNumberEntity, BaseSwitchEntity, BaseSelectEntity
from custom_components.ecoflow_cloud.number import ChargingPowerEntity, MaxBatteryLevelEntity, MinBatteryLevelEntity, BatteryBackupLevel
from custom_components.ecoflow_cloud.select import DictSelectEntity, TimeoutDictSelectEntity
from custom_components.ecoflow_cloud.sensor import LevelSensorEntity, RemainSensorEntity, TempSensorEntity, \
    CyclesSensorEntity, InWattsSensorEntity, OutWattsSensorEntity, VoltSensorEntity, InMilliampSensorEntity, \
    InVoltSensorEntity, MilliVoltSensorEntity, InMilliVoltSensorEntity, \
    OutMilliVoltSensorEntity, ChargingStateSensorEntity, CapacitySensorEntity, StatusSensorEntity, \
    QuotaStatusSensorEntity
from custom_components.ecoflow_cloud.switch import EnabledEntity


class River3Plus(BaseDevice):

    @staticmethod
    def default_charging_power_step() -> int:
        return 50

    def sensors(self, client: EcoflowApiClient) -> list[BaseSensorEntity]:
        return [
            LevelSensorEntity(client, self, "bms_bmsStatus.soc", const.MAIN_BATTERY_LEVEL)
                .attr("bms_bmsStatus.designCap", ATTR_DESIGN_CAPACITY, 0)
                .attr("bms_bmsStatus.fullCap", ATTR_FULL_CAPACITY, 0)
                .attr("bms_bmsStatus.remainCap", ATTR_REMAIN_CAPACITY, 0),
            CapacitySensorEntity(client, self, "bms_bmsStatus.designCap", MAIN_DESIGN_CAPACITY, False),
            CapacitySensorEntity(client, self, "bms_bmsStatus.fullCap", MAIN_FULL_CAPACITY, False),
            CapacitySensorEntity(client, self, "bms_bmsStatus.remainCap", MAIN_REMAIN_CAPACITY, False),

            # ChargingStateSensorEntity(client, self, "bms_emsStatus.chgState", BATTERY_CHARGING_STATE),

            # InWattsSensorEntity(client, self, "pd.wattsInSum", const.TOTAL_IN_POWER),
            # OutWattsSensorEntity(client, self, "pd.wattsOutSum", const.TOTAL_OUT_POWER),

            # InWattsSensorEntity(client, self, "powInSumW", "Total input power"),
            # OutWattsSensorEntity(client, self, "powOutSumW", "Total output power"),

            # InWattsSensorEntity(client, self, "powGetQcusb1", "USB 1 Power"),
            # InWattsSensorEntity(client, self, "powGetQcusb2", "USB 2 Power"),

            # InWattsSensorEntity(client, self, "powGetTypec1", "Type-C 1 Power"),
            # InWattsSensorEntity(client, self, "powGetTypec2", "Type-C 2 Power"),

            # InWattsSensorEntity(client, self, "powGet_12v", "12V Power"),
            # InWattsSensorEntity(client, self, "powGetAc", "AC Power"),


            # VoltSensorEntity(client, self, "plugInInfoAcOutVol", "AC Output Voltage"),
            # VoltSensorEntity(client, self, "plugInInfoAcInVol", "AC Input Voltage"),
            # VoltSensorEntity(client, self, "plugInInfoBmsVol", "BMS Voltage"),
            # VoltSensorEntity(client, self, "bmsBattVol", "Battery Voltage"),

            # VoltSensorEntity(client, self, "cmsBattVol", "CMS Battery Voltage"),
            # VoltSensorEntity(client, self, "cmsChgReqVol", "CMS Charge Request Voltage"),
            # VoltSensorEntity(client, self, "llcRecvCmsChgReqVol", "LLC CMS Charge Request Voltage"),
            # VoltSensorEntity(client, self, "plugInInfoPvVol", "PV Voltage"),
            # VoltSensorEntity(client, self, "plugInInfo_12vVol", "12V Output Voltage"),
            # VoltSensorEntity(client, self, "llcBatVol", "LLC Battery Voltage"),
            # VoltSensorEntity(client, self, "llcBusVol", "LLC Bus Voltage"),
            # VoltSensorEntity(client, self, "plugInInfoDcpVol", "DCP Voltage"),
            # # Current sensors
            # InMilliampSensorEntity(client, self, "plugInInfoAcInAmp", "AC Input Current"),
            # InMilliampSensorEntity(client, self, "plugInInfoAcOutAmp", "AC Output Current"),
            # InMilliampSensorEntity(client, self, "bmsBattAmp", "Battery Current"),
            # InMilliampSensorEntity(client, self, "cmsBattAmp", "CMS Battery Current"),
            # InMilliampSensorEntity(client, self, "cmsChgReqAmp", "CMS Charge Request Current"),
            # InMilliampSensorEntity(client, self, "dcdcChgReqCur", "DCDC Charge Request Current"),
            # InMilliampSensorEntity(client, self, "plugInInfoPvAmp", "PV Current"),
            # InMilliampSensorEntity(client, self, "plugInInfo_12vAmp", "12V Output Current"),
            # InMilliampSensorEntity(client, self, "llcBatCur", "LLC Battery Current"),
            # InMilliampSensorEntity(client, self, "plugInInfoDcpAmp", "DCP Current"),
            # # Temperature sensors
            # TempSensorEntity(client, self, "tempPcsDc", "PCS DC Temperature"),
            # TempSensorEntity(client, self, "tempPcsAc", "PCS AC Temperature"),
            # TempSensorEntity(client, self, "tempPv", "PV Temperature"),
            # TempSensorEntity(client, self, "bmsHighTempIcon", "BMS High Temp"),
            # TempSensorEntity(client, self, "bmsLowTempIcon", "BMS Low Temp"),
            # # Diagnostic and status sensors (text entities)
            # LevelSensorEntity(client, self, "pcsWorkMode", "PCS Work Mode"),
            # LevelSensorEntity(client, self, "plugInInfoAcOutType", "AC Output Type"),
            # LevelSensorEntity(client, self, "bmsBalState", "BMS Balance State"),
            # LevelSensorEntity(client, self, "bmsAlmState", "BMS Alarm State"),
            # LevelSensorEntity(client, self, "bmsProState", "BMS Protection State"),
            # LevelSensorEntity(client, self, "bmsFltState", "BMS Fault State"),
            # LevelSensorEntity(client, self, "bmsAlmState_2", "BMS Alarm State 2"),
            # LevelSensorEntity(client, self, "bmsProState_2", "BMS Protection State 2"),
            # LevelSensorEntity(client, self, "invMainFsmstate", "Inverter Main FSM State"),
            # LevelSensorEntity(client, self, "l1MainFsmstate", "L1 Main FSM State"),

            self._status_sensor(client),
            # FanSensorEntity(client, self, "bms_emsStatus.fanLevel", "Fan Level"),

        ]

    # Implement numbers, switches, selects, etc. as needed
    def numbers(self, client: EcoflowApiClient):
        # Placeholder for number entities (e.g., settable values)
        return []

    def switches(self, client: EcoflowApiClient):
        # Placeholder for switch entities (e.g., toggles)
        return []

    def selects(self, client: EcoflowApiClient):
        # Placeholder for select entities (e.g., mode selectors)
        return []

    def _status_sensor(self, client: EcoflowApiClient) -> StatusSensorEntity:
        return QuotaStatusSensorEntity(client, self)
