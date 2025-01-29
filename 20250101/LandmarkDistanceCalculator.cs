using UnityEngine;
using System.Collections.Generic;

public class LandmarkDistanceCalculator : MonoBehaviour
{
    // Manually inputted coordinates of 7 landmarks (each Vector3 holds x, y, z)
    public List<Vector3> landmarkPositions;

    // Reference to the camera you want to adjust (minimap camera)
    public Camera minimapCamera;

    void Start()
    {
        // Calculate the pairwise distances between all landmarks
        List<float> distances = CalculateAllDistances(landmarkPositions);

        // Output the calculated distances to the Unity Console
        OutputDistances(distances);

        // Get the maximum distance from the list of distances (or other criteria)
        float maxDistance = GetMaxDistance(distances);

        // Adjust the camera size based on the maximum distance
        AdjustMinimapCamera(maxDistance);
    }

    // Calculate the pairwise distances between all landmarks
    List<float> CalculateAllDistances(List<Vector3> positions)
    {
        List<float> distances = new List<float>();

        // Loop through all pairs of landmarks
        for (int i = 0; i < positions.Count; i++)
        {
            for (int j = i + 1; j < positions.Count; j++)
            {
                // Calculate the Euclidean distance between the two landmarks
                float distance = Vector3.Distance(positions[i], positions[j]);
                distances.Add(distance);  // Store the distance
            }
        }

        return distances;
    }

    // Get the maximum distance from the list of distances
    float GetMaxDistance(List<float> distances)
    {
        float maxDistance = 0f;

        // Find the maximum distance
        foreach (float distance in distances)
        {
            if (distance > maxDistance)
            {
                maxDistance = distance;
            }
        }

        return maxDistance;
    }

    // Adjust the minimap camera size based on the maximum distance
    void AdjustMinimapCamera(float maxDistance)
    {
        // If using an orthographic camera for minimap
        if (minimapCamera.orthographic)
        {
            // Set the orthographic size based on the max distance (you may want to add some padding)
            minimapCamera.orthographicSize = maxDistance * 0.5f; // Adjust multiplier for better fit
        }
        // If using a perspective camera for minimap
        else
        {
            // Set the field of view (FOV) based on the max distance (you may need to tune this value)
            minimapCamera.fieldOfView = Mathf.Clamp(maxDistance * 0.5f, 30f, 90f); // Clamp between reasonable FOV values
        }

        Debug.Log("Minimap Camera Adjusted to Max Distance: " + maxDistance);
    }

    // Output the calculated distances to the Unity Console
    void OutputDistances(List<float> distances)
    {
        // Print each distance to the console
        for (int i = 0; i < distances.Count; i++)
        {
            Debug.Log("Distance " + (i + 1) + ": " + distances[i]);
        }
    }
}
