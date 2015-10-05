using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class OSCSender : MonoBehaviour {

	public SpringGrid grid;
	private int gridLength;

	Dictionary<string, ServerLog> servers = new Dictionary<string, ServerLog>();


	// Use this for initialization
	void Awake () {
		gridLength = grid.GetSideLength();
		OSCHandler.Instance.Init();

		SendGridLength();
	
	}
	
	// Update is called once per frame
	void Update () {
		SendBlockPositions();
	}

	private void SendBlockPositions()
	{
		List<float> positions = new List<float>();

		for(int x = 0; x < gridLength; x++){
			for(int z = 0; z < gridLength; z++){

				positions.Add(grid.GetBlock(x, z).Block.transform.position.x);
				positions.Add(grid.GetBlock(x, z).Block.transform.position.y);
				positions.Add(grid.GetBlock(x, z).Block.transform.position.z);

			}
		}
		OSCHandler.Instance.SendMessageToClient("Pyo", "/springGrid/blocks/positions", positions);
	}

	private void SendGridLength()
	{
		OSCHandler.Instance.SendMessageToClient("Pyo", "/springGrid/length", gridLength);
	}
}
