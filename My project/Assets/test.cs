using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Unity.Robotics.ROSTCPConnector;
using TwistMsg = RosMessageTypes.Geometry.TwistMsg;
public class test:MonoBehaviour
{
    ROSConnection ros;
    public string topicName = "/turtle1/cmd_vel";
    private TwistMsg currentTwist;
    public float speed = 0.5f;
    public float turn = 1.0f;
    private Rigidbody rb;
    private Vector3 movementDirection = Vector3.zero;
    private bool messageSent = false;
     
    public float directionMultiplier = 1.0f; // Default multiplier
    private Vector3 previousDirection=Vector3.zero;

    void Start()
    {
        ros = ROSConnection.GetOrCreateInstance();
        ros.RegisterPublisher<TwistMsg>(topicName);
        currentTwist = new TwistMsg();
        rb = GetComponent<Rigidbody>();
    }

    void Update()
    {
    // Check for sprint key
        if (Input.GetKey(KeyCode.LeftShift) || Input.GetKey(KeyCode.RightShift))
        {
            directionMultiplier = 2.0f; // Sprinting, so increase speed
        }
        else
        {
            directionMultiplier = 1.0f; // Not sprinting, use normal speed
        }
        HandleMovementInput();
        ProcessStopInput();
    }

    void HandleMovementInput()
    {
        Vector3 previousDirection = movementDirection;

        if (Input.GetKeyDown(KeyCode.UpArrow))
        {
            movementDirection = Vector3.forward;
            CalculateMovement();
        }
        else if (Input.GetKeyDown(KeyCode.DownArrow))
        {
            movementDirection = Vector3.back;
            CalculateMovement();
        }
        else if (Input.GetKeyDown(KeyCode.LeftArrow))
        {
            movementDirection = Vector3.left;
            CalculateMovement();
        }
        else if (Input.GetKeyDown(KeyCode.RightArrow))
        {
            movementDirection = Vector3.right;
            CalculateMovement();
        }
        else if (Input.GetKeyDown(KeyCode.Space))
        {
            movementDirection = Vector3.up;
            CalculateMovement();
        }
        else if (Input.GetKeyDown(KeyCode.LeftControl) || Input.GetKeyDown(KeyCode.RightControl))
        {
            movementDirection = Vector3.down;
            CalculateMovement();
        }

    }

    void ProcessStopInput()
    {
        if (Input.GetKeyDown(KeyCode.P)) // Use P for pause
        {
            rb.velocity = Vector3.zero; // Stop the Rigidbody movement
            movementDirection = Vector3.zero; // Reset movement direction
            SendTwistMessage(movementDirection); // Send stop signal
        }
    }
    void CalculateMovement()
    {
        if (previousDirection != movementDirection && !messageSent)
        {
            rb.velocity = movementDirection * speed * directionMultiplier;
            SendTwistMessage(movementDirection);
            previousDirection = movementDirection; // Update previousDirection for next comparison
            messageSent = false; // Ensure the message is marked as sent
        }
    }

        


    void SendTwistMessage(Vector3 direction)
    {
        if (messageSent== false)
        {
            // Construct and send the Twist message based on direction
            print("Success");
            currentTwist.linear.x = direction.z;
            currentTwist.linear.y = direction.x;
            currentTwist.angular.z = 0; // Modify as needed for your application
            Debug.Log($"Sending Twist Message: Direction {direction}");
            ros.Publish(topicName, currentTwist);
            messageSent = true; // Mark the message as sent

        }
    }
}