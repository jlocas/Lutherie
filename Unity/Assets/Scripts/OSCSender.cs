using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using System.IO;


public class OSCSender : MonoBehaviour {

	public SpringGrid grid;
	private int gridLength;
	private int groupsPerSide;

	// Use this for initialization
	void Start () {


		gridLength = grid.GetSideLength();
		groupsPerSide = grid.GroupsPerSide;

		OSCHandler.Instance.Init();

		SendGridLength();
	
	}

	// Update is called once per frame
	void Update () {
		SendBlockGroupData();
	}

	private void SendBlockGroupData()
	{
		List<float> positions = new List<float>();

		for(int x=0; x < groupsPerSide; x++){
			for(int z=0; z < groupsPerSide; z++){
				positions.Add(grid.BlockGroups[x,z].GetAveragePosition().x);
				positions.Add(grid.BlockGroups[x,z].GetAveragePosition().y);
				positions.Add(grid.BlockGroups[x,z].GetAveragePosition().z);

			}
		}
		OSCHandler.Instance.SendMessageToClient("Pyo", "/springGrid/blockGroups/positions", positions);

	}

	private void SendGridLength()
	{
		OSCHandler.Instance.SendMessageToClient("Pyo", "/springGrid/length", gridLength);
		OSCHandler.Instance.SendMessageToClient("Pyo", "/springGrid/groupsPerSide", groupsPerSide);

	}
}
