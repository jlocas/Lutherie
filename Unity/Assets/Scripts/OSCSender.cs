using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using System.IO;

public class OSCSender : MonoBehaviour {

	public SpringGrid grid;
	private int gridLength;

	string filename = "LeFichier.txt";

	StreamWriter sw = new StreamWriter("fichier.txt");

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
				sw.Write("block ");
				sw.WriteLine(x + z);
				sw.Write(": ");
				sw.WriteLine(grid.GetBlock(x,z).Block.transform.position.y);

			}
		}

		OSCHandler.Instance.SendMessageToClient("Pyo", "/springGrid/blocks/positions", positions);
	}

	private void SendGridLength()
	{
		OSCHandler.Instance.SendMessageToClient("Pyo", "/springGrid/length", gridLength);
		sw.Write("Grid size: ");
		sw.WriteLine(gridLength);
	}
}
