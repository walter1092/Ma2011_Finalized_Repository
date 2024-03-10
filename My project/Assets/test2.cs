using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Unity.Robotics.ROSTCPConnector;
using TwistMsg = RosMessageTypes.Geometry.TwistMsg;
public class test2:MonoBehaviour
{
    ROSConnection ros;
    public string topicName = "/turtle1/cmd_vel";
    private TwistMsg currentTwist;
    public float speed = 0.5f;
    public float turn = 1.0f;
    private Rigidbody rb;
    private Vector3 movementDirection = Vector3.zero;
    private bool messageSent = false;
    private bool wasSprinting = false;

     
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
        bool isSprinting = Input.GetKey(KeyCode.LeftShift) || Input.GetKey(KeyCode.RightShift);
        if (isSprinting != wasSprinting) // Check if sprinting state has changed
        {
            directionMultiplier = isSprinting ? 2.0f : 1.0f; // Update based on sprinting state
            if (movementDirection != Vector3.zero) // If already moving, adjust speed immediately
            {
                CalculateMovement(); // Recalculate movement with new sprinting state
            }
            wasSprinting = isSprinting; // Update the sprinting state for next frame
        }

        HandleMovementInput();
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
        else if (Input.GetKeyDown(KeyCode.P))
        {
            ProcessStopInput();
        }
    }

    void ProcessStopInput()
    {
        rb.velocity = Vector3.zero; // Stop the Rigidbody movement
        movementDirection = Vector3.zero; // Reset movement direction
        SendTwistMessage(movementDirection); // Send stop signal
    }

    void CalculateMovement()
    {
        // Adjust velocity based on current direction and multiplier
        rb.velocity = movementDirection * speed * directionMultiplier;

        // Send twist message only if not already sent or if sprinting state changed
        if (previousDirection != movementDirection)
        {
            SendTwistMessage(movementDirection);
            previousDirection = movementDirection; // Update previousDirection
            messageSent= false;
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