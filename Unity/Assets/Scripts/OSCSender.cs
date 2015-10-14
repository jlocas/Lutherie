using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using System.IO;


public class OSCSender : MonoBehaviour {

	public SpringGrid grid;
	private int gridLength;
	private int groupsPerSide;
	
	StreamWriter swDetail;
	StreamWriter swPure;

	// Use this for initialization
	void Start () {
		/*swDetail = new StreamWriter(Application.dataPath + "/" + "detailed.txt");
		swPure = new StreamWriter(Application.dataPath + "/" + "data.txt");*/


		gridLength = grid.GetSideLength();
		groupsPerSide = grid.GroupsPerSide;

		OSCHandler.Instance.Init();

		SendGridLength();
	
	}

	// Update is called once per frame
	void Update () {
		//SendBlockPositions();
		SendBlockGroupData();
	}

	private void SendBlockPositions()
	{
		List<float> positions = new List<float>();
		positions.Capacity = gridLength * gridLength;

		for(int x = 0; x < gridLength; x++){
			for(int z = 0; z < gridLength; z++){

				positions.Add(grid.GetBlock(x, z).Block.transform.position.x);
				positions.Add(grid.GetBlock(x, z).Block.transform.position.y);
				positions.Add(grid.GetBlock(x, z).Block.transform.position.z);

			}
		}
		OSCHandler.Instance.SendMessageToClient("Pyo", "/springGrid/blocks/positions", positions);

		/*swDetail.Write("\n\nNEW SEND\n\n");

		for(int x = 0; x < gridLength; x++){
			for(int z = 0; z < gridLength; z++){
				swDetail.Write(string.Format("Block({0}, {1}): ({2},{3},{4}) \n", x, z, positions[i*3], positions[i*3+1], positions[i*3+2]));
				swPure.Write(string.Format("{0}, {1}, {2}, ", positions[i*3], positions[i*3+1], positions[i*3+2]));
				i++;
			}
		}*/
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
