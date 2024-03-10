using UnityEngine;
using Unity.Robotics.ROSTCPConnector;
using QuaternionMessage = RosMessageTypes.Geometry.QuaternionStampedMsg;
//using Position = RosMessageTypes.Geometry.QuaternionStampedMsg;

public class imu_move_t2 : MonoBehaviour
{
    
public float multiplier =1;
    void Start()
    {
        ROSConnection.GetOrCreateInstance().Subscribe<QuaternionMessage>("/imu/dq", MoveCube);
    }

    void MoveCube(QuaternionMessage msg)
    {
        print(msg.quaternion.x);
        transform.rotation *= new Quaternion((float)msg.quaternion.x, (float)msg.quaternion.y, (float)msg.quaternion.z, (float)msg.quaternion.w)*Quaternion.Euler(multiplier,multiplier,multiplier);
    }
}