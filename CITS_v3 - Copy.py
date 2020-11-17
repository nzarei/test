import json, pickle
from enum import Enum

class CITS:
    def __init__(self):
        return


class DENM_MSG(CITS):
    def __init__(self, kind, approachZone):
        self.kind = kind
        self.approachZone = approachZone

        return

    def locationInApproachZone(self, cam):
        """Return True if point in DENM approach zone."""

        return


class IVI(CITS):
    def __init__(self):
        return


class CAMValue:
    def __init__(self, value=-1, confidence=-1):
        self.value = value
        self.confidence = confidence

        return

class ST(Enum):
    passengerCar = 5


class CAM:

    def __init__(self, stationID= -1, deltaTime=-1, stationType=-1, latitude=-1, longitude=-1, altitudeValue=-1, altitudeConfidence=-1, headingValue=-1, headingConfidence=-1, speedValue=-1, speedConfidence=-1, driveDirection=-1, vehicleLength=-1, vehicleWidth=-1, longitudinalAccelerationValue=-1 ,longitudinalAccelerationConfidence=-1, curvatureValue=-1, curvatureConfidence=-1, yawRateValue=-1, yawRateConfidence=-1, lateralAccelerationValue=-1, lateralAccelerationConfidence=-1):

        self.stationID = stationID
        self.deltaTime = deltaTime
        self.stationType = stationType
        #self.stationType = ST(5)  # this should be translated to an enumerated type

        #self.referencePosition = referencePosition  # make this seperate class? latitude, longitude, confidence
        self.latitude = latitude
        self.longitude = longitude

        self.altitude = CAMValue(altitudeValue, altitudeConfidence)  # value and confidence
        self.heading = CAMValue(headingValue, headingConfidence)  # value and confidence
        self.speed = CAMValue(speedValue, speedConfidence)  # value and confidence
        self.driveDirection = driveDirection
        self.vehicleLength = vehicleLength
        self.vehicleWidth = vehicleWidth
        self.curvature = CAMValue(curvatureValue, curvatureConfidence)  # value and confidence
        self.yawRate = CAMValue(yawRateValue, yawRateConfidence)  # value and confidence
        self.longitudinalAcceleration = CAMValue(longitudinalAccelerationValue,
                                                 longitudinalAccelerationConfidence)  # value and confidence
        self.lateralAcceleration = CAMValue(lateralAccelerationValue,
                                            lateralAccelerationConfidence)  # value and confidence

        return



    def CAM_initialise(self, CITS):
        element = CITS['_source']['layers']['etsiits']['its.CAM_element']
        parameters = element['its.cam_element']['its.camParameters_element']
        bsContainer = parameters['its.basicContainer_element']
        hfContainer = parameters['its.highFrequencyContainer_tree']['its.basicVehicleContainerHighFrequency_element']

        stationID = element['its.header_element']['its.stationID']
        deltaTime = element['its.cam_element']['its.generationDeltaTime']
        stationType = bsContainer['its.stationType']

        #self.referencePosition = referencePosition  # make this seperate class? latitude, longitude, confidence
        latitude = bsContainer['its.referencePosition_element']['its.latitude']
        longitude = bsContainer['its.referencePosition_element']['its.longitude']


        altitudeValue = bsContainer['its.referencePosition_element']['its.altitude_element']['its.altitudeValue']
        altitudeConfidence = bsContainer['its.referencePosition_element']['its.altitude_element']['its.altitudeConfidence']

        headingValue = hfContainer ['its.heading_element']['its.headingValue']
        headingConfidence = hfContainer ['its.heading_element']['its.headingConfidence']


        speedValue = hfContainer['its.speed_element']['its.speedValue']
        speedConfidence = hfContainer['its.speed_element']['its.speedConfidence']

        driveDirection = hfContainer['its.driveDirection']

        vehicleLength = hfContainer['its.vehicleLength_element']['its.vehicleLengthValue']
        vehicleWidth = hfContainer['its.vehicleWidth']

        longitudinalAccelerationValue = hfContainer['its.longitudinalAcceleration_element']['its.longitudinalAccelerationValue']
        longitudinalAccelerationConfidence = hfContainer['its.longitudinalAcceleration_element']['its.longitudinalAccelerationConfidence']

        curvatureValue = hfContainer['its.curvature_element']['its.curvatureValue']
        curvatureConfidence = hfContainer['its.curvature_element']['its.curvatureConfidence']

        yawRateValue =  hfContainer['its.yawRate_element']['its.yawRateValue']
        yawRateConfidence = hfContainer['its.yawRate_element']['its.yawRateConfidence']

        lateralAccelerationValue = hfContainer ['its.lateralAcceleration_element']['its.lateralAccelerationValue']
        lateralAccelerationConfidence = hfContainer ['its.lateralAcceleration_element']['its.lateralAccelerationConfidence']

        #print(stationID)
        self.__init__(stationID, deltaTime, stationType, latitude, longitude, altitudeValue, altitudeConfidence, headingValue, headingConfidence, speedValue, speedConfidence, driveDirection, vehicleLength, vehicleWidth, longitudinalAccelerationValue,longitudinalAccelerationConfidence, curvatureValue, curvatureConfidence, yawRateValue, yawRateConfidence, lateralAccelerationValue, lateralAccelerationConfidence)
        return



def fromPCAP( pcap):
    """Parse a JSON PCAP entry (not a list of PCAPS) into a CAM instance."""
    for index in range(3, len(pcap)):
        cam_instance = CAM()
        cam_instance.CAM_initialise(pcap[index])


def main():
    fileName = 'C:/nasim/projects/iMove/Data/Mt_Cotton_v1/2018.0306.0047_C04E548202200-0000_4847/tx.json'
    file = open(fileName, encoding="utf8")
    data = json.load(file)

    fromPCAP(data)
    return

main()