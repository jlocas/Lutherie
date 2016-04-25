using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using System.IO;


public class OSCSender : MonoBehaviour {

	public SpringGrid grid;
	private float counter;
	public float delay;
	private int gridLength;
	private int groupsPerSide;
	int which = 0;

	// Use this for initialization
	void Start () {


		gridLength = grid.GetSideLength();
		groupsPerSide = grid.GroupsPerSide;

		OSCHandler.Instance.Init();

		SendGridLength();

		InvokeRepeating("SendData", 1f, 0.025f);

	
	}

	// Update is called once per frame
	void Update () {
		//SendBlockGroupData();
	}

	private void SendBlockGroupHeight()
	{
		List<float> positions = new List<float>();

		for(int x=0; x < groupsPerSide; x++){
			for(int z=0; z < groupsPerSide; z++){
				//positions.Add(grid.BlockGroups[x,z].GetAveragePosition().x);
				positions.Add(grid.BlockGroups[x,z].GetAveragePosition().y);
				//positions.Add(grid.BlockGroups[x,z].GetAveragePosition().z);

			}
		}
		OSCHandler.Instance.SendMessageToClient("Pyo", "/springGrid/blockGroups/positions", positions);

	}

	private void SendAverageDeviation(){
		float avg = 0f;
		for(int x=0; x < groupsPerSide; x++){
			for(int z=0; z < groupsPerSide; z++){
				avg += grid.BlockGroups[x,z].GetDeviation();
			}
		}
		OSCHandler.Instance.SendMessageToClient("Pyo", "/springGrid/blockGroups/avgdev", avg/groupsPerSide);
	}

	private void SendAverageHeight(){
		float avg = 0f;
		for(int x=0; x < groupsPerSide; x++){
			for(int z=0; z < groupsPerSide; z++){
				avg += grid.BlockGroups[x,z].GetAveragePosition().y;
			}
		}
		OSCHandler.Instance.SendMessageToClient("Pyo", "/springGrid/blockGroups/avgy", avg/groupsPerSide);
	}

	private void SendAverageHeightDev(){
		float avg = 0f;
		for(int x=0; x < groupsPerSide; x++){
			for(int z=0; z < groupsPerSide; z++){
				avg += Mathf.Abs(grid.BlockGroups[x,z].GetAveragePositionAbs().y);
			}
		}
		OSCHandler.Instance.SendMessageToClient("Pyo", "/springGrid/blockGroups/avgydev", avg/groupsPerSide);
	}

	private void SendAverageVelocity(){
		float avg = 0f;
		for(int x=0; x < groupsPerSide; x++){
			for(int z=0; z < groupsPerSide; z++){
				avg += grid.BlockGroups[x,z].GetAverageSpeed();
			}
		}
		OSCHandler.Instance.SendMessageToClient("Pyo", "/springGrid/blockGroups/avgvel", avg/groupsPerSide);

	}

	private void SendBlockGroupVelocity(){
		List<float> vel = new List<float>();
		
		for(int x=0; x < groupsPerSide; x++){
			for(int z=0; z < groupsPerSide; z++){
				vel.Add(grid.BlockGroups[x,z].GetAverageSpeed());
			}
		}
		OSCHandler.Instance.SendMessageToClient("Pyo", "/springGrid/blockGroups/vels", vel);
	}

	private void SendAverages(){
		SendAverageDeviation();
		SendAverageHeight();
		SendAverageVelocity();
		SendAverageHeightDev();
	}

	private void SendData(){
		if (which==0){
			SendBlockGroupHeight();
		} else {
			SendBlockGroupVelocity();
		}

		SendAverageDeviation();
		SendAverageHeight();
		SendAverageVelocity();
		SendAverageHeightDev();

		which = (which + 1) % 2;
	}

	private void SendGridLength()
	{
		OSCHandler.Instance.SendMessageToClient("Pyo", "/springGrid/length", gridLength);
		OSCHandler.Instance.SendMessageToClient("Pyo", "/springGrid/groupsPerSide", groupsPerSide);

	}

	public void SendBall2Hit(int x, int z){
		List<int> pos = new List<int>(){x, z};
		OSCHandler.Instance.SendMessageToClient("Pyo", "/springGrid/rain2/ballHit", pos);
	}
}
