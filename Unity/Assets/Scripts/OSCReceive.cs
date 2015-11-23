using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class OSCReceive : MonoBehaviour {

	float[] ctl;
	Dictionary<string, ServerLog> servers = new Dictionary<string, ServerLog>();

	// Use this for initialization
	void Start () {

		ctl = new float[18];
	}
	
	// Update is called once per frame
	void Update () {
		OSCHandler.Instance.UpdateLogs();
		servers = OSCHandler.Instance.Servers;

		foreach(KeyValuePair<string, ServerLog> item in servers){
			if(item.Value.log.Count > 0){
				int lastPacketIndex = item.Value.packets.Count - 1;

				Debug.Log(item.Value.packets[lastPacketIndex].Address);
				Debug.Log(item.Value.packets[lastPacketIndex].Data[0].ToString());
			}
		}
	}
}
