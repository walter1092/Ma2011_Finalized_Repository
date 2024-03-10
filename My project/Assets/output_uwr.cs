using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Unity.Robotics.ROSTCPConnector;
using TwistMsg = RosMessageTypes.Geometry.TwistMsg;

public class output_uwr : MonoBehaviour
{
    ROSConnection ros;
    public string topicName = "/turtle1/cmd_vel";
    private TwistMsg currentTwist;

    public float speed = 0.5f;
    public float turn = 1.0f;

    void Start()
    {
        ros = ROSConnection.GetOrCreateInstance();
        ros.RegisterPublisher<TwistMsg>(topicName);
        currentTwist = new TwistMsg();
    }

    void Update()
    {
        ProcessInput();
    }

    void ProcessInput()
    {
                
        // Checking continuous press
        if (Input.GetButtonDown("Vertical") || Input.GetButtonDown("Horizontal") || Input.GetButtonDown("Fire1")) // Assuming Fire1 is mapped to a key for demonstration
        {
            float vertical = Input.GetAxis("Vertical");
            float horizontal = Input.GetAxis("Horizontal");
            float mouseX = Input.GetAxis("Mouse X");
            transform.Translate(Vector3.forward * speed * Time.deltaTime);
            //transform.Translate(Vector3.right * speed * Time.deltaTime);
            // Sending signals only when keys are pressed
            SendTwistMessage(vertical, horizontal, mouseX);
        }

        // Example for discrete action using GetButtonDown
        if (Input.GetButtonDown("Jump")) // Assuming Jump is a key press action
        {
            
            Debug.Log("Jump button pressed once.");
            // Implement action for Jump button pressed once
        }

        // Handling mouse scroll wheel separately for continuous detection
        float scrollWheel = Input.GetAxis("Mouse ScrollWheel");
        if (Mathf.Abs(scrollWheel) > 0.01f) // Adjust threshold as needed
        {
            Debug.Log("Sending signal due to scroll wheel action.");
            // Implement or call sending signal function here
        }
    }

    void SendTwistMessage(float vertical, float horizontal, float mouseX)
    {
        currentTwist.linear.x = vertical;
        currentTwist.linear.y = horizontal;
        currentTwist.angular.z = -mouseX * turn;
        Debug.Log($"Sending Twist Message: Vertical {vertical}, Horizontal {horizontal}, Mouse X {mouseX}");

        ros.Publish(topicName, currentTwist);
    }
}
