using UnityEngine;
using Unity.Robotics.ROSTCPConnector;
using QuaternionMessage = RosMessageTypes.Geometry.QuaternionStampedMsg;

public class RosSubscriberExample : MonoBehaviour
{
    

    void Start()
    {
        ROSConnection.GetOrCreateInstance().Subscribe<QuaternionMessage>("/imu/dq", MoveCube);
    }

    void MoveCube(QuaternionMessage msg)
    {
        transform.rotation *= new Quaternion((float)msg.quaternion.x, (float)msg.quaternion.y, (float)msg.quaternion.z, (float)msg.quaternion.w);
    }
}